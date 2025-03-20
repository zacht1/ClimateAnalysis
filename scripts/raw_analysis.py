#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 28 15:49:19 2025

@author: zach
"""

import pandas as pd
import statsmodels.api as sm
import matplotlib.pyplot as plt
import matplotlib.patches as patches

# --------- Vancouver Sea Level
van_sealvl = pd.read_csv("Van7735_SeaLevel_Daily_1950_2020.csv", skiprows = 7, usecols = [0,1])
van_sealvl["Obs_date"] = pd.to_datetime(van_sealvl["Obs_date"], format = "%Y/%m/%d")

van_sealvl["rolling_mean"] = van_sealvl["SLEV(metres)"].rolling(window=365).mean()

van_sealvl.set_index("Obs_date", inplace = True)
van_sealvl_monthly = van_sealvl.resample("M").mean()

valid_days_per_month = van_sealvl["SLEV(metres)"].resample("M").count()
van_sealvl_monthly = van_sealvl_monthly[valid_days_per_month >= 20]

plt.figure(figsize = (12,8))

plt.subplot(2, 1, 1)
plt.plot(van_sealvl["SLEV(metres)"], marker = 'o', linestyle = 'None', label = "Daily Sea Level")
plt.tick_params(axis='both', labelsize=14)
plt.xlabel("Date", fontsize = 16)
plt.ylabel("Sea Level", fontsize = 16)
plt.title("Daily Mean Water Level Data for Vancouver BC, Station 7735", fontsize = 18)
plt.legend(fontsize = 13)

plt.subplot(2, 1, 2)
plt.plot(van_sealvl_monthly["SLEV(metres)"], marker = 'o', linestyle = 'None', label = "Monthly Sea Level")
plt.plot(van_sealvl_monthly["rolling_mean"], label = "365-Day Rolling Mean", linewidth = 3)
plt.tick_params(axis='both', labelsize=14)
plt.xlabel("Date", fontsize = 16)
plt.ylabel("Sea Level", fontsize = 16)
plt.title("Monthly Mean Water Level Data for Vancouver BC, Station 7735", fontsize = 18)
plt.legend(fontsize = 13)

plt.tight_layout()
plt.show()


# --------- St John's Sea Level
sj_sealevel = pd.read_csv("905-01-JAN-1950_slev.csv", skiprows = 7, usecols = [0,1])
sj_sealevel["Obs_date"] = pd.to_datetime(sj_sealevel["Obs_date"], format = "%Y/%m/%d")

sj_sealevel["rolling_mean"] = sj_sealevel["SLEV(metres)"].rolling(window=365).mean()

sj_sealevel.set_index("Obs_date", inplace = True)
sj_sealevel_monthly = sj_sealevel.resample("M").mean()

valid_days_per_month = van_sealvl["SLEV(metres)"].resample("M").count()
van_sealvl_monthly = van_sealvl_monthly[valid_days_per_month >= 20]

plt.figure(figsize = (12,8))

plt.subplot(2, 1, 1)
plt.plot(sj_sealevel["SLEV(metres)"], marker = "o", linestyle = "None", label = "Daily Sea Level")
plt.tick_params(axis='both', labelsize=14)
plt.title("Daily Mean Water Level Data for St. John's NL, Station 65", fontsize = 18)
plt.xlabel("Date", fontsize = 16)
plt.ylabel("Sea Level", fontsize = 16)
plt.legend(fontsize = 13)

plt.subplot(2, 1, 2)
plt.plot(sj_sealevel_monthly["SLEV(metres)"], marker = "o", linestyle = "None", label = "Monthly Sea Level")
plt.plot(sj_sealevel_monthly["rolling_mean"], label = "365-Day Rolling Mean", linewidth = 3)
plt.title("Monthly Mean Water Level Data for St. John's NL, Station 65", fontsize = 18)
plt.xlabel("Date", fontsize = 16)
plt.ylabel("Sea Level", fontsize = 16)
plt.legend(fontsize = 13)

plt.tight_layout()
plt.show()


# -------- Vancouver Temperature
van_temp = pd.read_csv("VanHarbourCS_Temp_Monthly_1925_2007.csv")
van_temp["Date/Time"] = pd.to_datetime(van_temp["Date/Time"], format = "%Y-%m")

van_temp["rolling_mean"] = van_temp["Mean Temp (°C)"].rolling(window=12).mean()

van_temp.set_index("Date/Time", inplace = True)

plt.figure(figsize = (12,8))

plt.subplot(2, 1, 1)
plt.plot(van_temp["Mean Temp (°C)"], marker = 'o', linestyle = 'None', label = "Monthly Temperature")
plt.tick_params(axis='both', labelsize=14)
plt.title("Monthly Mean Temperature for Vancouver BC, Harbour CS Station", fontsize = 18)
plt.xlabel("Date", fontsize = 16)
plt.ylabel("Temperature (°C)", fontsize = 16)
plt.legend(fontsize = 13)

plt.subplot(2, 1, 2)
plt.plot(van_temp.loc["1950-01-01":"2007-12-31"]["Mean Temp (°C)"], marker = 'o', linestyle = 'None', label = "Monthly Temperature")
plt.plot(van_temp.loc["1950-01-01":"2007-12-31"]["rolling_mean"], label = "12-Month Rolling Mean", linewidth = 3)

# Get current axis and add a transparent rectangle
ax = plt.gca()
rect = patches.Rectangle(
    (pd.Timestamp("1962-05-01"), van_temp["Mean Temp (°C)"].min()),  # Bottom-left corner
    pd.Timestamp("1965-03-01") - pd.Timestamp("1962-05-01"),  # Width (duration)
    van_temp["Mean Temp (°C)"].max() - van_temp["Mean Temp (°C)"].min(),  # Height
    color="grey",
    alpha=0.3
)
ax.add_patch(rect)

plt.tick_params(axis='both', labelsize=14)
plt.title("Monthly Mean Temperature for Vancouver BC, Harbour CS Station", fontsize = 18)
plt.xlabel("Date", fontsize = 16)
plt.ylabel("Temperature (°C)", fontsize = 16)
plt.legend(fontsize = 13)

plt.tight_layout()
plt.show()

# -------- St John's Temperature
sj_temp = pd.read_csv("StJohnA_Temp_Monthly_1942_2012.csv")
sj_temp["Date/Time"] = pd.to_datetime(sj_temp["Date/Time"], format = "%Y-%m")

sj_temp["rolling_mean"] = sj_temp["Mean Temp (°C)"].rolling(window=12).mean()

sj_temp.set_index("Date/Time", inplace = True)

plt.figure(figsize = (12,8))

plt.subplot(2, 1, 1)
plt.plot(sj_temp.loc["1950-01-01":"2007-12-31"]["Mean Temp (°C)"], marker = 'o', linestyle = 'None', label = "Monthly Temperature")
plt.tick_params(axis='both', labelsize=14)
plt.title("Monthly Mean Temperature for St John's NL, Station A", fontsize = 18)
plt.xlabel("Date", fontsize = 16)
plt.ylabel("Temperature (°C)", fontsize = 16)
plt.legend(fontsize = 13)

plt.subplot(2, 1, 2)
plt.plot(sj_temp.loc["1950-01-01":"2007-12-31"]["Mean Temp (°C)"], marker = 'o', linestyle = 'None', label = "Monthly Temperature")
plt.plot(sj_temp.loc["1950-01-01":"2007-12-31"]["rolling_mean"], label = "12-Month Rolling Mean", linewidth = 3)
plt.tick_params(axis='both', labelsize=14)
plt.title("Monthly Mean Temperature for St John's NL, Station A", fontsize = 18)
plt.xlabel("Date", fontsize = 16)
plt.ylabel("Temperature (°C)", fontsize = 16)
plt.legend(fontsize = 13)

plt.tight_layout()
plt.show()

#------- El Nino Data
enso = pd.read_fwf("oni_data.txt")

enso = pd.melt(enso, id_vars=["Year"], var_name="Date", value_name="ONI")
enso["Date"] = enso["Date"] + "-" + enso["Year"].astype(str)
enso["Date"] = pd.to_datetime(enso["Date"], format="%b-%Y")
enso = enso.drop(columns="Year")

enso["rolling_mean"] = enso["ONI"].rolling(window=12).mean()

plt.figure(figsize = (12,6))
plt.plot(enso["Date"], enso["ONI"], marker = "o", linestyle = "None")
plt.tick_params(axis='both', labelsize=14)
plt.title("Oceanic Niño Index", fontsize=18)
plt.xlabel("Date", fontsize=16)
plt.ylabel("Oceanic Niño Index", fontsize=16)
plt.legend(fontsize=13)


