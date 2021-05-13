from rest_framework.serializers import ModelSerializer
from .models import Image

class ImageSerializer(ModelSerializer):

    class Meta:
        model = Image
        fields = ['pk', 'image']

    def to_representation(self, data):
        repr = {
                'path': f"/api/v1/images/{data.image}",
                'id': data.pk
            }
        return repr

