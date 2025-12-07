from xml.sax.handler import property_interning_dict

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import random as rd

from sympy.integrals.meijerint_doc import category
from sympy.physics.units.systems.si import units

# x = np.arange(1,11)
# y = x*2
# print(y)    


# plt.plot(x,y)
# plt.title("Simple Line graph")
# plt.xlabel("X values")
# plt.ylabel("y values")
# plt.show()

# x = np.random.randn(100)
# y = x*3+2+np.random.randn(100)

# plt.scatter(x,y)
# plt.title("Scatter plot")
# plt.xlabel("x values")
# plt.ylabel("y values")
# plt.show()

# data = {'Pokemon': ["Charizard",'Blastoise','Venusuar'],
#          "HP": [80,30,40]}

# df = pd.DataFrame(data)
# print(df)
# plt.bar(df['Pokemon'], df["HP"])
# plt.title("Hp comparison")
# plt.ylabel("Hp")
# plt.show()

#histograms

# data = np.random.normal(50,10, size=1000)
# print(data)
# plt.hist(data,bins=40)
# plt.title("Distribution of Data")
# plt.xlabel("Value")
# plt.ylabel("Frequency")
# plt.show()
#
# pokemon = pd.read_csv('pokemon.csv')
# types = pokemon['Type1'].drop_duplicates()
# group = pokemon.groupby('Type1')['Height'].mean()
#
# plt.figure(figsize=(10,6))
# bars = plt.barh(group.index, group.values)
# for bar in bars:
#     width = bar.get_width()
#     print(bar.get_y())
#     plt.text(width,bar.get_y() + bar.get_height()/2, f"{width:.2f}",ha='left',va='center',
#               fontsize=9)
#
# plt.xlabel('Mean Height')
# plt.ylabel('Pokemon Types')
# plt.title('Kanto Average Height')
# plt.show()

# days = np.arange(1,8)
# xp_gain = np.array([40,55,60,30,90,20,75])
#
# plt.plot(days,xp_gain, marker='o')
# plt.xlabel('Days',fontsize=10)
# plt.ylabel('XP Gain', fontsize=10)
# plt.title('XP Gain Over a Week', fontsize=10)
# plt.show()

# pokemon = pd.read_csv('stats.csv')
# poke = pokemon['Name']
# my_pokemon = rd.sample(list(poke), 3)
# subset = pokemon[pokemon["Name"].isin(my_pokemon)]
# bar = plt.barh(subset['Name'], subset['Attack'])
# for bar,value in zip(bar, subset['Attack']):
#     bar.set_facecolor('blue')
#     bar.set_edgecolor('blue')
#     bar.set_linewidth(0.5)
#     bar.set_alpha(0.5)
#     plt.text(bar.get_width(), bar.get_y()+bar.get_height()/2, f"{value}",
#              family='Arial', ha='left', va='center', fontsize=12)
#
# plt.xlabel('Attack STATE')
# plt.ylabel('Name')
# plt.show()

# pokemon = pd.read_csv('stats.csv')
# pokemons = pokemon['Name']
# random_pokemons = rd.sample(list(pokemons), 6)
# my_team = pokemon[pokemon['Name'].isin(random_pokemons)]
# stats = {}
# for index, row in my_team.iterrows():
#     stats[row['Name']] = {'Attack': row['Attack'], 'Defense': row['Defense'], 'Speed': row['Speed']}
# height = 0.25
# y = np.arange(len(stats))
# names = stats.keys()
#
# attack = np.array([stats[n]['Attack'] for n in names])
# defense = np.array([stats[n]['Defense'] for n in names])
# speed = np.array([stats[n]['Speed'] for n in names])
# plt.figure(figsize = (8,8))
# plt.barh(y-height,attack,label="Attack", height=height)
# plt.barh(y,defense,label="Defense",height=height)
# plt.barh(y+height,speed,label="Speed", height=height)
# plt.yticks(y,names,va='center')
# plt.xlabel('Stat Value',fontsize=12)
# plt.ylabel('Pokemon Names', fontsize = 10)
# plt.legend(loc='upper right')
# plt.show()



# sales = pd.read_csv('sales.csv')
# plt.plot(sales['Month'],sales['Revenue'], marker='o')
# plt.ylabel('Revenue')
# plt.xlabel('Month')
# plt.title('Revenue Over The Year')
# plt.show()
#

# sales = pd.read_csv('sales.csv')
# electronics = sales.loc[sales['Category'] == 'Electronics']
# clothing = sales.loc[sales['Category'] == 'Clothing']
# furniture = sales.loc[sales['Category'] == 'Furniture']
# home = sales.loc[sales['Category'] == 'Home']
# color = ['blue', 'red', 'green', 'yellow']
#
# values = {"electronics": {'Units_Sold': electronics["Units_Sold"],"Revenue": electronics["Revenue"]},
#          "clothing": {'Units_Sold': clothing["Units_Sold"],"Revenue": clothing["Revenue"]},
#          "furniture": {'Units_Sold': furniture["Units_Sold"],"Revenue": furniture["Revenue"]},
#          "home": {'Units_Sold': home["Units_Sold"],"Revenue": home["Revenue"]}
#          }
#
# print(values)
# i = 0
# for key,value in values.items():
#  plt.scatter(value['Units_Sold'],value["Revenue"],color=color[i],label=key,)
#  i+=1
# plt.legend(loc='best',fontsize='8')
# plt.show()


# sales = pd.read_csv('sales.csv')
# group = sales.groupby('Category').sum()
# categories = group.index
# items_dict = {}
# color = ['red', 'blue', 'green', 'yellow']
# for category in categories:
#     items_dict[category] = group.loc[category,'Revenue']
# i = 0
# for key, value in items_dict.items():
#     bar = plt.bar(key, value, color=color[i], label=key)
#     i+=1
#     plt.text(key, value, f"{value:.2f}", ha='center', va='bottom')
# plt.legend(loc='upper right', fontsize='8')
# plt.xlabel('Category')
# plt.ylabel('Revenue')
# plt.show()

# sales = pd.read_csv('sales.csv')
# plt.hist(sales['Expenses'], bins=10)
# plt.show()

# sales = pd.read_csv('sales.csv')
# months = sales['Month']
# revenues = sales['Revenue']
# expenses = sales['Expenses']
# dict_of_values = {}
# height = 0.35
#
# y = np.arange(len(months))
# plt.barh(y+height,revenues, label='Revenue', height=height)
# plt.barh(y,expenses, label='Expenses', height=height)
# for i,rec in enumerate(revenues):
#  plt.text(rec+50,y[i]+height,f"{rec}",ha='left',va='center')
# for i,rec in enumerate(expenses):
#  plt.text(rec+50,y[i],f"{rec}",ha='left',va='center')
# plt.yticks(y+height, months)
# plt.legend()
# plt.show()

# sales = pd.read_csv('sales.csv')
# month = sales['Month']
# data = sales['Revenue'] - sales['Expenses']
# plt.plot(month,data, marker='o')
# plt.show()


