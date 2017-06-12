def fibo(N):
	if N<1:
		return N
	else:
		return fibo(N-1)+fibo(N-2)

if _name_=="_main_":
	print ("fibo(5)", fibo(5))