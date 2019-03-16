import math


class Point:
    def reset(self):
        self.x = 0
        self.y = 0

    def move(self, x, y):
        self.x = x
        self.y = y

    def calculate_distance(self, other_point):
        return math.sqrt((self.x - other_point.x) ** 2 + (self.y - other_point.y) ** 2)


p = Point()
p.reset()
print(p.x, p.y)

q = Point()
Point.reset(q)
print(q.x, q.y)

q.move(2, 3)
print(p.calculate_distance(q))

p.move(1, 2)
print(p.calculate_distance(q))
