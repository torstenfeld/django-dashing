from dashing.widgets.widget import Widget

class GraphWidget(Widget):
    title = ''
    more_info = ''
    value = ''
    data = []

    def get_title(self):
        return self.title

    def get_more_info(self):
        return self.more_info

    def get_value(self):
        return self.value

    def get_data(self):
        return self.data

    def get_context(self):
        return {
            'title': self.get_title(),
            'more_info': self.get_more_info(),
            'value': self.get_value(),
            'data': self.get_data(),
        }
