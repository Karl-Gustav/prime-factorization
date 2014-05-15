import sys

def main():
	number = int(sys.argv[1])
	primeFactors = primes(number)
	print ', '.join(str(x) for x in primeFactors)

def primes(n):
    primfac = []
    d = 2
    while d*d <= n:
        while (n % d) == 0:
            primfac.append(d)
            n /= d
        d += 1
    if n > 1:
        primfac.append(n)
    return primfac
	
if __name__  == '__main__': main()