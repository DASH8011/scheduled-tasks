import os
import requests
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient

proxy_client = TwilioHttpClient(proxy={'http': os.environ['http_proxy'], 'https': os.environ['https_proxy']})

account_sid = os.environ.get("SID_KEY")
auth_token = os.environ.get("AUTH_TOKEN")
api_key = os.environ.get("OWM_API_KEY")

my_lat = 35.467560
my_long = -97.516426

parameters = {
    "lat": my_lat,
    "lon": my_long,
    "appid": api_key,
    "cnt": 4
}

response = requests.get(url="https://api.openweathermap.org/data/2.5/forecast", params=parameters)
response.raise_for_status()
raw_data = response.json()

rawdata_0 = raw_data["list"][0]
time_0 = rawdata_0["dt_txt"].split(" ")[1].split(":")[0]
id_0 = rawdata_0["weather"][0]["id"]
desc_0 = rawdata_0["weather"][0]["description"]

rawdata_1 = raw_data["list"][1]
time_1 = rawdata_1["dt_txt"].split(" ")[1].split(":")[0]
id_1 = rawdata_1["weather"][0]["id"]
desc_1 = rawdata_1["weather"][0]["description"]

rawdata_2 = raw_data["list"][2]
time_2 = rawdata_2["dt_txt"].split(" ")[1].split(":")[0]
id_2 = rawdata_2["weather"][0]["id"]
desc_2 = rawdata_2["weather"][0]["description"]

rawdata_3 = raw_data["list"][3]
time_3 = rawdata_3["dt_txt"].split(" ")[1].split(":")[0]
id_3 = rawdata_3["weather"][0]["id"]
desc_3 = rawdata_3["weather"][0]["description"]

weather_dictionary = {
    time_0:[id_0, desc_0],
    time_1:[id_1, desc_1],
    time_2:[id_2, desc_2],
    time_3:[id_3, desc_3],
}


message = "Bring an umbrella my dear. "

rainy_weather = False

for (key, value) in weather_dictionary.items():

    if value[0] < 700:
        rainy_weather = True
        message += f"Weather at {key} is reported as {value[1]}. "


if rainy_weather:
    print("sending")
    print(message)
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        from_="whatsapp:+14155238886",
        body= message,
        to="whatsapp:+12158215697"
    )
