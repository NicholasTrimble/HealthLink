import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium
from folium.plugins import MarkerCluster

# -----------------------------
# Page & Theme Setup
# -----------------------------
st.set_page_config(page_title="HealthLink", layout="wide")
st.title("❤️ HealthLink")
st.subheader("Find local health and aid services instantly.")

# How to Use Guide
st.info(
    """
    **How to Use HealthLink:**  
    1. Select a category on the sidebar (Clinic, Mental Health, Food Aid).  
    2. Optionally, filter by service name or city.  
    3. View featured services or expand to see all matching services.  
    4. Click 📧 to view emails, or download filtered results as CSV.  
    5. Toggle Dark Mode for easier viewing.  
    6. Explore the map to see service locations with colored markers.
    """
)

# -----------------------------
# Dark Mode Toggle
# -----------------------------
dark_mode = st.checkbox("🌙 Dark Mode")
if dark_mode:
    st.markdown(
        """
        <style>
        .stApp {background-color: #000000; color: #ffffff;}
        [data-testid="stSidebar"] {background-color: #111111; color: #ffffff;}
        h1,h2,h3,h4,h5,h6 {color: #ffffff;}
        a {color: #1E90FF;}
        .stText, .stMarkdown {color: #ffffff;}
        button[kind="primary"] {background-color: #1E90FF; color: #ffffff;}
        header, footer, .css-1v3fvcr {visibility: hidden;}
        </style>
        """, unsafe_allow_html=True
    )

# -----------------------------
# Load Data
# -----------------------------
category_files = {
    "clinic": "clinics.csv",
    "mental health": "mental_health.csv",
    "food aid": "food_aid.csv"
}
dataframes = {cat: pd.read_csv(file) for cat, file in category_files.items()}

# -----------------------------
# Sidebar Filters
# -----------------------------
st.sidebar.header("Filter Services")
category_options = list(category_files.keys())
selected_category = st.sidebar.selectbox("Select a category", category_options)
search_term = st.sidebar.text_input("Search by service name")
city_search = st.sidebar.text_input("Search by city/address (optional)")

# -----------------------------
# Filter Data
# -----------------------------
data = dataframes[selected_category]
filtered = data.copy()
if search_term:
    filtered = filtered[filtered['name'].str.contains(search_term, case=False)]
if city_search:
    filtered = filtered[filtered['address'].str.contains(city_search, case=False)]

# -----------------------------
# Category Emojis
# -----------------------------
category_emojis = {"clinic": "🏥", "mental health": "🧠", "food aid": "🍎"}
category_colors = {"clinic": "red", "mental health": "blue", "food aid": "green"}
category_icons = {"clinic": "plus-sign", "mental health": "heart", "food aid": "cutlery"}

# -----------------------------
# Layout: Left = List, Right = Map
# -----------------------------
left_col, right_col = st.columns([2, 3])

with left_col:
    # Featured Services
    if not filtered.empty:
        featured = filtered.sample(min(3, len(filtered)))
        st.markdown("### 🌟 Featured Services")
        for _, row in featured.iterrows():
            st.markdown(
                f"{category_emojis[selected_category]} **{row['name']}** — {row['address']} — {row['phone']}  \n"
                f"[Website]({row['website']})"
            )
            with st.expander("📧 Show Email"):
                st.text(row['email'])

    # All Services in Expander
    st.markdown("### 📋 All Matching Services")
    if not filtered.empty:
        with st.expander(f"Show all {len(filtered)} services"):
            for _, row in filtered.iterrows():
                st.markdown(
                    f"{category_emojis[selected_category]} **{row['name']}**  \n"
                    f"Address: {row['address']}  \n"
                    f"Phone: {row['phone']}  \n"
                    f"[Website]({row['website']})"
                )
                with st.expander("📧 Show Email"):
                    st.text(row['email'])
    else:
        st.write("No matching services found.")

    # Download filtered results
    if not filtered.empty:
        csv = filtered.to_csv(index=False)
        st.download_button("⬇️ Download Filtered Services as CSV", csv, "services.csv", "text/csv")

with right_col:
    if not filtered.empty:
        show_map = st.checkbox("Show Map", value=True)
        if show_map:
            m = folium.Map(
                location=[filtered['latitude'].mean(), filtered['longitude'].mean()],
                zoom_start=13
            )

            marker_cluster = MarkerCluster().add_to(m)

            for _, row in filtered.iterrows():
                folium.Marker(
                    [row['latitude'], row['longitude']],
                    popup=(
                        f"<b>{row['name']}</b><br>"
                        f"{row['address']}<br>"
                        f"{row['phone']}<br>"
                        f"Website: <a href='{row['website']}' target='_blank'>{row['website']}</a><br>"
                        f"Email: {row['email']}"
                    ),
                    icon=folium.Icon(color=category_colors[selected_category])
                ).add_to(marker_cluster)

            st_folium(m, width=700, height=500)
