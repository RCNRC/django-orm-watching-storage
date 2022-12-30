# Django-orm-watching-storage

Это сайт для просмотра активных карт доступа к хранилищу. По каждой карте доступа есть список всех посещений. Также можно узнать кто находится в хранилище прямо сейчас.

## Установка

Скачать гит репозиторий. В корне репозитория создать файл `.env` и поместить внутрь строку `BITLY_API_ACCESS_TOKEN=ваш токен`, где заменить строку `ваш токен` на ваш уникальный токен.

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

Запустить файл main.py как Python скрипт.