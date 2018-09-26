import json

filename = 'backup_config.json'
with open(filename) as fh:
    conf = json.load(fh)

with open(filename, 'w') as fh:
    json.dump(conf, fh, indent=4, separators=(',', ':'))
