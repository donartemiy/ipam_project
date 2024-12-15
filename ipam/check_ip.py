# Параметр arping -w 4 подобран опытным путём.

import sqlite3
import subprocess
import ipaddress
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor, as_completed
import os

time_start = datetime.now()
count_arp = 0


def extruct_mac(output):
    """ Функция для извлечения MAC-адреса из вывода arping. """
    global count_arp
    for line in output.splitlines():
        if "bytes from" in line and ":" in line:
            # MAC-адрес идет после "from" в круглых скобках
            parts = line.split()
            for part in parts:
                if ":" in part and len(part) == 17:  # Формат MAC-адреса
                    count_arp += 1
                    return part  # Возвращаем MAC-адрес
    return False, None

def arping(ip):
    """ Функция для проверки доступности IP через ARP и получения MAC-адреса. """
    try:
        result = subprocess.run(
            ["arping", "-c", "2", "-w", "3", str(ip)],
            stdout=subprocess.PIPE,
            stderr=subprocess.DEVNULL,
            text=True,
        )
        if result.returncode == 0:
            return extruct_mac(result.stdout)
        return None
    except Exception as e:
        print(f"Ошибка ARP для {ip}: {e}")
        return None

def analyse(ip):
    mac_address = arping(ip)

    if mac_address:
        status = "used"
        last_seen = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    else:
        status = "free"
        last_seen = None
    return ip, status, last_seen, mac_address

def insert_or_update_ip(ip, subnet_id, status, mac_address, last_seen, user_id=None):
    # Используем полный путь к базе данных
    base_dir = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(base_dir, 'ipam_db.sqlite3')
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    # Проверим, существует ли уже запись для данного IP-адреса
    cursor.execute('''SELECT id, mac_address, last_seen FROM ips_ipaddressmodel WHERE ip_address = ?''', (str(ip),))
    result = cursor.fetchone()

    if result:
        record_id, current_mac, current_last_seen = result
        
        # Если статус стал free, оставляем прежние значения mac_address и last_seen
        if status == "free":
            mac_address = current_mac
            last_seen = current_last_seen

        # Обновляем запись
        cursor.execute('''
            UPDATE ips_ipaddressmodel
            SET status = ?, mac_address = ?, last_seen = ?
            WHERE id = ?
        ''', (status, mac_address, last_seen, record_id))
    else:
        # Если записи нет, создаем новую
        cursor.execute('''
            INSERT INTO ips_ipaddressmodel (subnet_id, ip_address, status, user_id, mac_address, last_seen)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (subnet_id, str(ip), status, user_id, mac_address, last_seen))

    conn.commit()
    conn.close()

# Основная функция
if __name__ == "__main__":
    """ Основная функция."""
    count = 0
    # subnet = ipaddress.ip_network("192.168.128.0/25")  # Подсеть
    subnet = ipaddress.ip_network("192.168.128.0/22")
    max_threads = 10  # Максимальное количество потоков
    subnet_id = 1  # Идентификатор подсети (он будет одинаковым для всех записей)

    # Создаем пул потоков
    with ThreadPoolExecutor(max_threads) as executor:
        # Отправляем каждую задачу в пул потоков для выполнения
        # Сохраняем связь между задачей (Future) и IP-адресом
        tasks = []  # Список для всех задач
        for ip in subnet:
            future = executor.submit(analyse, ip)  # Добавляем задачу для проверки IP
            tasks.append((future, ip))  # Сохраняем задачу и IP вместе

        # Обрабатываем завершенные задачи
        for future, ip in tasks:
            # Ждем завершения задачи и получаем ее результат
            ip, status, last_seen, mac_address = future.result()
            print(ip, mac_address)

            # Сохраняем результат в базу данных
            count += 1
            insert_or_update_ip(ip, subnet_id, status, mac_address, last_seen)

    time_finish = datetime.now()
    execution_time = time_finish - time_start
    print(f"count_arp: {count_arp}, time_start: {time_start.strftime('%Y-%m-%d %H:%M:%S')}, execution_time: {execution_time}, quntity ips: {count}")