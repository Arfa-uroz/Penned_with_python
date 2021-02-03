'''lstP = []
def prime(n):            #it returns all the prime numbers before n
    for i in range(2,n):
        count = 0
        for j in range(1,(i+1)):
            if i%j==0:
                count +=1
        if count == 2:
            lstP.append(i)
    return(lstP)

def primepartition(m):
    lstOfPrimes = prime(m)
    if m>0:
        for i in lstOfPrimes:
            for j in lstOfPrimes:
                if i+j == m:
                    return(True)
        else:
            return(False)
    else:
        return(False)'''
def isprime(n):
    for i in range(2,int(n/2)+1):
        if n%i == 0:
            return False
    return True

def prime(n):
    n = n+1
    while(True):
        if isprime(n) == True:
            return n
        else:
            n = n+1

def primepartition(num):
    if num < 0:
        return False
    nextprime = 2
    while(nextprime < num):
        part2 = num - nextprime
        if isprime(part2) == True:
            return True
        else:
            nextprime = prime(nextprime)
    return False

num = int(input("Enter a number: ").strip())
print(primepartition(num))
