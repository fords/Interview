'''Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), find the minimum number of conference rooms required.

Example 1:

Input: [[0, 30],[5, 10],[15, 20]]
Output: 2
Example 2:

Input: [[7,10],[2,4]]
Output: 1 '''
def minMeetingRooms(intervals):

    if not intervals:
        return 0

    # Heap intialization
    free_rooms = []

    # Sort meeting by starting time
    intervals.sort(key= lambda x: x[0])


    heapq.heappush(free_rooms, intervals[0][1])

    for i in intervals[1:]:

        if free_rooms[0] <= i[0]:
            heapq.heappop(free_rooms)

        heapq.heappush(free_rooms, i[1])

    return len(free_rooms)
