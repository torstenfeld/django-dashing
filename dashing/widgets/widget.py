# -*- coding: utf-8 -*-
import json
from django.http import HttpResponse
from django.views.generic.detail import View


class JSONResponseMixin(object):
    """
    A mixin that can be used to render a JSON response.
    """
    def render_to_json_response(self, context, **response_kwargs):
        """
        Returns a JSON response, transforming 'context' to make the payload.
        """
        return HttpResponse(
            self.convert_context_to_json(context),
            content_type='application/json',
            **response_kwargs
        )

    def convert_context_to_json(self, context):
        "Convert the context dictionary into a JSON object"
        return json.dumps(context)


class Widget(JSONResponseMixin, View):
    def get(self, request, *args, **kwargs):
        context = json.dumps(self.get_context())
        return HttpResponse(context, content_type="application/json")

    def render_to_response(self, context, **response_kwargs):
        return self.render_to_json_response(context, **response_kwargs)

