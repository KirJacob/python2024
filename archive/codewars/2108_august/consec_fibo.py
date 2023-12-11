def fibo_rec(n):
    if n == 0 or n == 1:
        return 1
    else:
        return fibo_rec(n - 1) + fibo_rec(n - 2)


def fibo_loop(n):
    def loop(n_limit, index, prev, acc):
        print(f"{n_limit} {index} {prev} {acc} {prev * acc}")
        if index == n_limit:
            return acc
        else:
            return loop(n_limit, index + 1, acc, prev + acc)

    if n == 1 or n == 2:
        return 1, 1
    else:
        return loop(n, 2, 1, 1), 0


def productFib(n):
    def loop(n_limit, index, prev, acc):
        print(f"{n_limit} {index} {prev} {acc} {prev * acc}")
        if n_limit <= prev * acc:
            flag = n_limit == prev * acc
            return [prev, acc, flag]
        else:
            return loop(n_limit, index + 1, acc, prev + acc)

    if n == 0:
        return [0,1,True]
    elif n == 1 :
        return [1,1,True]
    elif n == 2:
        return [1,2,True]
    else:
        return loop(n, 2, 1, 1)


# 1, 2, 6, 15, 40
# 1 1 2 3 5
# loop(3,1,0)
# loop
# loop(3,2,2)
print(f"fibo_loop(5)={fibo_loop(5)}")
print(f"fibo_loop(6)={fibo_loop(6)}")
print(f"fibo_loop(7)={fibo_loop_task(700)}")
