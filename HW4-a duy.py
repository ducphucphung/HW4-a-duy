#Bài 1:
import math
def songuyento(prime):
    for i in range (2, int(math.sqrt(prime)+1)):
        if prime%i==0:
            return False
    return True


def prime_a_b(prime):
    if songuyento(prime) is True:
        for a in range(2, prime-1):
            for b in range (2, prime-1):
                if songuyento(a) and songuyento(b) is True:
                    if a<b and a+b==prime:
                        print(a,b)
    if songuyento(prime) is False:
        print(-1)
                    
                    
                    
N=int(input("Nhập một số:"))
prime_a_b(N)


#Bài 2:
N=int(input("Nhập một số N:"))
list1=[ ]
for i in range (1, N):
    if N%i==0:
        list1.append(i)
k=0
for j in list1:
    k+=j
if k==N:
    print("Yes")
else:
    print("No")

#Bài 3:
list_length=int(input("Nhập độ dài mảng:"))
list1=list((input("Nhập dãy số:")).split( ))
if list_length==len(list1):
    dict1={ }
    for i in list1:
        dict1[i]=0
    for i in list1:
        dict1[i]+=1
    print(dict1.keys())
    print(dict1)
else:
    pass

#Bài 4:
string1=str(input("Nhập các kí tự"))
for i in string1:
    

        


    

                    
                
