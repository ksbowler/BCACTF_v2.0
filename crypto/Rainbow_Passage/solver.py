from tqdm import tqdm

f = open("message.txt")
mes = f.readline().strip()
print(mes)
f = open("enc.txt")
enc = f.readline().strip()
print(enc)
s = []
for block in range(16):
	for i in tqdm(range(2**16)):
		t = bin(i)[2:]
		while len(t) < 16: t = "0"+t
		check = True
		#print(enc[2*j+2*block:2*j+2+2*block])
		for j in range(0,len(mes)-16,16):
			#print(enc[2*j+2*block:2*j+2+2*block])
			x = 0
			for k in range(16):
				if j+k >= len(mes): break
				if t[k] == "1":
					x ^= ord(mes[j+k])
			x = hex(x)[2:]
			if len(x) == 1: x = "0" + x
			if enc[2*j+2*block:2*j+2+2*block] != x:
				check = False
				break
			#else:
			#	print(i)
		if check:
			s.append(i)
			print("find! :",i)
			break
pwd = ""
t = []
for S in s:
	x = bin(S)[2:]
	while len(x) < 16: x = "0"+x
	t.append(x)

for i in range(16):
	x = ""
	for j in range(16):
		x += t[j][i]
	x1 = x[:8]
	x2 = x[8:]
	pwd += chr(int(x1,2))
	pwd += chr(int(x2,2))
print("bcactf{"+pwd+"}")
