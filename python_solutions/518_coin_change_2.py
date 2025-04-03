import pytest

# INFO: Recognize that this is an unbounded knapsack problem


class DpTopDownOptimal:
    def change(self, amount: int, coins: list[int]) -> int:
        dp = [0] * (amount + 1)
        dp[0] = 1
        for coin in coins:
            for current_amount in range(coin, amount + 1):
                dp[current_amount] += dp[current_amount - coin]
        return dp[amount]


class DpTopDown:
    """
    Dynamic Programming (Top-Down). Keep a cache of previously calclulated values
    T: O(n*a)
    S: O(n*a)
    where 'n' is the number of coins and 'a' is the given amount
    """

    def change(self, amount: int, coins: list[int]) -> int:
        cache: dict[tuple[int, int], int] = {}

        def dfs(i: int, a: int) -> int:
            if a == amount:
                return 1
            if a > amount:
                return 0
            if i == len(coins):
                return 0
            if (i, a) in cache:
                return cache[(i, a)]

            cache[(i, a)] = dfs(i, a + coins[i]) + dfs(i + 1, a)
            return cache[(i, a)]

        return dfs(0, 0)


@pytest.mark.parametrize(
    "amount, coins, answer",
    [
        (5, [1, 2, 5], 4),
        (3, [2], 0),
        (10, [10], 1),
    ],
)
def test_solution(amount: int, coins: list[int], answer: int) -> None:
    assert DpTopDownOptimal().change(amount, coins) == answer
    assert DpTopDown().change(amount, coins) == answer
