from data import MENU, resources
power = True
money = 0


def check(user_req, cur_res):
    if not user_req in MENU:
        print("Invalid input, please try again.\n")
        return False
    for resource in cur_res:
        if cur_res[resource] < MENU[user_req]["ingredients"][resource]:
            print(f"Sorry there is not enough {resource}\n")
            return False
    return True


def process_coin(user_req):
    total = 0.0
    total += int(input("How many quarters would you like to insert? ")) * 0.25
    total += int(input("How many dimes would you like to insert? ")) * 0.10
    total += int(input("How many nickles would you like to insert? ")) * 0.05
    total += int(input("How many pennies would you like to insert? ")) * 0.01
    return round(total - MENU[user_req]["cost"], 2)


def make_coffee(user_req, cur_res):
    for resource in cur_res:
        cur_res[resource] -= MENU[user_req]["ingredients"][resource]


while power:
    request = input("What would you like? (espresso/latte/cappuccino): ")
    if request == "off":
        power = False
    elif request == "report":
        print(f"Water : {resources['water']}ml")
        print(f"Milk : {resources['milk']}ml")
        print(f"Coffee : {resources['coffee']}g")
        print(f"Money : ${money}\n")
    else:
        if check(request, resources):
            change = (process_coin(request))
            if change < 0:
                print("Sorry there is not enough money. money refunded")
            else:
                if change > 0:
                    print(f"Here is ${change} in change.")
                make_coffee(request, resources)
                print(f"Here is your {request}☕. Enjoy!\n")
                money += MENU[request]["cost"]
