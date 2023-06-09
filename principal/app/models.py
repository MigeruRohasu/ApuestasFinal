from django.db import models

# Create your models here.
    

class Usuario(models.Model):
    nombres = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)
    contraseña = models.CharField(max_length=100)
    pais = models.CharField(max_length=50, null=True, blank=True)
    ciudad = models.CharField(max_length=50, null=True, blank=True)
    direccion = models.CharField(max_length=100, null=True, blank=True)
    tipo_documento = models.CharField(max_length=50, null=True, blank=True)
    numero_documento = models.CharField(max_length=50, null=True, blank=True)
    fecha_expedicion_documento = models.DateField(null=True, blank=True)
    correo_electronico = models.CharField(max_length=100, unique=True)
    celular = models.CharField(max_length=20, null=True, blank=True)

    def __str__(self) -> str:
        return self.nombres + ' ' + self.apellidos

class MedioDeTransferencia(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    tipo = models.CharField(max_length=20)
    numero = models.CharField(max_length=50)
    banco = models.CharField(max_length=50, null=True, blank=True)
    fecha_registro = models.DateTimeField()
    costo_transferencia = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self) -> str:
        return self.tipo + ' (#' + self.numero + ')'

class Transaccion(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    tipo = models.CharField(max_length=10)
    cantidad = models.DecimalField(max_digits=10, decimal_places=2)
    fecha = models.DateTimeField()

    def __str__(self) -> str:
        return self.tipo + ' - ' + str(self.cantidad)

class Juego(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField(null=True, blank=True)
    tipo = models.CharField(max_length=20, null=True, blank=True)

    def __str__(self) -> str:
        return self.nombre

class Apuesta(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    juego = models.ForeignKey(Juego, on_delete=models.CASCADE)
    tipo_apuesta = models.CharField(max_length=20)
    cantidad = models.DecimalField(max_digits=10, decimal_places=2)
    resultado = models.CharField(max_length=20, null=True)
    ganancias = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    perdidas = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    fecha = models.DateTimeField()

    def __str__(self) -> str:
        return self.fecha