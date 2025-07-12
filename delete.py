from db_config import db
from models import User

users = db.query(User).all()

first_user = db.query(User).filter_by(id=3).first()

db.delete(first_user)
db.commit()
