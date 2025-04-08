# Luke Murdock, Currency Converter

def convert(): # Converts and displays inputted amount of an inputted currency into another inputted currency
    currencies = [["USD",1],["EUR",0.92782],["JPY",150.38],["GBP",0.77477],["AUD",1.58555],["CAD",1.427],["CHF",0.88371],["CNH",0.88371],["HKD",7.77528],["NZD",1.74173]]
    
    print("\nThis currency converter lets you convert an inputted amount of money from your starting currency into your desired ending currency. The currency options are the ten most used currencies.")
    print("\nDisclaimer:\nThis currency converter is not fully accurate because currency values are constantly changing.")
    while True:
        try:
            amount = round(float(input('\nHow much money are you converting? (Input a Number):\n').strip()), 2)
        except:
            print("\nInvalid Input Type (Input a Number)")
            continue
        start_amount = amount

        currency_names = "\n- US Dollar(USD)\n- Euro(EUR)\n- Japanese Yen(JPY)\n- British Pound(GBP)\n- Austrailian Dollar(AUD)\n- Canadian Dollar(CAD)\n- Swiss Franc(CHF)\n- Chinese Renminbi(CNH)\n- Hong Kong Dollar(HKD)\n- New Zealand Dollar(NZD)"
        start_currency = input(f"\nWhat currency are you converting FROM? (Type the currency's abbreviation):\n{currency_names}\n\nYour choice here: ").strip().upper()

        def convert_currency(user_currency, to_us): # Finds inputted currency and then converts the amount into either USD or the end currency
            nonlocal amount
            for currency in currencies:
                if user_currency == currency[0]:
                    if to_us == True:
                        amount = amount / currency[1]
                    if to_us == False:
                        amount = round(amount * currency[1], 2)
                    return True
            return False

        if convert_currency(start_currency, True) == False:
            print("\n\nStarting Currency is an Invalid Input (Insert the currency's abbreviation)")
            continue

        end_currency = input(f"\nWhat currency are you converting TO?:\n{currency_names}\n\nChoice: ").strip().upper()
        if convert_currency(end_currency, False) == False:
            print("\nEnding Currency is an Invalid Input (Insert the currency's abbreviation)")
            continue

        print(f"{start_amount} in {start_currency} is {amount} in {end_currency}\n")
        break