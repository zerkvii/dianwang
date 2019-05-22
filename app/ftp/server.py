from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer
import re
import json
# from app import create_app
from app.repository import *
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

        match = re.findall(r'[^(\\\\)]*\.json', file)
        record_dict = ''
        if len(match) > 0:
            json_file = 'json/' + match[0]
            with open(json_file, 'r', encoding='utf-8') as f:
                json_data = json.load(f)
                record_dict = json_data['record']

            # for item in list:
            #     print((item))
            try:
                # print(type(list))
                serial = record_dict['serial_number']
            except Exception as e:
                print(e)
            # create_app().app_context().push()

            loc = Record.objects(serial_number=serial).first()
            if not loc:
                record = Record.from_json(json.dumps(record_dict))
                record.save()
            else:
                record = Record.f
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
    # create_app().app_context().push()
    # from app.models import Record_location
    # Define a new user having full r/w permissions and a read-only
    # anonymous user
    print('start')
    users = FileUser.objects
    for user in users:
        authorizer.add_user(user.username, user.password, '.', perm='elradfmwM')
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
