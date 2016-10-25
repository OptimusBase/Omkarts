from django.contrib import admin

from .models import EmailGroup, EmailTemplate, EmailFrom, EmailAction, EmailSave


class EmailSaveAdmin(admin.ModelAdmin):

    def get_readonly_fields(self, request, obj=None):
        if obj is None:
            return self.readonly_fields + ['email_from', 'email_to', 'email_subject', 'email_body', 'email_sent_on']
        return self.readonly_fields

        # if request.user.is_superuser:
        #     return self.readonly_fields

        # readonly_fields = ('email_from', 'email_to', 'email_subject', 'email_body', 'email_sent_on')


admin.site.register(EmailGroup)
admin.site.register(EmailTemplate)
admin.site.register(EmailFrom)
admin.site.register(EmailAction)
admin.site.register(EmailSave)
