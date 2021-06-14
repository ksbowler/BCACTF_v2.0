from Crypto.Util.number import *

enc = [0xB6A46EE913B33E19, 0xBCA67BD510B43632, 0xA4B56AFE13AC1A1E, 0xBDAA7FE602E4775E, 0xEDF63AB850E67010]

key = 0xD4C70F8A67D5456D
for i in enc:
	t = key^i
	#print(hex(t)[2:])
	print(long_to_bytes(t).decode(),end="")
print()
