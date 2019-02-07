from typing import List
from test_framework import generic_test

# one brute force method would be to calculate all the
# relative buy sell possiblities and keep track of the largest
# Proportional to O(n^2) time complexity
def buy_and_sell_stock_once(prices: List[float]) -> float:
    largest = 0.0
    for i in range(len(prices)):
        for j in range(i + 1, len(prices)):
            transaction = prices[j] - prices[i]
            if transaction > largest:
                largest = transaction
    return largest


# the trick here is to recognize that the max sell will always use
# the minumum price seen so far, so we iterate through the list
# once and track the min_price updating it when needed and always
# computing the max sell based in it
# O(n) time complexity
def buy_and_sell_stock_once(prices: List[float]) -> float:
    min_price = prices[0]
    max_sell = 0.0
    for price in prices:
        sell = price - min_price
        if sell > max_sell:
            max_sell = sell
        if price < min_price:
            min_price = price
    return max_sell


#
if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("buy_and_sell_stock.py",
                                       "buy_and_sell_stock.tsv",
                                       buy_and_sell_stock_once))
