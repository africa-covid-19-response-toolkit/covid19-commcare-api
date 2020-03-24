from pydantic import BaseModel
from typing import List, Optional

import datetime


class CommunityInspection(BaseModel):
    FullName: Optional[str]
    Sex: Optional[str]
    Age: Optional[int]
    Region: str
    SubcityOrZone: str
    Woreda: str
    Kebele: str
    HouseNo: str
    PhoneNo: str
    Occupation: str
    CallDate: datetime.datetime
    CallerType: Optional[str]
    Fever: Optional[bool]
    Cough: Optional[bool]
    Headache: Optional[bool]
    RunnyNose: Optional[bool]
    UnwellnessFeeling: Optional[bool]
    BreathingDifficulty: Optional[bool]
    BodyPain: Optional[bool]
    TravleHx: Optional[bool]
    HaveSex: bool
    AnimalMarket: bool
    HealthFacility: bool
    ReceiverName: Optional[str]
    FormStatus: Optional[str]
    Source: Optional[str]
    Version: int
    ID: int
    CreatedDate: datetime.datetime
    ModifiedDate: datetime.datetime


class Community(BaseModel):
    fullName: str
    sex: str
    age: int
    region: str
    subcityOrZone: str
    woreda: str
    kebele: str
    houseNo: str
    phoneNo: str
    latitude: str
    longitude: str
    occupation: str
    callDate: datetime.datetime
    callerType: str
    fever: bool
    cough: bool
    headache: bool
    runnyNose: bool
    unwellnessFeeling: bool
    breathingDifficulty: bool
    bodyPain: bool
    travleHx: bool              # This appears to be a misspelling
    haveSex: bool
    healthyFacility: bool
    receiverName: str
    formStatus: str
    source: str
    version: int
    id: int
    createDate: datetime.datetime
    modifiedDate: datetime.datetime
 

class Travller(BaseModel):
    firstName: str
    middleName: str
    lastName: str
    gender: str
    passportNo: str
    birthdate: datetime.datetime
    nationality: str
    region: str
    subcity: str
    woreda: str
    houseNo: str
    phoneNo: str
    hotelName: str
    travelFrom: str
    flightNumber: str
    transitFrom: str
    seatNumber: str
    hasFever: bool
    hasDryCough: bool
    hasSOB: bool
    temperature: float
    createdAt: datetime.datetime
    id: int


class AuthenticateVm(BaseModel):
    UserName: Optional[str]
    Password: Optional[str]


class CovidAuthenticateResult(BaseModel):
    Token: Optional[str]
    Expiration: Optional[datetime.datetime]
    Role: Optional[str]


class CovidError(BaseModel):
    Errors: Optional[List[str]]