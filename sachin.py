me = []
for i in range (0,11):
    if i % 2 == 0:
        print(i)
        me.append(i)
print(me)


#list
def list_sum(input_list):
    sum = 0
    for element in input_list:
        sum += element
    # todo: Write a for loop that adds the elements
    # of input_list to the sum variable

    return sum


# These test cases check that list_sum works correctly
test1 = list_sum([1, 2, 3])
print("expected result: 6, actual result: {}".format(test1))

test2 = list_sum([-1, 0, 1])
print("expected result: 0, actual result: {}".format(test2))

#
manifest = [["bananas", 15], ["mattresses", 34], ["dog kennels",42], ["machine that goes ping!", 120], ["tea chests", 10], ["cheeses", 0]]
cargo_weight = 0
cargo_list = []
for cargo in manifest :
    if cargo_weight + cargo[1] >= 100:
        break
    else:
        cargo_list.append(cargo[0])
        cargo_weight += cargo[1]
print(cargo_weight)
print(cargo_list)

#dictionaries stores data in pairs
elements = {'hydrogen':1, 'helium':2 , 'carbon':6}
print(elements['carbon'])

#dictionaries in dictonary
elements = {'hydrogen': {'number': 1, 'weight': 1.00794, 'symbol': 'H'},
            'helium': {'number': 2, 'weight': 4.002602, 'symbol': 'He'}}
print(elements['helium'])

print(elements.get('unobtainium', 'There\'s no such element!'))
print(elements['helium']['weight'])


#tuples
def hours2days(input_hours):
    days = input_hours // 24
    hours = input_hours % 24
    return days, hours


call = hours2days(100)
print(call)