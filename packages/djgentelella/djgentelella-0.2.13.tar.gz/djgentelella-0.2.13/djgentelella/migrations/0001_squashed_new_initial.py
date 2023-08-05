# Generated by Django 4.1.1 on 2022-10-08 02:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import djgentelella.chunked_upload.models
import djgentelella.settings


def forwards_func(apps, schema_editor):
    Settings = apps.get_model("djgentelella", "GentelellaSettings")
    Settings.objects.create(
        key='site_title',
        value='Django Gentelella Alela!'
    )
    Settings.objects.create(
        key='site_logo',
        value='<h1><i class="fa fa-paw"></i></h1>'
    )
    model = apps.get_model('djgentelella', 'MenuItem')
    logout = model.objects.filter(title='Logout').first()
    if logout is not None:
        logout.only_icon=False
        logout.save()

    help = model.objects.filter(icon='fa fa-envelope-o').first()
    if help is not None:
        help.title = 'Help'
        help.save()

    Settings = apps.get_model("djgentelella", "GentelellaSettings")
    Settings.objects.create(
        key='site_theme',
        value='gentelella/css/custom.css'
    )

    MenuItem = apps.get_model('djgentelella', 'MenuItem')
    for obj in MenuItem.objects.all():
        if hasattr(obj, 'lft'):
            obj.position = obj.tree_id * 100000 + obj.lft
            obj.save(update_fields=['position'])

class Migration(migrations.Migration):
    replaces = [('djgentelella', '0001_initial'), ('djgentelella', '0002_auto_20200214_2038'), ('djgentelella', '0003_help'), ('djgentelella', '0004_loadsettings'), ('djgentelella', '0005_notification'), ('djgentelella', '0006_permissionscategorymanagement'), ('djgentelella', '0007_edit_footer'), ('djgentelella', '0008_defaulttheme'), ('djgentelella', '0009_chunkedupload'), ('djgentelella', '0010_menuitem_position'), ('djgentelella', '0011_remove_menuitem_level_remove_menuitem_lft_and_more')]

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='GentelellaSettings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.CharField(max_length=100)),
                ('value', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Help',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_view', models.CharField(help_text='View id', max_length=50)),
                ('question_name', models.CharField(help_text='Is a identificaction for question label', max_length=250)),
                ('help_title', models.CharField(max_length=350, verbose_name='Help title')),
                ('help_text', models.TextField(blank=True, default='', verbose_name='Help text')),
            ],
        ),
        migrations.CreateModel(
            name='PermissionsCategoryManagement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Name')),
                ('category', models.CharField(max_length=50, verbose_name='Category')),
                ('url_name', models.CharField(max_length=50, verbose_name='Url Name')),
                ('permission', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auth.permission', verbose_name='Permission')),
            ],
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(verbose_name='Description')),
                ('link', models.URLField(verbose_name='Link')),
                ('message_type', models.CharField(choices=[('default', 'Default'), ('info', 'Information'), ('success', 'Success'), ('warning', 'Warning'), ('danger', 'Danger')], max_length=150, verbose_name='Message Type')),
                ('state', models.CharField(choices=[('visible', 'Visible'), ('hide', 'Hidden')], default='visible', max_length=150, verbose_name='State')),
                ('category', models.UUIDField(blank=True, null=True, verbose_name='Category')),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
                ('update_date', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
            options={
                'ordering': ['-creation_date'],
            },
        ),
        migrations.CreateModel(
            name='MenuItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500)),
                ('url_name', models.CharField(max_length=500)),
                ('category', models.CharField(default='main', help_text='Clasifica items', max_length=200)),
                ('is_reversed', models.BooleanField(default=False)),
                ('reversed_kwargs', models.CharField(blank=True, help_text='Ej key:value,key1:value,key2:value2', max_length=500, null=True)),
                ('reversed_args', models.CharField(blank=True, help_text='Comma separed atributes, can access to template context with request.user.pk', max_length=500, null=True)),
                ('is_widget', models.BooleanField(default=False)),
                ('icon', models.CharField(blank=True, max_length=50, null=True)),
                ('only_icon', models.BooleanField(default=False)),
                ('position', models.IntegerField(default=0)),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='djgentelella.menuitem', verbose_name='parent')),
                ('permission', models.ManyToManyField(blank=True, to='auth.permission')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ChunkedUpload',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('upload_id', models.CharField(default=djgentelella.chunked_upload.models.generate_upload_id, editable=False, max_length=32, unique=True)),
                ('file', models.FileField(max_length=255, upload_to=djgentelella.settings.default_upload_to)),
                ('filename', models.CharField(max_length=255)),
                ('offset', models.BigIntegerField(default=0)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('status', models.PositiveSmallIntegerField(choices=[(1, 'Uploading'), (2, 'Complete')], default=1)),
                ('completed_on', models.DateTimeField(blank=True, null=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='chunked_uploads', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.RunPython(forwards_func)
    ]
