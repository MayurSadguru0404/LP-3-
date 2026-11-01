def job_sequencing(jobs):
    jobs.sort(key=lambda x: x[2],reverse=True)
    max_deadline=max(job[1] for job in jobs)
    slots=[False]*max_deadline
    total_profit=0
    result=[]
    for job in jobs:
        for j in range(job[1]-1,-1,-1):
            if not slots[j]:
                slots[j]=True
                result.append(job[0])
                total_profit+=job[2]
    print("Selected Jobs:",result)
    print("Maximum Profit:",total_profit)
n=int(input("Enter number of jobs:"))
jobs=[]
for i in range(n):
    job_id=input("Enter job ID:")
    deadline=int(input("Enter deadline:"))
    profit=int(input("Enter profit:"))
    jobs.append((job_id,deadline,profit))
job_sequencing(jobs)