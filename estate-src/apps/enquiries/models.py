from django.db import models
from django.utils.translation import gettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField
from apps.common.models import TimeStampedUUIDModel

class Enquiry(TimeStampedUUIDModel):
    name = models.CharField(_('Your Name'), max_length=250)
    phone_number = PhoneNumberField(_('Phone Number'), max_length=30, default="+917717720891")
    email = models.EmailField(_('Your Email'))
    subject = models.CharField(_('Subject'), max_length=150)
    message = models.TextField(_('Message'))

    def __str__(self):
        return self.email
    
    class Meta:
        verbose_name_plural = "Enquiries"
