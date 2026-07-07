# Intensive Plant Survey Analysis (2025)

This project analyzes data from a 2025 intensive survey tracking individual *Antirrhinum majus* plants (commonly named snapdragons). The collected data includes weekly flower and fruit counts, paired with biweekly flowering-stem and fruting-stem counts. Ultimately, this survey supports a larger, ongoing research project that studies the ecological and evolutionary dynamics within a hybrid zone of magenta (A. majus pseudomajus) and yellow (A. majus striatum) morphs.

---

## 📋 Table of Contents
- [Project Overview](#-project-overview)
- [Background Theory](#background-theory)
- [Methology] (#methology)
- [Installation & Setup](#-installation--setup)
- [Key Analyses & Visualizations](#-key-analyses--visualizations)
- [Handling Anomalies & Outliers](#-handling-anomalies--outliers)
- [Conclusions](#-conclusion)

---

## Project Aim
This project processes field data from the `Intensive_Survey_2025.csv` dataset that weekly tracked the estimated flower number, estimated fruit number and biweekly the number of flowering stems and number of fruiting stems of *Anthurium majus*. The selected plants were growing along the lower road (LRYF1, LRC and LRMF1) of the hybrid zone. The goal of the Survey is to generate a dataset that follows the same individuals of *Anthurium majus* for a longer period of time, tracking the plants flower production and seed production.

My project plan/Questions I am intrested in answering: 
- Look at the ratio of flower production and fruit production, does higher flower production result in higher fruit yield. Is there a correclation between this or not?
- I also want to create an interactive html file where the Pf samples are visualized as nots along the lower road and the user can walk through the time frame to see the change in the flower production. This html file should also contain plots of improtant and intresting biological questions that have not already been studied. 
- Also looking at if the age of the plant correspond to the flower production? Does older plants actually produce more flowers?
Also I want to add if the flower colour is related to the aount of flower production ratio to fruit yeild. Example: Does white hybrids have less fruits even thought they produce many flowers? 
- Maybe look at correlation of flowering stems and number of lfowers and number of fruiting stems. 
- Flowering effort correspond to fruit production. (Messure of fitness)

---

## Background Theory
- Life history paper
- Papers Seas sent
- Feys background
- how many lives does a snapdragon have?
- How long can snapdragons live? oldest plant is 11 year
- 

---

## Methology of the Intensive Server
During the 2025 field season, an intensive survey was conducted to monitor a maximum of 395 individual snapdragon plants. The survey transect spanned the lower hybrid core (LC), initiating in magenta flank 1 (LMF1) and extending into yellow flank 1 (LYF1). 

Upon initial inclusion, each individual was assigned a unique identification number and sampled according to standard sampling protocols (SOURCE). In addition, to minimize time searcing, a small highly visible red tape pieces was affixed to the stem of each plant included in the server to increase their visability. 

Monitoring occurred semi-weekly (every Monday and Thursday) over a nine-week period from May 26 to July 24, 2025. Additional individuals were incorporated into the dataset as the season progressed and new plants appeared. Sampling was strictly limited to accessible plants, defined as those safely reachable from the ground without the aid of specialized climbing equipment or ladders. Standard semi-weekly data collection included absolute counts of open flowers and mature fruits. On alternating Thursdays, this protocol was supplemented with biweekly assessments of total flowering and fruiting stem numbers. 

To minimize inter-observer bias and maintain data consistency, all field measurements were performed by a fixed pair of volunteers. Task allocation within the pair remained constant throughout the duration of the study. One volunteer consistently performed all visual counts (flowers, fruits, and stems), while the second cross-referenced plant IDs against a physical master sheet and recorded the metadata digitally using KoboToolbox on a mobile device.

---

## 💻 Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/yourusername/plant-survey-analysis.git](https://github.com/yourusername/plant-survey-analysis.git)
   cd plant-survey-analysis
   