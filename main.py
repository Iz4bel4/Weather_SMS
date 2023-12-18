import requests
from twilio.rest import Client

api_key = "ec215b60b47fe21acdaf11c68ee3020c"
account_sid = "account_sid"
auth_token = "auth_token"

parameters = {
    'lat': 52.229675,
    'lon': 21.012230,
    'appid': api_key,
    'cnt': 4
}
response = requests.get(url="https://api.openweathermap.org/data/2.5/forecast", params=parameters)
response.raise_for_status()
data = response.json()

will_rain = False

for specific_hour in data['list']:
    id_status = specific_hour['weather'][0]['id']
    if id_status < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="It's going to rain today. Bring your umbrella",
        from_='phone_number',
        to='+phone_number'
    )
    print(message.status)