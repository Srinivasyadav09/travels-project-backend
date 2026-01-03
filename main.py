from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
import models
import schemas
from database import engine, SessionLocal
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI(title="Travels API", description="API for managing bookings, vehicles, and packages")



app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://shambhavi-travels.vercel.app/"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Create tables
models.Base.metadata.create_all(bind=engine)

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# ------------------ BOOKINGS ------------------

@app.get("/bookings", response_model=List[schemas.BookingResponse], tags=["Bookings"])
def get_all_bookings(db: Session = Depends(get_db)):
    return db.query(models.Booking).all()

@app.post("/booking_request", response_model=schemas.BookingResponse, tags=["Bookings"])
def book_request(booking: schemas.BookingCreate, db: Session = Depends(get_db)):
    new_booking = models.Booking(**booking.dict())
    db.add(new_booking)
    db.commit()
    db.refresh(new_booking)
    return new_booking

@app.put("/bookings/{booking_id}", response_model=schemas.BookingResponse, tags=["Bookings"])
def update_booking(booking_id: int, booking_data: schemas.BookingUpdate, db: Session = Depends(get_db)):
    booking = db.query(models.Booking).filter(models.Booking.id == booking_id).first()
    if not booking:
        raise HTTPException(status_code=404, detail="Booking not found")
    for key, value in booking_data.dict(exclude_unset=True).items():
        setattr(booking, key, value)
    db.commit()
    db.refresh(booking)
    return booking

@app.delete("/bookings/{booking_id}", tags=["Bookings"])
def delete_booking(booking_id: int, db: Session = Depends(get_db)):
    booking = db.query(models.Booking).filter(models.Booking.id == booking_id).first()
    if not booking:
        raise HTTPException(status_code=404, detail="Booking not found")
    db.delete(booking)
    db.commit()
    return {"message": f"Booking {booking_id} deleted successfully"}

# ------------------ VEHICLES ------------------

@app.get("/vehicles", response_model=List[schemas.VehicleResponse], tags=["Vehicles"])
def get_vehicles(db: Session = Depends(get_db)):
    return db.query(models.Vehicle).all()

@app.post("/vehicles", response_model=schemas.VehicleResponse, tags=["Vehicles"])
def create_vehicle(vehicle: schemas.VehicleCreate, db: Session = Depends(get_db)):
    new_vehicle = models.Vehicle(**vehicle.dict())
    db.add(new_vehicle)
    db.commit()
    db.refresh(new_vehicle)
    return new_vehicle

@app.put("/vehicles/{vehicle_id}", response_model=schemas.VehicleResponse, tags=["Vehicles"])
def update_vehicle(vehicle_id: int, vehicle_data: schemas.VehicleUpdate, db: Session = Depends(get_db)):
    vehicle = db.query(models.Vehicle).filter(models.Vehicle.id == vehicle_id).first()
    if not vehicle:
        raise HTTPException(status_code=404, detail="Vehicle not found")
    for key, value in vehicle_data.dict(exclude_unset=True).items():
        setattr(vehicle, key, value)
    db.commit()
    db.refresh(vehicle)
    return vehicle

@app.delete("/vehicles/{vehicle_id}", tags=["Vehicles"])
def delete_vehicle(vehicle_id: int, db: Session = Depends(get_db)):
    vehicle = db.query(models.Vehicle).filter(models.Vehicle.id == vehicle_id).first()
    if not vehicle:
        raise HTTPException(status_code=404, detail="Vehicle not found")
    db.delete(vehicle)
    db.commit()
    return {"message": f"Vehicle {vehicle_id} deleted successfully"}

# ------------------ PACKAGES ------------------

@app.get("/packages", response_model=List[schemas.PackageResponse], tags=["Packages"])
def get_packages(db: Session = Depends(get_db)):
    return db.query(models.Package).all()

@app.post("/packages", response_model=schemas.PackageResponse, tags=["Packages"])
def create_package(package: schemas.PackageCreate, db: Session = Depends(get_db)):
    db_package = models.Package(**package.dict())
    db.add(db_package)
    db.commit()
    db.refresh(db_package)
    return db_package

@app.put("/packages/{package_id}", response_model=schemas.PackageResponse, tags=["Packages"])
def update_package(package_id: int, package_data: schemas.PackageUpdate, db: Session = Depends(get_db)):
    db_package = db.query(models.Package).filter(models.Package.id == package_id).first()
    if not db_package:
        raise HTTPException(status_code=404, detail="Package not found")
    for key, value in package_data.dict(exclude_unset=True).items():
        setattr(db_package, key, value)
    db.commit()
    db.refresh(db_package)
    return db_package

@app.delete("/packages/{package_id}", tags=["Packages"])
def delete_package(package_id: int, db: Session = Depends(get_db)):
    db_package = db.query(models.Package).filter(models.Package.id == package_id).first()
    if not db_package:
        raise HTTPException(status_code=404, detail="Package not found")
    db.delete(db_package)
    db.commit()
    return {"message": f"Package {package_id} deleted successfully"}
