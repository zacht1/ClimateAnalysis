#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 20 00:08:12 2025

@author: zach
"""
import os
import seaborn
import pandas as pd
import matplotlib.pyplot as plt

from scipy import stats

# os.chdir(os.path.dirname(os.path.dirname(os.path.abspath("__file__")))) # set working directory
os.chdir("/Users/zach/Documents/EOSC 442/eosc442_project")

# read all cleaned data sets
van_sealvl = pd.read_csv("./data/Van7735_SeaLvl_M_1950_2007.csv")
sj_sealvl = pd.read_csv("./data/StJohnA_SeaLvl_M_1957_2007.csv")

van_temp = pd.read_csv("./data/VanHarbourCS_Temp_M_1950_2007.csv")
sj_temp = pd.read_csv("./data/StJohnA_Temp_M_1950_2007.csv")

enso_oni = pd.read_csv("./data/ONI_M_1950_2007.csv")


# RESEARCH Q1 : linear correlation between Vancouver temperature and sea level
# ------------------------------------------------------------------------------------
# TODO : ryan



# RESEARCH Q2 : linear correlation between St. John's temperature and sea level
# ------------------------------------------------------------------------------------
# TODO : ryan




# RESEARCH Q3 : linear correlation between Vancouver temperature and St John's temperature'
# ------------------------------------------------------------------------------------
# TODO : ryan




# RESEARCH Q4 : linear correlation between Vancouver sea level and St John's sea level
# ------------------------------------------------------------------------------------
# TODO : zach

combined_slev = pd.merge(van_sealvl, sj_sealvl, on="date", suffixes=("_van", "_sj"))

corr_sea_lvl, p_value_sea_lvl = stats.pearsonr(combined_slev["sea_lvl_van"], combined_slev["sea_lvl_sj"])

plt.figure(figsize=(8, 6))
seaborn.regplot(x=combined_slev["sea_lvl_van"], y=combined_slev["sea_lvl_sj"])
plt.xlabel("Vancouver Sea Level (m)")
plt.ylabel("St. John's Sea Level (m)")
plt.title("Correlation between Vancouver and St. John's Sea Levels")
# plt.grid(True)
plt.show()

plt.savefig('van_sj_sealvl_corr.png')


# RESEARCH Q5 : linear correlation between Vancouver temperature and ONI
# ------------------------------------------------------------------------------------
# TODO : zach

van_temp["date"] = pd.to_datetime(van_temp["date"])
enso_oni["date"] = pd.to_datetime(enso_oni["date"])

van_temp["year_month"] = van_temp["date"].dt.to_period("M")
enso_oni["year_month"] = enso_oni["date"].dt.to_period("M")

combined_data = pd.merge(van_temp, enso_oni, on="year_month", suffixes=("_temp", "_oni"))

plt.figure(figsize=(8, 6))
seaborn.regplot(x=combined_data["mean_temp"], y=combined_data["oni"])
plt.xlabel("Vancouver Temperature (ºC)")
plt.ylabel("Oceanic Nino Index")
plt.title("Correlation between Vancouver Air Temperature and Oceanic Nino Index")
plt.show()

plt.savefig('vantemp_oni_corr.png')


# RESEARCH Q6 : linear correlation between St John's temperature and INO
# ------------------------------------------------------------------------------------

sj_temp["date"] = pd.to_datetime(sj_temp["date"])
sj_temp["year_month"] = sj_temp["date"].dt.to_period("M")

combined_data = pd.merge(sj_temp, enso_oni, on="year_month", suffixes=("_temp", "_oni"))

plt.figure(figsize=(8, 6))
seaborn.regplot(x=combined_data["mean_temp"], y=combined_data["oni"])
plt.xlabel("St. John's Temperature (ºC)")
plt.ylabel("Oceanic Nino Index")
plt.title("Correlation between St John's Air Temperature and Oceanic Nino Index")
plt.show()

plt.savefig('sjtemp_oni_corr.png')

