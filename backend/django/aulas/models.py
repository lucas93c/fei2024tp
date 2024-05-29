from django.db import models

# Create your models here.

class Carrera(models.Model):
    id = models.AutoField(primary_key=True) 
    nombre = models.CharField(max_length=128, null=False)

class Profesor(models.Model):
    id = models.AutoField(primary_key=True) 
    nombre = models.CharField(max_length=128, null=False)
    apellido = models.CharField(max_length=128, null=False)
    mostrar = models.CharField(max_length=256, null=False)

class Materia(models.Model):
    id = models.AutoField(primary_key=True) 
    nombre = models.CharField(max_length=128, null=False)
    cant_alumnos = models.IntegerField(default=5, null=False)
    id_carrera = models.ForeignKey(Carrera, on_delete=models.CASCADE)
    id_profesor = models.ForeignKey(Profesor, on_delete=models.CASCADE)

class Aula(models.Model):
    id = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=128, null=False)
    ubicacion = models.CharField(max_length=128, null=False)
    cant_proyector = models.IntegerField(default=0)
    aforo = models.IntegerField(default=0)
    es_climatizada = models.BooleanField(default=False)

class Reserva_aula(models.Model):
    id = models.AutoField(primary_key=True)
    id_aula = models.ForeignKey(Aula, on_delete=models.CASCADE)
    fh_desde = models.DateTimeField()
    fh_hasta = models.DateTimeField()
    observacion = models.TextField(max_length=256)
    
class Horario_materia(models.Model):
    id = models.AutoField(primary_key=True)
    id_materia = models.ForeignKey(Materia, on_delete=models.CASCADE)
    id_reserva = models.ForeignKey(Reserva_aula, on_delete=models.CASCADE)
    fh_desde = models.DateTimeField()
    fh_hasta = models.DateTimeField()

