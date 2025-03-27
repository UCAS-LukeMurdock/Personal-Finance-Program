# Luke Murdock, Currency Converter
"""
Procedure for currency converter:
    Find what currency the user is converting from
    Find how much of that currency
    Find what currency the user is converting to
    Turn their starting currency into USD using the currency's converter amount
    Turn this USD amount knto their desired end currency by using its converter amount
    Display their final amount in the end currency
"""

def convert():
    while True:
        start_currency = input("What currency are you converting from?: US(1) Euro(2) Yen(3) (4) (5) (6) (7) (8) (9) (10) \n")
        amount = input("How much money in that currency?:\n")
        end_currency = input("What currency are you converting to?:\n")
        
"""
US dollar (USD) 1
Euro (EUR) 0.92782
Japanese yen (JPY) 150.38
The pound sterling (GBP) 0.77477
Australian dollar (AUD) 1.58555
Canadian dollar (CAD) 1.427
Swiss franc (CHF) 0.88371
Chinese renminbi (CNH) 7.26052
Hong Kong dollar (HKD) 7.77528
New Zealand dollar (NZD) 1.74173
"""