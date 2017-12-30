from django.contrib import admin
from django.shortcuts import redirect
from Products.forms import ImageAdminForm
from Products import models


class ProductsAdmin(admin.ModelAdmin):
    exclude = ['sail_procent', 'availability', 'name_url']


class CategoryAdmin(admin.ModelAdmin):
    fields = ['name']


class ImageProductAdmin(admin.ModelAdmin):
    form = ImageAdminForm

    def add_view(self, request, *args, **kwargs):
        images = request.FILES.getlist('image', [])
        is_valid = ImageAdminForm(request.POST, request.FILES).is_valid()
        if request.method == 'GET' or len(images) <= 1 or not is_valid:
            return super(ImageProductAdmin, self).add_view(request, *args, **kwargs)
        for image in images:
            product = models.Product.objects.get(pk=request.POST['product'])
            photo = models.ImageProduct(product=product, image=image)
            photo.save()
        return redirect('/admin/Products/imageproduct/')


admin.site.register(models.Category, CategoryAdmin)
admin.site.register(models.Product, ProductsAdmin)
admin.site.register(models.ImageProduct, ImageProductAdmin)
admin.site.register(models.SettingsProduct)
