import datetime

from WriteFile import WriteFile


class LogFile(WriteFile):
    def write(self, text):
        date_string = datetime.datetime.now().strftime('%Y-%m-%d %H:%M')
        log_file = self.open_file()
        log_file.write(date_string + "\t" + text + "\n")
        log_file.close()

