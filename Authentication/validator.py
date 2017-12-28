from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

def validate_email_on_unicum(value):
    if value.lower() in list(map(lambda x: x['email'], User.objects.all().values('email'))):
        raise ValidationError(u'Почта "%s" уже зарегистрирована в системе' % value)