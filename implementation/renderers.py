from rest_framework.renderers import JSONRenderer


class CustomJSONRenderer(JSONRenderer):
    """
    Returns a custom json renderer for the API.
    """
    def render(self, data, accepted_media_type=None, renderer_context=None):
        """
        Reformat the response returned
        """
        status_code = renderer_context['response'].status_code

        # Get the full URL and then splitting to get the desired pattern and
        # add it to "type" key i.e users, goals, data, initiatives, activities
        # etc.
        full_url_path = renderer_context['request'].get_full_path().split('/')[-2]
        response = {
            "success": True,
            "message": None,
            "type": full_url_path,
            "payload": data,
        }

        if not str(status_code).startswith('2'):
            response['success'] = False
            response['payload'] = None
            try:
                response['message'] = data['detail']
            except KeyError:
                response['payload'] = data

        response = super(CustomJSONRenderer, self).render(
            response, accepted_media_type, renderer_context
        )

        return response
