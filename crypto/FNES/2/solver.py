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
def modifyXor(d):
	if len(d) == 0: return ""
	x = len(d)//2 + 1
	ret = ""
	for i in range(0,len(d),2):
		#print("xor",x,x-1-(i//2))
		t = int(d[i:i+2],16)^x^(x-1-(i//2))
		t = hex(t)[2:]
		if len(t) == 1: t = "0"+t
		ret += t
	#print("ret:",ret)
	return ret

#cnt = [i for i in range(0,1024,32)]
#HOSTはIPアドレスでも可
HOST, PORT = "crypto.bcactf.com", 49154
s, f = sock(HOST, PORT)
for _ in range(11): read_until(f)
#key = "Open sesame... Flag please!"
key = b"Open sesame... Flag please!\x05\x05\x05\x05\x05"
enc = "00"*48
d2 = ""
dec2 = ""
for i in range(16):
	print(i)
	for k in range(256):
		read_until(f)
		read_until(f,">>> ")
		s.send(b"D\n")
		read_until(f)
		read_until(f,">>> ")
		h = hex(k)[2:]
		#print("h:",h)
		if len(h) == 1: h = "0"+h
		print("h:",h)
		mes = "00"*16+"00"*(15-i)+ h + modifyXor(d2) + enc[64:96]
		s.send(mes.encode()+b"\n")
		check = read_until(f).strip()
		print(check)
		if "decoded" in check:
			print("Find!")
			d2 = h + d2
			t = k^(i+1)
			t = hex(t)[2:]
			if len(t) == 1: t = "0"+t
			dec2 = t + dec2
			break
c0 = hex(bytes_to_long(key[16:])^int(dec2,16))[2:]
assert len(c0) <= 32
while len(c0) < 32: c0 = "0" + c0
print("cipher 0:",c0)
d1 = ""
dec1 = ""

for j in range(16):
	print(j)
	hen = True
	for i in range(256):
		read_until(f)
		read_until(f,">>> ")
		s.send(b"D\n")
		read_until(f)
		read_until(f,">>> ")
		h = hex(i)[2:]
		#print("h:",h)
		if len(h) == 1: h = "0"+h
		print("h:",h)
		mes = "00"*(15-j)+ h + modifyXor(d1) + c0
		#print("mes:",mes)
		assert len(mes) == 64
		s.send(mes.encode()+b"\n")
		recv_m = read_until(f).strip()
		print(recv_m)
		if "decoded" in recv_m:
			hen = False
			print("Find!")
			d1 = h + d1
			t = i^(j+1)
			t = hex(t)[2:]
			if len(t) == 1: t = "0"+t
			dec1 = t + dec1
			break

iv = hex(bytes_to_long(key[:16])^int(dec1,16))[2:]
assert len(iv) <= 32
while len(iv) < 32: iv = "0" + iv
#c0 = hex(bytes_to_long(key[16:])^int(dec2,16))[2:]
#assert len(c0) <= 32
#while len(c0) < 32: c0 = "0" + c0
cit = iv + c0 + "00"*16
read_until(f)
read_until(f,">>> ")
s.send(b"D\n")
read_until(f)
read_until(f,">>> ")
s.send(cit.encode()+b"\n")
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

