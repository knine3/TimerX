import timer as ti

ins = ti.timer(0, 10)
print("Timer: ", ins)
go = input("Start (y/n): ")
if go.lower() == 'y':
	try:
		ins.Start()
	except KeyboardInterrupt:
		print("But why at", ins, "?")
else:
	print("Good luck!")