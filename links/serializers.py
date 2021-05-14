from rest_framework.serializers import ModelSerializer
from .models import Link

class LinkSerializer(ModelSerializer):

    class Meta:
        model = Link
        fields = ['value', 'expires', "protected_data"]


    def to_representation(self, data):
        repr = {
                'url': f"/api/v1/shared/{data.value}",
                'expires': data.expires,
                'data': data.protected_data
            }
        return repr


class SharedLinkSerializer(ModelSerializer):

    class Meta:
        model = Link
        fields = ['value', 'expires', 'protected_data']


    def to_representation(self, data):
        repr = {
                'url': f"/api/v1/shared/{data.value}",
                'expires': data.expires,
                'data': data.protected_data
            }
        return repr