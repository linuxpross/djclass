from django.contrib import admin
from django.urls import path
from djclass_1.views import index
from django.conf.urls.static import static
from django.conf import settings
from djclass_1.views import python_list
from djclass_1.views import web_cc
from djclass_1.views import webgo_app
from djclass_1.views import web_java_script
from djclass_1.views import registration_view
from djclass_1.views import login_view

urlpatterns = [
    path('', index, name='index'),
    path('go/',webgo_app,name='webgoo'),
    path('register/', registration_view, name='register'),
    path('login/', login_view, name='login'),
    path('javasc/',web_java_script,name='web_java_script'),
    path('admin/', admin.site.urls),
    path('python/', python_list, name='python'),
    path('C++/', web_cc, name='C++'),  # Измененный URL-шаблон
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

#python manage.py makemigrations
#python manage.py migrate