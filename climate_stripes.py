#!/usr/bin/python
# -*- coding: utf-8 -*-

#------------------------------------------------------------------------------
# PROGRAM: climate_stripes.py
#------------------------------------------------------------------------------
# Version 0.1
# 11 June, 2020
# Dr Michael Taylor
# https://patternizer.github.io
# patternizer AT gmail DOT com
#------------------------------------------------------------------------------

#------------------------------------------------------------------------------
# IMPORT PYTHON LIBRARIES
#------------------------------------------------------------------------------
import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.cm as cm
from matplotlib import colors as mcol
from matplotlib.cm import ScalarMappable

#------------------------------------------------------------------------------
# DATA MUNGING
#------------------------------------------------------------------------------
filename = 'cottbus-berkley-earth.txt'
#df = pd.read_csv(filename, sep='\t', lineterminator='\r')
headings = ['Year', 'Month', 'Temperature-Raw', 'Anomaly-Raw', 'QC-Failed', 'Continuity-Breaks', 'Temperature-Adjusted', 'Anomaly-Adjusted', 'Temperature-Regional-Expectation', 'Anomaly-Regional-Expectation']
df = pd.DataFrame(columns = headings)
datain = pd.read_csv(filename, delim_whitespace=True, header=86)
for i in range(len(df.columns)):
    df[df.columns[i]] = datain.values[:,i]

da = pd.DataFrame()
da['Year'] = df.groupby(df['Year']).mean()['Year']
da['Mean-Temperature-Raw'] = df.groupby(df['Year']).mean()['Temperature-Raw'].values
da['Mean-Anomaly-Raw'] = df.groupby(df['Year']).mean()['Anomaly-Raw'].values
da['Mean-Temperature-Adjusted'] = df.groupby(df['Year']).mean()['Temperature-Adjusted'].values
da['Mean-Anomaly-Adjusted'] = df.groupby(df['Year']).mean()['Anomaly-Adjusted'].values
da['Mean-Temperature-Regional-Expectation'] = df.groupby(df['Year']).mean()['Temperature-Regional-Expectation'].values
da['Mean-Anomaly-Regional-Expectation'] = df.groupby(df['Year']).mean()['Anomaly-Regional-Expectation'].values

da = da[da['Year']>1900]

# Calculate 1971-2000 mean
    
mu_temperature_raw = da[(da['Year']>1970) & (da['Year']<2001)]['Mean-Temperature-Raw'].mean()
mu_temperature_adjusted = da[(da['Year']>1970) & (da['Year']<2001)]['Mean-Temperature-Adjusted'].mean()
mu_temperature_regional_expectation = da[(da['Year']>1970) & (da['Year']<2001)]['Mean-Temperature-Regional-Expectation'].mean()
mu_anomaly_raw = da[(da['Year']>1970) & (da['Year']<2001)]['Mean-Anomaly-Raw'].mean()
mu_anomaly_adjusted = da[(da['Year']>1970) & (da['Year']<2001)]['Mean-Anomaly-Adjusted'].mean()
mu_anomaly_regional_expectation = da[(da['Year']>1970) & (da['Year']<2001)]['Mean-Anomaly-Regional-Expectation'].mean()

# Compute standard deviation of the annual average temperatures between 1901-2000: color range +/- 2.6 standard deviations 

sigma_temperature_raw = da[(da['Year']>1900) & (da['Year']<2001)]['Mean-Temperature-Raw'].std()
sigma_temperature_adjusted = da[(da['Year']>1900) & (da['Year']<2001)]['Mean-Temperature-Adjusted'].std()
sigma_temperature_regional_expectation = da[(da['Year']>1900) & (da['Year']<2001)]['Mean-Temperature-Regional-Expectation'].std()
sigma_anomaly_raw = da[(da['Year']>1900) & (da['Year']<2001)]['Mean-Anomaly-Raw'].std()
sigma_anomaly_adjusted = da[(da['Year']>1900) & (da['Year']<2001)]['Mean-Anomaly-Adjusted'].std()
sigma_anomaly_regional_expectation = da[(da['Year']>1900) & (da['Year']<2001)]['Mean-Anomaly-Regional-Expectation'].std()

#------------------------------------------------------------------------------
# Mean Annual Temperature - Comparison plot
#------------------------------------------------------------------------------
x = da['Year']
y = da['Mean-Temperature-Raw']

fig, ax = plt.subplots(figsize=((15/3.78)*3.78, (15/3.78)*1.89))
plt.bar(x, da['Mean-Temperature-Raw'], color='lightgrey', label='Raw')
plt.plot(x, da['Mean-Temperature-Adjusted'], color='red', label='Adjusted')
plt.plot(x, da['Mean-Temperature-Regional-Expectation'], color='black', label='Regional Expectation')
plt.legend()
plt.title('Mean annual temperature: Cottbus (Berkeley-Earth)')
plt.savefig('cottbus-berkeley-earth-Mean-Temperature.png')

#------------------------------------------------------------------------------
# Mean Annual Temperature Anomaly - Raw
#------------------------------------------------------------------------------
x = da['Year']
y = da['Mean-Temperature-Raw']
cmap = plt.cm.get_cmap('coolwarm')

mu = mu_temperature_raw
sigma = sigma_temperature_raw
maxval = +2.6 * sigma
minval = -2.6 * sigma

fig, ax = plt.subplots(figsize=((15/3.78)*3.78, (15/3.78)*1.89))
plt.bar(x, y-mu, color=cm.coolwarm((y-mu)/maxval+0.5))
ax.axis('off')
sm = ScalarMappable(cmap=cmap, norm=plt.Normalize(min(y-mu),max(y-mu)))
sm.set_array([])
cbar = plt.colorbar(sm, shrink=0.5)
cbar.set_label('Raw (relative to 1971-2000 mean)', rotation=270, labelpad=25)
plt.title('Mean annual temperature anomaly: Cottbus (Berkeley-Earth)')
plt.savefig('cottbus-berkeley-earth-Mean-Anomaly-Raw.png')

#------------------------------------------------------------------------------
# Mean Annual Temperature Anomaly - Adjusted
#------------------------------------------------------------------------------
x = da['Year']
y = da['Mean-Temperature-Adjusted']
cmap = plt.cm.get_cmap('coolwarm')

mu = mu_temperature_adjusted
sigma = sigma_temperature_adjusted
maxval = +2.6 * sigma
minval = -2.6 * sigma

fig, ax = plt.subplots(figsize=((15/3.78)*3.78, (15/3.78)*1.89))
plt.bar(x, y-mu, color=cm.coolwarm((y-mu)/maxval+0.5))
ax.axis('off')
sm = ScalarMappable(cmap=cmap, norm=plt.Normalize(min(y-mu),max(y-mu)))
sm.set_array([])
cbar = plt.colorbar(sm, shrink=0.5)
cbar.set_label('Adjusted (relative to 1971-2000 mean)', rotation=270, labelpad=25)
plt.title('Mean annual temperature anomaly: Cottbus (Berkeley-Earth)')
plt.savefig('cottbus-berkeley-earth-Mean-Anomaly-Adjusted.png')

#------------------------------------------------------------------------------
# Mean Annual Temperature Anomaly - Regional Expectation
#------------------------------------------------------------------------------
x = da['Year']
y = da['Mean-Temperature-Regional-Expectation']
cmap = plt.cm.get_cmap('coolwarm')

mu = mu_temperature_regional_expectation
sigma = sigma_temperature_regional_expectation
maxval = +2.6 * sigma
minval = -2.6 * sigma

fig, ax = plt.subplots(figsize=((15/3.78)*3.78, (15/3.78)*1.89))
plt.bar(x, y-mu, color=cm.coolwarm((y-mu)/maxval+0.5))
ax.axis('off')
sm = ScalarMappable(cmap=cmap, norm=plt.Normalize(min(y-mu),max(y-mu)))
sm.set_array([])
cbar = plt.colorbar(sm, shrink=0.5)
cbar.set_label('Regional Expectation (relative to 1971-2000 mean)', rotation=270, labelpad=25)
plt.title('Mean annual temperature anomaly: Cottbus (Berkeley-Earth)')
plt.savefig('cottbus-berkeley-earth-Mean-Anomaly-Regional-Expectation.png')

#------------------------------------------------------------------------------
# CLIMATE STRIPES - Raw
#------------------------------------------------------------------------------
x = da['Year']
y = da['Mean-Temperature-Raw']
cmap = plt.cm.get_cmap('coolwarm')

mu = mu_temperature_raw
sigma = sigma_temperature_raw
maxval = +2.6 * sigma
minval = -2.6 * sigma

fig, ax = plt.subplots(figsize=((15/3.78)*3.78, (15/3.78)*1.89))
z = (y-mu)*0.0+1.0
colors = cmap((y-mu)/maxval+0.5)
ax.bar(x, z, color=colors, width=1.0)
ax.axis('off')
sm = ScalarMappable(cmap=cmap, norm=plt.Normalize(min(y-mu),max(y-mu)))
sm.set_array([])
cbar = plt.colorbar(sm, shrink=0.5)
cbar.set_label('Raw (relative to 1971-2000 mean)', rotation=270, labelpad=25)
plt.title('Mean annual temperature anomaly: Cottbus (Berkeley-Earth)')
plt.savefig('cottbus-berkeley-earth-Mean-Anomaly-Raw-stripes.png')

#------------------------------------------------------------------------------
# CLIMATE STRIPES - Adjusted
#------------------------------------------------------------------------------
x = da['Year']
y = da['Mean-Temperature-Adjusted']
cmap = plt.cm.get_cmap('coolwarm')

mu = mu_temperature_adjusted
sigma = sigma_temperature_adjusted
maxval = +2.6 * sigma
minval = -2.6 * sigma

fig, ax = plt.subplots(figsize=((15/3.78)*3.78, (15/3.78)*1.89))
z = (y-mu)*0.0+1.0
colors = cmap((y-mu)/maxval+0.5)
ax.bar(x, z, color=colors, width=1.0)
ax.axis('off')
sm = ScalarMappable(cmap=cmap, norm=plt.Normalize(min(y-mu),max(y-mu)))
sm.set_array([])
cbar = plt.colorbar(sm, shrink=0.5)
cbar.set_label('Adjusted (relative to 1971-2000 mean)', rotation=270, labelpad=25)
plt.title('Mean annual temperature anomaly: Cottbus (Berkeley-Earth)')
plt.savefig('cottbus-berkeley-earth-Mean-Anomaly-Adjusted-stripes.png')

#------------------------------------------------------------------------------
# CLIMATE STRIPES - Regional Expectation
#------------------------------------------------------------------------------
x = da['Year']
y = da['Mean-Temperature-Regional-Expectation']
cmap = plt.cm.get_cmap('coolwarm')

mu = mu_temperature_regional_expectation
sigma = sigma_temperature_regional_expectation
maxval = +2.6 * sigma
minval = -2.6 * sigma

fig, ax = plt.subplots(figsize=((15/3.78)*3.78, (15/3.78)*1.89))
z = (y-mu)*0.0+1.0
colors = cmap((y-mu)/maxval+0.5)
ax.bar(x, z, color=colors, width=1.0)
ax.axis('off')
sm = ScalarMappable(cmap=cmap, norm=plt.Normalize(min(y-mu),max(y-mu)))
sm.set_array([])
cbar = plt.colorbar(sm, shrink=0.5)
cbar.set_label('Regional Expectation (relative to 1971-2000 mean)', rotation=270, labelpad=25)
plt.title('Mean annual temperature anomaly: Cottbus (Berkeley-Earth)')
plt.savefig('cottbus-berkeley-earth-Mean-Anomaly-Regional-Expectation-stripes.png')

#--------------------------------------------------------------------------
print('** END')

     
