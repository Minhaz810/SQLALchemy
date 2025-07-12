from db_config import db
from models import User

# creating dummy entries
# import random
# names = [
#     "Alice",
#     "Bob",
#     "Charlie",
#     "Diana",
#     "Ethan",
#     "Fiona",
#     "George",
#     "Hannah",
#     "Ian",
#     "Jasmine",
# ]
# ages = [23, 31, 19, 27, 35, 22, 40, 29, 25, 33]


# for name in names:
#     age = ages[random.randint(0, len(ages) - 1)]
#     user = User(name=name, age=age)

#     db.add(user)
# db.commit()


# query all user by age (asc)

users = db.query(User).order_by(User.age).all()

for user in users:
    print(f"User name is {user.name} and user age is {user.age}")


# query all user by age (desc)

print("---------------descending users-------------------")
descending_users = db.query(User).order_by(User.age.desc()).all()

for user in descending_users:
    print(f"User name is {user.name} and user age is {user.age}")

print("---------------sorting with name and age-----------")

ascending_user_with_name_and_age = db.query(User).order_by(User.age, User.name).all()

for user in ascending_user_with_name_and_age:
    print(f"User name is {user.name} and user age is {user.age}")

print("-----------descending sorting with name and age-----------")

descending_user_with_name_and_age = (
    db.query(User).order_by(User.age, User.name.desc()).all()
)

for user in descending_user_with_name_and_age:
    print(f"User name is {user.name} and user age is {user.age}")
