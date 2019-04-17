# find the sum of contigious element in array i.e. subarray
# the sum of subsequence'e element are divisible by k
# result for print(subarraySum([5,10,11,9,5], 5)) -> {{5}, {5,10}, {5,10,11,9}, {5,10,11,9, 10}, {10}, {10,11,9}, 
# {10,11,9, 5}, {11,9}, {11,9,5}, {5}}

def subarraySum(nums, k) -> int:
    subSequence_sum = [0]
    count = 0
    for idx, i in enumerate(nums):
        subSequence_sum.append(subSequence_sum[idx] + i)
    
    print(subSequence_sum)
    for i in range(len(subSequence_sum)):
        for j in range(i+1, len(subSequence_sum)):
            if (subSequence_sum[j] - subSequence_sum[i]) % k == 0:
                count += 1

    return count
    
def subarraySum(nums, k) -> int:
    subSequence_sum = [0]
    count = 0
    
    for i in range(len(nums)):
        total = 0
        for j in range(i, len(nums)):
            total += nums[j]
            if total % k == 0:
                count += 1

    return count

print(subarraySum([5,10,11,9,5], 5))
# print(subarraySum([1,1,1,1], 2))
