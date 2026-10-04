"""Lab 2: SPC run rule - a streak of points on one side of the mean

Goal: a process can be out of control even when no point crosses a control
limit. A common SPC run rule says 7 points in a row on the same side of the
mean signals a shift in the process. Build that check.

Instructions
1. Complete first_run_start(samples, length=7): return the position (counting
   from 0, like the dashboard chart) where the first streak of `length`
   points strictly above, or strictly below, the mean begins.
   Return -1 if there is no such streak. A point exactly on the mean
   breaks a streak.
2. Complete longest_run(samples): return the length of the longest streak
   on one side of the mean. An empty list returns 0.
3. Run this file. When every check says OK, you are done.
4. Stuck? Compare with the reference solution below.

Hint: loop through the points and keep two counters: which side the current
streak is on, and how long it is.
"""


def first_run_start(samples, length=7):
    # TODO: write your code here
    pass


def longest_run(samples):
    # TODO: write your code here
    pass


# ---------------- Reference solution ----------------
def _side(x, avg):
    if x > avg:
        return 1
    if x < avg:
        return -1
    return 0


def first_run_start_solution(samples, length=7):
    if not samples:
        return -1
    avg = sum(samples) / len(samples)
    run_side, run_len = 0, 0
    for i, x in enumerate(samples):
        side = _side(x, avg)
        if side != 0 and side == run_side:
            run_len += 1
        else:
            run_side = side
            run_len = 1 if side != 0 else 0
        if run_len == length:
            return i - length + 1
    return -1


def longest_run_solution(samples):
    if not samples:
        return 0
    avg = sum(samples) / len(samples)
    best, run_side, run_len = 0, 0, 0
    for x in samples:
        side = _side(x, avg)
        if side != 0 and side == run_side:
            run_len += 1
        else:
            run_side = side
            run_len = 1 if side != 0 else 0
        best = max(best, run_len)
    return best


# ---------------- Checks ----------------
def check(name, got, expected):
    if got is None:
        print(f"{name}: not done yet")
    elif got == expected:
        print(f"{name}: OK")
    else:
        print(f"{name}: expected {expected}, got {got}")


if __name__ == "__main__":
    shifted = [1, 5, 5, 5, 5, 5, 5, 5, 1, 1]   # 7 above the mean from position 1
    zigzag = [1, 9, 1, 9, 1, 9, 1, 9]          # never 2 in a row
    on_mean = [0, 0, 0, 3, 6, 6, 6]            # mean is 3, the middle point sits on it

    check("first_run_start (shift)", first_run_start(shifted), 1)
    check("first_run_start (zigzag)", first_run_start(zigzag), -1)
    check("first_run_start (point on mean, length 7)", first_run_start(on_mean), -1)
    check("first_run_start (point on mean, length 3)", first_run_start(on_mean, 3), 0)
    check("longest_run (shift)", longest_run(shifted), 7)
    check("longest_run (zigzag)", longest_run(zigzag), 1)
    check("longest_run (empty)", longest_run([]), 0)