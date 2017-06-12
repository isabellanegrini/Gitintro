from fibonacci import fibo as F

print("testing the identity sum_{n=1}^N F_n=F_{N+2}-1")

print("Fpr N={}".format(N))

print("LHS="+str(sum([F(n) for n in range(1,N+1)])))

print("LRS="+str(F(N+2)-1))