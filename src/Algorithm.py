import sys


def parse_input(text):
    inputs = [line.strip() for line in text.splitlines() if line.strip()]
    num_inputs = int(inputs[0])

    values = {}
    for i in range(1, num_inputs + 1):
        ch, val = inputs[i].split()
        values[ch] = int(val)

    a = inputs[num_inputs + 1]
    b = inputs[num_inputs + 2]
    return values, a, b


def algorithm(values, a, b):
    n = len(a)
    m = len(b)
    dp = []
    for i in range(n+1):
        dp.append([0] * (m+1))
    
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            comp_one = dp[i-1][j]
            comp_two = dp[i][j-1]
            if (a[i - 1] == b[j - 1]):
                dp[i][j] = max(values[a[i - 1]] + dp[i - 1][j - 1], comp_one, comp_two)
            else:
                dp[i][j] = max(comp_one, comp_two)

    i = n
    j = m
    ans = []

    while i > 0 and j > 0:
        if (a[i - 1] == b[j - 1] and dp[i][j] == values[a[i - 1]] + dp[i - 1][j - 1]):
            ans.append(a[i - 1])
            i -= 1
            j -= 1
        elif (dp[i - 1][j] >= dp[i][j - 1]):
            i -= 1
        else:
            j -= 1

    ans.reverse()
    return dp[n][m], ''.join(ans)


def main():
    values, a, b = parse_input(sys.stdin.read())
    max_val, optimal_sub = algorithm(values, a, b)
    print(max_val)
    print(optimal_sub)


if __name__ == '__main__':
    main()