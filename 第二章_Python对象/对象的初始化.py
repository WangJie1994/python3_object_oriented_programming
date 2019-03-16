class Point:
    def __init__(self, x=0, y=0):
        self.move(x, y)

    def reset(self):
        self.x = 0
        self.y = 0

    def move(self, x, y):
        self.x = x
        self.y = y


p = Point(3, 5)
print(p.x, p.y)
