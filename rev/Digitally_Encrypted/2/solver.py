from Crypto.Util.number import *

def rev_bit_32(x):
	x = bin(x)[2:]
	while len(x) < 32: x = "0"+x
	ret = ""
	for i in range(len(x)):
		if x[i] == "1": ret += "0"
		else: ret += "1"
	return int(ret,2)

def decoded(key1,key2,enc):
	e1 = int(enc[:8],16)
	e2 = int(enc[8:],16)
	tmp = rev_bit_32(key2^e1)
	pt1 = tmp^e2
	tmp = rev_bit_32(pt1^key1)
	pt2 = e1^tmp
	return (long_to_bytes(pt1) + long_to_bytes(pt2)).decode()

f = open("encrypted.txt")
a = f.readline().split()
print(a)
ptab = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz_{}"
ct2 = int(a[0][:8],16)
ct1 = int(a[0][8:],16)
for p1 in ptab:
	plain = "bcactf{"+p1
	plain = bin(bytes_to_long(plain.encode()))[2:]
	while len(plain) < 64: plain = "0"+plain
	pt1 = int(plain[32:],2)
	pt2 = int(plain[:32],2)
	tmp = ct1^pt2
	tmp = rev_bit_32(tmp)
	key1 = tmp^pt1
	tmp = ct2^pt1
	tmp = rev_bit_32(tmp)
	key2 = ct1^tmp
	k1 = bin(key1)[2:]
	while len(k1) < 32: k1 = "0" + k1
	k2 = bin(key2)[2:]
	while len(k2) < 32: k2 = "0" + k2
	if k1[:24] == k2[-24:]:
		print(key1,key2)
		print(p1)
		print("same! k124")
		break
	if k1[-24:] == k2[:24]:
		print("same! k1-24")
	"""
	pt1 = "bcac"
	pt1 = bytes_to_long(pt1.encode())
	#print("bit_length pt1",len(bin(pt1)[2:]))
	left = ct2^pt1
	#print("bit_length left",len(bin(left)[2:]))
	not_left = rev_bit_32(left)
	#print("bit_length not_left",len(bin(not_left)[2:]))
	key2 = not_left^ct1
	print(key2)
	#print(bin(key2)[2:])
	#print(len(bin(key2)[2:]))
	_key1 = bin(key2)[18:26]
	"""
	"""
	_k1 = ""
	for k in _key1:
		if k == "1": _k1 += "0"
		else: _k1 += "1"
	"""
	"""
	tmp = int(_key1,2)^ord("c")
	rev = ""
	tmp = bin(tmp)[2:]
	while len(tmp) < 8: tmp = "0"+tmp
	for t in tmp:
		if t == "1": rev += "0"
		else: rev += "1"
	print(int(a[0][6:8],16)^int(rev,2))
	break
	"""
	"""
	pt2 = "tf{"+p1
	pt2 = bytes_to_long(pt2.encode())
	left = ct1^pt2
	not_left = rev_bit_32(left)
	key1 = not_left^pt1
	k1 = bin(key1)[-24:]
	k2 = bin(key2)[2:]
	while len(k2) < 32: k2 = "0" + k2
	k2 = k2[:24]
	if k1 == k2:
		print("same!!")
	for enc in a:
		print(decoded(key1,key2,enc),end="")
	print()
	"""
#decode

for enc in a:
	e1 = int(enc[8:],16)
	e2 = int(enc[:8],16)
	tmp = rev_bit_32(e1^key2)
	pt1 = tmp^e2
	tmp = rev_bit_32(pt1^key1)
	pt2 = tmp^e1
	pt = pow(2,32)*pt2+pt1
	print(long_to_bytes(pt).decode(),end="")
print()
