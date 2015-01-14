from django.conf.urls import url
from os.path import join as os_join
from sys import modules as sys_modules
from pkgutil import iter_modules
from distutils.sysconfig import get_python_lib
from warnings import catch_warnings, simplefilter
from inspect import getmembers, isclass
import importlib

class Router(object):

    def __init__(self):
        self.registry = []

    def register(self, widget, basename, **parameters):
        """ Register a widget, URL basename and any optional URL parameters.

        Parameters are passed as keyword arguments, i.e.
            >>> router.register(MyWidget, 'mywidget', my_parameter="[A-Z0-9]+")

        This would be the equivalent of manually adding the following to urlpatterns:
            >>> url(r"^widgets/mywidget/(P<my_parameter>[A-Z0-9]+)/?", MyWidget.as_view(), "widget_mywidget")

        """
        self.registry.append((widget, basename, parameters))

    def __load_dashboards(self):
        self.dashboards = []
        dash_path = 'dashing.views'
        full_path = os_join(get_python_lib(), dash_path.replace('.', '/'))
        for importer, package_name, _ in iter_modules([full_path]):
            full_package_name = '%s.%s' % (dash_path, package_name)
            if full_package_name not in sys_modules:
                module = importlib.import_module(full_package_name)
                for name, obj in getmembers(module, isclass):
                    if 'Dashboard' not in name or 'Default' in name:
                        continue
                    self.dashboards.append(obj)

    def get_urls(self):
        urlpatterns = []
        with catch_warnings():
            simplefilter('ignore')
            self.__load_dashboards()
        for module in self.dashboards:
            methodname = module().dashname()
            dashboardname = '%sdashboard' % methodname
            #if not any(dashboardname in url_name.name for url_name in urlpatterns):
            urlpatterns.append(url(r'^%s/' % methodname, 
                                   module.as_view(),
                                   name=dashboardname)
                                  )

        for widget, basename, parameters in self.registry:
            urlpatterns += [
                url(r'/'.join((
                    r'^widgets/{}'.format(basename),
                    r'/'.join((r'(?P<{}>{})'.format(parameter, regex)
                               for parameter, regex in parameters.items())),
                )),
                    widget.as_view(),
                    name='widget_{}'.format(basename)),
            ]

        return urlpatterns

    @property
    def urls(self):
        return self.get_urls()


router = Router()
