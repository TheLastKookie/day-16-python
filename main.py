from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

run_machine = True
while run_machine:
    chosen_drink = input(f"What would you like? ({menu.get_items()}): ").lower()
    if chosen_drink == "off":
        run_machine = False
    elif chosen_drink == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        chosen_drink_object = menu.find_drink(chosen_drink)
        if chosen_drink_object is not None and \
                coffee_maker.is_resource_sufficient(chosen_drink_object) and \
                money_machine.make_payment(chosen_drink_object.cost):
            coffee_maker.make_coffee(chosen_drink_object)
