# Generated by Django 3.2.4 on 2021-09-06 14:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ('questionnaires', '0001_initial'),
        ('questions', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='indicator',
            name='question',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='questions.question',
                                    verbose_name='指向问题'),
        ),
        migrations.AddConstraint(
            model_name='indicator',
            constraint=models.CheckConstraint(
                check=models.Q(('parent_indicator__isnull', False), ('question__isnull', False), _negated=True),
                name='app_indicator_parent_question_null'),
        ),
    ]