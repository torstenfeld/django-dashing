from dashing.views.default import DefaultDashboard

class TestDashboard(DefaultDashboard):

    template_name = 'dashing/test_board.html'

    def get(self, request, *args, **kwargs):
        self.check_permissions(request)
        return super(TestDashboard, self).get(request, *args, **kwargs)

    def dashname(self):
        return 'test'
