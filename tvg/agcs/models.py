from django.db import models

# Create your models here.
#I want the Company as the parent class and the yearly data as child classes
class Companies(models.Model):
    name = models.CharField(max_length=100)
    DSCD = models.CharField(max_length=15)
    nation = models.CharField(max_length=100)
    ESG = models.CharField(max_length=15)
    ENV = models.CharField(max_length=15)
    SOC = models.CharField(max_length=15)
    CGV = models.CharField(max_length=15)
    QUAL = models.CharField(max_length=15)

    def __str__(self):
        return self.name + " - " + self.DSCD + " - " + str(self.ESG)

class Years(models.Model):
    company = models.ForeignKey(Companies, on_delete=models.CASCADE)
    year = models.CharField(max_length=4)
    ESG = models.CharField(max_length=15)
    ENV = models.CharField(max_length=15)
    SOC = models.CharField(max_length=15)
    CGV = models.CharField(max_length=15)
    QUAL = models.CharField(max_length=15)


    def __str__(self):
        return str(self.company.name) + " - " + str(self.year)
