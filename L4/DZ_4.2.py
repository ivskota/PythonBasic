nums = [1, 3, 5] # 30
#[6] # 36
#[] # 0

if not nums:
    result = 0
else:
    s = sum(nums[::2])
    result = s *nums[-1]
print(result)