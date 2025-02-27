recent_purchases = [36.13, 23.87, 183.35, 22.93, 11.62]
budget = 50
total_spent = 0
for purchase in recent_purchases:
    total_spent += purchase
if(total_spent > budget):
    print('This purchase is over budget!')
else:
    print('This purchase is within budget')