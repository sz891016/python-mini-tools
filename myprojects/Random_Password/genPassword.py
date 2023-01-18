import random
import string
if __name__ == '__main__':
    length = int(input("Enter passward length:"))
    if not length > 0:
        print("Password length need > 0")
        exit(0)
    # 大小写英文字母 + 数字 + 特殊字符
    collection = string.ascii_letters + string.digits + string.punctuation
    pwd = ''.join(random.sample(collection,length))
    print(f'password is:{pwd}')
