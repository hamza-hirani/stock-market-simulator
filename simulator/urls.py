from django.urls import path
from . import views
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('search/', views.search, name="search"),
    path('about/', views.about, name='about'),
    path('watchlist/', views.watchlist, name='watchlist'),
    path('settings/', views.settings, name='settings'),
    path('portfolio/', views.portfolio, name='portfolio'),
    path('trade/', views.trade, name='trade'),
    path('rankings/', views.rankings, name='rankings'),
    path('confirmorder/', views.confirmorder, name='confirmorder'),
    #path('addToWatchlist/', views.addToWatchlist, name='addToWatchlist'),
]