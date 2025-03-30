# Luke Murdock, Currency Converter

def convert(): # 
    currencies = [["USD",1],["EUR",0.92782],["JPY",150.38],["GBP",0.77477],["AUD",1.58555],["CAD",1.427],["CHF",0.88371],["CNH",0.88371],["HKD",7.77528],["NZD",1.74173]]
    
    while True:
        start_currency = input("\nWhat currency are you converting from? [Exit(0) Disclaimer(1)]:\nUS Dollar(USD) Euro(EUR) Japanese Yen(JPY) British Pound(GBP) Austrailian Dollar(AUD) Canadian Dollar(CAD) Swiss Franc(CHF) Chinese Renminbi(CNH) Hong Kong Dollar(HKD) New Zealand Dollar(NZD)\n").strip().upper()
        if start_currency == "0":
            break
        if start_currency == "1":
            print("This Currency Converter is not fully accurate because currency values are constantly changing.")
            continue
        try:
            amount = round(float(input("How much money in that currency?:\n").strip()),2)
            start_amount = amount
        except:
            print("Invalid Input Type (Input a Number)")
            continue
        end_currency = input("What currency are you converting to?:\nUS Dollar(USD) Euro(EUR) Japanese Yen(JPY) British Pound(GBP) Austrailian Dollar(AUD) Canadian Dollar(CAD) Swiss Franc(CHF) Chinese Renminbi(CNH) Hong Kong Dollar(HKD) New Zealand Dollar(NZD)\n").strip().upper()

        def convert_currency(user_currency, to_us):
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
            print("Invalid Input (Insert the currency's abbreviation)")
            continue
        if convert_currency(end_currency, False) == False:
            print("Invalid Input (Insert the currency's abbreviation)")
            continue

        print(f"{start_amount} in {start_currency} is {amount} in {end_currency}")