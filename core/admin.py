from django.contrib import admin

from .models import (
    Author,
    Category,
    Journal,
)

class JournalAdmin(admin.ModelAdmin):
    class Meta:
        model = Journal
    list_display = [
        'title',
        'author',
        'get_my_categories',
        'publish_date',
        'views',
        'reviewed',
    ]



admin.site.register(Author)
admin.site.register(Category)
admin.site.register(Journal, JournalAdmin)




