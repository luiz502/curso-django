from django.urls import path
import recipes.views as vw

urlpatterns = [
    path('', vw.home),
]