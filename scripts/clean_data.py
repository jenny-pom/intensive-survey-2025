# Read the original dirty file
with open("../data/raw/forJenny_IntensiveSurvey2025.csv", "r", encoding="utf-8") as f:
    lines = f.readlines()

# I only want to keep the lines that doesn't contain the NA string
target_string = "NA,NA,NA,NA,NA,NA,NA,NA,NA,NA,NA,NA,NA,NA"
clean_lines = [line for line in lines if target_string not in line]

# I save it to a new file
with open("../data/processed/CLEAN_forJenny_IntensiveSurvey2025.csv", "w", encoding="utf-8") as f:
    f.writelines(clean_lines)

print(f"Done!")