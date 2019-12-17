count = 0
for N in range(100,1000,10):
    if N % 4 == 0:
        count = count + 1

print "The probability that a three digit number"
print "with a zero ones digit is divisible by 4 is"
print count, "/ 100."
    
