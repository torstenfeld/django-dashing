from dashing.views.default import DefaultDashboard

class ExampleDashboard(DefaultDashboard):

    template_name = 'dashing/example.html'

    def get(self, request, *args, **kwargs):
        self.check_permissions(request)
        return super(ExampleDashboard, self).get(request, *args, **kwargs)

    def dashname(self):
        return 'example'
