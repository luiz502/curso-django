from django.urls import path
import recipes.views as vw

urlpatterns = [
    path('', vw.home),
    path('sobre/', vw.sobre),
    path('contato/', vw.contato),
]