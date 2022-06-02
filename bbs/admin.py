from django.contrib import admin
from .models import Topic, Category

class TopicAdmin(admin.ModelAdmin):
    list_display = ["id", "comment"]


admin.site.register(Topic, TopicAdmin)
admin.site.register(Category)

