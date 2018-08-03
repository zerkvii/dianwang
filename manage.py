from flask_script import Manager, Shell
from app import create_app
from app.models import *
from flask_migrate import Migrate, MigrateCommand

app = create_app()
app.debug = True
migrate = Migrate(app, db)
manager = Manager(app)

# Migration commands
manager.add_command('db', MigrateCommand)


# # Add interactive project shell
# def make_shell_context():
#     return dict(app=create_app, db=db)
# manager.add_command("shell", Shell(make_context=make_shell_context))


@manager.command
def create_db():
    db.create_all()


if __name__ == '__main__':
    # app.run()
    manager.run()
