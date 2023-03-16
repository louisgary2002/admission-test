def find_max(numbers):
    return max(numbers) #回傳最大值


print(find_max([1, 2, 4, 5]) ); # should print 5
print(find_max([5, 2, 7, 1, 6]) ); # should print 7



def find_position(numbers, target):
    for i in range(len(numbers)):
        if numbers[i] == target:
            return i
    return -1

print(find_position([5, 2, 7, 1, 6], 5)) # should print 0
print(find_position([5, 2, 7, 1, 6], 7)) # should print 2
print(find_position([5, 2, 7, 7, 7, 1, 6], 7)) # should print 2 (the first one)
print(find_position([5, 2, 7, 1, 6], 8)) # should print -1


input1 = ['a', 'b', 'c', 'a', 'c', 'a', 'x']

def count(input):
    counts = {}
    for item in input:
        if item in counts:
            counts[item] += 1
        else:
            counts[item] = 1
    return counts

print(count(input1))




def group_by_key(input_list):
    output_dict = {}
    for item in input_list:
        key = item['key']
        value = item['value']
        if key in output_dict:
            output_dict[key] += value
        else:
            output_dict[key] = value
    return output_dict


input2 = [
{'key': 'a', 'value': 3},
{'key': 'b', 'value': 1},
{'key': 'c', 'value': 2},
{'key': 'a', 'value': 3},
{'key': 'c', 'value': 5}
]

print(group_by_key(input2)) # should print {‘a’: 6, ‘b’: 1, ‘c’: 7}