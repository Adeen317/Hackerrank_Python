#Given the participants' score sheet for your University Sports Day,
#you are required to find the runner-up score. You are given  scores.
#Store them in a list and find the score of the runner-up.


n = int(input())
arr = map(int, input().split())
arr1=list(set(arr))
arr1.sort(reverse=True)
print(arr1[1])
