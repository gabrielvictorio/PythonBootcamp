#!/usr/bin/env python3

from logic.menu import Menu
from logic.coffee_maker import CoffeeMaker
from logic.money_machine import MoneyMachine

coffe_maker = CoffeeMaker()
charge = MoneyMachine()
menu = Menu()

not_stop = True
while not_stop:
  request = input(f"Please select one of the items: {menu.get_items()}: ").lower()
  if request == "report":
    coffe_maker.report()
    charge.report()
  elif request == "off":
    print("Entering maintenace mode, The machine will turn off")
    not_stop = False
  else:
    info_request = menu.find_drink(request)
    if coffe_maker.is_resource_sufficient(info_request):
      if charge.make_payment(info_request.cost):
        charge.money_received += info_request.cost
        coffe_maker.make_coffee(info_request)
