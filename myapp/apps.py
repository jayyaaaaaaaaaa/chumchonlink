from django.apps import AppConfig

class MyappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'myapp'

    def ready(self):
        import myapp.models # หรือ myapp.signals ถ้าคุณสร้างไฟล์ signals.py แยก