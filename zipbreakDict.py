import zipfile
import threading


def extract_zip(pwd, zip_file):
    try:
        zip_file.extractall(pwd=pwd.encode("utf-8"))
        print("密码破解", pwd)
        return pwd
    except Exception as e:
        print("密码破解失败", pwd)


def bruteforce(pwd_list, zip_file):
    threads = []
    for pwd in pwd_list:
        t = threading.Thread(target=extract_zip, args=(pwd, zip_file))
        threads.append(t)
        t.start()
    for t in threads:
        t.join()


def main():
    myzip = "your-zip-path"
    pwd_list_path = "your-dict-path"
    try:
        zip_file = zipfile.ZipFile(myzip)
    except FileExistsError:
        print("文件不存在")
        return
    with open(pwd_list_path, "r", encoding="latin-1") as f:
        pwd_list = f.read().splitlines()
    bruteforce(pwd_list, zip_file)


if __name__ == '__main__':
    main()
