from django.contrib import admin
from .models import Mailing


@admin.register(Mailing)
class MailingAdmin(admin.ModelAdmin):

    list_display = ("id", "first_send_at", "finish_send_at", "status", "message")
    search_fields = ("title", "content")
