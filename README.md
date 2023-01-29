# Django-orm-watching-storage

Это сайт для просмотра активных карт доступа к хранилищу. По каждой карте доступа есть список всех посещений. Также можно узнать кто находится в хранилище прямо сейчас.

## Установка

Скачать гит репозиторий. В корне репозитория изменить название файла `.env_template` на `.env` и заполнить его. Если в этом файле не будут установлены значения для SECRET_KEY, DEBUG, ALLOWED_HOSTS, то их значения будут установлены по дефолту.

## Требования к использованию

Требуется [Python](https://www.python.org/downloads/) версии 3.7 или выше и установленный [pip](https://pip.pypa.io/en/stable/getting-started/). Для установки необходимых зависимостей используйте команду:  
1. Для Unix/macOs:
```commandline
python -m pip install -r requirements.txt
```
2. Для Windows:
```commandline
py -m pip download --destination-directory DIR -r requirements.txt
```

## Использование

Программа использует переменную окружения DJANGO_SETTINGS_MODULE, где указано местоположение файла с настройками для django проекта (если не установлено значение переменной, то по умолчанию ставится `project.settings`).  
Запустить файл manage.py как Python скрипт с 1 аргументом - подкоммандой django.  
Пример запуска сервера на локальном адресе: `http://0.0.0.0:8000/`:
```comandline
> python manage.py runserver 0.0.0.0:8000
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
January 28, 2023 - 12:46:33
Django version 3.2.16, using settings 'project.settings'
Starting development server at http://0.0.0.0:8000/
Quit the server with CONTROL-C.
```