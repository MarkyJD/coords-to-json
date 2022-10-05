"""Purpose built for Earthle. Converts a line-seperated list of comma-seperated coordinates into a JSON file.

Usage:
    gen-coords.py -i <input_file>

Arguments:
    <input_file> (REQUIRED)  The input file to read from.

Options:
    -d <start_date> (OPTIONAL)  Start date for the coordinates in format YYYY-MM-DD. Defaults to current local date.

Output:
    A JSON file named with start and end dates of the coordinates.
      
Example:
    gen-coords.py -i coords.txt -d 2022-10-05

    example output:
      
      {
        "date": "2022-10-05",
          "location": {
            "lat": -38.15221989407775,
            "lng": 144.37571532382444
          }
      },
    
"""

import argparse
import json
import re
import os
from datetime import datetime, timedelta

parser = argparse.ArgumentParser(description='Generate json object with date and coordinates for a given list of comma seperated coordinates')
parser.add_argument('input_file', type=str, help="File path to .txt file containing lines or comma seperated coords in format <lat, long>")

parser.add_argument('-d', '--date', type=str, help="Starting date as <YYYY-MM-DD>. If not provided appends previous date by 1 day", required=False)

args = parser.parse_args()

date = datetime.today().strftime('%Y-%m-%d')


if args.date:
  if not re.match(r'^\d{4}\-(0[1-9]|1[012])\-(0[1-9]|[12][0-9]|3[01])$', args.date):
    print('Invalid date format. Must be real date and must be in format YYYY-MM-DD')
    exit(1)
  else:
    date = args.date

print('Start date: ' + date)
last_date = date

try:
  infile = open(args.input_file, 'r')
  outfile = open('coords.json', 'w', encoding='utf-8')
except:
  print('Invalid file path')
  exit(1)
with infile:
  data = []
  lines = infile.readlines()
  next_date = date
  for line in lines:
    coords = line.split(',')
    if len(coords) != 2:
      print('Invalid coordinates: ' + line)
      exit(1)
    
    data.append({
      'date': next_date,
      'location': {
        'lat': float(coords[0].strip()),
        'lng': float(coords[1].strip())
      }
    })
    next_date = (datetime.strptime(next_date, '%Y-%m-%d') + timedelta(days=1)).strftime('%Y-%m-%d')
    last_date = next_date

  json.dump(data, outfile, ensure_ascii=False, indent=2)
  outfile.close()
  infile.close()
  last_date = (datetime.strptime(last_date, '%Y-%m-%d') - timedelta(days=1)).strftime('%Y-%m-%d')
  os.rename('coords.json', 'coords-' + date + '--' + last_date + '.json')
