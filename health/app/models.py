from django.db import models

# Create your models here.
state_choices = (
    ('Miami', 'miami'),
    ('New York', 'new york'),
    ('California', 'california'),
    ('Alabama','alabama'),
    ('Chicago', 'chicago'),
    ('Texas','texas'),
    ('Ohio','ohio'),
    ('Georgia','georgia'),
    ('Alaska','alaska'),
    ('Washington','washington'),
    ('Virginia','virginia'),
    ('Colorado','colorado'),
    ('Illinois','illinois'),
    ('New Jersey','new jersey'),
    ('North Calorina','north calorina'),
    ('Michigan','michigan'),
    ('Oregon','oregon'),
    ('Indiana','indiana'),
    ('Utah','utah'),
    ('Montana','montana')
)

speciality_choices = (
    ('Primary Care','primary care'),
    ('Internal Medicine','internal medicine'),
    ('Anesthesiologist','anesthesiologist'),
)


class Records(models.Model):
    NIP = models.IntegerField(max_length=10)
    firstname = models.TextField()
    middlename = models.TextField()
    lastname = models.TextField()
    state = models.TextField(max_length = 20, choices=state_choices,default=None)
    speciality1 = models.TextField(max_length = 20, choices = speciality_choices, default= None)
    speciality2 = models.TextField(max_length = 20, choices = speciality_choices, default= None)
    speciality3 = models.TextField(max_length = 20, choices = speciality_choices, default= None)
    speciality4 = models.TextField(max_length = 20, choices = speciality_choices, default= None)

    def __str__(self):
        return self.NIP

