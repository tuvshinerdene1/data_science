import datetime
import random

import numpy as np
import pandas as pd
import matplotlib
matplotlib.use('TkAgg')
import pylab
from sklearn.metrics import r2_score

pylab.rcParams["lines.linewidth"] = 4
pylab.rcParams["axes.titlesize"] = 20
pylab.rcParams["axes.labelsize"] = 20
pylab.rcParams["xtick.labelsize"] = 16
pylab.rcParams["ytick.labelsize"] = 16
pylab.rcParams["xtick.major.size"] = 7
pylab.rcParams["ytick.major.size"] = 7
pylab.rcParams["lines.markersize"] = 10
pylab.rcParams["legend.numpoints"] = 1


def create_datetime_from_int(date_int):
    try:
        date_str = str(date_int)
        year = int(date_str[:4])
        month = int(date_str[4:6])
        day = int(date_str[6:])

        return datetime.datetime(year, month, day)
    except (ValueError, TypeError, IndexError):
        return None


df = pd.read_csv("lab11_temperatures.csv")

df[df["CITY"] == "SEATTLE"]

df["DATE_R"] = df["DATE"].apply(create_datetime_from_int)

seattle_2015 = df[
    (df["CITY"] == "SEATTLE")
    & (df["DATE_R"] >= "2015-01-01")
    & (df["DATE_R"] <= "2015-12-31")
].copy()

days = np.array([( d- seattle_2015["DATE_R"].min()).days for d in seattle_2015["DATE_R"]])
temps = seattle_2015["TEMP"].values

pylab.figure(figsize=(12,6))
pylab.plot(days, temps, 'bo', alpha=0.3, label="Actual Temp")

degrees = [1,2,8]
colors = ['r', 'g', 'm']

for i, degree in enumerate(degrees):
    model_coeffs = np.polyfit(days, temps, degree)
    est_func = np.poly1d(model_coeffs)
    est_temps = est_func(days)
    r2 = r2_score(temps, est_temps)
    pylab.plot(days, est_temps, color=colors[i], label=f"Degree {degree}($R^2$:{r2:.3f})")

pylab.title("Seattle Temperatures 2015: Polyfit Analysis")
pylab.xlabel("Days since Jan 1st")
pylab.ylabel("Temperature")
pylab.legend()
pylab.show()
pylab.plot(seattle_2015["DATE_R"], seattle_2015["TEMP"])
prior_data = df[(df["CITY"] == "SEATTLE") & (df["DATE_R"].dt.year < 2015)]
# Convert dates to a continuous day count for training
train_days = np.array([(d - prior_data["DATE_R"].min()).days for d in prior_data["DATE_R"]])
train_temps = prior_data["TEMP"].values

# Fit a model to historical data
model_2014 = np.polyfit(train_days, train_temps, 2)
predict_func = np.poly1d(model_2014)

print("Model training complete. Ready to predict 2015 values.")