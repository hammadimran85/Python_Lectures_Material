import pandas as pd

# CREATING A DICTIONARY
dict={
    'Name': ['Arsal','Ahsan','Hammad','Asad','Rizwan'],
    'Age':[22,22,23,25,25],
    'Degree':['SE','IT','CS','DS','AI']
}
# list = ["Hammad",[1,2,3,4],{'a':1},4.5,(1,2,34,4)]
# list2 = [1,2,3,4,5]
# dict2 = {'a':1,'b':2,'c':3}
# print(dict2)
# series = pd.Series(dict2)
# print(series)
# CREATING AND PRINTING THE TABLE
u = pd.DataFrame(dict)
# print(u.sort_values(by='Age', ascending=True))
print(u['Age'].drop_duplicates())
# print(u.fillna(20))
# print(u['Name'])
# print(u.iloc[0])

# CREATING THE CSV FILE
u.to_csv('sample_data.csv',sep='|',index=False,header=False,)
u.to_excel('sample.xlsx')

# #READING THE CSV FILE
# u = pd.read_csv('sample_data.csv')
# print(u)

# READING THE SPECIFIC COLUMN & Rows IN CSV FILE
# u = pd.read_csv('sample_data.csv', usecols=['Age'])
u = pd.read_csv('sample_data.csv', header=[0])
# print(u.values.tolist())

# READING SPECIFIC VALUES IN SPECIFIC COLUMNS
# u = pd.read_csv('sample_data.csv')
# col = u['Name']
# for i in col:
#     print(i[0])

# # DELETING SPECIFIC COLUMN
# u.pop('Degree')
# print(u)
#
# # FOR USING SUM FUNCTION
# print (u.sum())

# # FOR USING COUNT FUNCTION
# print (u.count())

# # FOR USING AVERAGE FUNCTION
# u1 = u['Age'].mean()
# print(u1)

# # ITERATING COLUMNS
# col=u['Name']
# for i in col:
#     print(i[1])

# Get Rows
# print(u.head(3))
# print(u.tail(3))
# print(u.sample())
# print(u.describe())
# print(u.query("Age>23"))
# print(u.loc[2,"Degree"])
