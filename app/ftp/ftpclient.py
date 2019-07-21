from ftplib import FTP
import glob
import os


# 连接ftp
def ftpconnect(host, port, username, password):
    ftp = FTP()
    # 打开调试级别2，显示详细信息
    # ftp.set_debuglevel(2)
    ftp.connect(host, port)
    ftp.login(username, password)
    return ftp


# 从ftp下载文件
def downloadfile(ftp, remotepath, localpath):
    # 设置的缓冲区大小
    bufsize = 1024
    fp = open(localpath, 'wb')
    ftp.retrbinary('RETR ' + remotepath, fp.write, bufsize)
    ftp.set_debuglevel(0)  # 参数为0，关闭调试模式
    fp.close()


# 从本地上传文件到ftp
def uploadfile(ftp, remotepath, localpath):
    bufsize = 1024
    fp = open(localpath, 'rb')
    ftp.storbinary('STOR ' + remotepath, fp, bufsize)
    ftp.set_debuglevel(0)
    fp.close()


if __name__ == "__main__":
    # host,port, username, password
    ftp = ftpconnect("127.0.0.1", 2021, "sg", "123456")
    print(ftp)
    # 获取当前路径
    pwd_path = ftp.pwd()
    print("FTP当前路径:", pwd_path)
    # 显示目录下所有目录信息
    ftp.dir()
    # 下载文件，第一个是ftp服务器路径下的文件，第二个是要下载到本地的路径文件
    # downloadfile(ftp, "./test.zip", r"C:\Users\Administrator\Desktop\file\test.zip")
    # 上传文件，第一个是要上传到ftp服务器路径下的文件，第二个是本地要上传的的路径文件
    file = 'gz20190101.json'
    downloadfile(ftp, remotepath='json/' + file, localpath='demo.json')
    # uploadfile(ftp, remotepath='cache/json/re.json', localpath="my.json")
