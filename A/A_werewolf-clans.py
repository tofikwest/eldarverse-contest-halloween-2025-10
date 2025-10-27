# Problem A: Werewolf Clans
# Contest: Eldarverse Long HALLOWEEN – October 2025
# Author: Tofik Hasanov


def solve_one(case_idx, N, S):
    from collections import defaultdict

    clan_size = defaultdict(int)

    idx = 0
    for _ in range(N):
        clan_size[S[idx]] += 1

        if idx >= len(S) - 1:
            idx = 0
        else:
            idx += 1

    max_clan = float("-inf")
    min_clan = float("inf")

    for clan in range(len(S)):
        v = clan_size[S[clan]]
        max_clan = max(max_clan, v)
        min_clan = min(min_clan, v)

    print(f"Case #{case_idx}: {max_clan} {min_clan}")


def main():
    T = int(input().strip())
    for case_idx in range(1, T + 1):
        # Each line: integer N, then string S
        parts = input().strip().split()
        N = int(parts[0])
        S = parts[1]
        solve_one(case_idx, N, S)


if __name__ == "__main__":
    main()
