import ipaddress
import subprocess
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor

from django.core.management.base import BaseCommand
from django.utils import timezone

from ips.models import IPAddressModel

print("Debug msg")

def extruct_mac(output):
    """ Функция для извлечения MAC-адреса из вывода arping. """
    for line in output.splitlines():
        if "bytes from" in line and ":" in line:
            # MAC-адрес идет после "from" в круглых скобках
            parts = line.split()
            for part in parts:
                if ":" in part and len(part) == 17:  # Формат MAC-адреса
                    return part  # Возвращаем MAC-адрес
    return False, None

def arping(ip):
    """ Функция для проверки доступности IP через ARP и получения MAC-адреса. """
    try:
        result = subprocess.run(
            ["sudo", "arping", "-c", "2", "-w", "3", str(ip)],
            stdout=subprocess.PIPE,
            stderr=subprocess.DEVNULL,
            text=True,
        )
        if result.returncode == 0:
            mac_address = extruct_mac(result.stdout)
            return mac_address
        return None
    except Exception as e:
        print(f"Ошибка ARP для {ip}: {e}")
        return None

def analyse(ip):
    mac_address = arping(ip)

    if mac_address:
        status = "used"
        last_seen = timezone.now()
    else:
        status = "free"
        last_seen = None
    return ip, status, last_seen, mac_address

def insert_or_update_ip(ip, subnet_id, status, mac_address, last_seen, user_id=None):
    ip_record, created = IPAddressModel.objects.get_or_create(ip_address=str(ip), defaults={
        'subnet_id': subnet_id,
        'status': status,
        'user_id': user_id,
        'mac_address': mac_address,
        'last_seen': last_seen,
    })
    if not created:
        if status == 'free':
            mac_address = ip_record.mac_address
            last_seen = ip_record.last_seen
        ip_record.status = status
        ip_record.mac_address = mac_address
        ip_record.last_seen = last_seen
        ip_record.save()

class Command(BaseCommand):
    help = "Запуск ARP-сканирования сети"
    print("Test")

    def handle(self, *args, **options):
        print("Test1")
        start_time = datetime.now()
        # Переменные для статистики
        ip_count = 0
        arp_count = 0

        subnet = ipaddress.ip_network("192.168.128.0/22")
        # subnet = ipaddress.ip_network("192.168.128.0/26")  # Подсеть
        max_threads = 5  # Максимальное количество потоков
        subnet_id = 1     # Идентификатор подсети (он будет одинаковым для всех записей)

        with ThreadPoolExecutor(max_threads) as executor:
            # Отправляем каждую задачу в пул потоков для выполнения
            # Сохраняем связь между задачей (Future) и IP-адресом
            tasks = []
            for ip in subnet:
                future = executor.submit(analyse, ip) # Добавляем задачу для проверки IP
                tasks.append((future, ip))  # Сохраняем задачу и IP вместе

            for future, ip in tasks:  # Обрабатываем завершенные задачи
                # Ждем завершения задачи и получаем ее результат
                ip, status, last_seen, mac_address = future.result()
                insert_or_update_ip(ip, subnet_id, status, mac_address, last_seen)
                ip_count += 1
                if mac_address:
                    arp_count += 1
        
        execution_time = datetime.now() - start_time
        self.stdout.write(self.style.SUCCESS(f"Сканирование заняло {execution_time}, проверено ip: {ip_count}, ответили по ARP: {arp_count}"))
