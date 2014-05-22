"""
ElGamal Cryptosystem
"""
from math import floor as floor
from math import log as log
from random import randint as randint
def main():
    p=472063
    g=randint(1,p)
    m=randint(1,p-1)
    k=randint(1,p-1)
    h=powermod(g,m,p)
    length=int(floor(log(p,26)))
    print 'p=',p,' g=',g,' m=',m,' h=',h,' length=',length
    print '[[ KEY= Z (mod '+str(p)+'),'+str(g)+','+str(h)+' ]]'
    omessage=[]
    omessage.append('MSUB')
    omessage.append('EARS')
    dmessage=[]
    encode=True        #leave as False unless encoding
    decode=True
    if encode==True:
        for i in xrange(len(omessage)):
            message=list(omessage[i]) #separates letters
            mess=[]
            for i in xrange(len(message)): #converts to numeric value
                x=getcharval(message[i])
                mess.append(x)
            print mess
        encmess=encrypt(mess,1,1)
        y=powermod(g,k,p)
        z=(encmess*(powermod(h,k,p)))%p
        print '(y,z)=('+str(y)+','+str(z)+')'
        decoded=powermod((y*z),(p-m),p)
        print decoded
        dmessage.append(int(decoded))
        #encvals=unpacke(encmess)
        #for i in xrange(len(encvals)):
        #    print getchars(encvals[i]),    #prints encoded message
    if decode==True:
        for i in xrange(len(dmessage)):
            decmess=dmessage[i]
            decvals=unpackd(decmess)
            for i in xrange(len(decvals)):
                print getchars(decvals[i]),  #prints decoded message
def encrypt(mess,e,n): #takes list arg of message returns coded val
    p1=mess[0]
    p2=mess[1]
    p3=mess[2]
    p4=mess[3]
    mapval=p1*26**3+p2*26**2+p3*26+p4
    #encval=powermod(mapval,e,n)
    return mapval


def unpackd(M): #takes decoded val and returns list of coefficients
    p4=M%26
    M=(M-p4)/26
    p3=M%26
    M=(M-p3)/26
    p2=M%26
    M=(M-p2)/26
    p1=M%26
    return [int(p1),int(p2),int(p3),int(p4)]

def getchars(num):   #gets string formatted letter from numeric value
    mydict={0:'A',1:'B',2:'C',3:'D',4:'E',5:'F',6:'G',7:'H',8:'I',9:'J',10:'K',11:'L',12:'M',13:'N',14:'O',15:'P',16:'Q',17:'R',18:'S',19:'T',20:'U',21:'V',22:'W',23:'X',24:'Y',25:'Z'}
    return mydict[num]

def getcharval(letter): #returns numeric value of string formatted letter 
    mydict={'A':0,'B':1,'C':2,'D':3,'E':4,'F':5,'G':6,'H':7,'I':8,'J':9,'K':10,'L':11,'M':12,'N':13,'O':14,'P':15,'Q':16,'R':17,'S':18,'T':19,'U':20,'V':21,'W':22,'X':23,'Y':24,'Z':25}
    return mydict[letter]

def powermod(base,power,modulus):  #powermod a^k (mod n) using %
    n=modulus
    a=base
    k=power
    binary=list((bin(k)[3:]))
    result=a
    for i in xrange(len(binary)):
        sqr=lambda x:x**2
        ext=lambda x:(x**2)*a
        p=int(binary[i])
        if p==0:
            result=sqr(result)%n
        else: result=ext(result)%n
    return (result)
main()
