import pandas as pd

# read both datasets: the coordinates dataset and the official plant list
coordinates_df = pd.read_csv("../data/processed/plant_coordinates.csv")
#plant_list_df = pd.read_csv("../data/raw/IntensiveSurvey_2025_list_v3.csv", sep=';')

# standardize the 'PlantID' column in both DataFrames to ensure consistent formatting for merging
coordinates_df['PlantID'] = coordinates_df['PlantID'].astype(str).str.strip().str.upper()
#plant_list_df['PlantID'] = plant_list_df['PlantID'].astype(str).str.strip().str.upper()

# merge the two DataFrames on the 'PlantID' column to filter out any PlantIDs not present in the official list
clean_coordinates_list_df = pd.merge(coordinates_df, plant_list_df, on='PlantID', how='inner')
clean_coordinates_list_df = clean_coordinates_list_df.drop_duplicates(subset=['PlantID'])

# remove the unnecessary columns from the merged DataFrame, keeping only 'PlantID', 'Latitude', and 'Longitude'
clean_coordinates_list_df = clean_coordinates_list_df[['PlantID', 'Latitude', 'Longitude']]

# Save the filtered and cleaned coordinates list to a new CSV file
clean_coordinates_list_df.to_csv("../data/processed/unique_coordinates_list.csv", index=False)
