from datetime import datetime
from typing import List

# pydantic
from pydantic import BaseModel


class Destination(BaseModel):
    city_name: str
    city_id: int
    stop_name: str
    stop_id: str


class Leg(BaseModel):
    carrier: str
    transport_type_id: int
    departure_date_time: datetime
    arrival_date_time: datetime
    duration: str
    origin: Destination
    destination: Destination
    carrier_icon: str
    transport_indicator: str


class Journey(BaseModel):
    journey_id: str
    departure_date_time: datetime
    arrival_date_time: datetime
    duration: str
    price: float
    origin: Destination
    destination: Destination
    legs: List[Leg]
    reservable_type: str
    service_information: str
    route_name: str
    low_stock_count: None
    transport_indicator: str
    promotion_code_status: str


class JourneyResponse(BaseModel):
    journeys: List[Journey]
    message: None
