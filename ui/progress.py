#python

m = lx.Monitor()
m.init(1000)

for i in range(0, 10000):
	m.step(1)
	
	for i in range(0, 1000000):
		a = 6
