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


class Matrix:
    def __init__(self, data):
        if isinstance(data, list):
            height = len(data)
            if height == 0:
                raise ValueError("Data cannot be empty")
            width = len(data[0])
            for row in data:
                if width != len(row):
                    raise ValueError("Shape needs to be rectangular")
            self.shape = (height, width)
            try:
                self.data = [[float(v) for v in row] for row in data]
            except ValueError:
                raise ValueError("Data should be numeric")
        elif isinstance(data, tuple):
            if len(data) != 2:
                raise ValueError("Shape needs to be rectangular")
            try:
                self.shape = (int(data[0]), int(data[1]))
            except ValueError:
                raise ValueError("Shape dimensions should be numeric")
            else:
                if self.shape[0] <= 0 or self.shape[1] <= 0:
                    raise ValueError("Shape dimensions should be > 0")
                self.data = [[0.0 for i in range(self.shape[1])]
                             for j in range(self.shape[0])]
        else:
            raise TypeError("Argument type should be list or tuple")

    def __str__(self):
        txt = f"(Matrix) {self.shape}\n"
        rows = []
        for row in self.data:
            vals = []
            for val in row:
                vals.append(f"{val:>5.2f}")
            rows.append(str(vals))
        txt += '\n'.join(rows)
        return txt

    def __repr__(self):
        return repr(self.__dict__)

    def __add__(self, other):
        """add: vectors and matrices,
        can have errors with vectors and matrices."""
        if isinstance(other, Matrix):
            if self.shape != other.shape:
                raise ValueError("Matrices should have the same dimensions")
            result = [
                [
                    self.data[i][j] + other.data[i][j]
                    for j in range(self.shape[1])
                ]
                for i in range(self.shape[0])
            ]
            return Matrix(result)
        elif isinstance(other, Vector):
            if self.shape[1] != 1 or other.size != self.shape[0]:
                raise ValueError("Vector should have the same size as matrix")
            result = [
                [self.data[i][0] + other.values[i]]
                for i in range(self.shape[0])
            ]
            return Matrix(result)
        else:
            return NotImplemented

    def __radd__(self, other):
        return self.__add__(other)

    def __sub__(self, other):
        """sub: vectors and matrices,
        can have errors with vectors and matrices."""
        if isinstance(other, Matrix):
            if self.shape != other.shape:
                raise ValueError("Matrices should have the same dimensions")
            result = [
                [
                    self.data[i][j] - other.data[i][j]
                    for j in range(self.shape[1])
                ]
                for i in range(self.shape[0])
            ]
            return Matrix(result)
        elif isinstance(other, Vector):
            if self.shape[1] != 1 or other.size != self.shape[0]:
                raise ValueError("Vector should have the same size as matrix")
            result = [
                [self.data[i][0] - other.values[i]]
                for i in range(self.shape[0])
            ]
            return Matrix(result)
        else:
            return NotImplemented

    def __rsub__(self, other):
        return self.__sub__(other)

    def __truediv__(self, other):
        """div: only scalars"""
        if isinstance(other, (int, float)):
            result = [
                [
                    self.data[i][j] / other
                    for j in range(self.shape[1])
                ]
                for i in range(self.shape[0])
            ]
            return Matrix(result)
        else:
            return NotImplemented

    def __rtruediv__(self, other):
        return NotImplemented

    def __mul__(self, other):
        """mul: scalars, vectors and matrices,
        can have errors with vectors and matrices

        return a Vector if we perform Matrix * Vector (dot product)"""
        if isinstance(other, Matrix):
            if self.shape[0] != other.shape[1]\
               or self.shape[1] != other.shape[0]:
                raise ValueError("Matrices should have compatible shape")
            result = [
                [
                    sum(
                        [
                            self.data[i][k] * other.data[k][j]
                            for k in range(self.shape[1])
                        ]
                    )
                    for j in range(self.shape[0])
                ] for i in range(self.shape[0])
            ]
            return Matrix(result)
        elif isinstance(other, Vector):
            if self.shape[1] != other.size:
                raise ValueError("Vector should have the same size as matrix")
            result = [Vector(self.data[i]) * other
                      for i in range(self.shape[0])]
            return Vector(result)
        elif isinstance(other, (int, float)):
            result = [
                [
                    self.data[i][j] * other
                    for j in range(self.shape[1])
                ]
                for i in range(self.shape[0])
            ]
            return Matrix(result)
        else:
            return NotImplemented

    def __rmul__(self, other):
        return self.__mul__(other)


try:
    m = Matrix([[0, 4, -2],
               [-4, -3, 0]])
    n = Matrix([[0, 1],
               [1, -1],
               [2, 3]])
    print('m:', m)
    print('n:', n)
    print('m * n:', m * n)
#    print('m + n:', m + n)
    print()
    p = Matrix([[1, -1, 2],
               [0, -3, 1]])
    v = Vector([2, 1, 0])
    print('p:', p)
    print('v:', v)
#   print('p + v:', p + v)
    print('p / 2:', p / 2)
    print('p * 2:', p * 2)
    print('p * v:', p * v)
except (TypeError, ValueError) as e:
    print("Error:", e)
