def convert(str_var, markers):
    line_sent_excluded = list(filter(lambda x: x != -1, list(map(lambda x: str_var.find(x), markers))))
    if len(line_sent_excluded) == 0:
        return str_var
    else:
        end_pos = min(line_sent_excluded)
        return str_var[0:end_pos].strip()


def solution(string, markers):
    lst_from_string = list(string.split("\n"))
    lst_converted = list(map(lambda x: convert(x, markers), lst_from_string))
    print(lst_converted)
    return "\n".join(lst_converted)


markers = ["!", "#"]
line = "apples, pears # and bananas\ngrapes\nbananas !apples"
lst_str = list(line.split("\n"))
print(convert("apples, pears # and bananas\n", markers))
print(solution(line, markers))