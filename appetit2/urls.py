"""
URL configuration for appetit2 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from .views import HomePage, AboutUs, AppleFlan, BananaCookies, Breakfast, BroccoliSoup, BrownieFit, CarrotCake
from .views import CarrotCookies, Chefs, ChickenChaufa, ChickpeaSalad, ChocolateDreams, Contact, Dessert, FlourlessMuffins
from .views import TresLeches, VeganBurrito, LentilBurguers, Lunch, Menu, Mushroom, ChocolateHazelnut, Recipes
from .views import KiwiBons, ApplePie, EggTart

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", HomePage.as_view(), name = "index"),
    path("about_us.html", AboutUs.as_view(), name = "about_us"),
    path("apple_flan.html", AppleFlan.as_view(), name = "apple_flan"),
    path("banana_protein_cookies.html", BananaCookies.as_view(), name = "banana_protein_cookies"),
    path("breakfast.html", Breakfast.as_view(), name = "breakfast"),
    path("broccoli_soup.html", BroccoliSoup.as_view(), name = "broccoli_soup"),
    path("brownie_healty_and_fit.html", BrownieFit.as_view(), name = "brownie_healty_and_fit"),
    path("carrot_and_walnut_cake.html", CarrotCake.as_view(), name = "carrot_and_walnut_cake"),
    path("carrot_cake_breakfast_cookies.html", CarrotCookies.as_view(), name = "carrot_cake_breakfast_cookies"),
    path("chefs.html", Chefs.as_view(), name = "chefs"),
    path("chicken_chaufa.html", ChickenChaufa.as_view(), name = "chicken_chaufa"),
    path("chickpea_salad.html", ChickpeaSalad.as_view(), name = "chickpea_salad"),
    path("chocolate_raspberry_dreams_breakfast_parfait.html", ChocolateDreams.as_view(), name = "chocolate_raspberry_dreams_breakfast_parfait"),
    path("contact.html", Contact.as_view(), name = "contact"),
    path("dessert.html", Dessert.as_view(), name = "dessert"),
    path("flourless_bite_sized_breakfast_muffins.html", FlourlessMuffins.as_view(), name = "flourless_bite_sized_breakfast_muffins"),
    path("healthy_tres_leches_cake.html", TresLeches.as_view(), name = "healthy_tres_leches_cake"),
    path("high_protein_vegan_breakfast_burrito.html", VeganBurrito.as_view(), name = "high_protein_vegan_breakfast_burrito"),
    path("lentil_and_oat_burgers.html", LentilBurguers.as_view(), name = "lentil_and_oat_burgers"),
    path("lunch.html", Lunch.as_view(), name = "lunch"),
    path("menu.html", Menu.as_view(), name = "menu"),
    path("mushroom_stuffed_eggplant.html", Mushroom.as_view(), name = "mushroom_stuffed_eggplant"),
    path("raw_chocolate_hazelnut_breakfast.html", ChocolateHazelnut.as_view(), name = "raw_chocolate_hazelnut_breakfast"),
    path("recipes.html", Recipes.as_view(), name = "recipes"),
    path("strawberry_and_kiwi_bons.html", KiwiBons.as_view(), name = "strawberry_and_kiwi_bons"),
    path("sugar_free_apple_pie_chia_seed_jam.html", ApplePie.as_view(), name = "sugar_free_apple_pie_chia_seed_jam"),
    path("vegetable_and_egg_tart.html", EggTart.as_view(), name = "vegetable_and_egg_tart"),
    path('comments/', include('comentarios.urls')),
]
