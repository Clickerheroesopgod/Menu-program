#This is a very simple program, when you run this program it will display the menu below and 
#ask if you would like to add, remove, or if you are ready to order. 
#Once again very simple but also kinda fun to use and play around with. 
#Btw U should try some of the sandwhichs listed on the menu, they are pretty good.




Sandwich_menu = {
    'club sandwich': {
        'ingredients': [
            'cheese',
            'bread',
            'Bacon',
            'Ham',
            'toast',
            'turkey meat',
            'mayonnaise',
            'Tomato',
            'lettuce',
        ],
    'price': 17.35,
    },
 
    'BLT': {
        'ingredients': [
            'Bacon',
            'tomato',
            'Bread',
            'lettuce',
            'mayonnaise',
        ],
    'price': 13.42,
    },
 
    'Egg sandwich': {
        'ingredients': [
            'eggs',
            'green oinons',
            'mayonnaise',
            'Dijon mustard',
            'salt',
            'pepper',
            'Garlic powder',
            'bread',
            'lettuce leaves',
        ],
    'price': 14.25,
    },
 
    'Ham sandwich': {
        'ingredients': [
            'mayonnaise',
            'parsley',
            'thyme',
            'extra-virgin olive oil',
            'garlic, minced',
            'sourdough bread',
            'herb mayo',
            'Dijon mustard',
            'deli ham',
            'provolone',
            'arugula',
            'tomato',
            'red onion',
            'bread',
        ],
    'price': 15.21,
    },
 
    'Barros Luco': {
        'ingredients': [
            'bread',
            'sirloin steak',
            'salt',
            'cheese',
            'butter',
            'bread',
        ],
    'price': 12.64,
    },
 
    'Philly Cheese steak': {
        'ingredients': [
            'vegetable oil',
            'yellow onion',
            'red bell pepper',
            'green bell pepper',
            'petite sirloin',
            'seasoned salt',
            'garlic pepper',
            'hoagie rolls',
            'softened butter',
            'Provolone cheese',
            'bread',
        ],
    'price': 17.58,
    },
 
    'Chacarero Chileno': {
        'ingredients': [
            'Kosher salt',
            'green beans',
            'pickled peperoncini',
            'skirt steak',
            'mayonnaise',
            'garlic',
            'extra-virgin olive oil',
            'ground black pepper',
            'telera',
            'tomato',
            'bread',
        ],
    'price': 17.58,
    },
 
    'Chicken shawarma': {
        'ingredients': [
            'garlic',
            'coriander',
            'cumin',
            'cardamon',
            'cayenne pepper',
            'paprika',
            'salt',
            'black pepper',
            'lemon juice',
            'olive oil',
            'flatbread',
            'lettuce',
            'bread',
        ],
    'price': 14.34,
    },
 
    'Carne Asada Torta': {
        'ingredients': [
            'telera rolls',
            'shredded iceberg',
            'avocado',
            'tomato',
            'red onion',
            'cotija',
            'jalapenos',
            'beans',
            'hot sauce',
            'bread',
        ],
    'price': 16.56,
    },
 
    'japanese fruit sandwich': {
        'ingredients': [
            'strawberries',
            'kiwis',
            'navel orange',
            'shokupan',
            'heavy cream',
            'sugar',
            'rum',
        ],
    'price': 10.42,
    },
 
    'Bombay grilled chutney sandwich': {
        'ingredients': [
            'Cilantro',
            'Mint leaves',
            'Ginger',
            'Thai chili',
            'Coconut',
            'Lime juice',
            'salt',
            'water',
            'white bread',
            'butter',
            'green chutney',
            'boiled potato',
            'tomato',
            'cucumber',
            'bell pepper',
            'Cheese',
            'Masala powder',
            'Ketchup',
            'bread',
        ],
    'price': 14.21,
    },
 
    'Classic Burger': {
        'ingredients': [
            'ground beef',
            'Worcestershire sauce',
            'seasoning salt',
            'garlic powder',
            'ground black pepper',
            'cheese',
            'hamburger buns',
            'lettuce',
            'bread',
        ],
    'price': 17.42,
    }
}
 
INDEXED_MENU = {k: v for k, v in enumerate(sorted(Sandwich_menu), start=1)}
 
# This gets the menu
def get_menu():
    """Gets order message and menu ready for you."""
    print('\nSandwich_menu\n====')
    for index, name in sorted(INDEXED_MENU.items()):
        cost = Sandwich_menu.get(name, {}).get('price', 0.0)
        print(f'{index:<4} {name:<30} {cost:>5.2f}')
    print()
 
# This function gets the orders
def display_order(order):
    """Gets the orders"""
    total = 0.0
    for item in order:
        cost = Sandwich_menu.get(item, {}).get('price', 0.0)
        print('cost', cost)
        total += cost
        print(f'{item:<30} {cost:>5.2f}')
    print()
 
# This asks if your would like to add remove or oder your itmen within the menu 
def get_action():
    get_menu()
    while True:
        action = input(f'Would you like to (A)dd, (R)emove or (O)rder?: ').lower()
        if action.startswith('a'):
            return 'add'
        if action.startswith('r'):
            return 'remove'
        if action.startswith('o'):
            return 'ordering'
        else:
            return

#adds an item  
def add_item(order):
    print()
    get_menu()
    while True:
        item_number = int(input('Item number to add? '))
        name = INDEXED_MENU.get(item_number)
        if name:
            order.append(name)
            break


#removes an item 
def remove_item(order):
    print()
    get_menu()
    while True:
        item_number = int(input('Item number to remove? '))
        name = INDEXED_MENU.get(item_number)
        try:
            order.remove(name)
        except ValueError:
            return
 
#this displays the menu 
def display_total(order):
    print('\nORDER\n=====')
    total = 0.0
    for name in sorted(order):
        cost = Sandwich_menu.get(name, {}).get('price', 0.0)
        ingredients = Sandwich_menu.get(name, {}).get('ingredients', [])
        total += cost
        print(f'{name:<30} {cost:>5.2f}')
        for ingredient in sorted(ingredients):
            print(f'    {ingredient}')
    print(f'\nTotal: {total:.2f}')
 
#main body of program 
def main():
    order = []
    while True:
        action = get_action()
        if action == 'ordering':
            if order:
                display_total(order)
            break
        elif action == 'add':
            add_item(order)
        else:
            remove_item(order)
        if order:
            display_total(order)
 
 
main()