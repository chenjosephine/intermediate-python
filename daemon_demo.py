import time
import threading

def daemon_task():
    while True:
        print('\tThis is Daemon')
        time.sleep(1)

t1 = threading.Thread(target=daemon_task, daemon=True)
t1.start()

for i in range(1,11):
    print(f'{i} --> This is Main')
    time.sleep(1)
