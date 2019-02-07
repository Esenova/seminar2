from myclass import Plov
from mybox import MyBox

p_type = input("Please, enter the plove type: ")

plov = Plov(p_type)

# print(plov.plov_type + ' ' + plov.name)
# print('Рис: ', plov.rice)
# print('Мясо: ', plov.meat)
# plov.get_portion()
# plov.add_carrot()

box = MyBox(plov())

print('length is: ', box.get_len())
print('Adding object to container: ', box.add('Cucumber'))
print('Removing object from container: ',box.remove('Cucumber'))
print('It contains the Плов:', box.contains('Плов'))
print('Iterating container: ')
box.iterator()
