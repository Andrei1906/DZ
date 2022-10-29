"# -- coding: utf-8 --"
N=int(input())
n1=1
n2=1
suma=2
for i in range(2,N):
    n1,n2=n2,n1+n2
    suma=suma+n2
print(suma)

