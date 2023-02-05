from utils.scraper_utils import scraper_utils

base_url = "https://uk.megabus.com/journey-planner/journeys"


if __name__ == "__main__":
    scraper = scraper_utils(base_url)
    journey_data = scraper.get_journey_data()
    print(journey_data)
