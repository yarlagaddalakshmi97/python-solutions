'''
 Suppose the cover price of a book is Rs.24.95, but bookstores get a 40% discount. Shipping costs
Rs.3 for the first copy and 0.75p for each additional copy. What is the total wholesale cost for
60 copies?

'''
no_copies=60
book_price=24.95
discount=(40/100)*60*24.95
shipping_cost_1copy=3*1
shipping_cost_addcopy=0.75*(no_copies-1)
wholesale_cost=(no_copies*book_price)-discount+shipping_cost_1copy+shipping_cost_addcopy
print(wholesale_cost)