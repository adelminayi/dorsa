from django.urls import path
from mytask.views import Adel


urlpatterns = [
    # path('', UserSecret.as_view() , name="secrets"),
    # path('<int:pk>/', UserSecretReform.as_view() , name="secrets_reform"),
    path('adel', Adel.as_view() , name="adelsecarets"),
]