import click
from app import create_app
from app.models import *
from flask_migrate import Migrate, MigrateCommand

app = create_app()
migrate = Migrate(app)


@click.group()
def boot():
    click.echo('boot mode')
    pass


@boot.command()
@click.option('--host', default='0.0.0.0', help='specified host')
@click.option('--port', default=80, help='specified port')
def runserver(host, port):
    app.run(host=host, port=port)


@boot.command()
def db_init():
    db.create_all()
