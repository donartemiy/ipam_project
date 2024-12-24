# ipam_project

## Description
MVP django IPAM project. Users can use it to manage ip net without DHCP-server. Possibilities:
 - reserv ips;
 - watch statistic for ip;
 - tool arping helps to find free ip.

## Visuals
Depending on what you are making, it can be a good idea to include screenshots or even a video (you'll frequently see GIFs rather than actual videos). Tools like ttygif can help, but check out Asciinema for a more sophisticated method.

## Usage
Python 3.12.3
```
git clone XXXX
python -m ven venv
source venv/bin/activate
pip intall -r requirements.txt
python manage.py migrate
python manage.py showmigrations
python manage.py createsuperuser
sudo crontab -e  # update absolute path
*/5 * * * * cd /home/username/ipam_project/ipam/ && /home/username/ipam_project/ipam/venv/bin/python /home/username/ipam_project/ipam/manage.py arping_task >> /home/username/ipam_project/cronjob.log 2>&1
grep CRON /var/log/syslog
sudo /home/username/ipam_project/ipam/venv/bin/python3 manage.py runserver 0.0.0.0:8000
```

Notice! django in debug mode.
On productuion you have to:
1. Turn off debug mode in settings.py
2. Add wsgi-server + nginx
3. Remove hardcode for 'subnet' in ipam_project/ipam/ips/management/commands/arping_task.py

## Roadmap
- возможность добавления новых подсетей
- проверку скриптом всех подсетей
- отрефакторить скрипт
- возможность регулировать частоту опроса?
- Педальку, что бы вверху выдавался любой свободный IP и сразу резервировался


## Authors and acknowledgment
My appreciation to https://github.com/ksunik

## License
MIT
