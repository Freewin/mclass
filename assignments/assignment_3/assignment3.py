class ConfigDict(dict):

    def __init__(self, filename):
        self._filename = filename

        # check if file exists
        try:
            fh = open(self._filename, 'r')
        except FileNotFoundError:
            print("File could not be found")

        for line in fh:
            line = line.rstrip()
            (key, value) = line.split('=', 1)
            dict.__setitem__(self, key, value)

        fh.close()

    def __setitem__(self, key, value):
        # Add new item to our dict
        dict.__setitem__(self, key, value)

        # Write entire dict to file overwriting existing file
        with open(self._filename, 'w') as fh:
            for k,v in self.items():
                fh.write('{0}={1}\n'.format(k, v))
