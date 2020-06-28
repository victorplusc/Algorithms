"""
Time Planner
Implement a function meetingPlanner that given the availability, slotsA and slotsB, of two people and a meeting duration dur, returns the earliest time slot that works for both of them and is of duration dur. If there is no common time slot that satisfies the duration requirement, return an empty array.

Time is given in a Unix format called Epoch, which is a nonnegative integer holding the number of seconds that have elapsed since 00:00:00 UTC, Thursday, 1 January 1970.

Each person’s availability is represented by an array of pairs. Each pair is an epoch array of size two. The first epoch in a pair represents the start time of a slot. The second epoch is the end time of that slot. The input variable dur is a positive integer that represents the duration of a meeting in seconds. The output is also a pair represented by an epoch array of size two.

In your implementation assume that the time slots in a person’s availability are disjointed, i.e, time slots in a person’s availability don’t overlap. Further assume that the slots are sorted by slots’ start time.

Implement an efficient solution and analyze its time and space complexities.

Examples:

input:  slotsA = [[10, 50], [60, 120], [140, 210]]
        slotsB = [[0, 15], [60, 70]]
        dur = 8
output: [60, 68]

input:  slotsA = [[10, 50], [60, 120], [140, 210]]
        slotsB = [[0, 15], [60, 70]]
        dur = 12
output: [] # since there is no common slot whose duration is 12

Constraints:
[time limit] 5000ms
[input] array.array.integer slotsA
1 ≤ slotsA.length ≤ 100
slotsA[i].length = 2
[input] array.array.integer slotsB
1 ≤ slotsB.length ≤ 100
slotsB[i].length = 2
[input] integer
[output] array.integer
"""
# Time complexity: O(N+M)
# Space complexity: O(1)
def meeting_planner(slotsA, slotsB, dur):
  i = j = 0
  n, m = len(slotsA), len(slotsB)
  while i < n and j < m:
      start_A, end_A = slotsA[i]
      start_B, end_B = slotsB[j]

      smallest_end = min(end_A, end_B)
      largest_start = max(start_A, start_B)

      if smallest_end - largest_start >= dur:
        return [largest_start, largest_start+dur]
      elif smallest_end is end_B:
        j += 1
      elif smallest_end is end_A:
        i += 1
  return []
