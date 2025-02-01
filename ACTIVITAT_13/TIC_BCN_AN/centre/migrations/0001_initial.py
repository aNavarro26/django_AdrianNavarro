# Generated by Django 4.2 on 2025-02-01 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rol', models.CharField(choices=[('student', 'Student'), ('teacher', 'Teacher')], help_text='Rol de la persona: estudiant o professor', max_length=10)),
                ('nom', models.CharField(help_text='Nom de la persona', max_length=50)),
                ('cognom1', models.CharField(help_text='Primer cognom de la persona', max_length=50)),
                ('cognom2', models.CharField(blank=True, help_text='Segon cognom de la persona (Opcional)', max_length=50, null=True)),
                ('correu', models.EmailField(help_text='Correu electrònic de la persona', max_length=254, unique=True)),
                ('curs', models.CharField(help_text='Cursos associats', max_length=100)),
                ('moduls', models.TextField(help_text='Moduls matriculats o impartits')),
                ('tutor', models.BooleanField(default=False, help_text='Es tutor? Només per a professors')),
            ],
        ),
    ]
