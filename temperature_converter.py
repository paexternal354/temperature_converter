def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32


def main():
    print("Temperature Converter")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    
    choice = input("Choose your conversion (1/2): ")
    
    if choice == '1':
        celsius = float(input("Enter temperature in Celsius: "))
        fahrenheit = celsius_to_fahrenheit(celsius)
        print(f"{celsius}°C is equal to {fahrenheit:.2f}°F")
    
        
    else:
        print("Invalid choice. Please select 1 or 2.")

if __name__ == "__main__":
    main()