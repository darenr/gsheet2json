import csv
import requests
import json
import cStringIO
import sys

def gsheet2json(url):
  print 'fetching', url
  result = []
  r = requests.get(url)
  print r
  if r.status_code == 200:
    rows = csv.DictReader(cStringIO.StringIO(r.text))
    for row in rows:
      result.append(row)

  return json.dumps(result, sort_keys=True, indent=2)
 
if __name__=="__main__":
  print sheet2Json(sys.argv[1])
