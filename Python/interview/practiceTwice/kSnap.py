'''
Created on 2015年12月1日
Consider a grid where all the points are represented by integers.

.........................................
...(-2,2)  (-1,2)  (0,2)  (1,2)  (2,2)...
...(-2,1)  (-1,1)  (0,1)  (1,1)  (2,1)....
...(-2,0)  (-1,0)  (0,0)  (1,0)  (2,0)...
...(-2,-1) (-1,-1) (0,-1) (1,-1) (2,-1)...
...(-2,-2) (-1,-2) (0,-2) (1,-2) (2,-2)...
..........................................

k-Snap point: A point whose digits sum up to less than or equal to k. In this
question, we ignore all the signs in the number.  For exxample, (1, 0) is a 1-snap point, (0, 10) is a 1-snap point, and (-100, 0) is also a 1-snap point; however (11, 0) is not a 1-snap point.

Question 1: Implement the following function
boolean isSnapPoint(Point p, int k)

Returns true if p is a k-snap point, and false otherwise.

Reachable k-snap point: A k-snap point is a reachable k-snap point if there is a path from (0,0) to that point, where the path only consists of k-snap points.

Question 2: Given k, return all the reachable k-snap points.


public boolean  isSnapPoint(Point p, int k) {
                int x = Math.abs(p.x);
                int y = Math.abs(p.y);
                int val = 0;
                while (x > 0) {
                        val += x % 10;
                        x /= 10;
                }
                while (y > 0) {
                        val += y % 10;
                        y /= 10;
                }
                return val <= k;
        }

        public HashSet<Point> ReachableKSnapPoint(int k) {
                HashSet<Point> points = new HashSet<Point>();
                if (k < 0) return points;
                helper(new Point(0, 0), k, points);
                return points;
        }
        public void helper(Point point, int k, HashSet<Point> points) {
                if(!isSnapPoint(point, k)) return;
                points.add(point);
                Point left = new Point(point.x - 1, point.y);
                if (!points.contains(left)) helper(left, k, points);
                Point right = new Point(point.x + 1, point.y);
                if (!points.contains(right)) helper(right, k, points);
                Point upper = new Point(point.x, point.y + 1);
                if (!points.contains(upper)) helper(upper, k, points);
                Point lower = new Point(point.x, point.y - 1);
                if (!points.contains(lower)) helper(lower, k, points);
        }
        
        public class Point {
                public int x, y;
                public Point(int x, int y) {
                        this.x = x;
                        this.y = y;
                }
                
                public boolean equals(Object point) {
                if (!(point instanceof Point)) {
                    return false;
                }
                        Point p = (Point) point;
                        return this.x == p.x && this.y == p.y;
                }
                
                public int hashCode() {
                     return (x + " " + y).hashCode();
                }
        }
@author: Darren
'''

def isKSnap(grid,i,j,k):
    pass

def reachableKSnap(grid,k):
    pass       
                
                
    
grid =[[(-1, 1), (-1, 2), (0, 2), (1, 2), (2, 2)],
       [(-2, 1), (-1, 1), (0, 1), (1, 1), (2, 1)],
       [(-2, 0), (-1, 0), (0, 0), (1, 0), (2, 0)],
       [(-2, -1), (-1, -1), (0, -1), (1, -1), (2, -1)],
       [(-2, -2), (-1, -2), (0, -2), (1, -2), (2, -2)]]


print(isKSnap(grid, 0, 0, 2))
print(reachableKSnap(grid, 3))
