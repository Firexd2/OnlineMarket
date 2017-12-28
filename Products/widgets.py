from django.contrib.admin import widgets
from django.utils.safestring import mark_safe


class MultiFileInput(widgets.AdminFileWidget):
    def render(self, name, value, attrs=None):
        attrs['multiple'] = 'true'
        output = super(MultiFileInput, self).render(name, value, attrs=attrs)
        return mark_safe(output)