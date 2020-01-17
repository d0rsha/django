from django.db import models
from django.urls import reverse


# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=120)
    descr = models.TextField(blank=True, null=True)
    price = models.DecimalField(decimal_places=2, max_digits=1000)
    featured = models.BooleanField(default=True)

    class Meta:
        verbose_name = ("Blog")
        verbose_name_plural = ("Blogs")

    def __str__(self):
        return self.title

    def __unicode__(self):
        return u"%s's Subscription Info" % self.user_rec

    def get_absolute_url(self):
        return reverse("Blog:article-details", kwargs={"id": self.id})
