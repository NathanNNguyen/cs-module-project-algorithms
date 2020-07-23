'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''
def sliding_window_max(nums, k):

    # len of the arr of output
    length = len(nums) - k + 1
    output = [0] * length

    # lets make a varible for moving the window
    count = 0

    while k < len(nums) + 1:
        # print(count, k)
        output[count] = max(nums[count: k])
        count += 1
        k += 1
        
    return output

    # first pass solution
    
    # window = []
    # max_values = []

    # for i in range(len(nums)):
    #     if len(window) < k:
    #         window.append(nums[i])
        
    #     else:
    #         max_val =  max(window)
    #         max_values.append(max_val)
    #         window.pop(0)
    #         if i < len(nums):
    #             window.append(nums[i])
                
    # max_values.append(max(window))
    # return max_values


if __name__ == '__main__':
    # Use the main function here to test out your implementation 
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
