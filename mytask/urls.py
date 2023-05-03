from django.urls import path
from mytask.views import sumView, totalView, historyView


urlpatterns = [
    path('sum/', sumView.as_view() , name="sum-view"),
    path('history/', totalView.as_view() , name="total-view"),
    path('total/', historyView.as_view() , name="history-view"),
]