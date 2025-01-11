# -*- coding: utf-8 -*-
"""Prediksi Performa Murid.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Veb8Aw31BL2oDCa2SHIuI0RBhCEErnyJ

# **Import Library**
"""

# Commented out IPython magic to ensure Python compatibility.
import gdown
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
# %matplotlib inline
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error
from sklearn.neighbors import KNeighborsRegressor
from sklearn.ensemble import RandomForestRegressor, AdaBoostRegressor

"""# **Data Loading**"""

url = 'https://drive.google.com/uc?id=1hWMo3PDw7DW2u3P0DnOSm4bS62Uzb6QJ'
output = 'student_performance.csv'

gdown.download(url, output, quiet=False)

data = pd.read_csv(output)

data.head()

"""# **Exploratory Data Analysis**"""

data.info()

data.describe()

# Check for missing values
missing_values = data.isnull().sum()
print("Missing values in each column:\n", missing_values)

# Check for invalid values
def check_invalid_values(column):
    return (data[column] <= 0).sum()

invalid_study_hours = check_invalid_values('Study Hours')
invalid_sleep_hours = check_invalid_values('Sleep Hours')
invalid_attendance = check_invalid_values('Attendance (%)')

print("Invalid Study Hours: ", invalid_study_hours)
print("Invalid Sleep Hours: ", invalid_sleep_hours)
print("Invalid Attendance: ", invalid_attendance)

# Visualize distribution of features
sns.boxplot(x=data['Study Hours'])

sns.boxplot(x=data['Sleep Hours'])

sns.boxplot(x=data['Attendance (%)'])

# Identify outliers using IQR method
numeric_features = ['Study Hours', 'Sleep Hours', 'Socioeconomic Score', 'Attendance (%)', 'Grades']
Q1 = data[numeric_features].quantile(0.25)
Q3 = data[numeric_features].quantile(0.75)
IQR = Q3 - Q1
data_cleaned = data[~((data[numeric_features] < (Q1 - 1.5 * IQR)) | (data[numeric_features] > (Q3 + 1.5 * IQR))).any(axis=1)]

print("Shape after removing outliers:", data_cleaned.shape)

# Visualize relationships
sns.pairplot(data_cleaned, diag_kind='kde')

plt.figure(figsize=(10, 8))
correlation_matrix = data_cleaned.corr().round(2)
sns.heatmap(data=correlation_matrix, annot=True, cmap='coolwarm', linewidths=0.5)
plt.title("Correlation Matrix for Numeric Features", size=20)

"""# **Data Preparation**"""

# Prepare data for modeling
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

X = data_cleaned.drop(["Grades"], axis=1)
y = data_cleaned["Grades"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1, random_state=42)

print(f'Total samples in dataset: {len(X)}')
print(f'Samples in training set: {len(X_train)}')
print(f'Samples in test set: {len(X_test)}')

# Standardize numeric features
scaler = StandardScaler()
numeric_features = ['Study Hours', 'Sleep Hours', 'Socioeconomic Score', 'Attendance (%)']
scaler.fit(X_train[numeric_features])
X_train[numeric_features] = scaler.transform(X_train[numeric_features])
X_test[numeric_features] = scaler.transform(X_test[numeric_features])

# Train models and evaluate performance
from sklearn.metrics import mean_squared_error
from sklearn.neighbors import KNeighborsRegressor
from sklearn.ensemble import RandomForestRegressor, AdaBoostRegressor

models = pd.DataFrame(index=['train_mse', 'test_mse'], columns=['KNN', 'RandomForest', 'Boosting'])

"""# **Model Development**"""

# KNN Regressor
knn = KNeighborsRegressor(n_neighbors=5)
knn.fit(X_train, y_train)
models.loc['train_mse', 'KNN'] = mean_squared_error(y_pred=knn.predict(X_train), y_true=y_train)
models.loc['test_mse', 'KNN'] = mean_squared_error(y_pred=knn.predict(X_test), y_true=y_test)

# Random Forest Regressor
rf = RandomForestRegressor(n_estimators=100, random_state=42)
rf.fit(X_train, y_train)
models.loc['train_mse', 'RandomForest'] = mean_squared_error(y_pred=rf.predict(X_train), y_true=y_train)
models.loc['test_mse', 'RandomForest'] = mean_squared_error(y_pred=rf.predict(X_test), y_true=y_test)

# AdaBoost Regressor
boosting = AdaBoostRegressor(n_estimators=50, learning_rate=0.1, random_state=42)
boosting.fit(X_train, y_train)
models.loc['train_mse', 'Boosting'] = mean_squared_error(y_pred=boosting.predict(X_train), y_true=y_train)
models.loc['test_mse', 'Boosting'] = mean_squared_error(y_pred=boosting.predict(X_test), y_true=y_test)

# Display MSE for all models
print(models)

# Visualize MSE comparison
fig, ax = plt.subplots()
models.T.plot(kind='bar', ax=ax)
plt.title('Model MSE Comparison')
plt.ylabel('MSE')
plt.xticks(rotation=0)
plt.grid(axis='y')
plt.show()

"""# **Testing**"""

# Prediction example
pred = X_test.iloc[:1]
predictions = {'y_true': y_test.iloc[:1]}
for name, model in {'KNN': knn, 'RandomForest': rf, 'Boosting': boosting}.items():
    predictions[f'pred_{name}'] = model.predict(pred).round(2)
pd.DataFrame(predictions)