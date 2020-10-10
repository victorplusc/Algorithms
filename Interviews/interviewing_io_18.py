'''
Given a set of points in the xy-plane, determine the minimum area of a rectangle formed from these points, with sides parallel to the x and y axes.

If there isn't any rectangle, return 0.

Example 1:
Input: [[1,1],[1,3],[3,1],[3,3],[2,2]]
Output: 4

 
 . .
  .
 . .
______________

Example 2:
Input: [[1,1],[1,3],[3,1],[3,3],[4,1],[4,3]]
Output: 2

 . .
 . .

 . .
 
# p = (x1, y1), q = (x2, y2)
a line exists if p[0] == q[0] or p[1] == q[1]

vertical_lines = []
horizontal_lines = []
if p[0] == q[0]:
    horizontal_lines.append((x1, x2, y1))
if p[1] == q[1]:
    vertical_lines.append((y1, y2, x2))
    
min_area = float('inf')
2) iterate through horizontal lines and find our best rectangle
    for i in range(len(horizontal_lines):
        for j in range(i+1, len(horizontal_lines):
            p_x1, p_x2, p_y = line[i]
            q_x1, q_x2, q_y = line[j]
            if sorted(p_x1, p_x2) != sorted(q_x1, q_x2):
                continue
            else:
                min_area = min(min_area, abs(p_x2-p_x1)*p_y)
    
3) iterate through vertical lines and find our best rectangle
    for i in range(len(vertical_lines):
        for j in range(i+1, len(vertical_lines):
            p_y1, p_y2, p_x = line[i]
            q_y1, q_y2, q_x = line[j]
            if sorted(p_y1, p_y2) != sorted(q_y1, q_y2):
                continue
            else:
                min_area = min(min_area, abs(p_y2-p_y1)*abs(p_x-q_x))

Example 1:
Input: [[1,1],[1,3],[3,1],[3,3],[2,2]]
Output: 4

 . .
  .
 . .
    
vertical_lines = [(1, 3, 1), (1, 3, 3)]
horizontal_lines = [(1, 3, 3), (1, 3, 1)]
min_area = float('inf')

p_x1, p_x2, p_y = 1, 3, 3
q_x1, q_x2, q_y = 1, 3, 1
if sorted(p_x1, p_x2) != sorted(q_x1, q_x2):
    continue
else:
    min_area = min(min_area, abs(p_x2-p_x1)*abs(p_y-q_y))
    
    min_area = min(min_area, abs(2)*abs(2))
    min_area = 4
  
  .        .


      .    .
  
       _____
  
  
  _________
  
          |
          |
          |
______________


'''

def min_rectangle_area(points):
    
    horizontal_lines = []
    
    for i in range(len(points)):
        for j in range(i+1, len(points)):
            x1, y1 = points[i]
            x2, y2 = points[j]
            if y1 == y2:
                horizontal_lines.append((x1, x2, y1))

        
    min_area = float('inf')
    # 2) iterate through horizontal lines and find our best rectangle
    for i in range(len(horizontal_lines)):
        for j in range(i+1, len(horizontal_lines)):
            p_x1, p_x2, p_y = horizontal_lines[i]
            q_x1, q_x2, q_y = horizontal_lines[j]
            if sorted((p_x1, p_x2)) != sorted((q_x1, q_x2)):
                continue
            else:
                min_area = min(min_area, abs(p_x2-p_x1)*abs(p_y-q_y))

                               
    return min_area
