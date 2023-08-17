# 左右两边下一个严格更小元素
n = len(nums)
left, right = [-1] * n, [n] * n
stack = []
for i in range(n):
    while stack and nums[i] <= nums[stack[-1]]:  # （严格）更大或者（严格）更小依据这里修改
        stack.pop()
    if stack:
        left[i] = stack[-1]
    stack.append(i)

stack = []
for i in range(n - 1, -1, -1):
    while stack and nums[i] <= nums[stack[-1]]:
        stack.pop()
    if stack:
        right[i] = stack[-1]
    stack.append(i)
