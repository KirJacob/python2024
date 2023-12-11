# type hinting in python
def list_avg(sequence: list) -> float:
    return sum(sequence) / len(sequence)


print(list_avg([1, 2, 34, 12]))

list_avg(123)
