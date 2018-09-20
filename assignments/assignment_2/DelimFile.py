from WriteFile import WriteFile


class DelimFile(WriteFile):
    def __init__(self, filename, delimiter):
        super(DelimFile, self).__init__(filename)
        self.delimiter = delimiter

    def write(self, text):
        count = 0
        delim_file = self.open_file()
        for token in text:
            count += 1

            if self.delimiter not in token:
                delim_file.write(token)

            else:
                print("found delimeter in token")
                delim_file.write("\"" + token + "\"")

            if count < len(text):
                delim_file.write(self.delimiter)

            else:
                delim_file.write("\n")

        delim_file.close()

