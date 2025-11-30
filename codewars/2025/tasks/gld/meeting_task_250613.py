# 23:49 -> 00:27
def sequential_count(line):
    def loop(acc, sequence, line):
        print(f"acc={acc}, sequence={sequence}, line={line}")
        head = line[0]
        tail = line[1:]
        if len(tail) == 0:
            acc.append((sequence, len(sequence)))
            return acc
        if head != tail[0]:
            acc.append((sequence, len(sequence)))
            return loop(acc, tail[0], tail)
        else:
            sequence = sequence + tail[0]
            return loop(acc, sequence, tail)
    result_tuple = loop([], line[0], line)
    temp_res = list(map(lambda x: x[0][0] + str(x[1]), result_tuple))
    return "".join(temp_res)


print(sequential_count("abbcccdde"))

