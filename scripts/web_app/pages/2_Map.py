
import pandas as pd
import streamlit as st
import folium
from streamlit_folium import st_folium

def get_base64_png(image_path):
   """
   Encode an image file as a base64 string for use in HTML.
   """
   with open(image_path, "rb") as image_file:
       encoded = base64.b64encode(image_file.read()).decode()
   return f"data:image/png;base64,{encoded}"

# Load the original tracking data and coordinates data
df = pd.read_csv('data/raw/forJenny_IntensiveSurvey2025.csv')coordinates_df = pd.read_csv("../../data/processed/unique_coordinates_list.csv")
raw_coordinates_df = pd.read_csv('data/processed/all_coordinates.csv')  # Load the raw coordinates for comparison

# set up the Streamlit page configuration
st.set_page_config(
    page_title="Spatial Distribution of Intensive Survey 2025", 
    layout="wide",
    initial_sidebar_state="expanded"
)

st.title("Spatial Distribution of Intensive Survey 2025")
st.markdown("This interactive map shows the locations of plants surveyed in 2025.")
total_plants = len(coordinates_df)
max_seasonal_fruits = df['Estim.Fruits.Nr'].max()

col_m1, col_m2 = st.columns(2)
with col_m1:
    st.metric(label="Total Unique Plants Tracked", value=total_plants)
with col_m2:
    st.metric(label="Max Fruit Yield Observed", value=f"{max_seasonal_fruits:.1f} fruits")

st.write("---")

# Devide page into text description (Left) & map (Right)
col_left, col_right = st.columns([0.5, 2]) # 1:2 ratio means the map gets double the width

with col_left:
    st.subheader("Spatial Distribution")
    st.markdown("""
    **Map Guide:**
    * Each marker represents a unique Plant.
    * Hover over a marker to see the PlantID.
    * Perennial plants in the intensive survey will be marked in dark blue.
    * Choice in the option to see the cleaned data plotted vs. the raw data plotted. 
    **Data Source:** The data used for this map is from the Intensive Survey 2025 dataset.
    """)
    data_view = st.radio(
        "Select dataset to display on the map:",
        ["Raw Survey Data", "Cleaned Survey Data"] 
    )
    if data_view == "Raw Survey Data":
        # Drop rows missing coordinates in the raw data
        active_df = raw_coordinates_df.dropna(subset=['Latitude', 'Longitude'])
        dot_color = "#e67e22"  # Distinct Orange for raw data
        view_label = "Showing unverified raw inputs"
    else:
        # Drop rows missing coordinates in the clean data
        active_df = coordinates_df.dropna(subset=['Latitude', 'Longitude'])
        dot_color = "#d81b60"  # Vibrant Pink/Red for clean data
        view_label = "Showing verified unique plant coordinates"

with col_right:
    st.subheader("Map of Plant Locations")
    raw_data = folium.FeatureGroup(name="Raw Data")
    cleaned_data = folium.FeatureGroup(name="Cleaned Data")

    # Build Map Base using the mean of the coordinates to center the map
    map_center = [active_df['Latitude'].mean(), active_df['Longitude'].mean()]

    m = folium.Map(location=map_center, 
                   zoom_start=14,
                   tiles="CartoDB positron") 

    # Loop and plot normal circles
    for index, coord_row in active_df.iterrows():
        folium.CircleMarker(
            location=[coord_row['Latitude'], coord_row['Longitude']],
            radius=6,                  # Size of the circle in pixels
            color="#d81b60",           # Border color (dark pink/red)
            fill=True,
            fill_color="#d81b60",      # Inside fill color
            fill_opacity=0.8,          # Slightly transparent so overlapping circles are visible
            weight=1.5,                # Border thickness
            popup=f"PlantID: {coord_row['PlantID']}"
        ).add_to(m)

    # Render map
    st_folium(m, use_container_width=True, height=550)