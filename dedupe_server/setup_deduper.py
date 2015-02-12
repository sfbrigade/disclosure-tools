import csv
import re
import sys

import dedupe
from unidecode import unidecode

# COPY-PASTED FROM csv_example.com
def preProcess(column):
    """
    Do a little bit of data cleaning with the help of Unidecode and Regex.
    Things like casing, extra spaces, quotes and new lines can be ignored.
    """
    import unidecode
    column = column.decode("utf8")
    column = unidecode.unidecode(column)
    column = re.sub('  +', ' ', column)
    column = re.sub('\n', ' ', column)
    column = column.strip().strip('"').strip("'").lower().strip()
    return column

def readData(filename):
    """
    Read in our data from a CSV file and create a dictionary of records, 
    where the key is a unique record ID and each value is dict
    """

    data_d = {}
    with open(filename) as f:
        reader = csv.DictReader(f)
        for row in reader:
            clean_row = [(k.lower().replace(' ', '_'), preProcess(v)) for (k, v) in row.items()]
            row_id = int(row['ID'])
            data_d[row_id] = dict(clean_row)

    return data_d
# END COPY-PASTE

def setup_deduper():
  input_file = sys.argv[1]
  data_d = readData(input_file)

  # THIS IS COPY-PASTED FROM csv_example.py
  # Define the fields dedupe will pay attention to
  #
  # Notice how we are telling dedupe to use a custom field comparator
  # for the 'Zip' field. 
  fields = [
      {'field' : 'Site name', 'type': 'String'},
      {'field' : 'Address', 'type': 'String'},
      {'field' : 'Zip', 'type': 'Exact', 'has missing' : True},
      {'field' : 'Phone', 'type': 'String', 'has missing' : True},
      ]

  # Create a new deduper object and pass our data model to it.
  deduper = dedupe.Dedupe(fields)

  # To train dedupe, we feed it a sample of records.
  deduper.sample(data_d, 150000)

  # END OF COPY-PASTE

  return deduper

