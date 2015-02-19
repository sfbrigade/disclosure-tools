
import pandas as pd

data = pd.read_csv('committee_names_with_all_columns.csv')
print '# Shape of the dataset : %d, %d' %(data.shape[0], data.shape[1])
print '\n'*2 + '#'*40

print '#'*10 + ' Working on names ' + '#'*10
print '#'*40 + '\n'*2

print '# Count for (last name + first name)'
print data.apply(lambda x: str(x['TreasurerLast']) + ', ' + str(x['TreasurerFirst']),1).value_counts()
print '#'*40 + '\n'*2


# Print how many Treasurers have N comittees to their name 
tmp = data.apply(lambda x: str(x['TreasurerLast']) + ', ' + str(x['TreasurerFirst']),1).value_counts().value_counts()
tmp.sort()
print '# How many Treasurers have N comittees to their name ?'
print 'Number of comittees with the same Treasurer | Number of occurences in the data' 
print tmp
print '#'*40 + '\n'*2

# To save to a CSV file
# data['TreasurerLast'].value_counts().to_csv('counts_names.csv') 

print '# Count for last name'
print data['TreasurerLast'].value_counts()
print '#'*40 + '\n'*2

# To save to a CSV file
# data['TreasurerLast'].value_counts().to_csv('counts_last_name.csv') 

# Printing the comittee names of a given Treasurer

Name_of_the_treasurer = 'Heneghan' # Paste the name of the guy here, the only line you should change
print '# These are the comittees where %s is Treasurer' %(Name_of_the_treasurer)
print data['Name'][data['TreasurerLast'] == Name_of_the_treasurer]

print '\n'*5 + '#'*40
print '#'*10 + ' Working on adresses ' + '#'*10
print '#'*40 + '\n'*2

print '# Count for adresses + Zip code'
print data.apply(lambda x: str(x['MailingLine1']) + ', ' + str(x['DisclosurePostalCode']),1).value_counts()
print '#'*40 + '\n'*2

print '# Count for adresses'
print data.apply(lambda x: str(x['MailingLine1']),1).value_counts()
print '#'*40 + '\n'*2

# Print how many adresses have N comittees in their building 
tmp2 = data.apply(lambda x: str(x['MailingLine1']) + ', ' + str(x['DisclosurePostalCode']),1).value_counts().value_counts()
tmp2.sort()
print '# How many adresses have N comittees in their building ?'
print 'Number of comittees with the same adress | Number of occurences in the data' 
print tmp2
print '#'*40 + '\n'*2

# Printing the comittee names that are register at a given address
Adress_of_the_comittee = '150 Post Street, Suite 405' # Paste the address of the comittee here, the only line you should change

print '# These are the comittees registered at %s' %(Adress_of_the_comittee)
print data['Name'][data['MailingLine1'] == Adress_of_the_comittee]

