# Final Prices With a Special Discount in a Shop

def final_prices(prices: list[int]) -> list[int]:
    discounted_prices: list[int] = []
    for index, price in enumerate(prices):
        for inner_index in range(index + 1, len(prices)):
            if prices[inner_index] <= price:
                discounted_prices.append(price - prices[inner_index])
                break
        if len(discounted_prices) != index + 1:
            discounted_prices.append(price)
    
    return discounted_prices


test_cases = (([8,4,6,2,3], [4,2,4,2,3]), ([1,2,3,4,5], [1,2,3,4,5]), ([10,1,1,6], [9,0,1,6]))

for test_case in test_cases:
    
    if test_case[1] == (result := final_prices(test_case[0])):
        print('\033[32mPASS\033[0m')
    else:
        print(f'\033[31mFAIL\033[0m\nfor {test_case}, result = {result}')
