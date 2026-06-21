# The following code to create a dataframe and remove duplicated rows is always executed and acts as a preamble for your script: 

# dataset = pandas.DataFrame(Dew point temperature(°C), Hour, Humidity(%), Rainfall(mm), Rented Bike Count, Snowfall (cm), Solar Radiation (MJ/m2), Temperature(°C), Visibility (10m), Wind speed (m/s))
# dataset = dataset.drop_duplicates()

# Paste or type your script code here:
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
import numpy as np

df = dataset.dropna()

X = df[
    [
        'Temperature(°C)',
        'Humidity(%)',
        'Wind speed (m/s)',
        'Visibility (10m)',
        'Hour',
        'Rainfall(mm)',
        'Snowfall (cm)',
        'Solar Radiation (MJ/m2)',
        'Dew point temperature(°C)'
    ]
]

y = df['Rented Bike Count']

model = LinearRegression()
model.fit(X, y)

y_pred = model.predict(X)

r2 = r2_score(y, y_pred)

plt.figure()
plt.scatter(y, y_pred, alpha=0.4)
plt.xlabel('Actual Bike Count')
plt.ylabel('Predicted Bike Count')
plt.title(f'Actual vs Predicted Bike Demand (R2 = {r2:.2f})')
plt.show()
