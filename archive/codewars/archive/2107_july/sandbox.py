class SomeClass:

    def __init__(self, tuple):
        self.tuple = tuple

    def print(self):
        print(f"x={self.tuple[0]} y={self.tuple[1]}")

SomeClass((1,0)).print()
