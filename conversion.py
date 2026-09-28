temperature_celsius = float(input("Enter temperature in Celsius: "))
temperature_kelvin = temperature_celsius + 273.15

print(f"Temperature in Kelvin: {temperature_kelvin} K")

temperature_fahrenheit = float(input("Enter temperature in Fahrenheit: "))
temperature_celsius = (temperature_fahrenheit - 32) * 5 / 9

print(f"Temperature in Celsius: {temperature_celsius} C")
