from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Positions, StockForm
import yfinance as yf


class searchStock:
    def __init__(self, new):
        self.new = new
        self.stock = yf.Ticker(new)
        self.symbol = self.stock.info['symbol']
        self.longName = self.stock.info['longName']
        self.price = self.stock.info['regularMarketPrice']
        self.marketCap = self.stock.info['marketCap']
        self.volume = self.stock.info['volume']
        self.forwardPE = self.stock.info['forwardPE']
        self.divYield = self.stock.info['trailingAnnualDividendRate']
        self.info = self.stock.info


def home(request):
    return render(request, 'simulator/home.html', {'title': 'Simulator'})

def search(request):
    
    if request.method == "POST":
        try: 
            searched = request.POST['searched']
            newStock = searchStock(searched)

            context = { 
                'symbol': newStock.symbol,
                'company': newStock.longName, 
                'price': newStock.price, 
                'marketCap': newStock.marketCap,
                'volume': newStock.volume,
                'forwardPE': newStock.forwardPE,
                'divYield': newStock.divYield, 
            }
        except:
            context = { 
                'symbol': '',
                'company': '', 
                'price': '', 
                'marketCap': '',
                'volume': '',
                'forwardPE': '',
                'divYield': '', 
            }
        
    else:
        context = { 
            'symbol': '',
            'company': '', 
            'price': '', 
            'marketCap': '',
            'volume': '',
            'forwardPE': '',
            'divYield': '', 
        }
    
    return render(request, 'simulator/search.html', context)


def about(request):
    return render(request, 'simulator/about.html', {'title': 'About'})

def watchlist(request):
    return render(request, 'simulator/watchlist.html', {'title': 'Watchlist'})

def settings(request):
    return render(request, 'simulator/settings.html', {'title': 'Settings'})

def portfolio(request):
    context = {
        'positions': Positions.objects.all()
    }
    return render(request, 'simulator/portfolio.html', context)

def trade(request):
    
    return render(request, 'simulator/trade.html', {'title': 'Trade'})


def rankings(request):
    return render(request, 'simulator/rankings.html', {'title': 'Rankings'})

def confirmorder(request):

    if request.method == "POST":
        try: 
            ticker = request.POST['ticker']
            quantity = request.POST['quantity']
            buyOrSell = request.POST['buyOrSell']
            newStock = searchStock(ticker)
            total = int(quantity) * int(newStock.price)

            context = { 
                'symbol': newStock.symbol,
                'quantity': quantity,
                'price': newStock.price,
                'longName': newStock.longName,
                'buyOrSell': buyOrSell
                ,'total': total
            }
        except:
            context = { 
                'symbol': '',
                'quantity': '',
                'price': '',
                'longName': '',
                'buyOrSell': ''
                ,'total': ''
            }
        
    else:
        context = { 
            'symbol': '',
            'quantity': '',
            'price': '',
            'longName': '',
            'buyOrSell': ''
            ,'total': ''
        }

    return render(request, 'simulator/confirmorder.html', context)

def addToWatchlist(request):
    return render(request, 'simulator/watchlist', {'title': 'Watchlist'})