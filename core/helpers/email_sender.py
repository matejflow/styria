from django.core.mail import EmailMessage
from django.template import Context
from django.template.loader import get_template


class SendEmail():
    def __init__(self, template_name=None, subject=None, to=None, data=None,
                 from_email='info@info.com'):
        self.template_name = template_name
        self.subject = subject
        self.to = to
        self.data = data
        self.from_email = from_email

        message = get_template('email/{}'.format(self.template_name)).render(Context(self.data))
        msg = EmailMessage(self.subject, message, to=self.to, from_email=self.from_email)
        msg.content_subtype = 'html'
        msg.send()

    def check_init(self):
        # check if template exists
        # check if subject is set
        # check if to is a list, and if emails are valid
        # check if data is set correctly for given template // not sure
        if not self.check_template():
            return False
        if not self.check_subject():
            return False
        if not self.check_send_to():
            return False
        if not self.check_data():
            return False
        if not self.send_from():
            return False
        return True

    def check_template(self):
        """
        Checks if given string can be found in app/emails/{{template_name}}
        """

        # try:
        #     path = {BASE_DIR}/core/templates/email/{template_name}'.format(
        #     BASE_DIR=settings.BASE_DIR, template_name=self.template_name
        #     with(path, r+) as f:
        #       return path
        # except Exception as e:
        #   log_error()
        return False

    def check_subject(self):
        """
        Check if given input is string
        """
        return True

    def check_send_to(self):
        """
        Check if userGroup object is passed, if yes, send it to all users
        in that group.
        Otherwise check if give input is string and valid email
        """
        return True

    def check_data(self):
        """
        Checks if this is dictionary
        ?? Check somehow for given template if everyhing is provided
        """
        return True

    def check_send_from(self):
        """
        Checks if send_from is string and valid email
        """
        return True

    def check_if_string_and_email(self, value):
        """
        Checks if given data is string and email
        used in self.send_to() and check.send_from()
        """
        return True
