def ROT23(enc):
	ret = ""
	for s in enc:
		if ord("A") <= ord(s) <= ord("Z"):
			x = ord(s)-ord("A")-3
			if x < 0: x += 26
			ret += chr(ord("A")+x)
		else: ret += s
	return ret

f = open("text.txt")
a = f.readline().split()
print(a)
enc = ""
for i in a:
	enc += chr(int(i[:3],8))
print(enc)
rot_enc = ROT23(enc)
print(rot_enc)
flag = "bcactf{"
for i in range(len(a)):
	if len(a[i]) < 4: flag += rot_enc[i]
	else:
		if "N" in a[i]: flag += rot_enc[i].lower()
		else: flag += rot_enc[i]
flag += "}"
print(flag)
