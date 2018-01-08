"""
Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), find the minimum number of conference rooms required.

For example,
Given [[0, 30],[5, 10],[15, 20]],
return 2.
"""

import heapq

def meetingRoomII(meetings):
    meetings.sort(key=lambda x:x[0])
    heap = []
    for meeting in meetings:
        if heap and heap[0] <= meeting[0]:
            heapq.heappop(heap)
        heapq.heappush(heap, meeting[1])
    return len(heap)
