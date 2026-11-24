import json
import logging

OUTFILE = 'datafile.txt'

def write_data(data):
    with open(OUTFILE, 'a') as f:
        
        f.write(f'{json.dumps(data)}\n')
        
def read_data():
    data = []
    try:
        with open(OUTFILE, 'r') as f:
            for rawline in f.readlines():
                line = json.loads(rawline)
                data.append(line)
        return data
    except (FileNotFoundError, json.JSONDecodeError):
        logging.exception('error reading data file')        
        return []
