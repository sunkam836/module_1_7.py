# This is a sample Python script.
#grades = [[5, 4, 3, 3, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
#students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
journal = {'Aaron':[5, 3, 3, 5, 4], 'Bilbo':[2, 2, 2, 3], 'Johnny':[4, 5, 5, 2], 'Khendrik':[4, 4, 3], 'Steve':[5, 5, 5, 4, 5]}
average_1 = sum(journal['Aaron'])/len(journal['Aaron'])
average_2 = sum(journal['Bilbo'])/len(journal['Bilbo'])
average_3 = sum(journal['Johnny'])/len(journal['Johnny'])
average_4 = sum(journal['Khendrik'])/len(journal['Khendrik'])
average_5 = sum(journal['Steve'])/len(journal['Steve'])
results = {'Aaron':average_1,'Bilbo':average_2,'Johnny':average_3,'Khendrik':average_4,'Steve':average_5}
print(results)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
