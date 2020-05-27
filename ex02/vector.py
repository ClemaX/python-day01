class Vector:
    def __init__(self, arg):
        if isinstance(arg, list):
            if not arg:
                raise ValueError("Vectors need at least 1 dimension")
            self.size = len(arg)
            try:
                self.values = list(float(v) for v in arg)
            except ValueError:
                raise ValueError("Values should be numeric")
        elif isinstance(arg, int):
            if arg <= 0:
                raise ValueError("Vectors need at least 1 dimension")
            self.size = arg
            self.values = list(range(0, arg))
        elif isinstance(arg, tuple):
            if (len(arg) != 2):
                raise ValueError("Range tuple must have two values")
            try:
                start = int(arg[0])
                end = int(arg[1])
            except ValueError:
                raise ValueError("Range values should be numeric")
            self.size = end - start
            if self.size <= 0:
                raise ValueError("Range should contain at least 1 value")
            self.values = [i * 1.0 for i in range(start, end)]
        else:
            raise TypeError("Invalid arguments")

    def __str__(self):
        return f"(Vector {self.values})"

    def __repr__(self):
        return repr(self.__dict__)

    def __add__(self, other):
        if isinstance(other, Vector):
            if other.size != self.size:
                raise ValueError("Vectors should have the same size")
            result = [self.values[i] + other.values[i]
                      for i in range(self.size)]
            return Vector(result)
        elif isinstance(other, (int, float)):
            return Vector([v + other for v in self.values])
        else:
            return NotImplemented

    def __radd__(self, other):
        return self.__add__(other)

    def __sub__(self, other):
        if isinstance(other, Vector):
            if other.size != self.size:
                raise ValueError("Vectors should have the same size")
            result = [self.values[i] - other.values[i]
                      for i in range(self.size)]
            return Vector(result)
        elif isinstance(other, (int, float)):
            return Vector([v - other for v in self.values])
        else:
            return NotImplemented

    def __rsub__(self, other):
        return self.__sub__(other)

    def __truediv__(self, other):
        if isinstance(other, (int, float)):
            return Vector([v / other for v in self.values])
        else:
            return NotImplemented

    def __rtruediv__(self, other):
        return NotImplemented

    def __mul__(self, other):
        if isinstance(other, Vector):
            if other.size != self.size:
                raise ValueError("Vectors should have the same size")
            result = sum([self.values[i] * other.values[i]
                          for i in range(self.size)])
            return result
        elif isinstance(other, (int, float)):
            return Vector([v * other for v in self.values])
        else:
            return NotImplemented

    def __rmul__(self, other):
        return self.__mul__(other)
