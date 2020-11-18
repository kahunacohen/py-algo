import time

start = time.time()
count = 10 ** 5
nums = []
for i in range(count):
    nums.insert(0, 1)
    
print(time.time() - start)
