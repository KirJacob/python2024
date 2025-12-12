# 1. Beautiful is better than ugly.
# Readable code is better than cryptic one.

# Bad
add_five_lambda = lambda a : a + 5

# Good
def add_five(num: int) -> int:
    return num + 5

print(add_five(10))
print(add_five(100))

# 2. Explicit is better than implicit.
# Code should not hide meaning.

# Implicit magic behavior
from math import *

# Explicit
from math import sqrt, pi

# 3. Simple is better than complex.
# Prefer straightforward solutions.

# Complex
[x for x in range(10) if x % 2 == 0 and x > 3]

# Simple
list(range(4, 10, 2))

# 4. Complex is better than complicated.
# If complexity is required, structure it logically—not chaotically.

# 5. Flat is better than nested.
# Avoid deep nested structures.
""""
# Too nested
if user:
    if user.active:
        if user.admin:
            print("OK")
# Flat
if user and user.active and user.admin:
    print("OK")
"""

# 6. Sparse is better than dense.
# Add spacing, avoid cramming.

# 7. Readability counts.
# Write code for humans first, machines second.

def add_five(a: int) -> int:
    return a + 5

with open("data.txt") as f:
    data = f.read()