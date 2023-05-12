

def calculatePrice1(drinkType, size, isWhippedCreamTopping):
    # Base case:
    if drinkType == 'hot' and size == 'S' and isWhippedCreamTopping == False:
        return 2.0
    
    price = 2.0
    if size == 'M': price += 0.5
    if size == 'L': price += 1

    if drinkType == 'blend': price += 1
    if isWhippedCreamTopping: price += 0.5

    return price

def calculatePrice2(drinkType, size, isWhippedCreamTopping, milkOption):

    # Base case:
    if drinkType == 'milk tea': 
        price = 2.25

        if size == 'M': price += 0.5
        if size == 'L': price += 1
        if size == 'XL': price += 1.5

        if milkOption: price += 0.5
        if isWhippedCreamTopping: price += 0.5

    else:        
        price = 2.0
    
        if size == 'M': price += 0.5
        if size == 'L': price += 1
        if size == 'XL': price += 1.5

        if drinkType == 'blend': price += 1
        if isWhippedCreamTopping: price += 0.5
        if milkOption: price += 0.5

    return price

def calculatePrice3(drinkType, size, isWhippedCreamTopping, milkOption, chocolateSauceOption):

    # Base case:
    if drinkType == 'milk tea': 
        price = 2.25

        if size == 'M': price += 0.5
        if size == 'L': price += 1
        if size == 'XL': price += 1.5

        if milkOption: price += 0.5
        if isWhippedCreamTopping: price += 0.5

        
    else:
        price = 2.0
        if size == 'M': price += 0.5
        if size == 'L': price += 1
        if size == 'XL': price += 1.5

        if drinkType == 'blend': price += 1
        if isWhippedCreamTopping: price += 0.5
        if milkOption: price += 0.5

    # chocolateSauceOption: number of pump
    if chocolateSauceOption in range(3, 7):
        price += (chocolateSauceOption * 0.5)

    return price

def calculatePrice4(drinkType, size, isWhippedCreamTopping, milkOption, chocolateSauceOption, breakfastItem):

    # Base case:
    if drinkType == 'milk tea': 
        price == 2.25

        if size == 'M': price += 0.5
        if size == 'L': price += 1
        if size == 'XL': price += 1.5

        if milkOption: price += 0.5
        if isWhippedCreamTopping: price += 0.5

        return price
        
    if drinkType == 'hot' and size == 'S' and isWhippedCreamTopping == False:
        return 2.0
    
    price = 2.0
    if size == 'M': price += 0.5
    if size == 'L': price += 1
    if size == 'XL': price += 1.5

    if drinkType == 'blend': price += 1
    if isWhippedCreamTopping: price += 0.5
    if milkOption: price += 0.5

    # chocolateSauceOption: number of pump
    

    if chocolateSauceOption in range(3, 7):
        price += (chocolateSauceOption * 0.5)

    # breakfastItem = {
    #   "sandwich": False,
    #   "egg": False,
    #   "turkey": False,
    #   "Bagel": False,
    #   "butter": False,
    #   "cream cheese": False
    # }
    breakfastPrice = 0.0
    if breakfastItem['sandwich'] == False and breakfastItem['Bagel'] == False:
        breakfastPrice = 0.0
    else: breakfastPrice = 2.0

    if breakfastItem['egg'] or breakfastItem['turkey']: breakfastPrice += 1.0
    if breakfastItem['butter'] or breakfastItem['cream cheese']: breakfastPrice += 0.5

    return price + breakfastPrice

def calculatePrice5(drinkType, size, isWhippedCreamTopping, milkOption, chocolateSauceOption, breakfastItem):

    # Base case:
    if drinkType == 'milk tea': 
        price == 2.25

        if size == 'M': price += 0.5
        if size == 'L': price += 1
        if size == 'XL': price += 1.5

        if milkOption: price += 0.5
        if isWhippedCreamTopping: price += 0.5
        
    
    else:
        price = 2.0
        if size == 'M': price += 0.5
        if size == 'L': price += 1
        if size == 'XL': price += 1.5

        if drinkType == 'blend': price += 1
        if isWhippedCreamTopping: price += 0.5
        if milkOption: price += 0.5


    

    if chocolateSauceOption in range(3, 7):
        price += (chocolateSauceOption * 0.5)

    # breakfastItem = {
    #   "sandwich": False,
    #   "egg": False,
    #   "turkey": False,
    #   "Bagel": False,
    #   "butter": False,
    #   "cream cheese": False
    # }
    breakfastPrice = 0.0
    if breakfastItem['sandwich'] == False and breakfastItem['Bagel'] == False:
        breakfastPrice = 0.0
    else: breakfastPrice = 2.0

    if breakfastItem['egg'] or breakfastItem['turkey']: breakfastPrice += 1.0
    if breakfastItem['butter'] or breakfastItem['cream cheese']: breakfastPrice += 0.5

    tax = (price + breakfastPrice) * (7.25 / 100)

    breakdown = {
        "Base drink": 2.25 if drinkType == 'milk tea' else 2.0,
        "size": 0.5 if size == 'M' else 1 if size == 'L' or size == 'XL' else 0,
        "whipped cream": 0.5 if isWhippedCreamTopping == True else 0,
        "milk option": 0.5 if milkOption == True else 0,
        "Chocolate Sauce": 0.5 * max(chocolateSauceOption - 2, 0),
        "breakfast Item": breakfastPrice
    }

    return price + breakfastPrice + tax, breakdown