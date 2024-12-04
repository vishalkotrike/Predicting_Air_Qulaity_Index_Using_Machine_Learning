
# CapstoneProject_DATA606

### Predicting Air Quality and Pollution Levels Using Machine Learning

This project is my Master's capstone project in Data Science. The goal is to develop a predictive model using historical data and meteorological factors to forecast air quality. The model will help identify trends, detect pollution peaks, and assist in data-driven decision-making.

## Table of Contents
1. [Introduction](#introduction)
2. [Data Collection](#data-collection)
3. [Methodology](#methodology)
4. [Results](#results)
5. [Conclusion](#conclusion)

## Introduction
Air pollution is a critical problem that impacts both public health and the environment. According to the World Health Organization, air pollution causes millions of deaths each year, and it contributes significantly to climate change. With rising pollution levels in many parts of the world, there is an urgent need for tools that can predict air quality and help mitigate its negative impacts. This project aims to create a predictive model that forecasts Air Quality Index (AQI) levels, helping authorities and the public take preemptive actions.

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

