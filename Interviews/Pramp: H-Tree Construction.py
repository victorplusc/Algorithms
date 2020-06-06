"""
H-Tree Construction
An H-tree is a geometric shape that consists of a repeating pattern resembles the letter “H”.

It can be constructed by starting with a line segment of arbitrary length, drawing two segments of the same length at right angles to the first through its endpoints, and continuing in the same vein, reducing (dividing) the length of the line segments drawn at each stage by √2.

Here are some examples of H-trees at different levels of depth:

altdepth = 1

altdepth = 2

altdepth = 3

Write a function drawHTree that constructs an H-tree, given its center (x and y coordinates), a starting length, and depth. Assume that the starting line is parallel to the X-axis.

Use the function drawLine provided to implement your algorithm. In a production code, a drawLine function would render a real line between two points. However, this is not a real production environment, so to make things easier, implement drawLine such that it simply prints its arguments (the print format is left to your discretion).

Analyze the time and space complexity of your algorithm. In your analysis, assume that drawLine's time and space complexities are constant, i.e. O(1).

Constraints:
[time limit] 5000ms
[input] double x
[input] double y
[input] double length
[input] double depth

0 ≤ depth ≤ 10
"""
# Time complexity: O(4**depth)
# Space complexity: O(depth)
def drawHTree(x, y, length, depth):
  if depth == 0:
    return
  d = length/2
  
  drawLine(x-d, y, x+d, y)
  drawLine(x-d, y+d, x-d, y-d)
  drawLine(x+d, y+d, x+d, y-d)
  
  d = d/(2**(1/2))
  
  drawHTree(x-d, y-d, length, depth-1)
  drawHTree(x+d, y-d, length, depth-1)
  drawHTree(x-d, y+d, length, depth-1)
  drawHTree(x+d, y+d, length, depth-1)
