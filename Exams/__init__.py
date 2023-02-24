from project_1508.bakery import Bakery

bakery = Bakery('Random')
print(bakery.add_food("g", 'spring', 250))
print(bakery.add_drink("Tea", 'mineral', 50, 'bankia'))
print(bakery.add_drink("Tea", 'cold', 500, 'nestle'))
print(bakery.add_table('OutsideTable', 55, 15))
print(bakery.reserve_table(10))
print(bakery.order_drink(55, "spring", "mineral", "ice", "cola" "fanta"))
print(bakery.leave_table(55))

print(bakery.get_total_income())
# print(bakery.add_table('OutsideTable', 56, 15))
# print(bakery.add_table('InsideTable', 5, 15))
# print(bakery.get_free_tables_info())

# print(bakery.add_food('Cake', "Carrot", 3.40))
# print(bakery.add_food('Bread', "BananaBread", 2.50))
# print(bakery.add_food('Cake', "ChokoCake", 4))
# print(bakery.add_table('OutsideTable', 55, 15))
# print(bakery.reserve_table(10))
#print(bakery.order_food(55, "Carrot", "BananaBread", "ChokoCake", "ff", "dd"  ))
# print(bakery.add_drink('Tea', "b", 2, "ff"))
# print(bakery.add_drink('Tea', "b", 3, "ff"))

# print(bakery.add_table("InsideTable", 1, 15))
# print(bakery.add_table("OutsideTable", 55, 10))
# print(bakery.reserve_table(10))
# print(bakery.reserve_table(5))