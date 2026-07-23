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
The raw dataset for this project is stored in `forJenny_IntensiveSurvey2025.csv`. 

Initial filtering is performed by running:

```bash
   python remove_NA.py
```
I then plot the data using my web_app/2_Map.py script to observed outliers. These are the observed outliers that I have either corrected or removed. 

| PlantID | Present in the IntensiveSurvey_2025_list | Comment | Removed |
| :--- | :---: | :---: | :---: |
| **PF0560** | NO | Only observed on 30/06/2025 and location was recorded at GR11. | YES |
| **PF5665** | NO | PE5665 exist and I think it was a typo (PF instead of PE) because PF5665 does not exist in the list and PE5665 was not recorded 07/07/2025 what PF5665 occurs. | NO (PE5665 -> PF5665) |
| **PE0131** | NO | PF0131 exists and was not recorded on the same day as PE0131, probably a typo | NO (PE0131 -> PF0131) |
| **PF0251** | NO | Only observed on the 19/06/2025. Comment says dead. | YES |
| **PE4507** | NO | Only observed on the 19/06/2025. No matching PF-id. | YES |
| **PF3512** | NO | Probably a mix up with PE3512 who was in the intensive survey | NO (PF3512 -> PE3512) |
| **PE2365** | NO | Only observed on the 23/06/2025. | YES |
| **PD2945** | NO | Probably a mix up with PE2945 (that was recorded for 4 days but not in the intensive survey list.) | YES |
| **PF0538** | NO | Probably a mix up with PE0538 | NO (PF0538 -> PE0538) |
| **PF0529** | NO | Probably a mix up with PE0529 | NO (PF0529 -> PE0529) |
| **PF3295** | NO | Proably a mix up with PE3295 | NO (PF3295 -> PE3295) |
| **PF3292** | NO | Proably a mix up with PE3295 | NO (PF3292 -> PE3292) | NO (PF3292 -> PE3292) |
| **PF0739** | NO | Only observed on the 12/06/2025. | YES |
| **PF0697** | NO | Only observed on the 07/07/2025. No PE or PE id exist. Checked all PF069* but they were recorded on the same date so no mix up with the last digit. | YES |
| **PE3570** | NO | Only observed on the 19/06/2025. No PF-id observed. | YES |

In addition to this there are 20+ individuals located in the lower yeloow flank 1 (LYF1) that was initally followed but then removed from the survey in June. They will not be removed from the data but they will not be included in the analysis.  
