'''
Input: an integer
Returns: an integer
'''
# cache = {}
def eating_cookies(n, cache={}):
    if n < 0:
        return 0
    if n == 0:
        return 1
    # else:
        # return eating_cookies(n-3) + eating_cookies(n-2) + eating_cookies(n-1)
    if n in cache:
        return cache[n]

    cache[n] = eating_cookies(n-3) + eating_cookies(n-2) + eating_cookies(n-1)
    return cache[n]

if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 50

    print(f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to each {num_cookies} cookies")
