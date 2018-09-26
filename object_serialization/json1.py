import json

filename = 'backup_config.json'
with open(filename) as fh:
    conf = json.load(fh)

print(conf)
print(type(conf))