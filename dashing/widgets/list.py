from dashing.widgets.widget import Widget

class ListWidget(Widget):
    title = ''
    more_info = ''
    updated_at = ''
    data = []

    def get_title(self):
        return self.title

    def get_more_info(self):
        return self.more_info

    def get_updated_at(self):
        return self.updated_at

    def get_data(self):
        return self.data

    def get_context(self):
        return {
            'title': self.get_title(),
            'more_info': self.get_more_info(),
            'updated_at': self.get_updated_at(),
            'data': self.get_data(),
        }
