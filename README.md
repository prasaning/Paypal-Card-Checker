# PayPal Card Validator

This is a Python script that validates a list of card numbers by interacting with the PayPal API. It checks the validity of credit cards using the PayPal service and logs the results into different files based on the outcome.

## Features:
- Reads card numbers from a file (`combo.txt`).
- Sends validation requests to the PayPal API using cookies and tokens from a configuration file (`config.json`).
- Logs the validation results:
  - **results.txt**: Valid card details.
  - **declined.txt**: Cards that were declined by the bank.
  - **failed.txt**: Cards that failed validation due to errors.
  - **errorlog.txt**: Errors encountered during execution.
- Provides status updates during the process with color-coded messages for easy identification.

## Prerequisites:
- Python 3.x
- Required Libraries:
  - `requests`
  - `colorama`
  - `os`
  - `json`
  - `warnings`
  - `assets` (custom module)

To install the required libraries, run the following:

```bash
pip install requests colorama
```

### Configuration File (`config.json`):
The script requires a configuration file (`config.json`) to store sensitive data like PayPal cookies, CSRF token, and other card-related details. The file should look like this:

```json
{
    "paypal_cookie": "your_paypal_cookie_here",
    "csrf_token": "your_csrf_token_here",
    "billing_address_id": "your_billing_address_id_here",
    "productClass": "your_product_class_here",
    "brand": "your_card_brand_here",
    "expDate": "your_expiry_date_here",
    "verificationCode": "your_cvv_here"
}
```

### Card Data File (`combo.txt`):
The card numbers should be placed in `combo.txt` in the format selected by the user:
- Option 1: `CCNUMBER|EXPRY_MONTH|EXPRY_YEAR|CVV`
- Option 2: `CCNUMBER` (requires aged PayPal account)

## How to Use:
1. Ensure you have the required Python libraries and a valid configuration in `config.json`.
2. Place the card numbers in `combo.txt` according to the selected format.
3. Run the script:

```bash
python Main.py
```

4. Follow the on-screen prompts to select the card processing option.
5. Review the logs in `results.txt`, `declined.txt`, `failed.txt`, and `errorlog.txt` for the outcomes of each card.

## Disclaimer:
This script is intended for educational and informational purposes only. Using this script to interact with any unauthorized services or attempt fraudulent activities is illegal and unethical. Please ensure you have permission to test and validate the cards.

## License:
This project is licensed under the MIT License.

