from database import SessionLocal, engine
from models import Base, Client, Note , Personal

Base.metadata.create_all(bind=engine)

db = SessionLocal()







clients = db.query(Client).all()

for client in clients:
    print(f"{client.id}: {client.name} ({client.status})")
personals = db.query(Personal).all()
for personal in personals:
    print(f"{personal.id}:{personal.username}")
db.close()
