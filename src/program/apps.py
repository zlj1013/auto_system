from django.apps import AppConfig


class ProgramConfig(AppConfig):
    name = 'program'
    verbose_name="项目管理"
    default_app_config='Program.apps.ProgramConfig'