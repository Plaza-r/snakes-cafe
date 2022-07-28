print(
    """
**************************************
**    Welcome to the Snakes Cafe!   **
**    Please see our menu below.    **
**
** To quit at any time, type "quit" **
**************************************
Appetizers
----------
Wings
Cookies
Spring Rolls
Entrees
-------
Salmon
Steak
Meat Tornado
A Literal Garden
Desserts
--------
Ice Cream
Cake
Pie
Drinks
------
Coffee
Tea
Unicorn Tears
***********************************
** What would you like to order? **
***********************************
"""
)




item_count = 0
order = ""

dinner_order = []

while order != "quit":
    order = input("> ")
    dinner_order.append(order)
    num_items = dinner_order.count(order)

    report1 = f"** {num_items} order of {order} have been added to your meal **"
    report2 = f"** {num_items} orders of {order} have been added to your meal **"

    if item_count == 1:
        print(report1)
    else:
        print(report2)