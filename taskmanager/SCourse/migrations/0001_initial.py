# Generated by Django 3.2 on 2021-04-18 05:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bundle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name_Bundle', models.CharField(max_length=255)),
                ('Discription', models.TextField()),
                ('Price', models.IntegerField()),
                ('Date_begin', models.DateField()),
                ('Date_end', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Operator',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name_Operator', models.CharField(max_length=255)),
                ('Login', models.CharField(max_length=30)),
                ('Password', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Town',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name_Town', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Street',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name_Street', models.CharField(max_length=255)),
                ('Number_Street', models.IntegerField()),
                ('Town', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='SCourse.town')),
            ],
        ),
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name_Client', models.CharField(max_length=255)),
                ('Phone_Number', models.IntegerField()),
                ('House', models.CharField(max_length=10)),
                ('Entrance', models.IntegerField()),
                ('Floor', models.IntegerField()),
                ('Flat', models.IntegerField()),
                ('Status', models.BooleanField()),
                ('Bundle', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='SCourse.bundle')),
                ('Operator', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='SCourse.operator')),
                ('Street', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='SCourse.street')),
                ('Town', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='SCourse.town')),
            ],
        ),
    ]