from random import randint as r

s=""

n=int(input("Enter the password length"))

k=0


uletters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lletters = "abcdefghijklmnopqrstuvwxyz"
digits = "0123456789"
punctuation = "!#$%&*+-/?@\^_|~"
a=[len(uletters),len(lletters),len(digits),len(punctuation)]
m=[r(0,i-1) for i in a]

s=s+uletters[m[0]]
s=s+lletters[m[1]]
s=s + digits[m[2]]
s = s + punctuation [m[3]]
while(k!=n-4):
    n2 = r(0,3)
    if(n2==0):
        n1=r(0,len(uletters)-1)
        s=s+uletters[n1]
        k = k+1    
        
    elif(n2==1):
        n1=r(0,len(lletters)-1)
        s=s+lletters[n1]
        k = k+1    
       
    elif(n2==2):
        n1=r(0,len(digits)-1)
        s=s+lletters[n1]
        k = k+1    
        F2=1
    else:
        n1=r(0,len(punctuation)-1)
        s=s+punctuation[n1]
        k = k+1
        


f=r(0,4)
   
print (s[f:]+s[:f])

   
    
