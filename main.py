# vending machine program
# link to asci art: https://emojicombos.com/vending-machine-ascii-art
print('''
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⠀⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⠀⢀⣀⡀⠀⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⠀⣿⣿⡟⠛⣿⣿⠋⣿⣿⣿⣿⣿⠀⣿⠉⣿⠀⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⠀⣿⣏⣁⣀⣉⣁⣀⣉⣉⣉⣉⣿⠀⠿⠶⠿⠀⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⠀⣿⣿⣿⣿⣿⣿⣿⡿⠛⢿⣿⣿⠀⠰⠶⠆⠀⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⠀⣿⣯⣭⣭⣭⣭⣭⣥⣤⣬⣭⣿⠀⠐⠶⠆⠀⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⠀⣿⣿⡟⢿⣿⠁⣿⣿⠉⢹⣿⣿⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⠀⣿⣧⣤⣤⣤⣤⣤⣤⣤⣤⣤⣿⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⠀⣿⣿⠉⠙⣿⠉⠉⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⠀⣿⣷⣶⣶⣶⣶⣶⣶⣶⣶⣶⣿⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠰⠶⠆⠀⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⠀⣉⣉⣉⣉⣉⣉⣉⣉⣉⣉⣉⣉⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⠀⣿⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⢻⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⠀⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
''')

print("Welcome to BVM")
print("This vending machine only accepts note: 1 - 5 - 10 - 20 - 50 - 100")

cart = [] # purchase > 1
# product list
products = {
  1: {
      'name': 'Mineral',
      'price': 2
    },
  2: {
      'name': '100-Plus',
      'price': 3
    },
  3: {
      'name': 'Sparkling Water',
      'price': 5
    },
  4: {
      'name': 'Ice Lemon Tea',
      'price': 2
    },
  5: {
      'name': 'Mountain Dew',
      'price': 3
    },
  6: {
      'name': 'Diet Soda',
      'price': 2
    },
  7: {
      'name': 'Nescafe',
      'price': 3
  },
  8: {
      'name': 'Farm Fresh',
      'price': 4
  },
  9: {
      'name': 'Oat Milk',
      'price': 3
  },
  10: {
      'name': 'Soy Drink',
      'price': 2
  }
}

# display product
print("Choose Your drink(s):\n")
for key, value in products.items():
  print(f"{key} - {value['name']} - RM {value['price']}")
print("\n")

# user input money
money = int(input("Insert amount of money: "))
print(f"\nYou have entered RM{money}\n")

# purchase more than one
while True:
  # User input
  choice = input("Enter product number or '0' to quit: ")

  if choice == '0':
    break
  try:
    choice = int(choice)
  except ValueError:
    print("Invalid code!")
    continue

  # check if item chosen is valid
  if choice in products:
    # add item to list/cart
    selected_drink = products[choice]
    cart.append(selected_drink)
  else:
    print("Invalid code!")

# calculate total price
total_price = sum(item['price'] for item in cart)

# check if money is enough
if money >= total_price:
  if cart:  # check if any items were selected
    print("\nYou have chosen the following item(s):")
    for item in cart:
      print(f"{item['name']} - RM {item['price']}")

    print(f"\nThe total is RM {total_price}")
    
    # calculate change
    change = money - total_price

    # print change
    print(f"\nYour change is RM {change}")

    # return least amount of note - unscc
    notes = [1, 5, 10, 20, 50, 100]
    change_notes ={}
    for note in notes:
      if change >= note:
        num_notes = int(change / note)
        change_notes[note] = num_notes
        change %= note
    
    for note, num_notes in change_notes.items():
      if num_notes > 0:
        print(f"{num_notes} x RM {note} note.")
        
    print("Thank you for your purchase!") 

  else:
    print(f"No items selected. Returning balance: RM{money}")
else:
  # not enough money message
  print(f"\nNot enough money! The total is RM {total_price}")
