from django.db import models

class Comentario(models.Model):
    usuario = models.CharField(max_length=20, blank=False, null=False)
    asunto = models.CharField(max_length=100, blank=False, null=False)
    fecha = models.DateField(auto_now=True)
    comentario = models.CharField(max_length=300, blank=False)

    class Meta:
        db_table = "comentarios_db"
    
    def __str__(self) -> str:
        return f"El usurio: {self.usuario} escribió un comentario el {self.fecha}"

    def get_fields(self):
        return [
            (field.verbose_name, field.value_from_objetc(self))
            for field in self.__class__._meta.fields[1:]
        ]