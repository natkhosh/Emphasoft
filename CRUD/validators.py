import re

from django.core.exceptions import ValidationError
from django.utils.translation import ugettext as _


class PassSymbolValidator(object):

    def validate(self, password, user=None):
        if not re.findall(r'^(?=.*[A-Z])(?=.*\d).{8,}$', password):
            raise ValidationError(
                _("The password is wrong: "),
                code='password_no_symbol',
            )
        if len(password) > 128:
            raise ValidationError(
                _("The password to long > 128 symbols"),
                code='invalid',
            )


