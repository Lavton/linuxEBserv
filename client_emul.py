#! /usr/bin/python3.4
import requests

def getRequest():
    """
    infinite cicle for test REST protocol.
    Press "s" to emulate sending and "c" to emulate getting info
    """
    req = 0
    while True:
        inp = input("go to Submit or to Check. Exit with Ctrl+C (S/C): ")
        if inp.lower().strip() == "s":
            req = submit_send()
        else:
            check_send(req)

def submit_send():
    """
    emulate sending solution
    """
    req = requests.post("http://127.0.0.1:5000/submit",
        data={"solution": "dasdasd"})
    print("get id={}".format(req.json()["id"]))
    return req.json()["id"]

def check_send(id):
    """
    emulate checking id
    """
    req = requests.post("http://127.0.0.1:5000/check",
        data={"id": id})
    print(req.json())

if __name__ == '__main__':
    getRequest()