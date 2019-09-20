# Python code to compute gcd

def gcd_list(x, y):
	cf = []
	for i in range(1,min(x,y)+1):
		if (x%i==0) and (y%i==0):
			cf.append(i)
	return(cf[-1])	

def gcd(x, y):
	for i in range(1,min(x,y)+1):
		if (x%i==0) and (y%i==0):
			mrcf=i
	return(mrcf)


def gcd_while(x,y):
	i=min(x,y)
	while i > 0:
		if (x%i==0) and (y%i==0):
			return i
		else:
			i= i-1

def gcd_euclid1(x,y):
	if (x<y) :
		(x,y)=(y,x)
	while y != 0:
		(x,y)=(y,x%y)
	return(x)


def gcd_euclid2(x,y):
	if (x<y) :
		(x,y)=(y,x)
	if(x%y==0):
		return(y)	
	else:
		return(gcd(max(x,x-y),min(x,x-y)))



print("gcd 	  : ",gcd(13,169))
l=gcd_list(14,196)
print("gcd_list  : ", l)

print("gcd_while : ",gcd_while(15,240))
print("gcd_euclid1 : ",gcd_euclid1(120,60))
print("gcd_euclid2 : ",gcd_euclid1(120,35))
