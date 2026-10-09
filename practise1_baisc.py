import numpy as np

# A list to store all the smartphones (it's a Dictionary)
phone_inventory = [
    {"brand": "Apple", "model": "iPhone 15", "price": 799.0},
    {"brand": "Samsung", "model": "Galaxy S24", "price": 799.99},
    {"brand": "Google", "model": "Pixel 8a", "price": 499.0},
    {"brand": "Motorola", "model": "Moto G Power", "price": 199.99},
    {"brand": "OnePlus", "model": "OnePlus 12R", "price": 499.99}
]

while True:
    print("\n--- Smartphone Analyzer Menu ---")
    print("1. Add a Phone")
    print("2. View All Phones")
    print("3. Analyze Prices (NumPy)")
    print("4. Search Phones Under a Budget")
    print("5. Exit")
    
    choice = input("Enter your choice (1-5): ").strip()

    # 1. Add a Phone
    if choice == '1':
        brand = input("Enter Brand (e.g., Apple, Samsung): ").strip()
        model = input("Enter Model (e.g., iPhone 15, S24): ").strip()
        
        # We use float() so we can do math calculations later
        try:
            price = float(input("Enter Price in USD (e.g., 999): ").strip())
            
            # Store as a dictionary
            phone = {
                "brand": brand,
                "model": model,
                "price": price
            }
            
            # Add to the list
            phone_inventory.append(phone)
            print("Success: " + brand + " " + model + " has been added!")
        except ValueError:
            print("Invalid price! Please enter a numerical value.")

    # 2. View All Phones
    elif choice == '2':
        if len(phone_inventory) == 0:
            print("No phones added yet! Please add some first.")
        else:
            print("\n--- Current Inventory ---")
            counter = 1
            for phone in phone_inventory:
                price_rounded = round(phone['price'], 2)
                print(str(counter) + ". Brand: " + phone['brand'] + " | Model: " + phone['model'] + " | Price: $" + str(price_rounded))
                counter += 1

    # 3. Analyze Prices with NumPy
    elif choice == '3':
        if len(phone_inventory) == 0:
            print("You need to add at least one phone to analyze prices!")
        else:
            # 1. Pull all prices into a normal list using a normal loop
            prices_list = []
            for phone in phone_inventory:
                prices_list.append(phone['price'])
            
            # 2. Convert that list into a NumPy array
            prices_array = np.array(prices_list)
            
            # 3. Use NumPy functions taught in class
            avg_price = np.mean(prices_array)
            cheapest = np.min(prices_array)
            expensive = np.max(prices_array)

            # Round the numbers so they look neat
            avg_rounded = round(avg_price, 2)
            cheap_rounded = round(cheapest, 2)
            exp_rounded = round(expensive, 2)
            
            # Find matching phone names using normal loops
            cheapest_name = ""
            expensive_name = ""
            for p in phone_inventory:
                if p['price'] == cheapest:
                    cheapest_name = p['brand'] + " " + p['model']
                if p['price'] == expensive:
                    expensive_name = p['brand'] + " " + p['model']
            
            print("\n--- NumPy Price Analysis ---")
            print("Total Phones Analyzed: " + str(len(prices_array)))
            print("Average Price: $" + str(avg_rounded))
            print("Most Expensive Phone: $" + str(exp_rounded) + " (" + expensive_name + ")")
            print("Cheapest Phone: $" + str(cheap_rounded) + " (" + cheapest_name + ")")

    # 4. Search by Budget
    elif choice == '4':
        if len(phone_inventory) == 0:
            print("Inventory is empty.")
        else:
            try:
                budget = float(input("Enter your maximum budget: $").strip())
                found = False
                
                budget_rounded = round(budget, 2)
                print("\n--- Phones Under $" + str(budget_rounded) + " ---")
                for phone in phone_inventory:
                    if phone['price'] <= budget:
                        p_rounded = round(phone['price'], 2)
                        print("- " + phone['brand'] + " " + phone['model'] + " ($" + str(p_rounded) + ")")
                        found = True
                
                if not found:
                    print("No phones found within that budget.")
            except ValueError:
                print("Invalid budget! Please enter a numerical value.")

    # 5. Exit
    elif choice == '5':
        print("Thank you for using Smartphone Analyzer. Goodbye!")
        break

    else:
        print("Invalid choice! Please select 1, 2, 3, 4, or 5.")
