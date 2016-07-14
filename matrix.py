# !/usr/bin/python
# -*- coding: utf8 -*-


class Matrix:

    def __init__(self):
        self.M = None
        self.N = None

    def new(self, arg):
        self.M = int(arg[0])
        self.N = int(arg[1])
        self.matrix = [[0 for y in range(self.M)] for x in range(self.N)]
        self._show()

    def _show(self):
        for row in self.matrix:
            print ''.join(map(str, row))

    def clear(self, arg):
        self.matrix = [[0 for y in range(self.M)] for x in range(self.N)]
        self._show()

    def pixel_color(self, arg):
        self.X = int(arg[0])
        self.Y = int(arg[1])
        self.C = arg[2]
        self.matrix[self.X][self.Y] = self.C.upper()
        self._show()

    def column_color(self, arg):
        self.X = int(arg[0])
        self.Y1 = int(arg[1])
        self.Y2 = int(arg[2])
        self.C = arg[3]
        for Y in range(self.Y1, self.Y2 + 1):
            self.matrix[Y][self.X] = self.C.upper()
        self._show()

    def row_color(self, arg):
        self.X1 = int(arg[0])
        self.X2 = int(arg[1])
        self.Y = int(arg[2])
        self.C = arg[3]
        for X in range(self.X1, self.X2 + 1):
            self.matrix[self.Y][X] = self.C.upper()
        self._show()

    def retangle(self, arg):
        self.X1 = int(arg[0])
        self.Y1 = int(arg[1])
        self.X2 = int(arg[2])
        self.Y2 = int(arg[3])
        self.C = arg[4]
        for X in range(self.X1, self.X2 + 1):
            for Y in range(self.Y1, self.Y2 + 1):
                self.matrix[X][Y] = self.C.upper()
        self._show()

    def region_color(self, arg):
        self.X = int(arg[0])
        self.Y = int(arg[1])
        self.C = arg[2].upper()
        matrix = self.matrix
        region, stack = [], [(self.X, self.Y)]
        while stack:
            pixel = stack.pop(0)
            if pixel not in region:
                if (pixel[0] >= 0) and (pixel[0] < len(matrix)):
                    if (pixel[1] >= 0) and (pixel[1] < len(matrix)):
                        for dx in (-1, 0, 1):
                            for dy in (-1, 0, 1):
                                if matrix[pixel[0]][pixel[1]] == matrix[dx - pixel[0]][dy - pixel[1]]:
                                    region.append(pixel)
                                    stack.append((dx + pixel[0], dy + pixel[1]))
        matrix[self.X][self.Y] = self.C
        for i, j in region:
            matrix[i][j] = self.C
        self._show()

    def save(self, arg):
        arq = open('%s.bmp' % arg, "w")
        for row in self.matrix:
            arq.write(''.join(map(str, row)) + "\n")
        arq.close()
        print "%s.bmp Saved!" % arg
