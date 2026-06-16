# Temperature Converter Program

print("Temperature Converter")
print("1. Celsius to Fahrenheit")
print("2. Fahrenheit to Celsius")

choice = int(input("Enter your choice (1 or 2): "))

temperature = float(input("Enter temperature value: "))

if choice == 1:
    fahrenheit = (temperature * 9/5) + 32
    print(f"{temperature}°C = {fahrenheit:.2f}°F")

elif choice == 2:
    celsius = (temperature - 32) * 5/9
    print(f"{temperature}°F = {celsius:.2f}°C")

else:
    print("Invalid choice! Please enter 1 or 2.")