# Time_Series_Anomalies_Detection

**Time series Analysis and anomalies detection of Oil and Gas plant**

Objective:
A typical work flow for data science team to detect anomalies in oil and gas plants are as follow:
1. Defining objectives
2. collecting and storing data
3. Preprocessing and cleaning data
4. Conducting Exploratory Data Analysis
5. Selecting and training Models
6. Deploying model for real time anomalies detection
7. setting up alerting and reporting mechanism
8. continuously improving the system based on feedback
9. Documenting the process and knowledge sharing
10. Providing support to ensure compliances and security

_________________________________________________________
Role:

# Defining objectives
* Requirement gathering: Collaborated with client to gather requirements and understand the context like according to them if missing value is below5% we could discard them,else we have to replace them using relevant technique. Also what are the prerequisite. Brief introduction about the plant, sensors and data.

* Identify Data Sources: Determine the sensors and systems that provide relevant data 
e.g., pressure sensors, temperature sensors, flow meters.

# Data Collection from OSI PI server
Here we typically deal with both real-time data and historical data. Here’s a detailed breakdown:
The real-time data is used for monitoring current conditions and detecting anomalies as they happen.
Historical data is crucial for training machine learning models. It provides a comprehensive view of past conditions, including normal operations plant and any anomalies that have occurred.

* Set Up Data Pipeline: Established a data pipeline to collect data from platforms like OSI PI Server
The Sensor Link extension connects RapidMiner to the OSIsoft PI System. It enable users to seamlessly access and process industrial data within RapidMiner for analysis, modeling, and reporting.
steps:
Install the Sensor Link Extension through RapidMiner Marketplace.
Using operators like PI Connector we could connect OSI PI system to RM studio.
Configure the Connection by entering the connection details such as server address, authentication credentials, and data point tags.
Use the Read PI Data operator to fetch data. the starting and end time was from Jan 2019 to Jan 2022.

**Analyzing Dataset**
Here are some potential column names for such a dataset:

Timestamp: The date and time when the sensor readings were recorded.
Sensor_ID: Unique identifier for each sensor in the plant.
Pressure: Pressure readings from various parts of the plant (e.g., pipes, tanks).
Temperature
Flow_Rate: The rate at which oil or gas is flowing through pipes or other equipment.
Vibration: Vibration levels of machinery and equipment.
Humidity: Humidity levels in different areas of the plant.
Level: Liquid levels in tanks or reservoirs.
Valve_Position: The position of control valves (e.g., open, closed, percentage open).
Pump_Status: The operational status of pumps (e.g., on, off, malfunctioning).
Motor_Current: Electrical current readings for motors.
Gas_Concentration: Concentration levels of different gases (e.g., methane, carbon dioxide).
Corrosion_Rate: Measurements of corrosion rates on pipes and equipment.
pH_Level: pH levels of liquids in different parts of the plant.
Flow_Turbulence: Measurements of flow turbulence in pipes.
Compressor_Pressure: Pressure readings specific to compressors.
Compressor_Temperature: Temperature readings specific to compressors.
Alarm_Status: Status of various alarms (e.g., triggered, not triggered).
Maintenance_Flag: Indication of scheduled or unscheduled maintenance activities.
Operational_Mode: The current operational mode of the plant (e.g., startup, shutdown, normal operation).

# Data Preprocessing

**Handeling Misiing Values**
Using "Replace Missing Value" operator in RapidMiner
In Python: using execute python operator in rapidminer.
* Calculate the percentage of missing values
    missing_percentage = df['value'].isnull().sum() / len(df) * 100

* If missing values are less than 5%, remove them
    if missing_percentage < 5:
        df = df.dropna()
    else:
    // Otherwise, use imputation techniques (e.g., mean, median)
        df['value'].fillna(df['value'].mean(), inplace=True)

***Techniques for Handling Missing Values***
1. Remove Missing Values: This method involves deleting rows or columns with missing values.
When to use:
When the percentage of missing values is very low (typically less than 5%) or are randomly distributed and do not have a pattern.
2. Imputation : filling in the missing values with substituted values like mean, median, mode, and more advanced methods like K-Nearest Neighbors (KNN) imputation.
Mean Imputation-When the data is normally distributed without outliers.e.g, temperature sensor data in a stable environment.
Median Imputation-When the data has outliers or is skewed means few values are extremely high
Mode Imputation-Fill missing values with the mode (most frequent value) of the column.eg. in categorical column like sensor status

When to use: For categorical data or numerical data with many repeated values
3. Predictive Modeling : When the relationships between features are strong, and  have enough data to train a model.Example: Using a regression model to predict missing temperature values based on pressure and flow rate.
4. Interpolation
5. Filling with Constants or Category Modes: missing categorical data with a constant numerical value like 0.
6. Using Algorithms that Support Missing Values:  Using XGBoost or certain implementations of decision trees that can handle missing values directly.When you want to simplify preprocessing.

Suppose an important attribute have all the values as null then to solbve this:
If possible, retrieve historical data for the same attribute to infer potential values.
Create new features or transformations that might capture the essence of the missing attribute.
Use Correlation Matrix to find features that are highly correlated with important_feature.
* Use Linear Regression or other suitable operators to train a model on other features to predict important_attribute.
* Use Replace Missing Values with the predicted values.


**Deal with Outliers**
Outliers are data points that deviate significantly from the rest of the observations in a dataset.they can skew and mislead the results of data analysis. 
* Identifying Outliers
1. using statistical methods like IQR(Inter Quartile Range):
Identify outliers based on the 50% of the data spread means beyond that range there are outliers.
Example Calculation
Consider the dataset: [6, 7, 15, 36, 39, 40, 41, 42, 43, 47, 49]

Sort the Data: The data is already sorted.

Calculate Q1 and Q3:

Q1: The median of the first half (6, 7, 15, 36, 39) = 15
Q3: The median of the second half (41, 42, 43, 47, 49) = 43
Compute IQR:
IQR=𝑄3−𝑄1=43−15=28
Lower Bound: 𝑄1−1.5×IQR 
Upper Bound: 𝑄3+1.5×IQR
Any data points outside these bounds are considered outliers.
2. using visualization technique like scatter plot

* dealing with outliers:
By setting a threshold to cap outliers at a maximum or floor them at a minimum value.
By simply remove the outliers from the dataset if they are due to measurement errors
By compressing the range of the data. 

**Remove Duplicates**
Check for and remove duplicate rows in the dataset.

**Correct Data Errors**
data type error, mislabeled categories.

**Normalization**
Process of maintaining uniform scale among all the attributes. All features scaled to same range. If some features have larger ranges they do not dominate the learning process.
because while using K means clustering algo or KNN then we need to calculate distance 

from sklearn.preprocessing import MinMaxScaler

# Example data
data = [[-1, 2], [-0.5, 6], [0, 10], [1, 18]]

# Apply Min-Max normalization
scaler = MinMaxScaler()
normalized_data = scaler.fit_transform(data)
print(normalized_data)

**Standardization**
also known as Z-score normalization in which the data point centered around zero and spread to 1. Meaning athe average distance of each point from mean should be equal say to 1.

Zi= (Xi−μ)/σ

Zi is the standardized value.
𝑋𝑖 is the original value.
μ is the mean of the original dataset.
σ is the standard deviation of the original dataset.

When to Use Normalization:
When the data does not follow a Gaussian distribution and When using algorithms that rely on the distance between data points, such as KNN, k-means, and neural networks.
When to Use Standardization:
When the data follows a Gaussian distribution.
When using algorithms that assume data is normally distributed, such as linear regression, logistic regression, and PCA.


Consider a dataset with features representing different measurements, such as height in centimeters and weight in kilograms. Even if both features follow a Gaussian distribution, their scales are different. 
![image discription](/Images/befor_standardization.PNG)
 The values of height_cm and weight_kg are plotted in their original units and the scales differ significantly.
![image discription](/Images/after_standardization.PNG)
The values are transformed to have a mean of zero and a standard deviation of one. The distributions are now on a common scale, allowing for easier comparison and analysis.

**Feature Engineering**
Feature engineering is the process of creating new features from raw data that make machine learning algorithms work better. It involves transforming, combining, and sometimes even creating new features from the existing data to improve the model's performance.

Here in oil and gas plant some feature creation was done:
Extract features like hour of the day
Change in pressure reading between consecutive time steps. This helped to detect sudden change and that might indicate anomalies.

# Selecting the model
overview of several algorithms and models used for time series anomaly detection,
1. Gaussian Mixture Model (GMM)
2. Autoencoders
3. K-Means Clustering
5. Long Short-Term Memory (LSTM) Networks
6. ARIMA (Autoregressive Integrated Moving Average)

# Training the model
Split data 70-80% for training, 10-15% for validating and 10-15% for testing

Initializing the model with approprieate parameters or hyperparameters
feed the training data through model,compute predictions and computing them to the actual target values, adjust parameter to minimize errors or loss (differences with actual values)
Defining the loss(cost) function that states how well the model predictions match the actual target example: MSE
Mean Squared Error

After training the data use validation techniques to ensure emprovements on new data. we check the outcome of model with past data and test on the next segment of data (or say some unseen set of data)in the same iteration.

# Cross validation
 involves dividing the dataset into multiple subsets (folds), training the model on several combinations of these subsets, and evaluating its performance.
RapidMiner provides operators and tools to perform cross-validation,
1. Temporal Split in RapidMiner:
Using the "Windowing" operator created rolling or sliding windows for time series cross-validation.
2. Cross-Validation Operators:
RapidMiner provides specific operators like Temporal Cross-Validation or Temporal Cross-Validation (Advanced) for handling time series data. These operators ensure that the temporal order is maintained during the validation process.

# setting up alert

After training the model, RapidMiner’s data exploration and visualization tools gave us to analyze the distribution of model scores (probabilities, reconstruction errors).

from the performance metrics,the  mean = 0.7 and kept threshold value as 0.7. Above this vale if data points occur or in a consecutive manner we set it as either alarming or warning condition after visualizing further. In order to increase precision for generating alert FP should be < TP. 
***Retuning:*** If we improve threshold value in order to decrease FP this is also called retuning.  

# Performance Visualization:
RapidMiner provides visualization tools to plot ROC curves, extension and operators for unsupervised learning like GMM and Autoencoders.
Use the Gaussian Mixture Model operator to model the probability densities of your data points.

________________________


 
