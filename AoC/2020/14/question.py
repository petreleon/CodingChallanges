# Python3 program to print sums of 
# all possible subsets. 

# Prints sums of all subsets of arr[l..r] 
def subsetSums(arr, l, r, sum = 0, set_ = []): 
    # Print current subset 
    if l > r:
        if sum == 208:
            print(set_) 
        return

	# Subset including arr[l]
    set_.append(arr[l])
    subsetSums(arr, l + 1, r, sum + arr[l], set_) 
    set_.pop()
	# Subset excluding arr[l] 
    subsetSums(arr, l + 1, r, sum, set_) 

# Driver code 
arr = [59, 58, 27, 27, 26, 26, 25, 24, 19, 18, 17, 16] 
n = len(arr) 
subsetSums(arr, 0, n - 1) 

# This code is contributed by Shreyanshi Arun. 
