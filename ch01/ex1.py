import time

start = time.time()
count = 10 ** 5
nums = []
for i in range(count):
  nums.append(i)

nums.reverse()
print(time.time() - start)
