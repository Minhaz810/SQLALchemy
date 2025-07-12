from db_config import db
from models import User

users = db.query(User)

only_john_doe = True

if only_john_doe:
    users = users.filter(User.name == "John Doe")

users = users.all()
for user in users:
    print(user.name)
    print(user.age)
