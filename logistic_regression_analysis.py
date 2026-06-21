# The following code to create a dataframe and remove duplicated rows is always executed and acts as a preamble for your script: 

# dataset = pandas.DataFrame(Dew point temperature(°C), Hour, Humidity(%), Rainfall(mm), Rented Bike Count, Snowfall (cm), Solar Radiation (MJ/m2), Temperature(°C), Visibility (10m), Wind speed (m/s))
# dataset = dataset.drop_duplicates()

# Paste or type your script code here:
# The following code to create a dataframe and remove duplicated rows is always executed and acts as a preamble for your script: 

# dataset = logical
# dataset = dataset.drop_duplicates()

# Paste or type your script code here:
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix
import seaborn as sns

df = dataset.dropna()

threshold = df['Rented Bike Count'].mean()
df['High_Demand'] = (df['Rented Bike Count'] > threshold).astype(int)

X = df[
    [
        'Temperature(°C)',
        'Humidity(%)',
        'Wind speed (m/s)',
        'Visibility (10m)',
        'Hour',
        'Rainfall(mm)',
        'Snowfall (cm)'
    ]
]

y = df['High_Demand']

model = LogisticRegression(max_iter=1000)
model.fit(X, y)

y_pred = model.predict(X)

acc = accuracy_score(y, y_pred)

cm = confusion_matrix(y, y_pred)

sns.heatmap(cm, annot=True, fmt='d', cmap='Blues')
plt.xlabel('Predicted')
plt.ylabel('Actual')
plt.title(f'Logistic Regression\nAccuracy = {acc:.2f}')
plt.show()
