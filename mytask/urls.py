from django.urls import path
from mytask.views import Adel, sumView, totalView, historyView


urlpatterns = [
    path('adel/', Adel.as_view() , name="adelsecarets"),
    path('sum/', sumView.as_view() , name="sum-view"),
    path('history/', totalView.as_view() , name="total-view"),
    path('total/', historyView.as_view() , name="history-view"),
]