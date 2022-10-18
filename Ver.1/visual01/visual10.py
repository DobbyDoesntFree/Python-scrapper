# -*- coding:utf-8 -*-

import matplotlib.pyplot as plt
from random import randint
import pandas as pd


fig = plt.figure(figsize=(15,10))

fruits = ['apple', 'watermelon', 'grape', 'banana', 'strawberry']

data = pd.DataFrame({'ages': list(randint(1,100) for i in range(100)),
                     'gender': list(randint(1, 4) for i in range(100)),
                     'fruits': list(fruits[randint(0, 4)] for i in range(100))})

fruit_list = list()
for fruit in fruits:
    fruit_list.append(data[data['fruits'] == fruit])

labels = ['child', 'young', 'middle', 'old']
colors = ['pink', 'red', 'green', 'blue']
man = data[(data['gender']== 1) | (data['gender']== 3)]
woman = data[(data['gender']== 2) | (data['gender']== 4)]

ax01 = fig.add_subplot(1, 2, 1)
ax01.hist(man['ages'], bins=10, color='blue', histtype='step', label='man')
ax01.hist(woman['ages'], bins=10, color='red', histtype='step', label='woman')

ax01.set_xticks(list(range(0, 101, 10)))
ax01.set_yticks(list(range(0, 16)))
ax01.set_xlim(0, 100)
ax01.set_ylim(0, 15)
ax01.legend()

fruit_age_count = {}
for i, fruit in enumerate(fruit_list):
    tmp_list = list()
    tmp_list.append(len(fruit[fruit['ages'] < 19]))
    tmp_list.append(len(fruit[(fruit['ages'] >= 19) & (fruit['ages'] < 40)]))
    tmp_list.append(len(fruit[(fruit['ages'] >= 40) & (fruit['ages'] < 60)]))
    tmp_list.append(len(fruit[fruit['ages'] > 60]))
    fruit_age_count[fruits[i]] = tmp_list

ax_list = list()
ax_list.append(fig.add_subplot(4, 4, 3))
ax_list.append(fig.add_subplot(4, 4, 4))
ax_list.append(fig.add_subplot(4, 4, 7))
ax_list.append(fig.add_subplot(4, 4, 8))
ax_list.append(fig.add_subplot(4, 4, 11))
for i, ax in enumerate(ax_list):
    ax.pie(fruit_age_count[fruits[i]], colors=colors, startangle=90, counterclock=False)
    ax.set_title(fruits[i])

ax07 = fig.add_subplot(4, 4, 12)
ax07.barh([1, 2, 3, 4], [1, 1, 1, 1], color=colors[::-1])
for i, label in enumerate(labels):
    ax07.text(1, 4-i, label, color=colors[i], fontweight='bold')

ax07.get_xaxis().set_visible(False)
ax07.get_yaxis().set_visible(False)
ax07.axis(xmin=0,xmax=3)


ax08 = fig.add_subplot(4, 2, 8)
fruit_len = [len(list(x for x in data['fruits'] if x == fruit)) for fruit in fruits]
ax08.bar(fruits, fruit_len)

man_fruits = list(map(lambda x: len(man['fruits'][data['fruits']==x]), fruits))
woman_fruits = list(map(lambda x: len(woman['fruits'][data['fruits']==x]), fruits))

ax08.plot(fruits, man_fruits, color='blue')
ax08.plot(fruits, woman_fruits, color='red')

ax08.tick_params(labelrotation=30)
ax08.set_yticks(list(range(0, 41, 5)))
ax08.set_ylim(0, 40)

plt.show()