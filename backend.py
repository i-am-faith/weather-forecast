import requests

api_key = "72bc7d2410d6afc7d9a2501574352ccd"


def get_data(place, forecast_days=None):
    url = f"https://api.openweathermap.org/data/2.5/forecast?q={place}&appid={api_key}"
    response = requests.get(url)
    data = response.json()
    filter_data = data["list"]
    filter_data = filter_data[:8*forecast_days]
    return filter_data


if __name__ == "__main__":
    print(get_data(place="bhubaneshwar", forecast_days=3, kind="Sky"))
