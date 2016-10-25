from django.core.mail import send_mail
from django.template import Context, Template
# import logging
import traceback

from .models import EmailGroup, EmailTemplate, EmailAction, EmailSave

# logger = logging.getLogger(__name__)


class Emailer():

    def send_email(self, action_name, data, fail_silently=False):

        # logger.info('INside Emailer and send_email!')

        email_action = EmailAction.objects.get(action_name=action_name)
        # logger.info('email_action defined, method name send_email')

        subject = Template(email_action.email_template.email_subject)
        subject = subject.render(Context(data))
        # logger.info('subject defined, method name send_email')

        message = Template(email_action.email_template.email_body)
        message = message.render(Context(data))
        # logger.info('message defined, method name send_email')

        email_from = email_action.email_from.email_id
        # logger.info('email_from defined, method name send_email')

        email_to = [x.name for x in email_action.email_group.email_list.all()]
        # logger.info('email_to defined, method name send_email')

        # logger.info('about to send email (method name send_email)')
        try:
            var_send_mail = send_mail(subject, message, email_from, email_to, fail_silently, html_message=message)
        except:
            traceback.print_exc()
            # logger.error('email failed to send, method name send_email')
            # logging.exception('Got exception on main handler')

        email_to_str = ''
        for email in email_to:
            email_to_str = ('%s, %s') % (email, email_to_str)

        # logger.info('trying to store sent email data in data base, method name send_email')
        # Storing email info in database
        if var_send_mail == 1:
            email_info = EmailSave(
                email_from=email_from,
                email_to=email_to_str,
                email_subject=subject,
                email_body=message)

            email_info.save()
            # logger.info('email data in data base stored successfully, method name send_email')

    def reply_to_sender(self, action_name, email_to, data, fail_silently=False):
        try:
            email_action = EmailAction.objects.get(action_name=action_name)
        except:
            pass
            # logger.error("email action not defined")

        try:
            subject = Template(email_action.email_template.email_subject)
        except:
            pass
            # logger.error("email subject not defined")
        try:
            subject = subject.render(Context(data))
        except:
            pass
            # logger.error("subject not rendered")

        try:
            message = Template(email_action.email_template.email_body)
        except:
            pass
            # logger.error("email body not templating")
        try:
            message = message.render(Context(data))
        except:
            pass
            # logger.error('message not rendering')
        try:
            email_from = email_action.email_from.email_id
        except:
            pass
            # logger.error("email from not defined")
        try:
            var_send_mail = send_mail(subject, message, email_from, [email_to], fail_silently, html_message=message)
        except:
            pass
            # logger.error("email not sent")
            # logger.error(var_send_mail)
        # Storing email info in database
        if var_send_mail == 1:
            email_info = EmailSave(
                email_from=email_from,
                email_to=email_to,
                email_subject=subject,
                email_body=message)

            email_info.save()
