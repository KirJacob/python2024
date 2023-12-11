import math


def check_exception(list_a, list_b):
    if len(list_a) != len(list_b):
        raise Exception("size of vectors is different")


class Vector:

    def __init__(self, list_args):
        self.list_args = list_args

    def __str__(self):
        return str(tuple(self.list_args)).replace(" ", "")

    def equals(self, parameter_list):
        result = True
        for index in range(0, len(parameter_list.list_args)):
            if self.list_args[index] != parameter_list.list_args[index]:
                return False
        return result

    def add(self, parameter_list):
        check_exception(self.list_args, parameter_list.list_args)
        return Vector(list(map(lambda x: self.list_args[x] + parameter_list.list_args[x],
                               range(0, len(parameter_list.list_args)))))

    def subtract(self, parameter_list):
        check_exception(self.list_args, parameter_list.list_args)
        return Vector(list(map(lambda x: self.list_args[x] - parameter_list.list_args[x],
                               range(0, len(parameter_list.list_args)))))

    def dot(self, parameter_list):
        check_exception(self.list_args, parameter_list.list_args)
        return sum(list(map(lambda x: x[0]*x[1], list(zip(self.list_args, parameter_list.list_args)))))

    def norm(self):
        return math.sqrt(sum(list(map(lambda x: x*x, self.list_args))))


a = Vector([1, 2, 3])
b = Vector([3, 4, 5])
print(a.dot(b))
print(a.equals(a))
print(a.equals(b))
print(a)

# If you try to add, subtract, or dot two vectors with different lengths, you must throw an error!
# Also provide:
# a toString method, so that using the vectors from above, a.toString() === '(1,2,3)' (in Python, this is a __str__ method, so that str(a) == '(1,2,3)')
# an equals method, to check that two vectors that have the same components are equal
# Note: the test cases will utilize the user-provided equals method.

