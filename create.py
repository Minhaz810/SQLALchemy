"""for doing the crud operation we need a session"""

from db_config import db
from models import User

user_1 = User(name="Minhaz Chowdhury", age=27)
user_2 = User(name="Miles Kennnedy", age=45)

db.add_all([user_1, user_2])
db.commit()
