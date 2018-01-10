from django.views.generic import DetailView, ListView, FormView, CreateView, UpdateView
from django.views.generic.base import View, TemplateView


class AdminPanelView(TemplateView):
    template_name = 'admin_panel.html'


class ListAdminView(ListView):
    template_name = 'table/order.html'
    filter = {}
    title = None

    def get_context_data(self, **kwargs):
        context = super(ListAdminView, self).get_context_data(**kwargs)
        context['objects'] = self.model.objects.filter(**self.filter)[::-1]
        context['title'] = self.title
        return context


class DetailObjectAdmin(DetailView):
    title = None

    def get_context_data(self, **kwargs):
        context = super(DetailObjectAdmin, self).get_context_data(**kwargs)
        context['title'] = self.title
        return context


class UpdateObjectAdmin(UpdateView):
    template_name = 'admin_create_object.html'
    success_url = '/admin_panel/'
