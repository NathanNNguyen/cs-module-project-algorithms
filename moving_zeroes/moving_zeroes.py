'''
Input: a List of integers
Returns: a List of integers
'''
def moving_zeroes(arr):
    # check length of the arr
    if len(arr) == 0:
        return
    elif len(arr) == 1:
        return arr
    
    else:
        count = 0
        for i in range(len(arr)):
            if arr[i] != 0:
                num = arr[i]
                arr.pop(i)
                arr.insert(count, num)
                count += 1
                
        # moving zeroes to the right
        # for i in range(len(arr)):
        #     if arr[i] == 0:
        #         arr.pop(i)
        #         arr.append(0)

    return arr


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")