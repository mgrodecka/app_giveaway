from django.db import models
from django.conf import settings

TARGETS = (
    (1, "dzieci"),
    (2, "samotne_matki"),
    (3, "bezdomni"),
    (4, "niepełnosprawni"),
    (5, "osoby_starsze"),
    (6, "bezrobotni"),
    (7, "all"),
)

DONATIONS = (
    (1, "ubrania, które nadają się do ponownego użycia"),
    (2, "ubrania do wyrzucenia"),
    (3, "zabawki"),
    (4, "książki"),
    (5, "inne"),
)


class TrustedInstitutions(models.Model):
    name = models.CharField(max_length=128)
    city = models.CharField(max_length=64)
    target_audience = models.IntegerField(choices=TARGETS)
    address = models.CharField(max_length=128)
    def __str__(self):
        return self.name

class UsersDonations(models.Model):
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE, null=True)
    number_donations = models.IntegerField(default=0)
    number_bags = models.IntegerField(default=0)
    number_institutions = models.IntegerField(default=0)

class Donations(models.Model):
    user =  models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE, null=True)
    donation_type = models.IntegerField(choices=DONATIONS)
    number_of_bags = models.IntegerField(default=0)
    recipient_type = models.IntegerField(choices=TARGETS)
    institution =  models.ForeignKey(TrustedInstitutions, on_delete = models.CASCADE, null=True)
    city = models.CharField(max_length=64)
    donation_date = models.DateTimeField(auto_now_add = True)
    pickup_address = models.CharField(max_length=128)
    phone = models.CharField(max_length=64)
    pickup_date = models.DateField()
    pickup_hour =  models.DateTimeField()
    transprt_notes = models.TextField()
    transfer_status = models.BooleanField(default=False)
