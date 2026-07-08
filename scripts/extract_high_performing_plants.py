import pandas as pd
# Load your dataset
df = pd.read_csv('../data/raw/forJenny_IntensiveSurvey2025.csv')

# I will measure "high performing plants" as plants that hit 10+ flowers at least once during the season.

# This filters the dataframe for rows >= 10, then extracts unique Plant IDs
high_flower_rows = df[df['Estim.Flowers.Nr'] >= 10]
high_flower_plants = high_flower_rows['PlantID'].unique().tolist()

chosen_plant_ids = high_flower_plants

# Filter the original dataframe to only include these "high-performing"" individuals
df_high_performers = df[df['PlantID'].isin(chosen_plant_ids)]

# Save this high-performer subset to a new CSV file
df_high_performers.to_csv('../data/processed/high_flowering_plants.csv', index=True)


# --- PRINT SUMMARY STATS ---
print("--- FLOWER COUNT ANALYSIS ---")
print(f"Total unique plants in dataset: {df['PlantID'].nunique()}")
print(f"Number of plants that hit 10+ flowers at least once: {len(high_flower_plants)}")

print("\nFiltered dataset saved successfully as 'high_flowering_plants.csv'.")