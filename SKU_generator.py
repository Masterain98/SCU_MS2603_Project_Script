import random


def randomSKU(number):
    # Length = 36
    charList = [chr(i) for i in range(65, 91)] + [str(i) for i in range(10)]
    for i in range(number):
        random_SKU = ""
        for j in range(12):
            randomNumber = random.randint(0, 35)
            random_SKU += charList[randomNumber]
        print(random_SKU)


randomSKU(5)