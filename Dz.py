import requests
from bs4 import BeautifulSoup

class CurrencyConverter:
    def __init__(self, exchange_rate):
        self.exchange_rate = exchange_rate

    def convert_to_usd(self, amount):
        """Converts the given amount of local currency to USD."""
        return amount / self.exchange_rate

def get_usd_exchange_rate():
    """
    Fetches the USD exchange rate from the National Bank of Ukraine website.
    Returns the exchange rate as a float, or None if an error occurs.
    """
    url = "https://bank.gov.ua/"
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for bad status codes
        soup = BeautifulSoup(response.content, 'html.parser')

        # Look for the USD exchange rate. The exact HTML structure might change,
        # so you might need to inspect the National Bank's website to find the
        # correct element. This is a common place to find it in a table.
        exchange_rate_element = soup.find('td', string='USD').find_next_sibling('td')
        if exchange_rate_element:
            rate_str = exchange_rate_element.text.replace(',', '.')
            return float(rate_str)
        else:
            print("Could not find the USD exchange rate on the page.")
            return None

    except requests.exceptions.RequestException as e:
        print(f"Error fetching the exchange rate: {e}")
        return None
    except AttributeError:
        print("Error parsing the exchange rate from the page. The website structure might have changed.")
        return None

if __name__ == "__main__":
    print("Welcome to the Currency Converter!")

    usd_rate = get_usd_exchange_rate()

    if usd_rate is not None:
        converter = CurrencyConverter(usd_rate)
        while True:
            try:
                local_currency_amount = float(input("Enter the amount of Ukrainian Hryvnia (UAH) to convert (or 'q' to quit): "))
                usd_amount = converter.convert_to_usd(local_currency_amount)
                print(f"{local_currency_amount:.2f} UAH is equal to {usd_amount:.2f} USD")
            except ValueError:
                user_input = input("Invalid input. Please enter a number or 'q' to quit: ").lower()
                if user_input == 'q':
                    break
            except Exception as e:
                print(f"An unexpected error occurred: {e}")

    print("Thank you for using the Currency Converter!")
