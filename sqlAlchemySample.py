
import csv
import os

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

#engine = create_engine(os.getenv("postgresql://postgres:tajuana@localhost/myDB"))
engine = create_engine("postgresql://postgres:tajuana@localhost/myDB")

db = scoped_session(sessionmaker(bind=engine))

def main():  
        flights = db.execute("select origin, destination, duration from flights")
        for flight in flights:
                print(f"{flight.origin} to {flight.destination} duration {flight.duration}")
        
        print('Open .CSV file')
        f = open("flights.csv")
        reader = csv.reader(f)  
        for xorigin, xdestination, xduration in reader:
                db.execute("insert into flights (origin, destination, duration) values (:origin, :destination, :duration)",
                {"origin": xorigin, "destination": xdestination, "duration": xduration})
               
                print(f"from {xorigin} to {xdestination} flight time {xduration}")
        db.commit()     

if __name__ == "__main__":
        main()
        