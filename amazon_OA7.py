# In managing tasks at analytics platform, the goal is to efficiently schedule both required and optional tasks within specified time constraints.
# There are n required tasks and n optional tasks.
# Two arrays, tasksRequired and tasksOptional, provide information on task hours, where tasksRequired [i] represents the duration in hours of the ith required task, and tasksOptional(i) represents the duration in hours of the th optional task.
# Each day on the platform has a time limit denoted as dailyTimeLimit in hours. One required task must be scheduled each day. If time remains after the required task, you can choose to schedule at most one optional task on that day. It's essential to ensure that the total hours does not exceed the specified daily TimeLimit.
# Determine the maximum number of optional tasks
# that can be scheduled during these n days while adhering to the given constraints.

# Example:
# DayLimit = 7
# Required = [4,5,2,4]
# Optional = [5, 6, 3, 4]
# One of the optimal scheduling can be:
# * Day 1: Schedule the first required task and the third
# optional task. Total time is 4 + 3 = 7.
# • Day 2: Schedule the second required task. Total time is 5.
# • Day 3: Schedule the third required task and first
# optional task. Total time is 2 + 5 = 7.
# • Day 4: Schedule the fourth required task. Total time
# IS 4.
# There is no other arrangement of optional tasks for which more than 2 optional tasks can be scheduled in 4 days.


def max_opt_days(dayLimit, Required, Optinal):
    Required.sort()
    Optinal.sort()
    # r, o = len(Required)-1, 0
    count = 0
    # while r >= 0 and o < len(Optinal):
        # if Required[r] + Optinal[o] > dayLimit:
        #     r+=1
        # else:
        #     count += 1
        #     while o < len(Optinal) and Required[r] + Optinal[o] <= dayLimit:
    for req in Required:
        rem_time = dayLimit-req
        l, r = 0, len(Optinal)-1
        best_fit_index = -1
        while l <= r:
            mid = (l+r)//2
            if Optinal[mid] <= rem_time:
                l = mid + 1
                best_fit_index = mid
            else:
                r = mid - 1
        if best_fit_index != -1:
            Optinal.pop(best_fit_index)
            count += 1
    return count

print(max_opt_days(7, [4, 5, 2, 4], [5, 6, 3, 4]))
print(max_opt_days(1, [1,1,1,1], [1,1,1,1]))
print(max_opt_days(2, [1,1,1,1], [1,1,1,1]))
print(max_opt_days(2, [1,1,1,1], [5,4,3,2]))
print(max_opt_days(10, [1,1,1,1], [0,0,0,0]))
