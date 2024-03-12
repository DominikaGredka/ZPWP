import argparse
import requests


class Brewery:
    def __init__(self, data):
        self.id = data["id"]
        self.name = data["name"]
        self.brewery_type = data["brewery_type"]
        self.address_1 = data["address_1"]
        self.address_2 = data["address_2"]
        self.address_3 = data["address_3"]
        self.street = data["street"]
        self.city = data["city"]
        self.state = data["state"]
        self.state_province = data["state_province"]
        self.postal_code = data["postal_code"]
        self.country = data["country"]
        self.phone = data["phone"]
        self.website_url = data["website_url"]
        self.longitude = data["longitude"]
        self.latitude = data["latitude"]

    def __str__(self):
        return (
            f"Browar: {self.name}, "
            f"typ {self.brewery_type}, "
            f"adres: {self.address_1} {self.postal_code} {self.city} {self.state_province} {self.country}"
            f"strona internetowa: {self.website_url}"
        )


def get_breweries(city=None):
    api_url = "https://api.openbrewerydb.org/v1/breweries"
    params = {"by_city": city, "per_page": 20}

    try:
        response = requests.get(api_url, params)
        response.raise_for_status()
        breweries_data = response.json()

        breweries_list = [Brewery(data) for data in breweries_data]
        return breweries_list

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return None


parser = argparse.ArgumentParser("Retrieve breweries from the Open Brewery DB API.")
parser.add_argument("--city", help="Filter breweries by city")
args = parser.parse_args()
city = args.city

breweries = get_breweries("Portland")

if breweries:
    for index, brewery in enumerate(breweries, 1):
        print(f"{index}. {brewery}")
else:
    print("Failed to retrieve breweries.")
