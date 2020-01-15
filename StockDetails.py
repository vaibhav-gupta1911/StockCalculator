from datetime import datetime
import requests
import itertools


print("WELCOME TO LIVE STOCK PRICE")
print("Enter Company Symbol(e.g. 'AAPL' for Apple Inc.) to get Live price")
for i in itertools.count():
  ticker = input("\n Enter the Company Symbol : ")
 
  res = requests.get("https://financialmodelingprep.com/api/v3/company/profile/"+ticker)

  if(res.json() == {}):
    print("Invalid Symbol")

  else:
    o_now = datetime.now()
    o_time = o_now.strftime("%d/%m/%Y %H:%M:%S")
    data = res.json()
    profile = data["profile"]
    print("Current date & time: " , o_time)
    print("Full name of the company: " , profile["companyName"])
    print("Stock price: " , profile["price"])
    print("Value changes: " , profile["changes"])
    print("Percentage changes: " , profile["changesPercentage"])

    #print(data)
