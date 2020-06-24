import math

class Point:
    def __init__(self, x=0, y=0):
        self.__x = x
        self.__y = y

    def distance(self, point):
        disX = abs(self.__x - point.__x)
        disY = abs(self.__y - point.__y)
        dis = math.sqrt(math.pow(disX, 2) + math.pow(disY, 2))
        return dis

    def __add__(self, point):
        disX = self.__x + point.__x
        disY = self.__y + point.__y
        return Point(disX, disY)

    def getPos(self):
        return self.__x, self.__y

p1 = Point(1, 1)
p2 = Point(2, 2)

distance = p1.distance(p2)
addPoint = p1.__add__(p2)

print('p1과 p2사이의 거리 : {0:.3f}'.format(distance))
print('p1 + p2 :', addPoint.getPos())
