from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer
import re
import json
from app import create_app, db
import os
import socketio


class MyHandler(FTPHandler):

    def on_connect(self):
        print("%s:%s connected" % (self.remote_ip, self.remote_port))

    def on_disconnect(self):
        # do something when client disconnects
        pass

    def on_login(self, username):
        # do something when user login
        pass

    def on_logout(self, username):
        # do something when user logs out
        pass

    def on_file_sent(self, file):
        # do something when a file has been sent
        print(file)

    def on_file_received(self, file):
        # do something when a file has been received
        sio = socketio.Client()
        sio.connect('http://localhost:8080', namespaces=['/upload'])

        match = re.findall(r'[^(\\\\)]*\.json', file)
        serial = ''
        if len(match) > 0:
            json_file = 'json/' + match[0]
            with open(json_file, 'r') as f:
                json_data = json.load(f)
                serial = json_data['serial']
        create_app().app_context().push()
        from app.models import Record
        loc = Record.query.filter_by(serial_number=serial).all()
        sio.send('ok')
        if len(loc) == 0:
            print('ok')
            location = Record(serial_number=serial, md5_name=serial, json_name=serial, rar_name=serial)
            db.session.add(location)
            db.session.commit()

        else:
            pass

    def on_incomplete_file_sent(self, file):
        # do something when a file is partially sent
        pass

    def on_incomplete_file_received(self, file):
        # remove partially uploaded files
        import os
        os.remove(file)


def start_serve():
    authorizer = DummyAuthorizer()
    create_app().app_context().push()
    from app.models import Fuser
    # from app.models import Record_location
    # Define a new user having full r/w permissions and a read-only
    # anonymous user
    fusers = Fuser.query.all()
    for user in fusers:
        user_map = user.get_user()
        authorizer.add_user(user_map['username'], user_map['password'], '.', perm='elradfmwM')
    # authorizer.add_anonymous(os.getcwd())

    # Instantiate FTP handler class
    handler = MyHandler
    handler.authorizer = authorizer

    # Define a customized banner (string returned when client connects)
    handler.banner = "pyftpdlib based ftpd ready."

    # Specify a masquerade address and the range of ports to use for
    # passive connections.  Decomment in case you're behind a NAT.
    # handler.masquerade_address = '151.25.42.11'
    # handler.passive_ports = range(60000, 65535)

    # Instantiate FTP server class and listen on 0.0.0.0:2121
    address = ('0.0.0.0', 2021)
    server = FTPServer(address, handler)

    # set a limit for connections
    server.max_cons = 256
    server.max_cons_per_ip = 5

    # start ftp server
    server.serve_forever()


if __name__ == '__main__':
    start_serve()
