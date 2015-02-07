
import pandas as pd

data = pd.read_csv('committee_names_with_all_columns.csv')
print 'Shape of the dataset : %d, %d' %(data.shape[0], data.shape[1])

print '#'*25
print 'count for (last name + first name)'
print data.apply(lambda x: str(x['TreasurerLast']) + ', ' + str(x['TreasurerFirst']),1).value_counts()

# To save to a CSV file
# data['TreasurerLast'].value_counts().to_csv('counts_names.csv') 

print '#'*25
print 'count for last name'
print data['TreasurerLast'].value_counts()

# To save to a CSV file
# data['TreasurerLast'].value_counts().to_csv('counts_last_name.csv') 


print '#'*25
