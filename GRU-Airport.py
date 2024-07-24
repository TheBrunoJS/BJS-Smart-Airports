# Databricks notebook source
from datetime import datetime, timedelta
import requests
import pandas as pd

opensky_url_arrival = "https://opensky-network.org/api/flights/arrival"
opensky_url_departure = "https://opensky-network.org/api/flights/departure"

icao_code = "SBGR" # GRU Airport Code

yesterday = datetime.utcnow()- timedelta(days=1)
start_date = int(datetime(yesterday.year, yesterday.month, yesterday.day, 0).timestamp())
end_date = int(datetime(yesterday.year, yesterday.month, yesterday.day, 23,59,59).timestamp())
print(start_date)

params = {
    "airport": icao_code,
    "begin": start_date,
    "end": end_date
}



# COMMAND ----------

# MAGIC %md
# MAGIC ### Get the Arrivals

# COMMAND ----------

# Make a request to the OpenSky API
response = requests.get(opensky_url_arrival, params=params)

if response.status_code == 200:
    arrival = response.json()
    df = pd.DataFrame(arrival)


# COMMAND ----------

# MAGIC %md
# MAGIC ### Get the Departures

# COMMAND ----------

# Make a request to the OpenSky API
response = requests.get(opensky_url_departure, params=params)

if response.status_code == 200:
    departure = response.json()
    display(departure)

