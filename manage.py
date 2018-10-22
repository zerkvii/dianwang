# -*- coding=utf-8 -*-
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager, Server

from app import create_app
from app.models import *

app = create_app()
migrate = Migrate(app, db)
manager = Manager(app)
# Migration commands
manager.add_command('db', MigrateCommand)
server = Server(host="0.0.0.0", port=5000)
manager.add_command("runserver", server)


# # Add interactive project shell
# def make_shell_context():
#     return dict(app=create_app, db=db)
# manager.add_command("shell", Shell(make_context=make_shell_context))


@manager.command
def create_db():
    db.create_all()


if __name__ == '__main__':
    manager.run()
