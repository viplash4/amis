def PurchaseFunc(CandyValue,CookiesValue):
    PurchaseValue = ("Ціна покупки складає %s",(CandyValue*0.400+CookiesValue*0.300))
    return [CandyValue,CookiesValue,PurchaseValue]
CandyValue = float(input('введіть ціну цукерок :'))
CookiesValue = float(input('Введіть ціну печива :'))
print(PurchaseFunc(CandyValue,CookiesValue))

