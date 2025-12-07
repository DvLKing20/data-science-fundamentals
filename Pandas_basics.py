import pandas as pd
import numpy as np

print(pd.__version__)
print("----------------------------------------------")
my_data = np.array(['bulbasaur', 'ivisaur', 'Venusaur','charmender','charmeleon','charizard'])
series = pd.Series(my_data,index=[data for data in range(1,len(my_data)+1)])
print(series)
print(series.loc[1])#for index
series.loc[1] = 'something'
print(series)
print(series.iloc[0])#for integer value
print(series[series == 'charizard'])

#with dicts
print("--------------------------------------------------------")
calories = {"day 1": 1400, "day 2": 1300, "day 3": 342}
cal = pd.Series(calories)
print(cal)
print("----------------------------------------------------------")
data = {'Name': ["Red", "Blue","Hilbert"],
        'age': [10,10,10],
        }
dataframe = pd.DataFrame(data, index=[f"trainer"+" "+str(tag) for tag in range(1,len(data.get('age'))+1)])
#how to add a colon
dataframe['pokemon'] = [150,100,100]
#how to add a row
rows = {'Name': ['oak'], 'age': [50], 'pokemon': [999999]}
new_row = pd.DataFrame(rows, index=[f"trainer"+" "+str(tag) for tag in range(len(dataframe)+1,len(dataframe)+len(rows.get('Name'))+1)])
dataframe = pd.concat([dataframe,new_row])
print(dataframe)
print(dataframe.loc['trainer 1'])
print(dataframe.iloc[0])
#csv
print("----------------------------------------------------------------------------------------\n\n")
dataframe = pd.read_csv('pokemon.csv',index_col='Name')#index_col changes the index to the Label instead
print(dataframe.to_string())
#for json same thing
# dataframe = pd.read_json("PATH")
# print(dataframe.to_string()) #to string is needed to print all of the contents of file be catious of when reading big files

#SELECTON BY COLON
# print(dataframe['Name'].to_string())
# print(dataframe['Weight'].to_string())
# print(dataframe['Height'].to_string())

#now i can do
# print(dataframe.loc['Charizard': 'Moltres', ['Height', 'Weight']])
# # ask = input("Enter a Pokemon Name: ").capitalize()
# # print(ask)
# # try: 
# #  print(dataframe.loc[ask])
# # except KeyError:
# #   print("not avalible in data")

dataframe = pd.read_csv('pokemon.csv')

print(dataframe[dataframe['Name'] == "Charizard"])
print(dataframe[dataframe['Legendary'] == True])
print(dataframe[(dataframe['Type1'] == "Fire") & (dataframe['Type2'] == 'Flying')])

#aggregation
#ALL  
print(dataframe.mean(numeric_only=True))
print(dataframe.std(numeric_only=True))
print(dataframe.sum(numeric_only=True))
print(dataframe.min(numeric_only=True))
print(dataframe.max(numeric_only=True))
print(dataframe.count())

#single colon

print(dataframe['Height'].mean(numeric_only=True))
print(dataframe['Weight'].std(numeric_only=True))
print(dataframe['No'].sum(numeric_only=True))
print(dataframe['Legendary'].min(numeric_only=True))
print(dataframe['Legendary'].max(numeric_only=True))
print(dataframe['Name'].count())

#group by

group = dataframe.groupby('Type1')
print(group['Height'].mean())
print(group['Height'].std())


#data cleaning

print(dataframe.drop(columns=["Legendary", "No"]))
print(dataframe.info())
print(dataframe.to_string())
print(dataframe.dropna(subset=["Type2"]).to_string())
print(dataframe.fillna({"Type2": "None"}))
dataframe['Type1'] = dataframe['Type1'].replace({"Fire": "Flying"})
print(dataframe)

#standardize text
dataframe['Name'] = dataframe['Name'].str.upper()
print(dataframe)

dataframe['Legendary'] = dataframe['Legendary'].astype(bool)
print(dataframe)

print(dataframe.drop_duplicates())

# class Person:
#     def __new__(cls):
#         return super().__new__(cls)

#     def  __init__(self):
#         self.name = 'kaif'
    
#     def pr(self):
#         print(self.name)


# p = Person.__new__(Person)
# Person.__init__(p)
# Person.pr(p)