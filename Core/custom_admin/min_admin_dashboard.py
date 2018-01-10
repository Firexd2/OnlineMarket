"""
This file was generated with the customdashboard management command, it
contains the two classes for the main dashboard and app index dashboard.
You can customize these classes as you want.

To activate your index dashboard add the following to your settings.py::
    ADMIN_TOOLS_INDEX_DASHBOARD = 'OnlineShop.dashboard.CustomIndexDashboard'

And to activate the app index dashboard::
    ADMIN_TOOLS_APP_INDEX_DASHBOARD = 'OnlineShop.dashboard.CustomAppIndexDashboard'
"""

from django.utils.translation import ugettext_lazy as _
try:
    from django.urls import reverse
except ImportError:
    from django.core.urlresolvers import reverse

from admin_tools.dashboard import modules, Dashboard, AppIndexDashboard
from admin_tools.utils import get_admin_site_name
from Core.custom_admin.modules.stat import block


class CustomIndexDashboard(Dashboard):

    columns = 2

    def init_with_context(self, context):
        # append an app list module for "Applications"
        self.children.append(modules.AppList(
            _(u'Блок управления данными'),
            exclude=('django.contrib.*',),
        ))

        # append an app list module for "Administration"
        self.children.append(modules.AppList(
            _('Administration'),
            models=('django.contrib.*',),
        ))

        # append a recent actions module
        self.children.append(modules.RecentActions(_('Recent Actions'), 5))

        self.children.append(modules.Group(
            title=u'Статистика',
            display='tabs',
            children=[
                block.StatOrderModule(),
                modules.AppList(
                    title='Applications',
                    exclude=('django.contrib.*',)),
            ]
        ))

    class Media:
        css = {'screen, projection':
                   ('/static_for_admin/admin_panel.css',)}


class CustomAppIndexDashboard(AppIndexDashboard):
    """
    Custom app index dashboard for OnlineShop.
    """

    # we disable title because its redundant with the model list module
    title = ''

    def __init__(self, *args, **kwargs):
        AppIndexDashboard.__init__(self, *args, **kwargs)

        # append a model list module and a recent actions module
        self.children += [
            modules.ModelList(self.app_title, self.models),
            modules.RecentActions(
                _('Recent Actions'),
                include_list=self.get_app_content_types(),
                limit=5
            )
        ]

    def init_with_context(self, context):
        """
        Use this method if you need to access the request context.
        """
        return super(CustomAppIndexDashboard, self).init_with_context(context)
