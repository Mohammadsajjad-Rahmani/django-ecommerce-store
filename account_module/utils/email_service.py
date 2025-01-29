from django.core.mail import send_mail
from django.template.loader import render_to_string  # template haro be str convert mikone va send mikone on haro context ba template mix mishe va jofteshon tabdil be reshte mishan
from django.utils.html import strip_tags  # reshte create shode ro optimize mikone
from django.conf import settings
import logging

logger = logging.getLogger(__name__)

def send_email(subject, to, context, template_name):
    try:
        html_message = render_to_string(template_name, context)
        # html_message = str(html_message)
        # html_message = html_message.encode('utf-8')
        plain_message = strip_tags(html_message)
        from_email = settings.EMAIL_HOST_USER
        send_mail(subject, plain_message, from_email, [to], html_message=html_message)
    except Exception as e:
        # اینجا باید از logging استفاده کنید تا خطاها را ثبت کنید
        print(f"Error sending email: {e}")

