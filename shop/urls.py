from django.urls import path
from shop import apis


urlpatterns = [
    path('trade_points', apis.get_all_trade_points, name='trade_points'),
    path('attend_tp', apis.attend_trade_point, name='attend_tp'),
]