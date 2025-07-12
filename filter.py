from db_config import db
from models import User

users = db.query(User).all()

user = db.query(User).filter_by(id=1).all()
single_user = db.query(User).filter_by(id=2).one_or_none()
first_user = db.query(User).filter_by(id=3).first()

print(user[0].name)
print(single_user.name)
print(first_user.name)
