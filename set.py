numbers = {21,34,54,12}
print('initial set:', numbers)
numbers.add(32)

print('updated set:', numbers)

companies = {'locoste','Ralph', 'Lauren'}
tech_companies = ('apple', 'google', 'apple')

companies.update(tech_companies)
print(companies)
languages = {'swift', 'java','python'}
print('initial set:', languages)

removevalue = languages.discard('java')

print('set after remove():', languages)
