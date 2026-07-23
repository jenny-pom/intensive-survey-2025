# Intensive Plant Survey Analysis (2025)

This project analyzes data from a 2025 intensive survey tracking individual *Antirrhinum majus* plants (commonly named snapdragons). The collected data includes weekly flower and fruit counts, paired with an intial flowering-stem and fruting-stem count and an end-of-season flowering-stem and fruting-stem count. Ultimately, this survey supports a much larger, ongoing research project that studies the ecological and evolutionary dynamics within a hybrid zone of magenta (*A. majus pseudomajus*) and yellow (*A. majus striatum*) morphs.

---

## 📋 Table of Contents
- [Project Overview](#-project-overview)
- [Background Theory](#-background-theory)
- [Methodology](#-methodology)
- [Installation & Setup](#-installation--setup)
- [Key Analyses & Visualizations](#-key-analyses--visualizations)
- [Handling Anomalies & Outliers](#-handling-anomalies--outliers)
- [Conclusions](#-conclusion)

---

## Project Overview
The primary objective of the 2025 intensive survey was to conduct a smaller-scale follow-up to the more extensive intensive surveys carried out in 2021 and 2022. Together, these consecutive efforts establish a long-term dataset that tracks the same Antirrhinum majus individuals over multiple seasons to monitor cumulative floral and reproductive output. Building upon this foundation, the specific aim of this project is to analyze the 2025 dataset to evaluate the correlation between flower production and fruit yield. Specifically, we seek to determine whether a higher investment in floral displays directly translates to increased reproductive success. This allows us to investigate whether larger, older plants achieve higher fruit yields simply by producing more flowers, or if smaller individuals with fewer flowers can achieve a comparable or higher relative fruit yield. To address these questions, we will model total flower counts against final fruit production. Furthermore, as a secondary objective, we will explore the influence of phenotypic traits such as flower color to better understand how these characteristics affect fruit yield. Finally, we aim to map or visualize the spatial distribution of these intensive survey individuals by generating an interactive HTML file.

---

## Background Theory
- Life history paper
- Papers Seas sent
- Feys background
- how many lives does a snapdragon have?
- How long can snapdragons live? oldest plant is 11 year
INCLUDE:
* resource Allocation
* self comaptibility in majus
* seed predation
* lination limitation


---

## Methodology
During the 2025 field season, an intensive survey was conducted to monitor a maximum of 299 individual snapdragon plants. The survey transect spanned the lower hybrid core (LC), initiating in magenta flank 1 (LMF1) and extending into yellow flank 1 (LYF1). 

Upon initial inclusion, each individual was assigned a unique identification number and sampled according to standard sampling protocols (SOURCE). In addition, to minimize time searcing, a small highly visible red tape pieces was affixed to the stem of each plant included in the server to increase their visability. 

Monitoring occurred semi-weekly (every Monday and Thursday) over a nine-week period from May 26 to July 24, 2025. Additional individuals were incorporated into the dataset as the season progressed and new plants appeared. Sampling was strictly limited to accessible plants, defined as those safely reachable from the ground without the aid of specialized climbing equipment or ladders. Standard semi-weekly data collection included absolute counts of open flowers and mature fruits. 

To minimize inter-observer bias and maintain data consistency, all field measurements were performed by a fixed pair of volunteers that changed once in the middle of the season. Task allocation within the pair remained constant throughout the duration of the study. One volunteer consistently performed all visual counts (flowers, fruits, and stems), while the second cross-referenced plant IDs against a physical master sheet and recorded the metadata digitally using KoboToolbox on a mobile device.

---

## Installation & Setup

**Clone the repository:**
   ```bash
   git clone https://github.com/jenny-pom/intensive-survey-2025.git

   ```

---
## Data Cleaning
My raw data file is 'forJenny_IntensiveSurvey2025.csv' and I intially clean the file by removing all rows containing NA. These rows correspond to the point where the plant was introduced to th3 survey and only location and ID was recorded. 
```bash
   python remove_NA.py
```
I then plot the data in using my web_app/2_Map.py script to observed outliers. 
| PlantID | Present in the IntensiveSurvey_2025_list | Comment | Removed |
| --------------- | --------------- | --------------- |
| Row 1,  PF0560   | Row 1, NO   | Row 1, Only observed on 30/06/2025 and location was recorded at GR11.   | Yes   |
| Row 2, PF5665   | Row 2, NO   | Row 2, PE5665 exist and I think it was a typo (PF instead of PE) because PF5665 does not exist in the list and PE5665 was not recorded 07/07/2025 what PF5665 occurs.   | YES   |
| Row 3, Cell 1   | Row 3, Cell 2   | Row 3, Cell 3   | Row 3, Cell 4   |
| Row 4, Cell 1   | Row 4, Cell 2   | Row 4, Cell 3   | Row 4, Cell 4   |
| Row 5, Cell 1   | Row 5, Cell 2   | Row 5, Cell 3   | Row 5, Cell 4   |
| Row 6, Cell 1   | Row 6, Cell 2   | Row 6, Cell 3   | Row 6, Cell 4   |
| Row 7, Cell 1   | Row 7, Cell 2   | Row 7, Cell 3   | Row 7, Cell 4   |
| Row 8, Cell 1   | Row 8, Cell 2   | Row 8, Cell 3   | Row 8, Cell 4   |
| Row 9, Cell 1   | Row 9, Cell 2   | Row 9, Cell 3   | Row 9, Cell 4   |
| Row 10, Cell 1  | Row 10, Cell 2  | Row 10, Cell 3  | Row 10, Cell 4  |
| Row 11, Cell 1  | Row 11, Cell 2  | Row 11, Cell 3  | Row 11, Cell 4  |
| Row 12, Cell 1  | Row 12, Cell 2  | Row 12, Cell 3  | Row 12, Cell 4  |
| Row 13, Cell 1  | Row 13, Cell 2  | Row 13, Cell 3  | Row 13, Cell 4  |
| Row 14, Cell 1  | Row 14, Cell 2  | Row 14, Cell 3  | Row 14, Cell 4  |
| Row 15, Cell 1  | Row 15, Cell 2  | Row 15, Cell 3  | Row 15, Cell 4  |
| Row 16, Cell 1  | Row 16, Cell 2  | Row 16, Cell 3  | Row 16, Cell 4  |
| Row 17, Cell 1  | Row 17, Cell 2  | Row 17, Cell 3  | Row 17, Cell 4  |
| Row 18, Cell 1  | Row 18, Cell 2  | Row 18, Cell 3  | Row 18, Cell 4  |
| Row 19, Cell 1  | Row 19, Cell 2  | Row 19, Cell 3  | Row 19, Cell 4  |
| Row 20, Cell 1  | Row 20, Cell 2  | Row 20, Cell 3  | Row 20, Cell 4  |

   