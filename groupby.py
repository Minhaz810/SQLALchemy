from sqlalchemy import func

from db_config import db
from models import User

users = db.query(User.age).group_by(User.age).all()

print(users)  # all the users grouped by age
print("")
print("-----------Counting number of users in a particular age group-----------\n ")

user_groups = db.query(User.age, func.count(User.id)).group_by(User.age).all()
print(user_groups)

print("")
print("-----------Ordering filtering and grouping together-----------\n ")

users_tuple = (
    db.query(User.age, func.count(User.id))
    .filter(User.age > 24)
    .group_by(User.age)
    .order_by(User.age)
).all()

for age, count in users_tuple:
    print(f"Age: {age}, Count:{count}")
