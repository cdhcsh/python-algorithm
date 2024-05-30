
def maxProfit(prices:list[int]):
    answer = 0
    buy = prices[0]
    for num in prices[1:]:
        if buy > num:
            buy = num
        if answer < num - buy:
            answer = num - buy
    return answer
