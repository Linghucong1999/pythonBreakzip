import zipfile
import multiprocessing


def extract_zip(pwd, zip_file):
    try:
        zip_file.extractall(pwd=pwd.encode("utf-8"))
        print("密码破解", pwd)
        return pwd
    except Exception as e:
        print("密码破解失败", pwd)


def bruteforce(pwd_gen, zip_file):
    pool = multiprocessing.Pool()
    for pwd in pwd_gen:
        pool.apply_async(extract_zip, args=(pwd, zip_file))
    pool.close()
    pool.join()


def pwdGen(pwdListPath):
    with open(pwdListPath, 'r', encoding="latin-1") as f:
        for line in f:
            yield line.strip()


def main():
    myzip = "your-zip-path"
    pwd_list_path = "your-dict-path"
    try:
        zip_file = zipfile.ZipFile(myzip)
        try:
            pwd_gen = pwdGen(pwd_list_path)
            bruteforce(pwd_gen, zip_file)
        finally:
            zip_file.close()
    except FileExistsError:
        print("你的文件不存在")
        return


if __name__ == "__main__":
    main()
