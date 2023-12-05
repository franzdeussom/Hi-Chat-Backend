from rest_framework.viewsets import ModelViewSet


class HichatModelViewSet(ModelViewSet):
    list_serializer_class = None

    def initialize_request(self, request, *args, **kwargs):
        request = super().initialize_request(request, *args, **kwargs)
        print(request.data)
        return request

    def get_serializer_class(self):
        if self.action == "list":
            return self.list_serializer_class or super().get_serializer_class()
        return super().get_serializer_class()
