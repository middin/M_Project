from flask_script import Manager
from app import app
from module import User

manager = Manager(app)

@manager.command
def save():
  user = User(3, 'jile')
  user.save()

@manager.command
def query_all():
  users = User.query()
  for user in users:
    print(user)


if __name__ == "__main__":
  manager.run()