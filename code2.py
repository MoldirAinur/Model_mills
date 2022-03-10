n1=int(input("Введите n1"))
n2=int(input("Введите n2"))
n12=int(input("Введите n12"))
print(n1,n2,n12)
E1=n12/n2
E2=n12/n1
print ("E1=",E1)
print ("E2=", E2)N=n12/(E1*E2)
print ("N=",N)
R=N-n1-n2+n12
print ("R=", R)
