from LogFile import LogFile
from DelimFile import DelimFile

log = LogFile("log.txt")
myDelim = DelimFile("data.csv", ",")


log.write("This is a log message")
log.write("This is another log message")

myDelim.write(['a', 'b', 'c', 'd'])
myDelim.write(['1', '2', '3', '4'])
