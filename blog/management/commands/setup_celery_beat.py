from django.core.management.base import BaseCommand
from django_celery_beat.models import IntervalSchedule, PeriodicTask


class Command(BaseCommand):
    help = "Create a test periodic task for Celery Beat."

    def handle(self, *args, **options):
        schedule, _ = IntervalSchedule.objects.get_or_create(
            every=30,
            period=IntervalSchedule.SECONDS,
        )
        task, created = PeriodicTask.objects.update_or_create(
            name="heartbeat every 30 seconds",
            defaults={
                "interval": schedule,
                "task": "blog.tasks.heartbeat",
                "enabled": True,
            },
        )
        verb = "Created" if created else "Updated"
        self.stdout.write(
            self.style.SUCCESS(f"{verb} periodic task: {task.name} -> {task.task}")
        )
