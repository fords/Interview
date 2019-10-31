
/*
You have some sticks with positive integer lengths.

You can connect any two sticks of lengths X and Y into one stick by paying a cost of X + Y.  You perform this action until there is one stick remaining.

Return the minimum cost of connecting all the given sticks into one stick in this way.


Example 1:

Input: sticks = [2,4,3]
Output: 14


Example 2:

Input: sticks = [1,8,3,5]
Output: 30
*/
// Edge case [474, 3166, 3259, 3354] -> output 20506


class Minimum_Cost_to_Connect_Sticks {
    public int connectSticks(int[] sticks) {
        PriorityQueue <Integer> pq = new PriorityQueue<>();
        for ( int i: sticks) {
            pq.add(i);
        }
        int res = 0;
        while (pq.size() > 1){
            int total = pq.poll() + pq.poll();
            res += total;
            pq.offer(total);
        }
        return res;
    }
}


// Python
/*
def connectSticks(self, sticks):
    """
    :type sticks: List[int]
    :rtype: int
    """
    if len(sticks) <= 1:
        return 0
    heapq.heapify(sticks)
    res = 0
    while len(sticks) > 1:
        a , b = heapq.heappop(sticks) , heapq.heappop(sticks)
        res += a + b
        heapq.heappush( sticks, a +b)
    return res   */
