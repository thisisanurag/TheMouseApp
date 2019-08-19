import socket
import threading
import pyautogui
ip="0.0.0.0"
port=90
sock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((ip,port))
sock.listen(1)
connections=[]
def handle(c,a):
    global connections
    f=0
    while True:
        data=c.recv(1024)
        d=data.decode('utf-8')
        d=d.strip()
        l=d.split();
        x=l[len(l)-2]
        y=l[len(l)-1]
        x=float(x)
        y=float(y)
        pyautogui.moveTo(x, y, duration=0.1)
        #pyautogui.moveTo(x, y)
        print(x,y)
        if not data:
            c.close()
            connections.remove(c)
            break
while True:
    c,a=sock.accept()
    t=threading.Thread(target=handle, args=(c,a))
    t.daemon=True
    t.start()
    connections.append(c)
    print(connections)
