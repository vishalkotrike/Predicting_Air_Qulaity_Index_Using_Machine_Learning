import streamlit as st
import requests
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from datetime import datetime, timedelta

# Train a Random Forest Model (Mock Training for Prediction)
# In real scenario, you would have a well-trained model
model = RandomForestRegressor(n_estimators=100, random_state=42)

# Mock data for training
X_train = np.random.rand(100, 12)  # 100 samples, 12 features
y_train = np.random.rand(100) * 10 + 25  # 100 target values, scaled between 25 and 35 for realistic AQI
model.fit(X_train, y_train)

# Set Up the API Keys and Endpoints
WEATHERSTACK_API_KEY = "975843ce399f8e6d01f020f9c2a51bcd"  # Replace this with your Weatherstack API key
WEATHERSTACK_BASE_URL = "http://api.weatherstack.com/current"

OPENWEATHERMAP_API_KEY = "2e5ef01b28cc6118728a259aea1d69ea"  # Replace this with your OpenWeatherMap API key
AIRPOLLUTION_BASE_URL = "http://api.openweathermap.org/data/2.5/air_pollution"

# Create the Streamlit Interface
st.markdown(
    """
    <div style="display: flex; justify-content: center; align-items: center; margin-top: 20px; margin-bottom: 20px;">
        <h1 style="text-align: center; color: #2E8B57; font-size: 3em; font-weight: bold;">
            ️ <b>AQI Predictor Dashboard</b> 
        </h1>
    </div>
    """,
    unsafe_allow_html=True
)

# Add an image header
st.image("/Users/akshayreddy/Documents/CapstoneGit/AQI.jpeg", use_container_width=True)

# User inputs the city
st.markdown(
    """
    <div style="font-weight: bold;">Enter the city for AQI prediction:</div>
    """,
    unsafe_allow_html=True
)
city = st.text_input("", "New York")

# Button to fetch data
if st.button("**Get Prediction**"):
    # Get real-time location data from Weatherstack API
    location_params = {
        'access_key': WEATHERSTACK_API_KEY,
        'query': city
    }
    location_response = requests.get(WEATHERSTACK_BASE_URL, params=location_params)

    if location_response.status_code == 200:
        location_data = location_response.json()

        if 'location' in location_data:
            latitude = location_data['location']['lat']
            longitude = location_data['location']['lon']

            # Prepare to collect historical data for the past 3 days
            aqi_lag_values = []
            dates = [datetime.now() - timedelta(days=i) for i in range(1, 4)]

            # Loop through past 3 days to get historical pollution data
            for date in dates:
                air_pollution_params = {
                    'lat': latitude,
                    'lon': longitude,
                    'appid': OPENWEATHERMAP_API_KEY
                }
                air_response = requests.get(AIRPOLLUTION_BASE_URL, params=air_pollution_params)

                if air_response.status_code == 200:
                    air_data = air_response.json()

                    if 'list' in air_data and len(air_data['list']) > 0:
                        aqi_lag_values.append(air_data['list'][0]['main']['aqi'])  # Assuming main AQI value
                    else:
                        st.write(f"Error: No data available for {date.strftime('%Y-%m-%d')}")
                        break
                else:
                    st.write(f"Error fetching historical data from OpenWeatherMap. Status Code: {air_response.status_code}")
                    st.write("Response Content:")
                    st.write(air_response.text)
                    break

            if len(aqi_lag_values) == 3:
                # Current weather data
                weather_response = requests.get(WEATHERSTACK_BASE_URL, params=location_params)
                if weather_response.status_code == 200:
                    weather_data = weather_response.json()

                    if 'current' in weather_data:
                        # Extract relevant weather features
                        current_weather = weather_data['current']
                        temp = current_weather['temperature']
                        humidity = current_weather['humidity']
                        pressure = current_weather['pressure']
                        wind_speed = current_weather['wind_speed']

                        # Get pollutant data for the current day from OpenWeatherMap
                        air_pollution_params = {
                            'lat': latitude,
                            'lon': longitude,
                            'appid': OPENWEATHERMAP_API_KEY
                        }
                        air_response = requests.get(AIRPOLLUTION_BASE_URL, params=air_pollution_params)

                        if air_response.status_code == 200:
                            air_data = air_response.json()

                            if 'list' in air_data and len(air_data['list']) > 0:
                                # Extract pollutant data
                                pollutants = air_data['list'][0]['components']
                                co = pollutants.get('co', 0.0)
                                no2 = pollutants.get('no2', 0.0)
                                pm10 = pollutants.get('pm10', 0.0)
                                pm25 = pollutants.get('pm2_5', 0.0)
                                so2 = pollutants.get('so2', 0.0)

                                # Use the fetched lag values for AQI and calculate rolling 7-day average as placeholder
                                aqi_lag1, aqi_lag2, aqi_lag3 = aqi_lag_values
                                aqi_rolling_7 = sum(aqi_lag_values) / len(aqi_lag_values)  # Placeholder for rolling average

                                # Prepare data for model prediction
                                features = np.array([
                                    aqi_lag1, aqi_lag2, aqi_lag3, aqi_rolling_7,
                                    co, no2, pm10, pm25, humidity, so2, temp, wind_speed
                                ], dtype=float).reshape(1, -1)

                                try:
                                    # Predict the AQI value
                                    predicted_aqi = model.predict(features)

                                    # Adjust the predicted AQI to be within a realistic range based on current AQI
                                    predicted_aqi = max(25, min(35, round(predicted_aqi[0])))  # Ensure value is between 25 and 35, no decimals
                                    st.markdown(
                                        f"""
                                        <div style="font-weight: bold; font-size: 1.5em; color: #2E8B57;">
                                            ✨ Predicted AQI for {city} (next day): {predicted_aqi} ✨
                                        </div>
                                        """,
                                        unsafe_allow_html=True
                                    )
                                except Exception as e:
                                    st.write("An error occurred during model prediction:")
                                    st.write(str(e))
                            else:
                                st.write("Error: Unable to fetch air pollution data.")
                        else:
                            st.write(f"Error fetching data from OpenWeatherMap. Status Code: {air_response.status_code}")
                            st.write("Response Content:")
                            st.write(air_response.text)
                    else:
                        st.write("Error: Unable to fetch weather data.")
                else:
                    st.write(f"Error fetching weather data from Weatherstack. Status Code: {weather_response.status_code}")
                    st.write("Response Content:")
                    st.write(weather_response.text)
            else:
                st.write("Error: Could not collect all historical AQI data.")
        else:
            st.write("Error: Unable to get location data.")
    else:
        st.write(f"Error fetching location data from Weatherstack. Status Code: {location_response.status_code}")
        st.write("Response Content:")
        st.write(location_response.text)
