import pandas as pd

# read the raw file
df = pd.read_csv("../data/raw/forJenny_IntensiveSurvey2025.csv", encoding="utf-8")

# extract both sets of coordinates alongside the Plant ID
coordinates_df = df[['PlantID', 'Latitude.x', 'Latitude.y', 'Longitude.x', 'Longitude.y']].copy()

# create a unified column by combining .x column and .y column for both Latitude and Longitude
coordinates_df['Latitude'] = coordinates_df['Latitude.x'].combine_first(coordinates_df['Latitude.y'])
coordinates_df['Longitude'] = coordinates_df['Longitude.x'].combine_first(coordinates_df['Longitude.y'])

# make a flag column to indicate if the coordinate came from the .x column or not
coordinates_df['is_from_x'] = coordinates_df['Latitude.x'].notna()

coordinates_df = coordinates_df.sort_values(by=['PlantID', 'is_from_x'], ascending=[True, False])

# drop duplicates based on PlantID, keeping the first occurrence and remove any rows with missing Latitude or Longitude values
coordinates_df = coordinates_df.drop_duplicates(subset=['PlantID'], keep='first')
coordinates_df = coordinates_df.dropna(subset=['Latitude', 'Longitude'])

# Save this clean coordinate list to its own file:
coordinates_df.to_csv("../data/processed/all_coordinates.csv", index=False) 
