import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import random as rd

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

pokemon = pd.read_csv('stats.csv')
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


pokemons = pokemon['Name']
random_pokemons = rd.sample(list(pokemons), 6)
my_team = pokemon[pokemon['Name'].isin(random_pokemons)]
stats = {}
for index, row in my_team.iterrows():
    stats[row['Name']] = {'Attack': row['Attack'], 'Defense': row['Defense'], 'Speed': row['Speed']}
height = 0.25
y = np.arange(len(stats))
names = stats.keys()

attack = np.array([stats[n]['Attack'] for n in names])
defense = np.array([stats[n]['Defense'] for n in names])
speed = np.array([stats[n]['Speed'] for n in names])
plt.figure(figsize = (8,8))
plt.barh(y-height,attack,label="Attack", height=height)
plt.barh(y,defense,label="Defense",height=height)
plt.barh(y+height,speed,label="Speed", height=height)
plt.yticks(y,names,va='center')
plt.xlabel('Stat Value',fontsize=12)
plt.ylabel('Pokemon Names', fontsize = 10)
plt.legend(loc='upper right')
plt.show()
