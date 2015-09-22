from flask import Flask, request
from gsheet2json import gsheet2json

app = Flask(__name__)

@app.route('/sheet')
def convert_sheet():
  return gsheet2json(request.args.get('url'))

if __name__ == '__main__':
  app.run(debug=True, host='0.0.0.0', port=5001, passthrough_errors=True)

