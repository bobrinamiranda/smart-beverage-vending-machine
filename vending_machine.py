items = {
    1: {"name": "coffee", "price": 35, "stock": 7},
    2: {"name": "lemontea", "price": 30, "stock": 6},
    3: {"name": "coke", "price": 40, "stock": 8},
}
max_stock = 20
change_stock = 500
running = True

while running:

    if change_stock == 0:
        print("\nMachine has no change left")
        print("Machine stopped")
        break

    print("\n---- Vending Machine ----")
    print("Available items")

    for key in items:
        print(key, ".", items[key]["name"],
              "Rs:", items[key]["price"],
              "Stock:", items[key]["stock"])

    print("4. Refill machine")
    print("5. Exit")

    while True:
        try:
            choice = int(input("Enter the item number: "))

            if choice == 5:
                print("Thank you for using vending machine")
                running = False
                break

            elif choice == 4:
                print("\n--- Refill Menu ---")
                print("1. Refill single item")
                print("2. Refill all items")
                print("3. Refill change money")

                while True:
                    option = input("Choose option (1/2/3): ")

                    if option == "1":
                        while True:
                            try:
                                item_choice = int(input("Enter item number to refill: "))

                                if item_choice not in items:
                                    print("Invalid item number")
                                    continue

                                while True:
                                    qty = input(
                                        f"Enter stock to add for {items[item_choice]['name']}: ")

                                    if not qty.isdigit():
                                        print("Enter numbers only")
                                        continue

                                    qty = int(qty)

                                    if qty <= 0:
                                        print("Enter valid stock")

                                    elif items[item_choice]["stock"] + qty > max_stock:
                                        print("Maximum stock limit is", max_stock)
                                        print("Current stock:",
                                              items[item_choice]["stock"])
                                        print("Enter smaller quantity")

                                    else:
                                        items[item_choice]["stock"] += qty
                                        print("\nStock updated successfully")
                                        print("\nUpdated Stock:")
                                        print(items[item_choice]["name"], ":",
                                              items[item_choice]["stock"])
                                        break
                                break

                            except ValueError:
                                print("Enter numbers only")
                        break

                    elif option == "2":
                        for key in items:
                            while True:
                                qty = input(
                                    f"Enter stock to add for {items[key]['name']}: ")

                                if not qty.isdigit():
                                    print("Enter numbers only")
                                    continue

                                qty = int(qty)

                                if qty <= 0:
                                    print("Enter valid stock")

                                elif items[key]["stock"] + qty > max_stock:
                                    print(items[key]["name"],
                                          "cannot exceed", max_stock)
                                    print("Current stock:",
                                          items[key]["stock"])
                                    print("Enter smaller quantity")

                                else:
                                    items[key]["stock"] += qty
                                    break

                        print("\nMachine refilled successfully")
                        print("\nUpdated Stock:")
                        for key in items:
                            print(items[key]["name"], ":",
                                  items[key]["stock"])
                        break

                    elif option == "3":
                        while True:
                            money = input("Enter change money to add: ")

                            if not money.isdigit():
                                print("Enter numbers only")
                                continue

                            money = int(money)

                            if money > 0:
                                change_stock += money
                                print("Change money updated successfully")
                                print("Available change:", change_stock)
                                break
                            else:
                                print("Enter valid amount")
                        break

                    else:
                        print("Invalid option")
                break

            elif choice in items:
                item = items[choice]

                if item["stock"] == 0:
                    print(item["name"], "is out of stock")
                    continue

                print("You selected", item["name"])
                print("Price:", item["price"])

                while True:
                    qty = input(f"How many {item['name']} do you want: ")

                    if not qty.isdigit():
                        print("Enter numbers only")
                        continue

                    qty = int(qty)

                    if qty <= 0:
                        print("Enter valid quantity")
                    elif qty > item["stock"]:
                        print("Only", item["stock"], "available")
                    else:
                        break

                total_price = item["price"] * qty
                print("Total price:", total_price)
                break

            else:
                print("Invalid selection")

        except ValueError:
            print("Invalid input")

    if running and choice in items and item["stock"] > 0:
        while True:
            try:
                money = int(input("Enter the money: "))

                if money < total_price:
                    print("Insufficient amount")
                    print("Returning Rs:", money)
                    continue

                change = money - total_price

                if change > change_stock:
                    print("Machine does not have enough change")
                    print("Returning Rs:", money)
                    continue

                item["stock"] -= qty
                change_stock -= change
                print(item["name"], "dispensed successfully")

                if change > 0:
                    print("Returning change Rs:", change)
                break

            except ValueError:
                print("Enter numbers only")

    if running and choice in items:
        while True:
            again = input("Do you want to buy another item? (yes/no): ").lower()

            if again == "yes":
                break
            elif again == "no":
                print("Thank you for using vending machine")
                running = False
                break
            else:
                print("Please enter only yes or no")
