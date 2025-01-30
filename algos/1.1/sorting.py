#in [] size n
#out [] =    order n¹ <= n² ...

def ehMaior(x, y): #o primeiro eh maior q o  segundo?
    if x > y:
        return True
    else:
        return False
    
def checkOrder(nums):
    for i, num in enumerate(nums):
        if i < len(nums) - 1:
            if num > nums[i+1]:
                return False
            if i == len(nums) - 1:
                return True


def sort(nums):
    for i, num in enumerate(nums):
        if i < len(nums)-1:
            if num > nums[i+1]:
                nums[i] = nums[i+1]
                nums[i+1] = num
                print(nums)
            if checkOrder(nums):
                print(nums)
                break

sort([3,1,2,5])