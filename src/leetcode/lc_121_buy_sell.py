from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_price = float("inf")
        for price in prices:
            min_price = min(price, min_price)
            profit = price - min_price
            max_profit = max(profit, max_profit)
        return max_profit


def test1():
    prices = [7, 1, 5, 3, 6, 4]
    expected = 5
    res = Solution().maxProfit(prices)
    try:
        assert expected == res
    except:
        raise Exception(f"\n{res} should be\n{expected}")


def test2():
    prices = [7, 6, 4, 3, 1]
    expected = 0
    res = Solution().maxProfit(prices)
    try:
        assert expected == res
    except:
        raise Exception(f"\n{res} should be\n{expected}")


if __name__ == "__main__":
    test1()
    test2()
