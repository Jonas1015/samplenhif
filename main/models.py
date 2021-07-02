from django.db import models




# Create your models here.
class Facility(models.Model):
    UserName = models.CharField(max_length = 100)
    FullName = models.CharField(max_length = 200, null = True, blank = True)
    Password = models.CharField(max_length = 50, null = True, blank = True)
    FacilityCode = models.CharField(max_length = 100, null = True, blank = True)
    EmployerNo = models.CharField(max_length = 100, null = True, blank = True)
    TelephoneNo = models.CharField(max_length = 100, null = True, blank = True)
    EmailAddress = models.EmailField(null = True, blank = True)

    class Meta:
        verbose_name_plural = "Facilities"


    def __str__(self):
        return self.UserName
