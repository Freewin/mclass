class MaxSizeList(object):

    def __init__(self, size):
        self.size = size
        self.my_list = []

    def push(self, element):
        if len(self.my_list) < self.size:
            self.my_list.append(element)
        else:
            self.my_list.pop(0)
            self.my_list.append(element)

    def get_list(self):
        return self.my_list
