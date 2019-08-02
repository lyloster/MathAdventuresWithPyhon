
#find the GCF of two numbers

def factor(num):
	factors = []
	for i in range(1, num+1):
		if num%i==0:
			factors.append(i)
	return factors

def gcf(num1, num2):
	num1Factors = factor(num1)
	num2Factors = factor(num2)
	mostFactors = len(num1Factors)>len(num2Factors)
	if mostFactors == True:
		for i in range(len(num2Factors)):
			if num2Factors[i]==num1Factors[i]:
				None
			else:
				return print(num2Factors[i])

	else:
		for i in range(len(num1Factors)):
			if num1Factors[i]==num2Factors[i]:
				None
			else:
				return print(num1Factors[i])


        
