from datetime import datetime
from typing import List

from pydantic import BaseModel


class Destination(BaseModel):
    cityName: str
    cityId: int
    stopName: str
    stopId: str


class Leg(BaseModel):
    carrier: str
    transportTypeId: int
    departureDateTime: datetime
    arrivalDateTime: datetime
    duration: str
    origin: Destination
    destination: Destination
    carrierIcon: str
    transportIndicator: str


class Journey(BaseModel):
    journeyId: str
    departureDateTime: datetime
    arrivalDateTime: datetime
    duration: str
    price: float
    origin: Destination
    destination: Destination
    legs: List[Leg]
    reservableType: str
    serviceInformation: str
    routeName: str
    lowStockCount: None
    transportIndicator: str
    promotionCodeStatus: str


class JourneyResponse(BaseModel):
    journeys: List[Journey]
    message: None


class QueryParams(BaseModel):
    days: int = 1
    concessionCount: int = 0
    departureDate: datetime
    destinationId: int
    inboundOtherDisabilityCount: int = 0
    inboundPcaCount: int = 0
    inboundWheelchairSeated: int = 0
    nusCount: int = 0
    originId: int
    otherDisabilityCount: int = 0
    pcaCount: int = 0
    totalPassengers: int = 1
    wheelchairSeated: int = 0
