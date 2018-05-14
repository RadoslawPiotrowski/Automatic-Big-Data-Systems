import numpy as np
data = np.random.randint(4, size=10)
samples = data
print (data)
for i in range(9):
    samples[i] += 1
print(data)

print(np.argmin(samples))
