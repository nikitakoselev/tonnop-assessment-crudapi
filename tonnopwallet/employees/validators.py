from django.core.exceptions import ValidationError
from django.contrib.auth.password_validation import CommonPasswordValidator

from django.contrib.auth.models import User

common = CommonPasswordValidator()


def validate_password(value, length=8):  # tested
    """Somewhat strict validator, returns True once all
    test cases pass, raises a ValidationError if it fails a test."""
    if len(value) < length:
        raise ValidationError("Password must be %s chars or more." % length)

    if value in common.passwords:
        raise ValidationError(
            "Password is a common password, vulnerable to brute force attacks."
        )
    
    return True



def validate_email(email):
    """Check if email is taken."""
    if User.objects.filter(email=email).exists():
        raise ValidationError(
            "A user with that email already exists."
        ) from None
    return True

def validate_username(username):
    """Validate length of username"""

    if len(username) < 4:
        raise ValidationError(
            "username needs to be longer than four character"
        ) from None

    if len(username) > 15:
        raise ValidationError(
            "username cannot be longer than fifteen characters."
        ) from None

    return True