from django.contrib.auth.models import User
from django.http import HttpResponse, JsonResponse
from django.views.generic import TemplateView
from django.views.generic.base import View
from Baskets.models import ElementBasket
from Products.models import Product


class BasketTemplateView(TemplateView):
    template_name = 'basket.html'
    operated_object = ElementBasket.objects.filter

    def user_object(self):
        return self.request.user.id

    def kwargs_auth(self, **kwargs):
        field_user = {}
        if self.request.user.is_authenticated:
            field_user['user'] = self.user_object()
        else:
            field_user['session_id'] = self.request.session.session_key
        return field_user

    def get_element_basket(self, **kwargs):
        field_user = self.kwargs_auth(**kwargs)
        return self.operated_object(product=self.request.POST['id'], **field_user)

    def get_context_data(self, **kwargs):
        context = super(BasketTemplateView, self).get_context_data(**kwargs)
        field_user = self.kwargs_auth(**kwargs)
        context['elementsBasket'] = self.operated_object(**field_user)
        return context


class BasketView(BasketTemplateView, View):
    pass


class BasketDelete(BasketView):

    def post(self, request, *args, **kwargs):
        self.get_element_basket(**kwargs).delete()
        return HttpResponse('ok')


class BasketCount(BasketView):

    def post(self, request, *args, **kwargs):
        self.get_element_basket(**kwargs).update(count=self.request.POST['count-in-basket'])
        return HttpResponse('ok')


class BasketAdd(BasketView):
    operated_object = ElementBasket

    def user_object(self):
        return User.objects.get(id=self.request.user.id)

    def post(self, request, *args, **kwargs):
        field_user = self.kwargs_auth(**kwargs)
        self.operated_object(**field_user, product=Product.objects.get(id=self.request.POST['id']),
                             count=self.request.POST['count']).save()
        return HttpResponse('ok')


class BasketGet(BasketView):

    def get(self, request, *args, **kwargs):
        data = {}
        field_user = self.kwargs_auth(**kwargs)
        list_ids = [item.product.pk for item in self.operated_object(**field_user)]
        for i in list_ids:
            data[i] = ''
        return JsonResponse(data)
