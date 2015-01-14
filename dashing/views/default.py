from django.views.generic import TemplateView
from django.core.exceptions import PermissionDenied

from dashing.settings import dashing_settings

class DefaultDashboard(TemplateView):

    template_name = 'dashing/default.html'
    permission_classes = dashing_settings.PERMISSION_CLASSES

    def check_permissions(self, request):
        """
        Check if the request should be permitted.
        Raises an appropriate exception if the request is not permitted.
        """
        permissions = [permission() for permission in self.permission_classes]
        for permission in permissions:
            if not permission.has_permission(request):
                raise PermissionDenied()

    def get(self, request, *args, **kwargs):
        self.check_permissions(request)
        return super(DefaultDashboard, self).get(request, *args, **kwargs)

    def dashname(self):
        return 'default'
