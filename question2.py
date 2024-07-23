def minimum_shots_to_see_ali(tc):
    results = []
    for case in tc:
        n, k, heights = case
        shots_needed = 0
        for height in heights:
            if height > k:
                shots_needed += 1
        results.append(shots_needed)
    return results

# Reading input
T = int(input())
tc = []

for _ in range(T):
    N, K = map(int, input().split())
    heights = list(map(int, input().split()))
    tc.append((N, K, heights))

# Getting results
results = minimum_shots_to_see_ali(tc)

# Printing results
for result in results:
    print(result)
