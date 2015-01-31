import pandas as pd

print 'Start join'

# Loading both tables to memory
small_table = pd.read_csv('committee_names_unedited_excludes_candidate_control_committees.csv')
big_table = pd.read_csv('funding_committees_includes_candidate_control.csv')

# We don't need this (and causes a conflict bc the other table also has a column named like that.)
small_table = small_table.drop('ID', axis=1)

# When we actually do the join
joined_table = pd.merge(small_table, big_table, left_on='committee name', right_on='Name', how='left')

print joined_table[:10]