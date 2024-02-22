from django.db import models


class dasteha(models.Model):
  name = models.CharField(max_length=100, blank=True)
  id = models.AutoField(primary_key=True)

  def __str__(self):
    return str(self.name)

class zirdaste(models.Model):
  dastehaa = models.ForeignKey(dasteha, related_name='zirdasteha', on_delete=models.CASCADE)
  name = models.CharField(max_length=100, blank=True)
  id = models.AutoField(primary_key=True)




  