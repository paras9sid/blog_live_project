from django.db import models

# Create your models here.
class SocialLinks(models.Model):
    title = models.CharField(max_length=100)
    url = models.URLField()
    
    class Meta:
        verbose_name_plural = 'social links'
        
    def __str__(self) -> str:
        return self.title