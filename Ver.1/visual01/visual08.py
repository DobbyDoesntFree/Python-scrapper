import matplotlib.pyplot as plt
from random import randint
import numpy as np


fig,ax=plt.subplots()
ages=list(randint(1,100) for i in range(100))
print(ages)

child = list(x for x in ages if x<19)
young = list(x for x in ages if 19<=x<40)
middle = list(x for x in ages if 40<=x<60)
old = list(x for x in ages if 60 <=x)

# print(child)
# print(young)
# print(middle)
# print(old)

labels=['child','young','middle','old']
count=[len(child), len(young), len(middle),len(old)]
ax.pie(count, labels=labels, counterclock=False, startangle=90)

plt.show()