# This is a class of matrix
from Vector import *
class Matrix(object):
    def __init__(self, l):
        # Takes a 2D list to initialize
        rows, cols = len(l), len(l[0])
        self.mat = dict()
        for row in xrange(rows):
            for col in xrange(cols):
                self.mat[(row,col)] = l[row][col]
        self.rows, self.cols = rows, cols
        self.l = l
    def getRowVectors(self):
        # return a list of vector
        return [Vector(self.l[i]) for i in xrange(self.rows)]
            
