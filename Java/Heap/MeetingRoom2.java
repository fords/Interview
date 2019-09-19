/*
Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), find the minimum number of conference rooms required.

Example 1:

Input: [[0, 30],[5, 10],[15, 20]]
Output: 2
Example 2:

Input: [[7,10],[2,4]]
Output: 1
*/
class MeetingRoom2 {
    public int minMeetingRooms(int[][] intervals) {
        if (intervals.length == 0)
            return 0;
        // Use PriorityQueue
        PriorityQueue<Integer> pq = new PriorityQueue<>(Comparator.comparingInt(c ->c) );

        // Sort meeting time by starting time
        Comparator<int[]> cmp = (o1,o2) -> o1[0] - o2[0];
        Arrays.sort(intervals, cmp);

        pq.add(intervals[0][1]);

        // Compare end time of PriorityQueue to start time of interval
        for ( int i = 1 ; i < intervals.length ; i++){
            if ( intervals[i][0] >= pq.peek()){
                pq.poll();
            }
            pq.add(intervals[i][1]);
        }

        return pq.size();
    }
}
