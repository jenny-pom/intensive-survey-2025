import pandas as pd

df_large = pd.read_csv("../data/raw/IntensiveSurvey_2025_list_v3.csv", sep=';')
df_small = pd.read_csv("../data/processed/unique_coordinates_list.csv")

# Extract the IDs as sets (Replace 'PlantID' with your exact column header)
# Use .dropna() just in case an ID is missing or blank
df_large['PlantID'] = df_large['PlantID'].astype(str).str.upper()
df_small['PlantID'] = df_small['PlantID'].astype(str).str.upper()

# Find the difference
ids_large = set(df_large['PlantID'].dropna())
ids_small = set(df_small['PlantID'].dropna())
missing_in_small = ids_large.difference(ids_small)
missing_in_large = ids_small.difference(ids_large)

# Print the clear results to your terminal
print("\n=== COMPARISON RESULTS ===")
print(f"Total Unique IDs in Large File: {len(ids_large)}")
print(f"Total Unique IDs in Small File: {len(ids_small)}")

if missing_in_small:
    print(f"\n⚠️ The missing ID(s) from all_coordinates.csv: {missing_in_small}")
    
if missing_in_large:
    print(f"\n⚠️ IDs in all_coordinates.csv that aren't in the raw list: {missing_in_large}")
print("==========================\n")

# --- DUPLICATE HUNTING ---

# Find rows where the PlantID is duplicated
duplicates_large = df_large[df_large.duplicated(subset=['PlantID'], keep=False)]
duplicates_small = df_small[df_small.duplicated(subset=['PlantID'], keep=False)]

print("\n=== DUPLICATE ANALYSIS ===")

if not duplicates_large.empty:
    print(f"Found {len(duplicates_large)} duplicate rows in the Large File:")
    # Print the specific IDs and their row details
    print(duplicates_large[['PlantID']])
else:
    print("✓ No duplicate PlantIDs found in the Large File.")

if not duplicates_small.empty:
    print(f"\nFound {len(duplicates_small)} duplicate rows in the Small File:")
    print(duplicates_small[['PlantID']])
else:
    print("✓ No duplicate PlantIDs found in the Small File.")

# 2. Check for empty/blank ID rows that might be throwing off the row count
blank_large = df_large['PlantID'].isna().sum()
blank_small = df_small['PlantID'].isna().sum()
print(f"\nBlank/NaN IDs in Large File: {blank_large}")
print(f"Blank/NaN IDs in Small File: {blank_small}")
print("==========================\n")

#Result
"""
=== COMPARISON RESULTS ===
Total Unique IDs in Large File: 298
Total Unique IDs in Small File: 298
==========================


=== DUPLICATE ANALYSIS ===
⚠️ Found 2 duplicate rows in the Large File:
   PlantID
82  PF0643
92  PF0643
✓ No duplicate PlantIDs found in the Small File.

Blank/NaN IDs in Large File: 0
Blank/NaN IDs in Small File: 0
==========================
"""