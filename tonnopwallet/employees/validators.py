from django.core.exceptions import ValidationError
from .models import Employee



def validate_email(email):
    """Check if email is taken."""
    if Employee.objects.filter(email=email).exists():
        raise ValidationError(
            "An employee with that email already exists."
        ) from None
    return True