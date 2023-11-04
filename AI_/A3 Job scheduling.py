profit =[10,27,15,100,150]
jobs = ['j1','j2','j3','j4','j5']
deadline = [2,3,3,3,4]

profitNjobs = list(zip(profit,jobs,deadline))
profitNjobs = sorted(profitNjobs,key= lambda x:x[0], reverse=True)

slot= []
for _ in range(len(jobs)):
    slot.append(0)

profit=0
ass = []
for i in range(len(jobs)):
    ass.append('null')

for i in range(len(jobs)):
    job = profitNjobs[i]
    for j in range(job[2],0,-1):
        if slot[j]==0:
            ass[j]=job[1]
            profit += job[0]
            slot[j]=1
            break

print("Job schduled are: ",ass[1:])
print(profit)        


# Jobs, Profit, Slot
# profit = [15,27,10,100, 150]
# jobs = ["j1", "j2", "j3", "j4", "j5"]
# deadline = [2,3,3,3,4] 
# profitNJobs = list(zip(profit,jobs,deadline))
# profitNJobs = sorted(profitNJobs, key = lambda x: x[0], reverse = True)
# slot = []
# for _ in range(len(jobs)):
#     slot.append(0)

# profit = 0
# ans = []

# for i in range(len(jobs)):
#     ans.append('null')

# for i in range(len(jobs)):
#         job = profitNJobs[i]
#         #check if slot is occupied
#         for j in range(job[2], 0, -1): 
#             if slot[j] == 0:
#                 ans[j] = job[1]
#                 profit += job[0]
#                 slot[j] = 1
#                 break
        
# print("Jobs scheduled buddy:",ans[1:])
# print(profit)   

# # num_jobs = int(input("Enter the number of jobs: "))

# # profit = []
# # jobs = []
# # deadline = []

# # max_deadline = 0

# # for i in range(num_jobs):
# #     job_name = input("Enter the name of job {}: ".format(i+1))
# #     job_profit = int(input("Enter the profit for job {}: ".format(i+1)))
# #     job_deadline = int(input("Enter the deadline for job {}: ".format(i+1)))
# #     jobs.append(job_name)
# #     profit.append(job_profit)
# #     deadline.append(job_deadline)
# #     max_deadline = max(max_deadline, job_deadline)

# # profitNJobs = list(zip(profit, jobs, deadline))
# # profitNJobs = sorted(profitNJobs, key=lambda x: x[0], reverse=True)

# # slot = [0] * (max_deadline + 1)
# # total_profit = 0
# # ans = ['null'] * num_jobs

# # for i in range(num_jobs):
# #     job = profitNJobs[i]
# #     for j in range(job[2], 0, -1):
# #         if slot[j] == 0:
# #             ans[i] = job[1]
# #             total_profit += job[0]
# #             slot[j] = 1
# #             break

# # print("Jobs scheduled:", ans)
# # print("Total profit:", total_profit)
