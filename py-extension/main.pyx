def prime_finder_vanilla(count):
    primes = []
    
    found = 0
    number = 2
    while found < count:
        for x in primes:
            if number % x == 0:
                break
        else:
            primes.append(number)
            found += 1
        number += 1
        
    return primes


def prime_finder_optimized(int count):
    
    cdef int number, x, found
    cdef int primes[100000]
    
    count = min(count, 100000)
    
    found = 0
    number = 2
    while found < count:
        for x in primes[:found]:
            if number % x == 0:
                break
        else:
            primes[found] = number
            found += 1
        number += 1
    
    return_list = [p for p in primes[:found]]
    return return_list

