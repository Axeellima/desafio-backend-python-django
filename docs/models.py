from django.db import models

# Create your models here.
class Doc(models.Model):
    value = models.CharField(max_length=10)
    cpf = models.CharField(max_length=11)
    card = models.CharField(max_length=12)
    hour = models.TimeField(null=True)
    owner = models.CharField(max_length=14)
    event_date = models.DateField(null=True)
    type = models.ForeignKey(
        "type.Type",
        on_delete=models.CASCADE,
        null=True
    )
    store = models.ForeignKey(
        "store.Store",
        on_delete=models.CASCADE,
        null=True,
        related_name="doc"
    )

