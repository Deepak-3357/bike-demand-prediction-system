# The following code to create a dataframe and remove duplicated rows is always executed and acts as a preamble for your script: 

# dataset = pandas.DataFrame(Functioning Day, Holiday, Hour, Humidity(%), Rented Bike Count, Temperature(°C), Visibility (10m), Wind speed (m/s), Seasons)
# dataset = dataset.drop_duplicates()

# Paste or type your script code here:
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestRegressor

# Data from Power BI
df = dataset.copy()

# Rename columns for simplicity
df.rename(columns={
    'Rented Bike Count': 'BikeCount',
    'Temperature(°C)': 'Temp',
    'Humidity(%)': 'Humidity',
    'Wind speed (m/s)': 'Wind',
    'Visibility (10m)': 'Visibility'
}, inplace=True)

# Encode categorical columns
df['Seasons'] = df['Seasons'].astype('category').cat.codes
df['Holiday'] = df['Holiday'].astype('category').cat.codes
df['Functioning Day'] = df['Functioning Day'].astype('category').cat.codes

# Features & target
X = df[['Hour', 'Temp', 'Humidity', 'Wind', 'Visibility',
        'Seasons', 'Holiday', 'Functioning Day']]
y = df['BikeCount']

# Train model
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X, y)

# Predict (IMPORTANT: X not x)
df['Predicted'] = model.predict(X)

# Plot
plt.figure()
plt.scatter(df['Hour'], df['BikeCount'], label='Actual', alpha=0.5)
plt.scatter(df['Hour'], df['Predicted'], label='Predicted', alpha=0.5)
plt.xlabel("Hour")
plt.ylabel("Bike Demand")
plt.title("Seoul Bike Demand Prediction")
plt.legend()
plt.show()


