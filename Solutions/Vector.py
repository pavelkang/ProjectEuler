# This is a class of vector
class Vector(object):
    def __init__(self, l):
        # Takes a list to initialize
        self.vec = {k:v for (k,v) in zip(range(len(l)), l)}
        self.D = set(self.vec.keys())
    def __eq__(self, other):
        return self.D == other.D and self.vec == other.vec
    def __add__(self, other):
        if other == 0:
            return self
        assert(type(other).__name__ == "Vector")
        assert(len(self.D) == len(other.D))
        result = [self.vec[i]+other.vec[i] for i in self.D]
        return Vector(result)
    def __sub__(self, other):
        assert(type(other).__name__ == "Vector")
        assert(len(self.D) == len(other.D))
        result = [self.vec[i]-other.vec[i] for i in self.D]
        return Vector(result)
    def __mul__(self, other):
        # vec * int
        if type(other).__name__ == "int":
            return Vector([self.vec[i]*other for i in self.D])
        # vec * mat
        if type(other).__name__ == "Matrix":
            assert(len(self.D) == other.rows)
            rowVectors = other.getRowVectors()
            vectors = [rowVectors[i] * self.vec[i] for i in self.D]
            return sum(vectors, Vector([0]*len(self.D)))
    def __str__(self):
        return "Vector :" + str(self.vec)
        
