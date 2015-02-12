
import sqlite3
from numpy import nan

from bottle import route, run, jinja2_view, request, redirect

# Local imports
from setup_deduper import setup_deduper

deduper = setup_deduper()
uncertain_pairs = deduper.uncertainPairs()
labels = {'distinct' : [], 'match' : []}

fields = set(field[0] for field in deduper.data_model.field_comparators)

@route('/run')
@jinja2_view('run.html', template_lookup=['.', 'templates'])
def dedupe_get():
  label = ''
  labeled = False

  record_pair = uncertain_pairs[0]

  return { 'record_pair': record_pair, 'fields': fields }

@route('/run/submit', method='POST')
def dedupe_submit():
  print request.forms.get('answer')
  redirect('/run')

if __name__ == '__main__':
  print 'starting server...'
  run(host='localhost', port=8080)
