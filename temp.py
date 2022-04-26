def twosum(nums, sum_01):    
    s = {}
    for i in range(len(nums)):
        diff = sum_01 - nums[i]
        if diff in s:
            return f'{s.get(diff)}, {i}'
        s.update({nums[i]: i})

n = input()
n = n.replace(',', ' ')
n = list(map(int, list(n.split())))
print(n)
sum_1 = int(input())

print(twosum(n, sum_1))