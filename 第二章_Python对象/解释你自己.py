class Point:
    """
    点类型
    """
    def __init__(self, x=0, y=0):
        """
        初始化点
        :param x: 横坐标
        :param y: 纵坐标
        """
        self.move(x, y)

    def reset(self):
        """
        重置一个点
        :return:
        """
        self.x = 0
        self.y = 0

    def move(self, x, y):
        """
        移动一个点
        :param x: 横坐标
        :param y: 纵坐标
        :return:
        """
        self.x = x
        self.y = y
