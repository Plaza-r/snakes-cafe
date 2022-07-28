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

# initialize empty meal dictionary
# dinner = {}
#while True:
# start loop here until user enters quit

#quit = false

# create a variable to store the user's order
 #   order = input("> ")
  #  if order == 'quit':

        # print the order in some fancy way we're still figuring out
   # if order not in dinner:
    #    dinner[order] = 1
    #report = f"** {dinner} order of {order} have been added to your meal **"
    #print =(report)

    #else:
    #dinner[order] += 1
    #report = f"** {dinner[order] } orders of {order} have been added to your meal **"

      #      print(report)
# end loop


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