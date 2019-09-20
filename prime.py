def factors(n):
    factorlist=[]
    for i in range(1,n+1):
        if n%i == 0:
            factorlist = factorlist + [i]
    return(factorlist)

def isprime(m):
    return(factors(m)==[1,m])

def primesupto(n):
    primelist=[]
    for i in range(1,n+1):
        if isprime(i):
            primelist=primelist+[i]
    return(primelist)
