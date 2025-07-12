from sqlalchemy import and_, not_, or_

from db_config import db
from models import User

users_all = db.query(User).all()

print("----------filter method----------------")
users_filtered = db.query(User).filter(User.age > 27).all()

print(f"Number of users {len(users_all)}")
print(f"Number of filtered user {len(users_filtered)}")


# filter_by method

# query all the users with age =30
print("----------filter_by method----------------")
age_30_users = (
    db.query(User).filter_by(age=30).all()
)  # filter_by() in SQLAlchemy is only for simple equality comparisons

for user in age_30_users:
    print(user.name)


# where method
print("----------where method----------------")
above_30_user = db.query(User).where(User.age >= 30).all()

for user in above_30_user:
    print(user.name)
    print(user.age)

# and in filter

print("----------and_in_filters----------------")
above_30_user_whose_name_is_john_doe = (
    db.query(User)
    .where(User.age >= 3, User.name == "John Doe")
    .all()  # we can set explicit and_ and bitwise and as well
)


for user in above_30_user_whose_name_is_john_doe:
    print(user.name)
    print(user.age)

print("----------or_in_filters----------------")

below_25_user_or_name_is_john_doe = (
    db.query(User).where(or_(User.age < 25, User.name == "John Doe")).all()
)

for user in below_25_user_or_name_is_john_doe:
    print(user.name)
    print(user.age)


print("----------bitwise_or----------------")

bit_below_25_user_or_name_is_john_doe = (
    db.query(User).where((User.age < 25) | (User.name == "John Doe")).all()
)

for user in bit_below_25_user_or_name_is_john_doe:
    print(user.name)
    print(user.age)


print("--------------not operator------------")
not_john_doe = db.query(User).where(not_(User.name == "John Doe")).all()

for user in not_john_doe:
    print(user.name)
    print(user.age)

print("-------three operator together----------")
combined_users = db.query(User).where(
    or_(not_(User.name == "John Doe"), and_(User.age > 26, User.age < 29))
)


for user in combined_users:
    print(user.name)
    print(user.age)
