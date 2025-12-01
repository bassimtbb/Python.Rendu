temp = input("Input the temperature you like to convert? (e.g., 45F, 102C etc.) : ")

value = float(temp[:-1])
unit = temp[-1].upper()

if unit == 'C':
    fahrenheit = (value * 9/5) + 32
    print(f"The temperature in Fahrenheit is {fahrenheit:.0f} degrees.")
elif unit == 'F':
    celsius = (value - 32) * 5/9
    print(f"The temperature in Celsius is {celsius:.0f} degrees.")
else:
    print("Invalid unit. Please use 'C' or 'F'.")
