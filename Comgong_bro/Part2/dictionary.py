#dictionary
m = {}
m["Yoondy"] = 40
m["Sky"] = 40
m["Jerry"] = 40
print("size:", len(m))
for k in m:
	print(k, m[k])


# Set
s = set()
s.add(456)
s.add(45)
s.add(456)
s.add(7890)
s.add(7890)
s.add(456)
print(s)
s.remove(456)
print(s)