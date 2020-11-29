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
            for i in x:
                print(i)
            if len(x)<1:
                print('Nothing')
            break
        x.append(meal)
        counting=x.count(meal)
        if counting>1:
            print(f'** {counting} orders of {meal} have been added to your meal **')
        else:
            print(f'** {counting} order of {meal} have been added to your meal **')






print("\n")
print('**************************************')
print('**    Welcome to the Snakes Cafe!   **')
print('**    Please see our menu below.    **')
print('**')
print('** To quit at any time, type "quit" **')
print('**************************************')

appetizers_print()

entrees_print()

desserts_print()

drinks_print()

print('***********************************')
print('** What would you like to order? **')
print('***********************************')

order_loop()