from db_config import db
from models import User

users = db.query(User).all()

for user in users:
    print(user.id)
    print(user.name)
    print(user.age)
