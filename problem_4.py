# it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
# A = {19, 22, 24, 20, 25, 26}
# B = {19, 22, 20, 25, 26, 24, 28, 27}
# age = [22, 19, 24, 25, 26, 24, 25, 24]
# • Find the length of the set it_companies
# • Add 'Twitter' to it_companies
# • Insert multiple IT companies at once to the set it_companies
# • Remove one of the companies from the set it_companies
# • What is the difference between remove and discard
# • Join A and B
# • Find A intersection B
# • Is A subset of B
# • Are A and B disjoint sets
# • Join A with B and B with A
# • What is the symmetric difference between A and B
# • Delete the sets completely
# • Convert the ages to a set and compare the length of the list and the set.

it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]


print(f'length of It companies: {len(it_companies)}')


it_companies.add('Twitter')
print(f'after adding Twitter to IT companies: {it_companies}')

it_companies.update(['Zen 3', 'Paypal', 'Red Bus'])
print(f'after adding multiple items to IT companies: {it_companies}')


it_companies.remove('Paypal')
print(f'after removing paypal from IT companies: {it_companies}')


# ? Difference between Discard and Remove
# * Discard will not throw an error if the item do not exit. Remove will throw an error if the item do not exist

C = A.union(B)
# A.update(B)
print(f'After join of B on A: {C}')

intersection = A.intersection(B)
print(f'After Intersection of A and B: {intersection}')


print(f'is A subset of B?: {A.issubset(B)}')

print(f'are A and B disjoint?: {A.isdisjoint(B)}')



A_with_B = A.union(B)
B_with_A = B.union(A)
print(f'join A with B: {A_with_B} and B with A: {B_with_A}')


print(f'symmetric difference between A and B: {A.symmetric_difference(B)}')


A.clear()
print(f'A after deleting: {A}')

ages_list = list(age)
print(f'length of ages set: {len(age)}, length of ages list: {len(ages_list)}')