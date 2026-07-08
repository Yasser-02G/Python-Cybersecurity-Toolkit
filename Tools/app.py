import argparse
import requests

def help():
    print("tool1 : use : python app.py tool1")
    print("tool2 : use : python app.py tool2")


def tool1():
    print("-------------------------------")
    print("   tool1 - request  ")
    print("-------------------------------")

    url = 'http://testphp.vulnweb.com/'
    res = requests.get(url)
    if res.status_code == 200:
       print("ok!")
    else:
        print("no!")

def tool2():
    print("-------------------------------")
    print("   tool1 - request  ")
    print("-------------------------------")

    url = input('enter link please : ')
    res = requests.get(url)
    if res.status_code == 200:
       print("ok!")
    else:
        print("no!")


parser = argparse.ArgumentParser(description="[2025] Python Tools Cyber New")
parser.add_argument("command",choices=['help','tool1','tool2','Ddos'],help="commands to run")

args = parser.parse_args()

if args.command == 'help':
    help()

if args.command == 'tool1':
    tool1()

if args.command == 'tool2':
    tool2()