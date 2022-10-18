import matplotlib.pyplot as plt
import random

#fig = plt.figure()
# ax01 = fig.add_subplot(2,2,1)
# ax02 = fig.add_subplot(2,2,2)
# ax03 = fig.add_subplot(2,2,3)
# ax04 = fig.add_subplot(2,2,4)

fig, ax = plt.subplots(2,2)

x = list(range(50))

y01 = list(random.randint(0,50) for i in range(50))
y02 = list(random.randint(0,50) for i in range(50))
y03 = list(random.randint(0,50) for i in range(50))
y04 = list(random.randint(0,50) for i in range(50))

ax[0,0].scatter(x, y01, color='red')
ax[0,1].scatter(x, y02, color='green')
ax[1,0].scatter(x, y03, color='blue')
ax[1,1].scatter(x, y04, color='yellow')

fig.tight_layout()
plt.show()