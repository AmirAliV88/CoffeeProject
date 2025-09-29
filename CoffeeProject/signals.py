from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

@receiver(post_save, sender=User)
def create_product(sender, instance, created, **kwargs):
   if created: Proudct.objects.create()
    
@receiver(post_delete, sender=User)
def delete_product(sender, instance, **kwargs): 
   instance.Proudct.delete()