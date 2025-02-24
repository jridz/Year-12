class CurrencyConverter:

    def __init__(self):

        # Mock exchange rates

        self.exchange_rates = {"USD": 1.2, "EUR": 1.1}

    def convert(self, amount, currency):

        try:

            if currency not in self.exchange_rates:
                raise ValueError(f"Unsupported currency: {currency}")

            converted = amount * self.exchange_rates[currency]

            return round(converted, 2)

        except ValueError as e:

            print(f"Error: {e}")

        except TypeError:

            print("Error: Invalid amount type. Please enter a number.")

        finally:

            print("Conversion attempt finished.")

        # Usage


converter = CurrencyConverter()

try:

    amount = float(input("Enter the amount in your currency: "))

    currency = input("Enter the target currency (USD/EUR): ").upper()

    result = converter.convert(amount, currency)

    if result:
        print(f"Converted amount: {result} {currency}")

except ValueError:

    print("Invalid input. Please enter a valid amount.")
