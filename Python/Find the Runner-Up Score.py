'''Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score.
You are given scores. Store them in a list and find the score of the runner-up.

Input Format
The first line contains n . The second line contains an array A[] of n integers each separated by a space.

Constraints
2<=n<=10
-100<=A[i]<=100

Output Format
Print the runner-up score.

Sample Input
5
2 3 6 6 5

Sample Output:
5

Explanation :
Given list is [2,3,6,6,5]. The maximum score is , second maximum is . Hence, we print as the runner-up score.'''


#SOLUTION

def runner_up():
	n = int(input())

	# Read the scores as a list of integers
	l = list(map(int, input().split()))

	# Find the maximum score
	max_score = max(l)

	# Remove all occurrences of the maximum score
	while max_score in l:
		l.remove(max_score)

	# Find the runner-up score
	runner_up_score = max(l)

	# Print the runner-up score
	print(runner_up_score)


# Test the function
runner_up()
