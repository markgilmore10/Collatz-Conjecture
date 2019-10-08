# Number we will use for collatz
n = 20

# Keep looking until we reach one
# Note: this assumes the Collatz conjecture is true
while n != 1:
    # Print the current value of n
    print (n)
    # Check if n is even
    if n % 2 == 0:
        # If n is even divide it by two
        n = n / 2
    else:
        # If n is odd multiply it by three and add one
        n = (3 * n) + 1

# Print one
print (n)
