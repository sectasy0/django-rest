from datetime import datetime, timedelta
from django.shortcuts import get_object_or_404
from rest_framework import status
from django.utils.timezone import now
from uuid import uuid4

from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Link
from images.models import UserPlan
from .serializers import LinkSerializer, SharedLinkSerializer


@api_view(['GET'])
def access_link(request, url_param):
    link = get_object_or_404(Link, value=url_param)

    if link.expires <= now():
        link.delete()
        return Response({"detail": "the given link has expired."})

    serializer = SharedLinkSerializer(link)
    return Response(serializer.data)

class LinkView(APIView):
    permission_classes = (IsAuthenticated,)

    def put(self, request):
        user_plan = UserPlan.objects.filter(user=request.user).first()
        if not user_plan:
            return Response({'detail': "you don't have a plan assigned"}, status=403)

        if not user_plan.plan.expiration_links:
            return Response({'detail': "your plan doesn't allow you to do this"}, status=403)

        if ('expires' in request.data.keys() and 
            300 <= int(request.data.get('expires')) <= 30000):
                protected_data = request.data.copy()
                protected_data.pop('expires', None)

                expires_data = (datetime.now() + 
                    timedelta(seconds=int(request.data.get('expires'))))
                value = uuid4().hex[:12]

                link = Link(expires=expires_data, user=request.user, 
                    value=value, protected_data=protected_data)
                link.save()

                serializer = LinkSerializer(link)

                return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response({"detail": "expires value must be between 300 and 30000 seconds"}, 
                    status=status.HTTP_422_UNPROCESSABLE_ENTITY)
    
    def get(self, request):
        links = Link.objects.filter(user=request.user)
        if links is None:
            return Response(status=status.HTTP_204_NO_CONTENT)

        serializer = LinkSerializer(links, many=True)
        return Response(serializer.data)