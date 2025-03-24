#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 28 15:49:19 2025

@author: zach
"""
import os
import pandas as pd
import statsmodels.api as sm
import matplotlib.pyplot as plt
import matplotlib.patches as patches

# os.chdir(os.path.dirname(os.path.dirname(os.path.abspath("__file__")))) # set working directory
os.chdir("/Users/zach/Documents/EOSC 442/eosc442_project")

# --------- Vancouver Sea Level
van_sealvl = pd.read_csv("./data/raw/Van7735_SeaLevel_Daily_1950_2020.csv", skiprows = 7, usecols = [0,1])
van_sealvl["Obs_date"] = pd.to_datetime(van_sealvl["Obs_date"], format = "%Y/%m/%d")

van_sealvl["rolling_mean"] = van_sealvl["SLEV(metres)"].rolling(window=365).mean()
van_sealvl = van_sealvl.rename(columns={"Obs_date":"date", "SLEV(metres)":"sea_lvl"})

van_sealvl.set_index("date", inplace = True)
van_sealvl_monthly = van_sealvl.resample("M").mean()

valid_days_per_month = van_sealvl["sea_lvl"].resample("M").count()
van_sealvl_monthly = van_sealvl_monthly[valid_days_per_month >= 20]
van_sealvl_monthly = van_sealvl_monthly.loc[van_sealvl_monthly.index < pd.to_datetime("2008-01-01")]

van_sealvl_monthly.to_csv("./data/Van7735_SeaLvl_M_1950_2007.csv")

plt.figure(figsize = (12,8))

plt.subplot(2, 1, 1)
plt.plot(van_sealvl["sea_lvl"], marker = 'o', linestyle = 'None', label = "Daily Sea Level")
plt.tick_params(axis='both', labelsize=14)
plt.xlabel("Date", fontsize = 16)
plt.ylabel("Sea Level", fontsize = 16)
plt.title("Daily Mean Water Level Data for Vancouver BC, Station 7735", fontsize = 18)
plt.legend(fontsize = 13)

plt.subplot(2, 1, 2)
plt.plot(van_sealvl_monthly["sea_lvl"], marker = 'o', linestyle = 'None', label = "Monthly Sea Level")
plt.plot(van_sealvl_monthly["rolling_mean"], label = "365-Day Rolling Mean", linewidth = 3)
plt.tick_params(axis='both', labelsize=14)
plt.xlabel("Date", fontsize = 16)
plt.ylabel("Sea Level", fontsize = 16)
plt.title("Monthly Mean Water Level Data for Vancouver BC, Station 7735", fontsize = 18)
plt.legend(fontsize = 13)

plt.tight_layout()
plt.show()


# --------- St John's Sea Level
sj_sealevel = pd.read_csv("./data/raw/905-01-JAN-1950_slev.csv", skiprows = 7, usecols = [0,1])
sj_sealevel["Obs_date"] = pd.to_datetime(sj_sealevel["Obs_date"], format = "%Y/%m/%d")

sj_sealevel["rolling_mean"] = sj_sealevel["SLEV(metres)"].rolling(window=365).mean()
sj_sealevel = sj_sealevel.rename(columns={"Obs_date":"date", "SLEV(metres)":"sea_lvl"})

sj_sealevel.set_index("date", inplace = True)
sj_sealevel_monthly = sj_sealevel.resample("M").mean()

valid_days_per_month = sj_sealevel["sea_lvl"].resample("M").count()
sj_sealevel_monthly = sj_sealevel_monthly[valid_days_per_month >= 20]
sj_sealevel_monthly = sj_sealevel_monthly.loc[sj_sealevel_monthly.index < pd.to_datetime("2008-01-01")]

sj_sealevel_monthly.to_csv("./data/StJohnA_SeaLvl_M_1957_2007.csv")

plt.figure(figsize = (12,8))

plt.subplot(2, 1, 1)
plt.plot(sj_sealevel["sea_lvl"], marker = "o", linestyle = "None", label = "Daily Sea Level")
plt.tick_params(axis='both', labelsize=14)
plt.title("Daily Mean Water Level Data for St. John's NL, Station 65", fontsize = 18)
plt.xlabel("Date", fontsize = 16)
plt.ylabel("Sea Level", fontsize = 16)
plt.legend(fontsize = 13)

plt.subplot(2, 1, 2)
plt.plot(sj_sealevel_monthly["sea_lvl"], marker = "o", linestyle = "None", label = "Monthly Sea Level")
plt.plot(sj_sealevel_monthly["rolling_mean"], label = "365-Day Rolling Mean", linewidth = 3)
plt.title("Monthly Mean Water Level Data for St. John's NL, Station 65", fontsize = 18)
plt.xlabel("Date", fontsize = 16)
plt.ylabel("Sea Level", fontsize = 16)
plt.legend(fontsize = 13)

plt.tight_layout()
plt.show()


# -------- Vancouver Temperature
van_temp = pd.read_csv("./data/raw/VanHarbourCS_Temp_Monthly_1925_2007.csv")
van_temp["Date/Time"] = pd.to_datetime(van_temp["Date/Time"], format = "%Y-%m")

van_temp["rolling_mean"] = van_temp["Mean Temp (°C)"].rolling(window=12).mean()

van_temp = van_temp[["Date/Time", "Mean Temp (°C)", "rolling_mean"]]
van_temp = van_temp.rename(columns={"Mean Temp (°C)":"mean_temp", "Date/Time":"date"})

van_temp.set_index("date", inplace = True)
van_temp = van_temp.loc[van_temp.index > pd.to_datetime("1959-12-31")]
van_temp = van_temp.loc[van_temp.index < pd.to_datetime("2008-01-01")]

van_temp.to_csv("./data/VanHarbourCS_Temp_M_1950_2007.csv")

plt.figure(figsize = (12,8))

plt.subplot(2, 1, 1)
plt.plot(van_temp["mean_temp"], marker = 'o', linestyle = 'None', label = "Monthly Temperature")
plt.tick_params(axis='both', labelsize=14)
plt.title("Monthly Mean Temperature for Vancouver BC, Harbour CS Station", fontsize = 18)
plt.xlabel("Date", fontsize = 16)
plt.ylabel("Temperature (°C)", fontsize = 16)
plt.legend(fontsize = 13)

plt.subplot(2, 1, 2)
plt.plot(van_temp["mean_temp"], marker = 'o', linestyle = 'None', label = "Monthly Temperature")
plt.plot(van_temp["rolling_mean"], label = "12-Month Rolling Mean", linewidth = 3)

# add rectangles for gaps in data
ax = plt.gca()
rect1 = patches.Rectangle(
    (pd.Timestamp("1962-05-01"), van_temp["mean_temp"].min()),  # Bottom-left corner
    pd.Timestamp("1965-03-01") - pd.Timestamp("1962-05-01"),  # Width (duration)
    van_temp["mean_temp"].max() - van_temp["mean_temp"].min(),  # Height
    color="grey",
    alpha=0.3
)
rect2 = patches.Rectangle(
    (pd.Timestamp("1988-04-01"), van_temp["mean_temp"].min()),  # Bottom-left corner
    pd.Timestamp("1989-09-01") - pd.Timestamp("1988-04-01"),  # Width (duration)
    van_temp["mean_temp"].max() - van_temp["mean_temp"].min(),  # Height
    color="grey",
    alpha=0.3
)
ax.add_patch(rect1)
ax.add_patch(rect2)

plt.tick_params(axis='both', labelsize=14)
plt.title("Monthly Mean Temperature for Vancouver BC, Harbour CS Station", fontsize = 18)
plt.xlabel("Date", fontsize = 16)
plt.ylabel("Temperature (°C)", fontsize = 16)
plt.legend(fontsize = 13)

plt.tight_layout()
plt.show()

# -------- St John's Temperature
sj_temp = pd.read_csv("./data/raw/StJohnA_Temp_Monthly_1942_2012.csv")
sj_temp["Date/Time"] = pd.to_datetime(sj_temp["Date/Time"], format = "%Y-%m")
sj_temp["rolling_mean"] = sj_temp["Mean Temp (°C)"].rolling(window=12).mean()

sj_temp = sj_temp[["Date/Time", "Mean Temp (°C)", "rolling_mean"]]
sj_temp = sj_temp.rename(columns={"Mean Temp (°C)":"mean_temp", "Date/Time":"date"})

sj_temp.set_index("date", inplace = True)
sj_temp = sj_temp.loc[sj_temp.index > pd.to_datetime("1949-12-31")]
sj_temp = sj_temp.loc[sj_temp.index < pd.to_datetime("2008-01-01")]

sj_temp.to_csv("./data/StJohnA_Temp_M_1950_2007.csv")

plt.figure(figsize = (12,8))

plt.subplot(2, 1, 1)
plt.plot(sj_temp["mean_temp"], marker = 'o', linestyle = 'None', label = "Monthly Temperature")
plt.tick_params(axis='both', labelsize=14)
plt.title("Monthly Mean Temperature for St John's NL, Station A", fontsize = 18)
plt.xlabel("Date", fontsize = 16)
plt.ylabel("Temperature (°C)", fontsize = 16)
plt.legend(fontsize = 13)

plt.subplot(2, 1, 2)
plt.plot(sj_temp["mean_temp"], marker = 'o', linestyle = 'None', label = "Monthly Temperature")
plt.plot(sj_temp["rolling_mean"], label = "12-Month Rolling Mean", linewidth = 3)
plt.tick_params(axis='both', labelsize=14)
plt.title("Monthly Mean Temperature for St John's NL, Station A", fontsize = 18)
plt.xlabel("Date", fontsize = 16)
plt.ylabel("Temperature (°C)", fontsize = 16)
plt.legend(fontsize = 13)

plt.tight_layout()
plt.show()

#------- El Nino Data
enso = pd.read_fwf("./data/raw/oni_data.txt")

enso = pd.melt(enso, id_vars=["Year"], var_name="Date", value_name="ONI")

enso["date"] = enso["Date"] + "-" + enso["Year"].astype(str)
enso["date"] = pd.to_datetime(enso["date"], format="%b-%Y")
enso = enso.drop(columns=["Year", "Date"])

enso["rolling_mean"] = enso["ONI"].rolling(window=12).mean()

enso = enso.rename(columns={"ONI":"oni"})

enso.set_index("date", inplace = True)

enso = enso.loc[enso.index > pd.to_datetime("1949-12-31")]
enso = enso.loc[enso.index < pd.to_datetime("2008-01-01")]
enso.to_csv("./data/ONI_M_1950_2007.csv")

plt.figure(figsize = (12,6))
plt.plot(enso["oni"], marker = "o", linestyle = "None")
plt.tick_params(axis='both', labelsize=14)
plt.title("Oceanic Niño Index", fontsize=18)
plt.xlabel("Date", fontsize=16)
plt.ylabel("Oceanic Niño Index", fontsize=16)
plt.legend(fontsize=13)


