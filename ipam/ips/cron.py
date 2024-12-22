# ВАЖНО. django-cron не запускает задачи. Это инструмент для описания задач.
# Задачу запускает обычный crontab
# */10 * * * * /home/ar-zhuravlev/ipam_project/ipam/venv/bin/python /home/ar-zhuravlev/ipam_project/ipam/manage.py runcrons

# */10 * * * * source /home/ar-zhuravlev/.bashrc && source /home/ar-zhuravlev/ipam_project/ipam/venv/bin/activate && python /home/ar-zhuravlev/ipam_project/ipam/manage.py runcrons >> /home/ar-zhuravlev/ipam_project/cronjob.log 2>&1

from django_cron import CronJobBase, Schedule
from ips.management.commands.arping_task import Command

print("Debug msg")

class ArpingCronJob(CronJobBase):
    RUN_EVERY_MINS = 10  # Интервал в минутах

    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = 'ips.arping_cron_job_5min'  # Просто идентификатор задачи

    def do(self):
        cmd = Command()
        cmd.handle()