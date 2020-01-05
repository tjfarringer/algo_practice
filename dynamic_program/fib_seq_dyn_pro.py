
from datetime import datetime

# Overall idea is to store intermediate results in a hash table
# continually return to the hash table to prevent unnecessary calculations

fib_cache = {}


def calc_fib_w_cache(n: int) -> int:
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        if fib_cache.get(n, -5) != -5:
            return fib_cache[n]
        else:
            value = (calc_fib_w_cache(n - 1) + calc_fib_w_cache(n - 2))
            fib_cache[n] = value
            return value

test = datetime.now()
answer = calc_fib_w_cache(1000)
test2 = datetime.now()

print("answer is: ", answer)
print("time to run was: ", test2-test)
