def primes(n):
    primes=[]
    primes.append(1)
    for x in range(1, n+1):
        for y in range(1, x):
            if x == 2:
                primes.append(x)
            elif y != 1 and y != x and x % y == 0:
                break
            elif y != 1 and y == x - 1 and x % y != 0:
                primes.append(x)

    return primes

def prime_factorization(n):
    prime_nums = primes(n)
    factors = []
    j=1
    if n in prime_nums:
            factors.append(n)
            return factors
    while(n>0 and j < len(prime_nums)):
        if n/prime_nums[j] == 1:
            factors.append(prime_nums[j])
            break
        elif n % prime_nums[j]==0:
            factors.append(prime_nums[j])
            n = n/prime_nums[j]
        else:
            j+=1
            continue
    return factors
print(prime_factorization(20))

