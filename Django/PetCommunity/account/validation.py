import re

from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

def validate_password(value):
    passwordReg = r'^01([0|1|6|7|8|9]?)-?([0-9]{3,4})-?([0-9]{4})$'
    regex = re.compile(passwordReg)

    if not regex.match(value):
        raise ValidationError(
            _('%(value)s(은)는 잘못 입력된 전화번호입니다'),
            params = {'value' : value},
        )

def validate_email(value):
    email_reg = r"[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*@(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?"
    regex = re.compile(email_reg)

    if not regex.match(value):
        raise ValidationError(
            _('%(value)s은 잘못 입력된 이메일입니다.'),
            params = {'value' : value},
        )