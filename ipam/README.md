# ipam_project

```bash
django-admin startproject ipam
python3 manage.py startapp ips
cd ~/ipam_project/ipam 
python3 manage.py runserver 0.0.0.0:8000

python manage.py makemigrations && python manage.py migrate

python manage.py createsuperuser

python manage.py arping_task

python manage.py showmigrations

grep CRON /var/log/syslog


sudo /home/username/ipam_project/ipam/venv/bin/python3 manage.py runserver 192.168.131.129:80

*/5 * * * * cd /home/username/ipam_project/ipam/ && /home/username/ipam_project/ipam/venv/bin/python /home/username/ipam_project/ipam/manage.py arping_task >> /home/username/ipam_project/cronjob.log 2>&1

```

# TODO 
Сделать:
- возможность добавления новых подсетей
- проверку скриптом всех подсетей
- отрефакторить скрипт
- возможность регулировать частоту опроса?
- Педальку, что бы вверху выдавался любой свободный IP и сразу резервировался


## Getting started

To make it easy for you to get started with GitLab, here's a list of recommended next steps.

Already a pro? Just edit this README.md and make it your own. Want to make it easy? [Use the template at the bottom](#editing-this-readme)!

## Add your files

- [ ] [Create](https://docs.gitlab.com/ee/user/project/repository/web_editor.html#create-a-file) or [upload](https://docs.gitlab.com/ee/user/project/repository/web_editor.html#upload-a-file) files
- [ ] [Add files using the command line](https://docs.gitlab.com/ee/gitlab-basics/add-file.html#add-a-file-using-the-command-line) or push an existing Git repository with the following command:

```
cd existing_repo
git remote add origin https://gitlab.com/donartemiy_devops/ipam_project.git
git branch -M main
git push -uf origin main
```

## Integrate with your tools

- [ ] [Set up project integrations](https://gitlab.com/donartemiy_devops/ipam_project/-/settings/integrations)

## Collaborate with your team

- [ ] [Invite team members and collaborators](https://docs.gitlab.com/ee/user/project/members/)
- [ ] [Create a new merge request](https://docs.gitlab.com/ee/user/project/merge_requests/creating_merge_requests.html)
- [ ] [Automatically close issues from merge requests](https://docs.gitlab.com/ee/user/project/issues/managing_issues.html#closing-issues-automatically)
- [ ] [Enable merge request approvals](https://docs.gitlab.com/ee/user/project/merge_requests/approvals/)
- [ ] [Set auto-merge](https://docs.gitlab.com/ee/user/project/merge_requests/merge_when_pipeline_succeeds.html)

## Test and Deploy

Use the built-in continuous integration in GitLab.

- [ ] [Get started with GitLab CI/CD](https://docs.gitlab.com/ee/ci/quick_start/index.html)
- [ ] [Analyze your code for known vulnerabilities with Static Application Security Testing (SAST)](https://docs.gitlab.com/ee/user/application_security/sast/)
- [ ] [Deploy to Kubernetes, Amazon EC2, or Amazon ECS using Auto Deploy](https://docs.gitlab.com/ee/topics/autodevops/requirements.html)
- [ ] [Use pull-based deployments for improved Kubernetes management](https://docs.gitlab.com/ee/user/clusters/agent/)
- [ ] [Set up protected environments](https://docs.gitlab.com/ee/ci/environments/protected_environments.html)

***

# Editing this README

When you're ready to make this README your own, just edit this file and use the handy template below (or feel free to structure it however you want - this is just a starting point!). Thanks to [makeareadme.com](https://www.makeareadme.com/) for this template.

## Suggestions for a good README

Every project is different, so consider which of these sections apply to yours. The sections used in the template are suggestions for most open source projects. Also keep in mind that while a README can be too long and detailed, too long is better than too short. If you think your README is too long, consider utilizing another form of documentation rather than cutting out information.

----

## Simple IPAM plus arping

## Description
MVP django IPAM project. Users can use it to manage ip net without DHCP-server. Possibilities:
 - reserv ips;
 - watch statistic for ip;
 - tool arping helps to find free ip.

## Visuals
Depending on what you are making, it can be a good idea to include screenshots or even a video (you'll frequently see GIFs rather than actual videos). Tools like ttygif can help, but check out Asciinema for a more sophisticated method.

## Usage
Python 3.12.3
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

## Project status
If you have run out of energy or time for your project, put a note at the top of the README saying that development has slowed down or stopped completely. Someone may choose to fork your project or volunteer to step in as a maintainer or owner, allowing your project to keep going. You can also make an explicit request for maintainers.
