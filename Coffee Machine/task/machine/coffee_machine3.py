# Write your code here
# 200 ml of water, 50 ml of milk, and 15 g of coffee beans.
WATER_PER_CUP = 200
MILK_PER_CUP = 50
BEANS_PER_CUP = 15


# 根据水，牛奶、咖啡豆计算可以做多少杯咖啡
def how_many_cup_can_make(water, milk, beans):
    return min(water // WATER_PER_CUP, milk // MILK_PER_CUP, beans // BEANS_PER_CUP)


print("Write how many ml of water the coffee machine has:")
available_water = int(input())

print("Write how many ml of milk the coffee machine has:")
available_milk = int(input())

print("Write how many grams of coffee beans the coffee machine has:")
available_beans = int(input())

print("Write how many cups of coffee you will need:")
cups = int(input())

water = WATER_PER_CUP * cups
milk = MILK_PER_CUP * cups
beans = BEANS_PER_CUP * cups
if water <= available_water and milk <= available_milk and beans <= available_beans:
    # "Yes, I can make that amount of coffee (and even 2 more than that)"
    more_cup = how_many_cup_can_make(available_water - water, available_milk - milk, available_beans - beans)
    print("Yes, I can make that amount of coffee{}"
          .format(f" (and even {more_cup} more than that)" if more_cup > 0 else ""))
else:
    max_cups_of_coffee = how_many_cup_can_make(available_water, available_milk, available_beans)
    print(f"No, I can make only {max_cups_of_coffee} cups of coffee")
