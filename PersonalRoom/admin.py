from django.contrib import admin

from Core.admin import MixinSearchElements
from PersonalRoom.models import AdditionalUser, FavoritesProducts

admin.site.register(AdditionalUser, MixinSearchElements)

admin.site.register(FavoritesProducts, MixinSearchElements)
