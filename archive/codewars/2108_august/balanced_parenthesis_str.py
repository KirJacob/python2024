# balanced_parens(0, 0) => [""][0] = ""
# balanced_parens(1, 0) => ["()"][0] = "()"
# balanced_parens(2, 0) => ["(())","()()"][0] = "(())"
# balanced_parens(2, 1) => ["(())","()()"][1] = "()()"
# balanced_parens(3, 3) => ["((()))", "(()())", "(())()", "()(())", "()()()"][3] = "()(())"
import math


def binomialCoeff(n, k):
    res = 1
    if k > n - k:
        k = n - k
    for i in range(k):
        res *= (n - i)
        res /= (i + 1)
    return int(res)


def catalan(n):
    c = binomialCoeff(2 * n, n)
    return int(c / (n + 1))


def balanced_parens(n, k):
    total = []
    print(f"n={n} k={k} cat={catalan(n)}")

    def loop(acc, left_balance, right_balance):
        if left_balance > 0 and right_balance > 0:
            loop(acc + "(", left_balance - 1, right_balance)
        if 0 <= left_balance < right_balance:
            loop(acc + ")", left_balance, right_balance - 1)
        if right_balance == 0 and left_balance == 0:
            total.append(acc)
            return acc

    if k < 0 or k > catalan(n):
        return None
    else:
        loop("", n, n)
        print(len(total))
        if k <= len(total) - 1:
            return total[k]
        else:
            return None


def balanced_parens(n):
    total = []
    print(f"n={n} cat={catalan(n)}")

    def loop(acc, left_balance, right_balance):
        if left_balance > 0 and right_balance > 0:
            loop(acc + "(", left_balance - 1, right_balance)
        if 0 <= left_balance < right_balance:
            loop(acc + ")", left_balance, right_balance - 1)
        if right_balance == 0 and left_balance == 0:
            total.append(acc)
            return acc

    loop("", n, n)
    print(len(total))
    return total



# print(balanced_parens(3, 4))
# print(balanced_parens(3, 0))
# print(balanced_parens(4, 0))
# print(balanced_parens(5, 0))
# print(balanced_parens(6, 0))
# print(balanced_parens(7, 0))
# print(balanced_parens(8, 0))

print(balanced_parens(6))



# (
    # ((
        # (((
            # ((()
                # ((())
                    # ((()))
        # (()
            # (()(
                # (()()
                    # (()())
            # (())
                # (())(
                    # (())()
    # ()
        # ()(
            # ()((
                # ()(()
                    # ()(())
            # ()()
                # ()()(
                    # ()()()
