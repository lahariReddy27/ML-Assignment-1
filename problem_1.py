# The following is a list of 10 students ages:
# ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
# • Sort the list and find the min and max age
# • Add the min age and the max age again to the list
# • Find the median age (one middle item or two middle items divided by two)
# • Find the average age (sum of all items divided by their number)
# • Find the range of the ages (max minus min)

import statistics

ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages.sort()
print(f'sorted list: {ages}')
print(f'min element: {ages[0]}, max element: {ages[-1]}')
ages = [ages[0]] + ages + [ages[-1]]
print(f'modified ages: {ages}')
print(f'median of the ages: {statistics.median(ages)}')
print(f'average of the ages: {sum(ages) // len(ages)}')
print(f'range: {max(ages) - min(ages)}')