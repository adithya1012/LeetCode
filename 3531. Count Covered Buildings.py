class Solution:
    def countCoveredBuildings(self, buildings) -> int:
        directions = [[0, 1], [1, 0], [-1, 0], [0, -1]]
        # building_set = set()
        x_axis = {}
        y_axis = {}

        for i, j in buildings:
            if i in x_axis:
                if len(x_axis[i]) == 1:
                    x_axis[i].append(j)
                    x_axis[i].sort()
                else:
                    if x_axis[i][0] > j:
                        x_axis[i][0] = j
                    elif x_axis[i][1] < j:
                        x_axis[i][1] = j
            else:
                x_axis[i] = [j]

            if j in y_axis:
                if len(y_axis[j]) == 1:
                    y_axis[j].append(i)
                    y_axis[j].sort()
                else:
                    if y_axis[j][0] > i:
                        y_axis[j][0] = i
                    elif y_axis[j][1] < i:
                        y_axis[j][1] = i
            else:
                y_axis[j] = [i]

        tmp = x_axis.copy()
        for i in tmp:
            if len(x_axis[i]) == 1:
                del x_axis[i]
        tmp = y_axis.copy()
        for j in tmp:
            if len(y_axis[j]) == 1:
                del y_axis[j]

        if not x_axis or not y_axis:
            return 0
        res = 0
        for i, j in buildings:
            if i not in x_axis or j not in y_axis:
                continue
            if x_axis[i][0] < j < x_axis[i][1] and y_axis[j][0] < i < y_axis[j][1]:
                res += 1
        return res


Solution().countCoveredBuildings([[1,2],[2,2],[3,2],[2,1],[2,3]])
