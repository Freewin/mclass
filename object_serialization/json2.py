import json

filename = 'backup_config.json'
with open(filename) as fh:
    conf = json.load(fh)

conf['newkey'] = 5.0005

with open(filename, 'w') as fh:
    json.dump(conf, fh)