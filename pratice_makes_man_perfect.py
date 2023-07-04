'''
    Given the number of problems chef solves actually solved in each week over 4 weeks P1,P2,P3,P4. These are output the number of weeks in which Chef met his target.
    Output a single integer in a single line - the number of weeks in which Chef solved at least 10 problems.
    I/P :- 12 15 8 10
    O/P :- 3
'''
count=0
def goal_reached(nums,count):
    for i in range(len(nums)):
        if nums[i]>=10:
            count+=1
    return count
nums1=list(map(int,input().split()))
print(goal_reached(nums1,count))

