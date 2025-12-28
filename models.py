from sqlalchemy import Column, Integer, String, Date, Time, Float
from database import Base

class Booking(Base):
    __tablename__ = "bookings"

    id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String, nullable=False)
    phone = Column(String, nullable=False)
    pickup_location = Column(String, nullable=False)
    dropoff_location = Column(String, nullable=False)
    cab_type = Column(String, nullable=False)
    trip_type = Column(String, nullable=False)
    pickup_date = Column(Date, nullable=False)
    pickup_time = Column(Time, nullable=False)


class Vehicle(Base):
    __tablename__ = "vehicles"

    id = Column(Integer, primary_key=True, index=True)
    vehicle_name = Column(String, nullable=False, unique=True)
    rate_per_km = Column(Float, nullable=False)
    daily_running = Column(Float, nullable=False)
    toll = Column(Float, nullable=False)
    parking = Column(Float, nullable=False)
    image_url = Column(String, nullable=True)


class Package(Base):
    __tablename__ = "packages"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    description = Column(String, nullable=False)
    duration = Column(String, nullable=False)
    image_url = Column(String, nullable=True)
