from django.contrib import admin
from .models import Mailing, Message, MailingAttempt, Recipient

admin.site.register(Recipient)
admin.site.register(Message)
admin.site.register(MailingAttempt)


@admin.register(Mailing)
class MailingAdmin(admin.ModelAdmin):

    list_display = ("id", "first_send_at", "finish_send_at", "status", "message")
    search_fields = ("title", "content")
