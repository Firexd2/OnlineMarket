from django.contrib import admin
from PersonalRoom.models import AdditionalUser, FavoritesProducts
from Core.admin import MixinSearchElements

admin.site.register(AdditionalUser, MixinSearchElements)

admin.site.register(FavoritesProducts, MixinSearchElements)
