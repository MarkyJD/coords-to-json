# coords-to-json

Purpose built for Earthle. Converts a line-seperated list of comma-seperated coordinates into a JSON file.

## Usage:
    coords-to-json.py -i <input_file>

## Arguments:
    <input_file> (REQUIRED)  The input file to read from.

## Options:
    -d <start_date> (OPTIONAL)  Start date for the coordinates in format YYYY-MM-DD. Defaults to current local date.

## Output:
    A JSON file named with start and end dates of the coordinates.
      
## Example:
    coords-to-json.py -i coords.txt -d 2022-10-05
This sets the start from 2022-10-05 

## Example Output
```json
{
  "date": "2022-10-05",
  "location": {
    "lat": -38.15221989407775,
    "lng": 144.37571532382444
  }
}
```
