from database import SessionLocal
import models

def print_bookings():
    db = SessionLocal()
    try:
        bookings = db.query(models.Booking).all()
        for b in bookings:
            print(b.__dict__)
    finally:
        db.close()

if __name__ == "__main__":
    print_bookings()
