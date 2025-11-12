# [0, 1, 0, 12, 3] # [1, 12, 3, 0, 0]
#[0]  #[0]
# 1, 0, 13, 0, 0, 0, 5] # [1, 13, 5, 0, 0, 0, 0]
nums = [9, 0, 7, 31, 0, 45, 0, 45, 0, 45, 0, 0, 96, 0] # [9, 7, 31, 45, 45, 45, 96, 0, 0, 0, 0, 0, 0, 0]
nozero = []
skolko_zero = 0
for x in nums:
    if x == 0:
        skolko_zero += 1
    else:
        nozero.append(x)
nozero.extend([0] * skolko_zero)
print(nozero)
