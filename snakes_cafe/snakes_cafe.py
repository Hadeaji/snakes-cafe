appetizers=['Wings','Cookies','Spring Rolls']
entrees=['Salmon','Steak','Meat Tornado','A Literal Garden']
desserts=['Ice Cream','Cake','Pie']
drinks=['Coffee','Tea','Unicorn Tears']

def appetizers_print():
    print('Appetizers')
    print('----------')
    for i in appetizers:
        print(i)

def entrees_print():
    print('Entrees')
    print('-------')
    for i in entrees:
        print(i)

def desserts_print():
    print('Desserts')
    print('--------')
    for i in desserts:
        print(i)

def drinks_print():
    print('Drinks')
    print('------')
    for i in drinks:
        print(i)



def order_loop():
    x=[]
    while True:  
        meal=input('>').title()
        if meal=='Quit':
            print('You Ordered')
            print("\n")
            for i in x:
                print(i)
            if len(x)<1:
                print('Nothing')
            break
        x.append(meal)
        counting=x.count(meal)
        if counting>1:
            print("\n")
            print(f'** {counting} orders of {meal} have been added to your meal **')
            print("\n")
        else:
            print("\n")
            print(f'** {counting} order of {meal} have been added to your meal **')
            print("\n")






print("\n")
print('**************************************')
print('**    Welcome to the Snakes Cafe!   **')
print('**    Please see our menu below.    **')
print('**')
print('** To quit at any time, type "quit" **')
print('**************************************')
print("\n")

appetizers_print()
print("\n")

entrees_print()
print("\n")

desserts_print()
print("\n")

drinks_print()
print("\n")

print('***********************************')
print('** What would you like to order? **')
print('***********************************')

order_loop()