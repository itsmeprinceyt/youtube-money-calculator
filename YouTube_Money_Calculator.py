import requests
import calendar
from datetime import datetime
import os

class YouTubeMoney():
    YouTube_First_Channel_Name="ItsMe Prince Helps"
    YouTube_Second_Channel_Name="ItsMe Prince 0"
    url="https://v6.exchangerate-api.com/v6/4660ead9cb813dc8886441dc/latest/USD"
    inr_rate=0.0
    USD_YouTube_First_Channel_Earning=0.0
    USD_YouTube_Second_Channel_Earning=0.0
    USD_Total=0.0
    USD_Average=0.0

    INR_YouTube_First_Channel_Earning=0.0
    INR_YouTube_Second_Channel_Earning=0.0
    INR_Total=0.0
    INR_Average=0.0
    Days=None
    Month=None
    def star(self):
        print("-----------------------")
    def update(self,url):
        response= requests.get(url)
        data= response.json()
        exchange_rates = data['conversion_rates']
        self.inr_rate = round((exchange_rates['INR']),2)
        Current_Date= datetime.now()
        year=Current_Date.year
        month = Current_Date.month
        self.Month=month
        self.Days= calendar.monthrange(year,month)[1]
    def boot(self):
        self.USD_YouTube_First_Channel_Earning=round(float(input(f"{self.YouTube_First_Channel_Name} | Enter Earning: $")),2)
        self.USD_YouTube_Second_Channel_Earning=round(float(input(f"{self.YouTube_Second_Channel_Name} | Enter Earning: $")),2)
        YouTubeMoney.star(self)
        self.INR_YouTube_First_Channel_Earning=round((self.USD_YouTube_First_Channel_Earning*self.inr_rate),2)
        self.INR_YouTube_Second_Channel_Earning=round((self.USD_YouTube_Second_Channel_Earning*self.inr_rate),2)
        print(f"{self.YouTube_First_Channel_Name} | [USD] Earning: ${self.USD_YouTube_First_Channel_Earning}")
        print(f"{self.YouTube_Second_Channel_Name} | [USD] Earning: ${self.USD_YouTube_Second_Channel_Earning}")
        YouTubeMoney.star(self)
        print(f"{self.YouTube_First_Channel_Name} | [INR] Earning: ₹{self.INR_YouTube_First_Channel_Earning}")
        print(f"{self.YouTube_Second_Channel_Name} | [INR] Earning: ₹{self.INR_YouTube_Second_Channel_Earning}")
        YouTubeMoney.star(self)
        self.INR_Total=round((self.INR_YouTube_First_Channel_Earning+self.INR_YouTube_Second_Channel_Earning),2)
        self.USD_Total=round((self.USD_YouTube_First_Channel_Earning+self.USD_YouTube_Second_Channel_Earning),2)
        print(f"[USD] Total Channel Earning Combined: ${self.USD_Total}")
        print(f"[INR] Total Channel Earning Combined: ₹{self.INR_Total}")
        YouTubeMoney.star(self)
        self.INR_Average=round((self.INR_Total/self.Days),2)
        self.USD_Average=round((self.USD_Total/self.Days),2)
        print(f"[USD] Distributed Earning in the month: ${self.USD_Average}")
        print(f"[INR] Distributed Earning in the month: ₹{self.INR_Average}")
    def export(self):
        Find_DAY= datetime.now()
        FD = Find_DAY.day
        FY = Find_DAY.year
        directory="DataExport"
        if not os.path.exists(directory):
            os.makedirs(directory)
        with open(os.path.join(directory,"Data.txt"),'a', encoding='utf-8') as f:
            f.write(f"Day: {FD}\n")
            f.write(f"Month: {self.Month}\n")
            f.write(f"Year: {FY}\n")
            f.write(f"Rate: $1 -> ₹{round(self.inr_rate,2)}\n\n")
            f.write(f"[USD] {self.YouTube_First_Channel_Name} | Earning: ${self.USD_YouTube_First_Channel_Earning}\n")
            f.write(f"[USD] {self.YouTube_Second_Channel_Name} | Earning: ${self.USD_YouTube_Second_Channel_Earning}\n\n")
            f.write(f"[INR] {self.YouTube_First_Channel_Name} | Earning: ₹{self.INR_YouTube_First_Channel_Earning}\n")
            f.write(f"[INR] {self.YouTube_Second_Channel_Name} | Earning: ₹{self.INR_YouTube_Second_Channel_Earning}\n\n")
            f.write(f"[USD] Total: ${self.USD_Total}\n")
            f.write(f"[INR] Total: ₹{self.INR_Total}\n\n")
            f.write(f"[USD] Distributed Earning in this month: ${self.USD_Average}\n")
            f.write(f"[INR] Distributed Earning in the month: ₹{self.INR_Average}\n\n\n\n\n")
    def for_intro(self):
        YouTubeMoney.update(self,YouTubeMoney.url)
    def main(self):
        YouTubeMoney.boot(self)
if __name__=="__main__":
    start = YouTubeMoney()
    while True:
        start.star()
        start.for_intro()
        print(f"YouTube Money Calculator - $1 : {start.inr_rate}")
        start.star()
        print("1. Calculate")
        print("2. Exit")
        start.star()
        UI=int(input("Enter your choice: "))
        start.star()
        if UI == 1:
            start.main()
        elif UI == 2:
            start.export()
            break