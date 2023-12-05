from django.db import models

# Create your models here.
class Comment(models.Model):
    username = models.CharField(max_length=30, blank=False, null=False)
    subject = models.CharField(max_length=100, blank=False, null=False)
    comment = models.CharField(max_length=500, blank=False)
    date = models.DateField(auto_now=True)

    class Meta:
        db_table = "comments"
    
    def __str__(self) -> str:
        return f"The user {self.username}, commented on {self.date}"
    
    def get_fields(self):
        return [
            (field.verbose_name, field.value_from_object(self))
            for field in self.__class__._meta.fields[1:]
        ]