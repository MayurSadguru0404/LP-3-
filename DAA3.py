def fractional_knapsack(capacity,items):
    items.sort(key=lambda x: x[2],reverse=True)
    total_profit=0
    for item in items:
        if capacity>=item[0]:
            capacity-=item[0]
            total_profit+=item[1]
        else:
            fraction=capacity/item[0]
            total_profit+=item[1]*fraction
            break
    print("Maximum Profit : ", total_profit)
n=int(input("Enter number of items: "))
items=[]
for i in range(n):
    weight=float(input("Enter weight:"))
    profit=float(input("Enter profit:"))
    ratio=profit/weight
    items.append((weight,profit,ratio))
capacity=float(input("Enter knaspsack capacity:"))
fractional_knapsack(capacity,items)