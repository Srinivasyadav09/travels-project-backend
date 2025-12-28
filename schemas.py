from pydantic import BaseModel
from datetime import date, time
from typing import Optional

# Booking Schemas
class BookingCreate(BaseModel):
    full_name: str
    phone: str
    pickup_location: str
    dropoff_location: str
    cab_type: str
    trip_type: str
    pickup_date: date
    pickup_time: time

class BookingUpdate(BaseModel):
    full_name: Optional[str] = None
    phone: Optional[str] = None
    pickup_location: Optional[str] = None
    dropoff_location: Optional[str] = None
    cab_type: Optional[str] = None
    trip_type: Optional[str] = None
    pickup_date: Optional[date] = None
    pickup_time: Optional[time] = None

class BookingResponse(BookingCreate):
    id: int
    class Config:
        orm_mode = True

# Vehicle Schemas
class VehicleCreate(BaseModel):
    vehicle_name: str
    rate_per_km: float
    daily_running: float
    toll: float
    parking: float
    image_url: Optional[str] = None

class VehicleUpdate(BaseModel):
    vehicle_name: Optional[str] = None
    rate_per_km: Optional[float] = None
    daily_running: Optional[float] = None
    toll: Optional[float] = None
    parking: Optional[float] = None
    image_url: Optional[str] = None

class VehicleResponse(VehicleCreate):
    id: int
    class Config:
        orm_mode = True

# Package Schemas
class PackageCreate(BaseModel):
    name: str
    description: str
    duration: str
    image_url: Optional[str] = None

class PackageUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    duration: Optional[str] = None
    image_url: Optional[str] = None

class PackageResponse(PackageCreate):
    id: int
    class Config:
        orm_mode = True
