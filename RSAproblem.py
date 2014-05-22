"""
Filename:           RSAproblem.py
Author:             Tristen Wentling
Purpose:            Encrypt/Decrypt messages

Used to solve problem 7 on final exam
"""
def main():
    nrecip=12074181603861285697
    erecip=4774715375191615501
    drecip=6901955715833969989
    n_self=2161926180097578217
    e_self=30216720412799147
    d_self=402178956129334623
    encode=True
    textfile=open("ptext1.txt","r") #get text to encrypt
    lines=textfile.readlines()
    textfile.close()
    blocklength=8
    pad=len(lines[0])%blocklength  #pad the text to get multiples of 8
    xs='X'
    for i in xrange(1,pad):
        xs=xs+'X'
    y=lines[0]
    lines[0]=y[:-1]+xs
    splitter=lambda x,y: [ x[i:i+y] for i in xrange(0,len(x),y)]
    splitlist=splitter(lines[0],blocklength) #parse list into length 8 blocks
    print splitlist
    print "Encoding"
    messagelist=[]
    if encode==True:
        for i in xrange(len(splitlist)):
            message=list(splitlist[i]) #separates letters
            mess=[]
            for i in xrange(len(message)): #converts to numeric value
                x=getcharval(message[i])
                mess.append(x)
            encmess=rsaencrypt(mess,d_self,n_self)
            signedmess=rsasigned(encmess,erecip,nrecip)
            returned=rsadecrypt(signedmess,e_self,n_self,drecip,nrecip)
            messagelist.append(str(signedmess))  
            #print signedmess   #prints encoded message
    messagereturn=str(messagelist[0])
    for i in xrange(1,len(messagelist)):
        messagereturn=messagereturn+str(messagelist[i])
    #outfile=open("outext.txt",'w')
    #outfile.write(messagereturn)
def rsaencrypt(mess,e,n): #takes list arg of message returns coded val
    encnum=str(mess[0])
    for i in xrange(1,len(mess)):
        encnum=encnum+str(mess[i])
    encnum=int(encnum)
    print encnum
    encblock=powermod(encnum,e,n)
    print encblock
    #encblock=(encnum**e)%n
    return encblock

def rsasigned(encblock,d,n):
    signblock=powermod(encblock,d,n)
    #signblock=(encblock**d)%n
    print signblock
    return signblock
    
def rsadecrypt(num,e_self,n_self,drecip,nrecip):
    step1=powermod(num,drecip,nrecip)
    step2=powermod(step1,e_self,n_self)
    print step1,step2
    return step2

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
    binary=list((bin(k)[3:])) #slices off beginning prefix and first '1' of bin number
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
