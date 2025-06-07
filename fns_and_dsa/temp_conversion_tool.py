FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5


def convert_to_celsius(fahrenheit):
    fahrenheit_to_celsius = (fahrenheit -32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return fahrenheit_to_celsius


def convert_to_fahrenheit(celsius):
    celsius_to_fahrenheit = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
    return  celsius_to_fahrenheit



def main():
    while True:
        try:
            temperature = float(input("Enter the temperature to convert: "))
            temperature_state = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").capitalize()
        except ValueError:
            print("Invalid temperature. Please enter a numeric value.")
            continue

        if temperature_state == "C":
            fahrenheit_convert = convert_to_fahrenheit(temperature)
            print(f"{temperature}°C is {fahrenheit_convert}°F")
            break
        elif temperature_state == 'F':
            celsius_convert = convert_to_celsius(temperature)
            print(f"{temperature}°F is {celsius_convert}°C")
            break
        else:
            print("Invalid choice. Please try again.")





if __name__ == "__main__":
    main()
