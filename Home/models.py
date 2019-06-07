from django.db import models

# Create your models here.

class Services(models.Model):
    title = models.CharField(max_length=100, )
    image = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    description = models.TextField(blank=True)

    class Meta:
        verbose_name_plural = 'Services'

    def __str__(self):
        return self.title

class WhyUs(models.Model):
    description = models.TextField()

    class Meta:
        verbose_name_plural = 'WhyUs'

    def __str__(self):
        return self.description