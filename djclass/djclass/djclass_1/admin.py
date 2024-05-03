from django.contrib import admin
from .models import Post
from .models import PythonModel
from .models import webCCC
from .models import webgo
from .models import webjavascript

admin.site.register(Post)
admin.site.register(PythonModel)
admin.site.register(webCCC)
admin.site.register(webgo)
admin.site.register(webjavascript)

