import abc


class WriteFile(object):
    def __init__(self, filename):
        self.filename = filename
        self.file = open(self.filename, "a")

    def __main__(self):
        pass

    @abc.abstractmethod
    def write(self, text):
        return

    def open_file(self):
        return self.file

    def close_file(self):
        self.file.close()



