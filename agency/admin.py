from django.contrib import admin

from agency.models import Picture
from django.utils.safestring import mark_safe
from adminsortable2.admin import SortableAdminMixin


@admin.register(Picture)
class PictureAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ("pk", "name", "image", "preview")

    def preview(self, obj):
        return mark_safe(f"<img src='{obj.image.icons.get('64')}'>")
