from django.db import models

class Product(models.Model):
   name = models.CharField(max_length=180)
   description = models.TextField(max_length=255)
   price = models.IntegerField()
   created = models.DateTimeField(auto_now_add=True)
   Image = models.ImageField(upload_to="productsimages/", default="/default-picture.jpg")

   def save(self, *args, **kwargs):
      if self.profile_picture:
         DocFile = os.path.splitext(self.profile_picture.name)[1]
         self.profile_picture.name = f"{slugify(self.name)}.{slugify(self.created)}{DocFile}"
      super(UserProfile, self).save(*args, **kwargs)

   def __str__(self): return self.name



