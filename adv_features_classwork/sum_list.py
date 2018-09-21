# This is work done in the lecture that
# demonstrates overloading the core methods
# that are available in Python


class SumList(object):

    def __init__(self, this_list):
        self.mylist = this_list

    def __add__(self, other):

        new_list = [x + y for x, y in zip(self.mylist, other.mylist)]

        # The following 4 lines are the same as the line above
        # new_list = []
        # zipped_list = zip(self.mylist, other.mylist)
        # for tup in zipped_list:
        #   newlist.append(tup[0] + tup[1])

        return SumList(new_list)

    def __repr__(self):
        return str(self.mylist)


cc = SumList([1, 2, 3, 4, 5])
dd = SumList([100, 200, 300, 400, 500])

ee = cc + dd        # cc.__add__(dd)
print(ee)           # should give 1 + 100, 2 + 200, 3 + 300, ...