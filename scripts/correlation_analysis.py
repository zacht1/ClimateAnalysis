#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 20 00:08:12 2025

@author: zach
"""
import os
import pandas as pd

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




# RESEARCH Q5 : linear correlation between Vancouver temperature and ONI
# ------------------------------------------------------------------------------------
# TODO : zach




# RESEARCH Q6 : linear correlation between St John's temperature and INO
# ------------------------------------------------------------------------------------
# TODO : zach


