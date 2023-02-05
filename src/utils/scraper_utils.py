# Webscrapper for megabus.com

import requests
from bs4 import BeautifulSoup
import json
import os
import time
import datetime
import sys
import re
from utils.megabus_types import JourneyResponse, QueryParams


# Given base url and params, return a url
def convert_url(base_url: str, params: dict):
    url = base_url + "?"
    for key, value in params.items():
        url += f"{key}={value}&"
    url = url[:-1]
    return url


class scraper_utils:
    def __init__(
        self,
        base_url="https://uk.megabus.com/journey-planner/journeys",
    ) -> None:
        self.base_url = base_url
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"
        }

    # Accept diferrent parameters and return a url
    def _get_url(
        self,
        departureDate="2023-02-09",
        destinationId="58",
        originId="34",
        totalPassengers="1",
    ) -> str:
        params = QueryParams(
            departureDate=departureDate,
            destinationId=destinationId,
            originId=originId,
            totalPassengers=totalPassengers,
        )

        url = convert_url(self.base_url, params.dict())
        return url

    # Get Journey data
    def get_journey_data(
        self,
        departureDate=datetime.datetime.now(),
        destinationId="58",
        originId="34",
        totalPassengers="1",
    ) -> JourneyResponse:
        url = self._get_url(departureDate, destinationId, originId, totalPassengers)
        page = requests.get(url, headers=self.headers)
        soup = BeautifulSoup(page.content, "html.parser")

        # Get the json data from the html window.SEARCH_RESULTS
        json_data = soup.find("script", text=re.compile("window.SEARCH_RESULTS")).string

        # Remove the window.SEARCH_RESULTS = from the string
        json_data = json_data.replace("window.SEARCH_RESULTS = ", "").strip()
        # Remove the ; from the end of the string if it exists
        if json_data[-1] == ";":
            json_data = json_data[:-1]

        # Convert the json object to a JourneyResponse object
        json_data = json.loads(json_data)
        json_data = JourneyResponse.parse_obj(json_data)

        return json_data
