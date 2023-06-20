import zipfile
import itertools

password = ""
chars = "qwertyuiopasdfghjklzxcvbnm1234567890QWERTYUIOPASDFGHJKLZXCVBNM!@#$%^&*()_+=-[]{}\|,.<>"
length = 1


def brutefoce(zfile):
    try:
        myzip = zipfile.ZipFile(zfile)
    except FileExistsError:
        print("你传入的zip文件不存在")
        return
    global length
    while True:
        password = itertools.product(chars, repeat=length)
        total = len(chars) ** length
        for i, passwd in enumerate(password):
            passwd = ''.join(passwd)
            try:
                myzip.extractall(pwd=passwd.encode("utf-8"))
                print('密码破解', passwd)
                return
            except Exception as e:
                print('密码破解失败', passwd)
            if i == total - 1:
                length += 1
                break


zfile = "your-path"

brutefoce(zfile)



