from Crypto.Util.number import *
from functools import reduce
from operator import mul
from itertools import combinations
import sys
import socket, struct, telnetlib

# --- common funcs ---
def sock(remoteip, remoteport):
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((remoteip, remoteport))
	return s, s.makefile('rw')

def read_until(f, delim='\n'):
	data = ''
	while not data.endswith(delim):
		data += f.read(1)
	return data

#cnt = [i for i in range(0,1024,32)]
#HOSTはIPアドレスでも可
HOST, PORT = "crypto.bcactf.com", 49153
s, f = sock(HOST, PORT)
for _ in range(12): read_until(f)
key = "Open sesame... Flag please!"

#for i in range(len(key)):
read_until(f)
read_until(f,">>> ")
s.send(b"E\n")
read_until(f)
read_until(f,">>> ")
enc = "0"*len(key)
s.send(enc.encode()+b"\n")
read_until(f)
ct = read_until(f).strip()
s.close()
s, f = sock(HOST, PORT)
print(ct)
assert len(ct) == len(key)*2
pt = ""
for i in range(0,len(ct),2):
	x = int(ct[i:i+2],16)^ord("0")^ord(key[i//2])
	x = hex(x)[2:]
	if len(x) == 1: x = "0" + x
	pt += x

for _ in range(12): read_until(f)
read_until(f)
read_until(f,">>> ")
s.send(b"D\n")
read_until(f)
read_until(f,">>> ")
s.send(pt.encode()+b"\n")
while True: print(read_until(f))


#read_untilの使い方
#返り値があるのでprintするか、何かの変数に入れる
#1行読む：read_until(f)
#特定の文字まで読む：read_until(f,"input")
#配列に格納する：recv_m = read_until(f).split() or .strip()

#サーバーに何か送るとき
#s.send(b'1\n') : 1を送っている
#バイト列で送ること。str->bytesにするには、変数の後に.encode()
#必ず改行を入れること。終了ポイントが分からなくなる。ex) s.send(flag.encode() + b'\n')

