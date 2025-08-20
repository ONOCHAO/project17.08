from database import SessionLocal
from models import Client, Note

class Action:
    @staticmethod
    def add_client(name, check, status):
        db = SessionLocal()
        client = Client(name=name, check=check, status=status)
        db.add(client)
        db.commit()
        db.refresh(client)
        db.close()
        return client

    @staticmethod
    def add_note(title, descrip, data, id_client):
        db = SessionLocal()
        note = Note(title=title, descrip=descrip, data=data, id_client=id_client)
        db.add(note)
        db.commit()
        db.refresh(note)
        db.close()
        return note

    @staticmethod
    def delete_client(client_id):
        db = SessionLocal()
        client = db.query(Client).filter(Client.id == client_id).first()
        if client:
            db.delete(client)
            db.commit()
            db.close()
            return True
        db.close()
        return False

    @staticmethod
    def delete_note(note_id):
        db = SessionLocal()
        note = db.query(Note).filter(Note.id == note_id).first()
        if note:
            db.delete(note)
            db.commit()
            db.close()
            return True
        db.close()
        return False
