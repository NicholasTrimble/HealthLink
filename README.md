

Healthlink


Inspiration

I live in a community where there are a lot of senior citizens. It is kind of a retirement town. I wanted to build something that could help people like them find essential services quickly. The elderly tend to struggle just getting around so i think something that could help them locate clinics, mental health support, and food aid services would be a huge help for these people, so why not put it all in one compact application for people to use.
What it does

HealthLink makes it easy to discover local health and aid services. You can filter by category or city, see featured services, view all matching results, check contact info safely, download results, and explore locations on an interactive map. It’s fast, intuitive, and designed to make a difference.
How we built it

I built HealthLink using Python and Streamlit, with pandas to manage the data and Folium to create the interactive maps. Each service has its own marker on the map, color-coded by category, and clustering is used for busy areas. The app also has a dark mode for better accessibility. I also added CSV files to pull data from. For the CSV files i used random comic book locations to make it fun for viewers.
Challenges we ran into

One of the biggest challenges was making the map interactive. I wanted it to start over the US since that is where I am from, but zoom to the filtered results dynamically. I also wanted the search to feel natural, so I added an autocomplete dropdown instead of a separate suggestions box.
Accomplishments that we're proud of

I’m proud that HealthLink is fully functional and easy to deploy online. It’s polished enough to demo smoothly, and includes features like smart map zooming, marker clustering that is color coded for density, it has a dark mode, and downloadable CSVs. It’s a tool that actually works for real-world use, and all that is needed is to swap the CSV files out for files that use real locations.
What we learned

I learned how to integrate multiple CSV datasets with Python, build interactive maps in Folium, and use Streamlit to create a custom user-friendly interface. I also gained experience in thinking about accessibility and making an app intuitive for people who just want to find services that they need quickly.
What's next for HealthLink

Next, I’d like to add city level autocomplete for searches, allow users to filter by distance or opening hours, and maybe include real-time data updates. My goal is to make HealthLink even more responsive and helpful for everyone out there who need essential services.
