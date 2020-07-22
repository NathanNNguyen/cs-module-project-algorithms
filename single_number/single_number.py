'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''

# this method would work if we're given that specific array

def single_number(arr):
    # check for length of arr
    if len(arr) == 0:
        return

    elif len(arr) == 1:
        return arr[0]

    i = 0

    while i in range(len(arr)):
        if arr[i] != arr[i + 1]:
            return arr[i]
        i += 2

    return arr[i]


if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")