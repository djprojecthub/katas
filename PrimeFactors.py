def PrimeFactors(num):
    res = []
    
    if num <= 0:
        raise Exception("Logical Issue!!! Numbers equal to or below 0 are not allowed.")
    remainder = int(num)
    if remainder == 1:
        return res
    
    divisor = 2
    while remainder > 1:
        while remainder > 0 and remainder % divisor == 0:
            res.append(divisor)
            remainder = remainder/divisor
        divisor = divisor + 1
    return res