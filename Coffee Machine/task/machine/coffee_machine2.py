# Write your code here
# 200 ml of water, 50 ml of milk, and 15 g of coffee beans.
WATER_PER_CUP = 200
MILK_PER_CUP = 50
BEANS_PER_CUP = 15

print("Write how many cups of coffee you will need:")
cups = int(input())

water = WATER_PER_CUP * cups
milk = MILK_PER_CUP * cups
beans = BEANS_PER_CUP * cups
print(f"For {cups} cups of coffee you will need:")
print(f"{water} ml of water")
print(f"{milk} ml of milk")
print(f"{beans} g of coffee beans")
