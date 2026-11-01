# def knapsack(capacity,weights,profit,n):
#     dp=[[0]*(capacity+1) for _ in range(n+1)]
#     for i in range(1,n+1):
#         for w in range(capacity+1):
#             if weights[i-1]<=w:
#                 include=profit[i-1]+dp[i-1][w-weights[i-1]]
#                 exclude=dp[i-1][w]
#                 dp[i][w]=max(include,exclude)
#             else:
#                 dp[i][w]=dp[i-1][w]
#     print("Maximum Profit :",dp[n][capacity])
# n=int(input("Enter number of items:"))
# weights=[]
# profits=[]
# for i in range(n):
#     weight=int(input("Enter weight:"))
#     profit=int(input("Enter profit:"))
#     weights.append(weight)
#     profits.append(profit)
# capacity=int(input("Enter knapsack capacity:"))
# knapsack(capacity,weights,profits,n)


#BRANCH AND BOUND
def knapsack(capacity,items):
    items.sort(key=lambda x : x[1]/x[0],reverse=True)
    n=len(items)
    best_profit=0
    def bound(i,weight,profit):
        total=profit
        while i<n and weight + items[i][0] <= capacity:
            weight += items[i][0]
            total += items[i][1]
            i+=1
        if i<n:
            total+=(capacity-weight)*items[i][1]/items[i][0]
        return total
    def solve(i,weight,profit):
        nonlocal best_profit
        if profit>best_profit:
            best_profit=profit
        if i==n or bound(i,weight,profit)<=best_profit:
            return
        if weight+items[i][0] <= capacity:
            solve(i+1,weight+items[i][0],profit+items[i][1])
        solve(i+1,weight,profit)
    solve(0,0,0)
    print("Maximum Profit:",best_profit)
n=int(input("Enter number of items:"))
items=[]
for i in range(n):
    weight=int(input("Enter weight:"))
    profit=int(input("Enter Profit:"))
    items.append((weight,profit))
capacity=int(input("Enter Knapsack capacity:"))
knapsack(capacity,items)

