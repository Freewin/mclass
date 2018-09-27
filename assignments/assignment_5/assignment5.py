import os
import pickle


class ConfigKeyError(Exception):
    def __init__(self, this, key):
        self.key = key
        self.keys = this.keys()

    def __str__(self):
        return 'key "{0}" not found. Available keys: ({1})'.format(self.key, ', '.join(self.keys))


class ConfigPickleDict(dict):

    config_dir = '/Users/grojas/Documents/configs'

    def __init__(self, picklename):
        self._filename = os.path.join(ConfigPickleDict.config_dir, picklename + '.pickle')
        if not os.path.isfile(self._filename):
            with open(self._filename, 'wb') as fh:
                pickle.dump({}, fh)
        with open(self._filename, 'rb') as fh:
            pkl = pickle.load(fh)
            self.update(pkl)

    def __getitem__(self, key):
        if not key in self:
            raise ConfigKeyError(self, key)
        return dict.__getitem__(self, key)

    def __setitem__(self, key, value):
        # Add new item to our dict
        dict.__setitem__(self, key, value)

        # Write entire dict to file overwriting existing file
        with open(self._filename, 'w') as fh:
            for k,v in self.items():
                fh.write('{0}={1}\n'.format(k, v))
