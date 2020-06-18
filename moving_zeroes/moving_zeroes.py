'''
Input: a List of integers
Returns: a List of integers
'''
def moving_zeroes(arr):
    # Your code here
    checkingArray = []
    zero_counter = 0
    for i in range(len(arr)):
        if arr[i] != 0:                    
            checkingArray.append(arr[i])
        else:                             
            zero_counter += 1

    while zero_counter > 0:
        checkingArray.append(0)
        zero_counter -= 1
    return checkingArray

if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")