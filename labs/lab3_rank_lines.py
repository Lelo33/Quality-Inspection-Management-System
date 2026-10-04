"""Lab 3: Rank production lines by defect rate

Goal: app.py asks for the production line and a pass/fail result for every
inspection. Use that data to find which line needs attention first.

Instructions
1. Complete defect_rates(inspections): `inspections` is a list of
   (production_line, result) pairs. Return a dictionary that maps each line
   to its defect rate as a percentage (anything that is not "pass" is a
   defect), rounded to 1 decimal place. An empty list returns {}.
2. Complete rank_lines(rates): take that dictionary and return a list of
   (line, rate) pairs sorted from the highest defect rate to the lowest.
   If two lines have the same rate, sort them by line name, A to Z.
3. Run this file. When every check says OK, you are done.
4. Stuck? Compare with the reference solution below.

Hints: dict.get(key, 0) gives a default for a missing key.
sorted(..., key=...) can sort by more than one thing if the key returns a tuple.
"""


def defect_rates(inspections):
    # TODO: write your code here
    pass


def rank_lines(rates):
    # TODO: write your code here
    pass


# ---------------- Reference solution ----------------
def defect_rates_solution(inspections):
    totals, fails = {}, {}
    for line, result in inspections:
        totals[line] = totals.get(line, 0) + 1
        if result != "pass":
            fails[line] = fails.get(line, 0) + 1
    return {line: round(100 * fails.get(line, 0) / n, 1) for line, n in totals.items()}


def rank_lines_solution(rates):
    return sorted(rates.items(), key=lambda item: (-item[1], item[0]))


# ---------------- Checks ----------------
def check(name, got, expected):
    if got is None:
        print(f"{name}: not done yet")
    elif got == expected:
        print(f"{name}: OK")
    else:
        print(f"{name}: expected {expected}, got {got}")


if __name__ == "__main__":
    data = [
        ("Line A", "pass"), ("Line A", "fail"), ("Line B", "pass"),
        ("Line B", "pass"), ("Line A", "fail"), ("Line C", "fail"),
    ]
    rates = {"Line A": 66.7, "Line B": 0.0, "Line C": 100.0}

    check("defect_rates", defect_rates(data), rates)
    check("defect_rates (empty list)", defect_rates([]), {})
    check("rank_lines", rank_lines(rates),
          [("Line C", 100.0), ("Line A", 66.7), ("Line B", 0.0)])
    check("rank_lines (tie sorts A to Z)",
          rank_lines({"B": 10.0, "A": 10.0, "C": 50.0}),
          [("C", 50.0), ("A", 10.0), ("B", 10.0)])