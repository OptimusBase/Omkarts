from django.db import models
from ckeditor.fields import RichTextField
import tagulous.models

EMAIL_GROUP_TYPE = (
    (1, 'Customer Care'),
    (2, 'Managers'))


class EmailGroup(models.Model):
    group_name = models.CharField(
        max_length=1000,
        verbose_name='Group name',
        help_text='')

    description = RichTextField(
        max_length=5000,
        blank=True,
        verbose_name='Group description',
        help_text='Enter a text which will be shown on top of the image')

    email_list = tagulous.models.TagField(
        verbose_name='Email list',
        help_text='Enter comma seperated email ids',
        space_delimiter=True,
        case_sensitive=False)

    group_type = models.IntegerField(choices=EMAIL_GROUP_TYPE)

    class Meta:
        verbose_name = 'Email Group'
        verbose_name_plural = 'Email Groups'

    def __unicode__(self):
        return self.group_name or ''


class EmailTemplate(models.Model):
    template_name = models.CharField(
        max_length=1000,
        verbose_name='Template name',
        help_text='')

    email_subject = models.CharField(
        max_length=500,
        blank=True,
        verbose_name='Email subject',
        help_text='')

    email_body = RichTextField(
        max_length=5000,
        blank=True,
        verbose_name='Email body',
        help_text='')

    class Meta:
        verbose_name = 'Email Template'
        verbose_name_plural = 'Email Templates'

    def __unicode__(self):
        return self.template_name or ''


class EmailFrom(models.Model):
    email_from_name = models.CharField(
        max_length=500,
        verbose_name='Email From',
        help_text='')

    email_id = models.CharField(
        max_length=100,
        blank=True,
        verbose_name='Email Id',
        help_text='')

    class Meta:
        verbose_name = 'Email From'
        verbose_name_plural = 'Email From Data'

    def __unicode__(self):
        return self.email_from_name or ''


class EmailAction(models.Model):
    action_name = models.CharField(
        max_length=100,
        verbose_name='Action name',
        help_text='')

    email_group = models.ForeignKey(
        EmailGroup,
        blank=True,
        null=True,
        related_name='email_action_for_group')

    email_template = models.ForeignKey(
        EmailTemplate,
        blank=True,
        null=True,
        related_name='email_action_for_template')

    email_from = models.ForeignKey(
        EmailFrom,
        blank=True,
        null=True,
        related_name='email_action_for_email_from')

    class Meta:
        verbose_name = 'Email Action'
        verbose_name_plural = 'Email Actions'

    def __unicode__(self):
        return self.action_name or ''


class EmailSave(models.Model):
    email_from = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        verbose_name='Email From',
        help_text='')

    email_to = models.TextField(
        blank=True,
        verbose_name='Email To',
        help_text='')

    email_subject = models.TextField(
        blank=True,
        null=True,
        verbose_name='Email Subject',
        help_text='')

    email_body = models.TextField(
        blank=True,
        null=True,
        verbose_name='Email Body',
        help_text='')

    email_sent_on = models.DateTimeField(
        blank=True,
        null=True,
        verbose_name='Email Sent On',
        auto_now_add=True)

    def __unicode__(self):
        return self.email_from or ''
