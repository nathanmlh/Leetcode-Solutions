class Solution(object):
    def checkStraightLine(self, coordinates):
        """
        :type coordinates: List[List[int]]
        :rtype: bool
        """
        (x1, y1), (x2, y2) = coordinates[:2]

        if len(coordinates) == 2:
            return True

        for i in range(2, len(coordinates)):
            (x, y) = coordinates[i]
            if ((y2 - y1) * (x1 - x) != (y1 - y) * (x2 - x1)):
                return False
        return True