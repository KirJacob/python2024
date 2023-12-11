def ips_between(start, end):
    def weight_calc(lst):
        power = 256
        return int(lst[0]) * power * power * power + int(lst[1]) * power * power + int(lst[2]) * power + int(lst[3])
    return weight_calc(end.split(".")) - weight_calc(start.split("."))


print(ips_between("10.0.0.0", "10.0.0.50"))
print(ips_between("10.0.0.0", "10.0.1.0"))
print(ips_between("20.0.0.10", "20.0.1.0"))


