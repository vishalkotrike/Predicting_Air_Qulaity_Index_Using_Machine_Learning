
# CapstoneProject_DATA606

### Predicting Air Quality and Pollution Levels Using Machine Learning

This project is my Master's capstone project in Data Science. The goal is to develop a predictive model using historical data and meteorological factors to forecast air quality. The model will help identify trends, detect pollution peaks, and assist in data-driven decision-making.

## Table of Contents
1. [Introduction](#introduction)
2. [Objective](#objective)
3. [Data Collection](#data-collection)
4. [Methodology](#methodology)
5. [Results](#results)
6. [Conclusion](#conclusion)
7. [Limitations](#limitations)
8. [Future Directions](#futureDirections)
9. [How to Run the Project](#HowtoRuntheProject)


## Introduction
Air pollution is a critical problem that impacts both public health and the environment. According to the World Health Organization, air pollution causes millions of deaths each year, and it contributes significantly to climate change. With rising pollution levels in many parts of the world, there is an urgent need for tools that can predict air quality and help mitigate its negative impacts. This project aims to create a predictive model that forecasts Air Quality Index (AQI) levels, helping authorities and the public take preemptive actions.

## Objective
This project aims to create a predictive model that forecasts Air Quality Index (AQI) levels for the next day, helping authorities and the public take preemptive actions.

## Data Collection
The data used in this project was obtained from the U.S. Environmental Protection Agency (EPA). The datasets were downloaded using BeautifulSoup for web scraping, and the data is provided in CSV format. The datasets cover air quality and meteorological data from 2016 to 2024, containing about 1.6 million rows each. The key variables include:

- **Pollutant Concentrations:** PM10, PM2.5, Nitrogen Dioxide (NO₂), Sulfur Dioxide (SO₂), Carbon Monoxide (CO).
- **Meteorological Variables:** Temperature, Humidity, Wind Speed, Wind Direction, Pressure.

After data collection, pre-processing steps such as cleaning, handling missing values, and normalization were conducted to prepare the data for modeling.

## Methodology
A supervised learning approach was used, focusing on regression models to predict AQI. The following models were tested:

- **CatBoost**
- **Random Forest**
- **Gradient Boosting**

Feature engineering was performed to enhance model accuracy, including adding lagged features and rolling averages to capture temporal dependencies in the data. The data was split into training and test sets to evaluate model performance.

## Results
The **Random Forest model** was chosen as the final model due to its superior performance. Key metrics include:

- **R² Score:** 0.89 on the test set.
- **Stability and Bias-Variance Trade-off:** The model demonstrated high stability, low overfitting, and a good trade-off between bias and variance compared to CatBoost and Gradient Boosting.

The model is effective at predicting AQI levels and can help forecast air quality trends, which is valuable for decision-makers.

## Conclusion
The predictive model developed in this project effectively forecasts AQI levels, allowing authorities and the public to take preemptive measures. Further improvement could be achieved by incorporating additional data sources or exploring advanced ensemble techniques.

## Limitations
The model cannot predict AQI during extreme events.

## Future Directions
**Predicting Additional Pollutants:** Extend the current model to predict other pollutants, such as PM2.5, PM10, SO2, NO2, and CO, beyond just the AQI. This would provide a more comprehensive view of air quality.

**Geographic and Socioeconomic Considerations:** Include additional variables such as geographic terrain type and socioeconomic factors to improve the accuracy of predictions and provide targeted warnings to specific vulnerable groups.

**Mobile Application Integration:** Develop a mobile application to make AQI predictions and information available on-the-go, increasing accessibility.

**Regional Comparisons:** Expand the dashboard's functionality to allow users to compare air quality between multiple regions or cities.


## How to Run the Project

**Data Collection:**

The data was collected from the U.S. Environmental Protection Agency (EPA) website.

We used web scraping with a tool called BeautifulSoup to download the datasets.

The collected datasets were provided in CSV format.

**Data Preparation:**

All the downloaded files were combined into a single dataset.

Pre-processing steps such as cleaning, handling missing values, and normalization were performed to prepare the data for modeling.

**Library Installation:**

Install the necessary libraries using the following command:

pip install -r requirements.txt

The libraries required include pandas, numpy, scikit-learn, catboost, matplotlib, seaborn, and streamlit.

**Literature Research and Exploratory Data Analysis (EDA):**

We conducted a literature review to understand the methodologies used in similar projects.

Exploratory Data Analysis (EDA) was performed to visualize the data and identify trends.

**Model Development:**

We developed ensemble models, including Random Forest, CatBoost, and Gradient Boosting.

The models were trained and evaluated using the prepared dataset.

**Project Structure and File Upload:**

The files were organized in a neat and structured format:

datasets/: Contains the air quality datasets from EPA.

notebooks/: Contains Jupyter notebooks for data preprocessing, EDA, and model training.

images/: Contains visualizations and plots used in the project.

docs/: Contains documentation and reports.

**Run the Dashboard:**

To demonstrate the results, a Streamlit dashboard was created.

To run the dashboard, use the following link:

[streamlit run dashboard.py](https://capstoneprojectdata606.streamlit.app/)


The dashboard allows users to predict AQI levels and see predicted AQI values interactively.

