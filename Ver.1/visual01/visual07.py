import matplotlib.pyplot as plt
from random import randint
import numpy as np

fig, ax = plt.subplots()

x = list(randint(0,1000) for i in range(10))
print(x)
print(np.mean(x))
print(np.median(x))

ax.boxplot(x)

plt.show()