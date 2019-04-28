from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer
import re
import json
from app import create_app
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
        list = ''
        if len(match) > 0:
            json_file = 'json/' + match[0]
            with open(json_file, 'r', encoding='utf-8') as f:
                json_data = json.load(f)
                list = json_data['采集终端软件备案明细表']
            # for item in list:
            #     print((item))
            try:
                # print(type(list))
                serial = list['number']
                producer = list['厂家名称']
                producer_id = list['厂家代码']
                backup_type = list['备案种类']
                contact_person = list['联系人姓名']
                em_version = list['电能表型号']
                details = list['详细信息']
                backup_version = list['程序版本号']
                date = list['填写日期']
            except:
                print("err:")
                print(list)
            create_app().app_context().push()
            from app.models import Record
            details = str(details)
            loc = Record.query.filter_by(serial_number=serial).first()
            if not loc:
                print('添加备案')
                location = Record(serial_number=serial, md5_name=serial, json_name=serial, rar_name=serial,
                                  producer=producer, producer_id=producer_id, type=backup_type,
                                  contact_person=contact_person, date=date,
                                  em_version=em_version, backup_version=backup_version, details=details)
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
