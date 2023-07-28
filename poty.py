# Module need
import  socket
import  threading
import sys

syntax = '''[:]  The syntax is like 
python3 poty.py <ip> <start_port> <end_port>'''
if len(sys.argv) != 4:
    print(syntax)
    sys.exit()

try:
    target = socket.gethostbyname(sys.argv[1])
except socket.gaierror:
    print("Name Resolution error")
    sys.exit()

s_port = int(sys.argv[2])
e_port = int(sys.argv[3])

print("[*] Started........")
print("_____________________________________________________________________")
def scan_poty(port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    connec = s.connect_ex((target, port))
    if (connec == 0):
        print(f"[*] The port is runing like fire, homie = {port}", end="\n")
        s.close

for port in range(s_port, e_port):
    thread = threading.Thread(target=scan_poty, args=(port,))
    thread.start()

thread.join()
print("_____________________________________________________________________")
print("______________________Nasa is hacked_________________________________")