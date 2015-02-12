
import sqlite3
import csv

# Expects as arguments:
# - columns [dictionary (column_name -> sql_type)]
# - table_name [string]
# - database_cursor [sql_cursor]
#
# This function will coerce column names and the table name to lowercase
def table_from_columns(columns, table_name, db_cursor):
  db_fields = ', '.join('%s %s' % (k.lower(), v) for (k, v) in columns.iteritems())

  query = 'CREATE TABLE %s (%s)' % (table_name, db_fields)
  print query
  db_cursor.execute(query)

def create_csv_460_table(db_cursor):
  csv_fields = {
    'Filer_ID': 'varchar(255)',
    'Filer_NamL': 'varchar(255)',
    'Report_Num': 'varchar(255)',
    'Committee_Type': 'varchar(255)',
    'Rpt_Date': 'varchar(255)',
    'From_Date': 'varchar(255)',
    'Thru_Date': 'varchar(255)',
    'Elect_Date': 'varchar(255)',
    'tblCover_Office_Cd': 'varchar(255)',
    'tblCover_Offic_Dscr': 'varchar(255)',
    'Rec_Type': 'varchar(255)',
    'Form_Type': 'varchar(255)',
    'Tran_ID': 'varchar(255)',
    'Entity_Cd': 'varchar(255)',
    'Payee_NamL': 'varchar(255)',
    'Payee_NamF': 'varchar(255)',
    'Payee_NamT': 'varchar(255)',
    'Payee_NamS': 'varchar(255)',
    'Payee_Adr1': 'varchar(255)',
    'Payee_Adr2': 'varchar(255)',
    'Payee_City': 'varchar(255)',
    'Payee_State': 'varchar(255)',
    'Payee_Zip4': 'varchar(255)',
    'Expn_Date': 'varchar(255)',
    'Amount': 'varchar(255)',
    'Cum_YTD': 'varchar(255)',
    'Expn_ChkNo': 'varchar(255)',
    'Expn_Code': 'varchar(255)',
    'Expn_Dscr': 'varchar(255)',
    'Agent_NamL': 'varchar(255)',
    'Agent_NamF': 'varchar(255)',
    'Agent_NamT': 'varchar(255)',
    'Agent_NamS': 'varchar(255)',
    'Cmte_ID': 'varchar(255)',
    'Tres_NamL': 'varchar(255)',
    'Tres_NamF': 'varchar(255)',
    'Tres_NamT': 'varchar(255)',
    'Tres_NamS': 'varchar(255)',
    'Tres_Adr1': 'varchar(255)',
    'Tres_Adr2': 'varchar(255)',
    'Tres_City': 'varchar(255)',
    'Tres_ST': 'varchar(255)',
    'Tres_ZIP4': 'varchar(255)',
    'Cand_NamL': 'varchar(255)',
    'Cand_NamF': 'varchar(255)',
    'Cand_NamT': 'varchar(255)',
    'Cand_NamS': 'varchar(255)',
    'Office_Cd': 'varchar(255)',
    'Offic_Dscr': 'varchar(255)',
    'Juris_Cd': 'varchar(255)',
    'Juris_Dscr': 'varchar(255)',
    'Dist_No': 'varchar(255)',
    'Off_S_H_Cd': 'varchar(255)',
    'Bal_Name': 'varchar(255)',
    'Bal_Num': 'varchar(255)',
    'Bal_Juris': 'varchar(255)',
    'Sup_Opp_Cd': 'varchar(255)',
    'Memo_Code': 'varchar(255)',
    'Memo_RefNo': 'varchar(255)',
    'BakRef_TID': 'varchar(255)',
    'G_From_E_F': 'varchar(255)',
    'XRef_SchNm': 'varchar(255)',
    'XRef_Match': 'varchar(255)',
    'Payee_Location': 'varchar(255)',
    'Tres_Location': 'varchar(255)',
  }

  table_from_columns(csv_fields, 'csv_460', cursor)

def import_csv_460(file_name):
  pass

def create_user_table(cursor):
  pass

def create_csv_committees_table(cursor):
  column_names = {
    'id': 'varchar(255)',
    'committee_name': 'varchar(255)',
    'name': 'varchar(255)',
    'status': 'varchar(255)',
    'type': 'varchar(255)',
    'fppcid': 'varchar(255)',
    'penid': 'varchar(255)',
    'mailingline1': 'varchar(255)',
    'mailingline2': 'varchar(255)',
    'mailingcity': 'varchar(255)',
    'mailingstate': 'varchar(255)',
    'mailingzip': 'varchar(255)',
    'disclosureline1': 'varchar(255)',
    'disclosureline2': 'varchar(255)',
    'disclosurecity': 'varchar(255)',
    'disclosurestate': 'varchar(255)',
    'disclosurepostalcode': 'varchar(255)',
    'treasurerfirst': 'varchar(255)',
    'treasurerlast': 'varchar(255)',
    'treasurerprefix': 'varchar(255)',
    'asst_treasurer_first': 'varchar(255)',
    'asst_treasurer_last': 'varchar(255)',
    'asst_treasurer_prefix': 'varchar(255)',
    'cont_cand_first': 'varchar(255)',
    'cont_cand_last': 'varchar(255)',
    'cont_cand_prefix': 'varchar(255)',
  }

  table_from_columns(column_names, 'csv_committees', cursor)

from setup_deduper import readData
def import_csv_committees_table(file_name, cursor):
  data = readData(file_name)

  for (row_id, row) in data.iteritems():
    columns, values = zip(*row.iteritems())

    column_list = ", ".join("'%s'" % (item.replace("'", "''"),) for item in columns)
    value_list = ", ".join("'%s'" % (item.replace("'", "''"),) for item in values)

    query = "INSERT INTO csv_committees (%s) VALUES (%s)" % (column_list, value_list)
    print query
    cursor.execute(query)

db_name = 'dedupe_server.sql'
def migrate_csv_committees(file_name):
  connection = sqlite3.connect(db_name)
  cursor = connection.cursor()

  create_csv_committees_table(cursor)
  import_csv_committees_table(file_name, cursor)

  connection.commit()

  return connection

if __name__ == '__main__':
  migrate_csv_committees('committee_names_with_all_columns.csv')
