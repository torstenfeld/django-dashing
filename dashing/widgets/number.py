from dashing.widgets.widget import Widget

class NumberWidget(Widget):
    title = ''
    more_info = ''
    updated_at = ''
    detail = ''
    value = ''

    def get_title(self):
        return self.title

    def get_more_info(self):
        return self.more_info

    def get_updated_at(self):
        return self.updated_at

    def get_detail(self):
        return self.detail

    def get_value(self):
        return self.value

    def get_context(self):
        return {
            'title': self.get_title(),
            'more_info': self.get_more_info(),
            'updated_at': self.get_updated_at(),
            'detail': self.get_detail(),
            'value': self.get_value(),
        }
