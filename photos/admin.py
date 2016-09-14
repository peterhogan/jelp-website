from django.contrib import admin

from .models import Photo

list_display = ('title','date_created','orientation','recent_photo')
readonly_fields = ('img_tag',)

admin.site.register(Photo)
