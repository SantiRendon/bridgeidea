
from django.db import models
from django.utils.timezone import now
from django.utils.translation import gettext_lazy as _
from django.dispatch import receiver
from django.db.models.signals import post_save

class Company(models.Model):
    
    created_at = models.DateTimeField(default=now)
    name = models.CharField('Name', max_length = 300)
    ceo_name = models.CharField('CEO name', max_length = 300)
    location = models.CharField('Location', max_length = 300)
    hash_id = models.TextField('Hash', null=True, default=None)
    
    def save(self, *args, **kwargs):
        pass
        return super().save(*args, **kwargs)
        
        
@receiver(post_save, sender=Company)
def register_transaction(sender, instance: Company, created, **kwargs) -> None:
    if created:
        pass
        #TODO: register in network