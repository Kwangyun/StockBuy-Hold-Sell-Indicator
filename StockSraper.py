 
#Provide today's stock price + and professional suggestion regarding BUY/HOLD/SELL 
#Make an average.
#Todo Ask user to input stock they wish.
#save to file and into CSV
#execute the file everyday and send an email
#For personal use/ user agent must be modified 
import requests
from bs4 import BeautifulSoup
#User agent is used for data access to barchart website
headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36"}

#function that takes in a url to request data from website
def create_soup(url):
    res= requests.get(url, headers=headers)
    res.raise_for_status #Check if the website is functioning
    soup=BeautifulSoup(res.text, 'lxml')
    return soup

#Recieve the most current stock price from YahooFinance
def getStockInfo(stock):
    stock_name=stock
    soup= create_soup(f"https://finance.yahoo.com/quote/{stock_name}?p={stock_name}")
    price= soup.find("fin-streamer",attrs={"class" :"Fw(b) Fz(36px) Mb(-4px) D(ib)"}).text

    print("[Stock Price Information]")
    print(f"Today's {stock_name} stock price is $ "+price)
    
#Recieve analysits' recommendation on stock from barchart.com
def recommend(stock):
    stock_name=stock
    try:
        soup= create_soup(f"https://www.barchart.com/stocks/quotes/{stock_name}/overview")
        buy_or_sell= soup.find("div", attrs={"class": "rating"}).text.upper()
        exper= soup.find("span", attrs={"class": "desc"}).text.replace('.','')
        print("[Recommendation from analysist]")
        print(exper + ": "+ buy_or_sell )

    except AttributeError:
        print("No analysis view yet")

if __name__ == "__main__":
    while True:
        stock=input("Enter a stock ticker (eg..AAPL, NVDA , TSLA, FB): ")
        try:
            getStockInfo(stock)
            recommend(stock)
        #Case when stock ticker is not found 
        except AttributeError:
            print("Enter a valid Stock Ticker. E.G Apple -> AAPL, Samsung-> SSNLF ")
            continue
        
