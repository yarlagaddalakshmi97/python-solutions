'''
10.Observe the Code Snippet

x = 25
epsilon = 0.01
numGuesses = 0
low = 0.0
high = max(1.0, x)
ans = (high + low)/2.0
while abs(ans**2 - x) >= epsilon:
print 'low =', low, 'high =', high, 'ans =', ans
numGuesses += 1
if ans**2 < x:
low = ans
else:
high = ans
ans = (high + low)/2.0
print 'numGuesses =', numGuesses
print ans, 'is close to square root of', x

a. What would the code above return if the statement x = 25 were replaced by x = -25?

b. What would have to be changed to make the code above for finding an approximation to the cube root of both negative and positive numbers? (Hint: think about changing low to ensure that the answer lies within the region being searched.)

'''
x =25
epsilon = 0.01
numGuesses = 0
low = 0.0
high = max(1.0, x)
ans = (high + low)/2.0
while abs(ans**2 - x) >= epsilon:
    print ('low =', low, 'high =', high, 'ans =', ans)
    numGuesses += 1
    if ans**2 < x:
        low = ans
    else:
        high = ans
    ans = (high + low)/2.0
print('numGuesses =', numGuesses)
print(ans, 'is close to square root of', x)
