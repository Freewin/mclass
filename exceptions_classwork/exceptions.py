
my_dict = {'a':1, 'b':2, 'c':3, 'd':4}

key = input('please enter a key: ')

try:
    print('testing for error')
    print('the value for {0}a is {1}'.format(key, my_dict[key]))

except KeyError:
    print('trapped error')
    print('the key ' + key + ' does not exist')

print('The program continues...')