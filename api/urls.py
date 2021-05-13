"""api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include


from images.views import ImageView, ImagesView, upload_image
from links.views import LinkView, access_link


urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/v1/auth/', include('djoser.urls.authtoken')),

    path('api/v1/images/', ImagesView.as_view()),
    path('api/v1/image/<int:pk>', ImageView.as_view()),
    path('api/v1/image/', ImageView.as_view()),
    path('api/v1/image/upload/', upload_image),

    path('api/v1/shared/', LinkView.as_view()),
    path('api/v1/shared/<str:url_param>', access_link),
    
]
