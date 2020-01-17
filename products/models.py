from django.db import models
from django.urls import reverse


# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=120)
    descr = models.TextField(blank=True, null=True)
    price = models.DecimalField(decimal_places=2, max_digits=1000)
    summary = models.TextField()
    featured = models.NullBooleanField()

    # Dynamic URL
    def get_absolute_url(self):
        return reverse("products:product-details", kwargs={"id": self.id})
        # return f"/products/{self.id}/"
