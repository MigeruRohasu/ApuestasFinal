# Generated by Django 4.2.1 on 2023-05-16 16:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
       migrations.CreateModel(
            name='Apuesta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_apuesta', models.CharField(max_length=20)),
                ('cantidad', models.DecimalField(decimal_places=2, max_digits=10)),
                ('resultado', models.CharField(max_length=20, null=True)),
                ('ganancias', models.DecimalField(decimal_places=2, max_digits=10, null=True)),
                ('perdidas', models.DecimalField(decimal_places=2, max_digits=10, null=True)),
                ('fecha', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Juego',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('descripcion', models.TextField(blank=True, null=True)),
                ('tipo', models.CharField(blank=True, max_length=20, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='MedioDeTransferencia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(max_length=20)),
                ('numero', models.CharField(max_length=50)),
                ('banco', models.CharField(blank=True, max_length=50, null=True)),
                ('fecha_registro', models.DateTimeField()),
                ('costo_transferencia', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='Transaccion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(max_length=10)),
                ('cantidad', models.DecimalField(decimal_places=2, max_digits=10)),
                ('fecha', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombres', models.CharField(max_length=50)),
                ('apellidos', models.CharField(max_length=50)),
                ('contraseña', models.CharField(max_length=100)),
                ('pais', models.CharField(blank=True, max_length=50, null=True)),
                ('ciudad', models.CharField(blank=True, max_length=50, null=True)),
                ('direccion', models.CharField(blank=True, max_length=100, null=True)),
                ('tipo_documento', models.CharField(blank=True, max_length=50, null=True)),
                ('numero_documento', models.CharField(blank=True, max_length=50, null=True)),
                ('fecha_expedicion_documento', models.DateField(blank=True, null=True)),
                ('correo_electronico', models.CharField(max_length=100, unique=True)),
                ('celular', models.CharField(blank=True, max_length=20, null=True)),
            ],
        ),
        
        migrations.AddField(
            model_name='transaccion',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.usuario'),
        ),
        migrations.AddField(
            model_name='mediodetransferencia',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.usuario'),
        ),
        migrations.AddField(
            model_name='apuesta',
            name='juego',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.juego'),
        ),
        migrations.AddField(
            model_name='apuesta',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.usuario'),
        ),
    ]