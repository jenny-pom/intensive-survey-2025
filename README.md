# Intensive Plant Survey Analysis (2025)

Data analysis and visualization pipeline for tracking plant phenology, flower production, and fruit set efficiency over the 2025 growing season.

---

## 📋 Table of Contents
- [Project Overview](#-project-overview)
- [Dataset Structure](#-dataset-structure)
- [Installation & Setup](#-installation--setup)
- [Key Analyses & Visualizations](#-key-analyses--visualizations)
- [Handling Anomalies & Outliers](#-handling-anomalies--outliers)
- [Contributing](#-contributing)

---

## 🌸 Project Overview
This project processes field data from the `Intensive_Survey_2025.csv` dataset. It tracks the life cycle timelines (phenology) of various plant samples, specifically isolating and contrasting standard samples against **"PF" genotypes** (case-insensitive tracking).

The goal is to determine:
1. **Peak Bloom Windows:** When does the community hit maximum flower density?
2. **Fruit Set Success Rate:** The average ratio of fruits successfully produced per flower.

---

## 📊 Dataset Structure
The scripts expect a CSV file with the following core columns:
* `end` (Datetime): The date the observation window concluded (used as the timeline index).
* `Plant_ID` (String): The unique identifier for individual plants (e.g., `pf-01`, `PF-02`, `control-05`).
* `Estim.Flowers.Nr` (Integer): Estimated count of open flowers.
* `Estim.Fruit.Nr` (Integer): Estimated count of set fruits.

---

## 💻 Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/yourusername/plant-survey-analysis.git](https://github.com/yourusername/plant-survey-analysis.git)
   cd plant-survey-analysis
   
