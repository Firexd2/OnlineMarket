from django.views.generic import DetailView, ListView, FormView
from django.views.generic.base import View, TemplateView


class AdminPanelView(TemplateView):
    template_name = 'admin_panel.html'


class ListAdminView(ListView):
    template_name = 'admin_order_table.html'
    filter = {}
    title = None
    model = None

    def get_context_data(self, **kwargs):
        context = super(ListAdminView, self).get_context_data(**kwargs)
        context['objects'] = self.model.objects.filter(**self.filter)[::-1]
        context['title'] = self.title
        return context



