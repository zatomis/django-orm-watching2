# Пульт охраны

Пульт охраны - это сайт, который можно подключить к удаленной БД с визитами и карточками пропуска сотрудников нашего банка.
Программа анализирует базу данных посещений хранилища
## Как начать

* Python3 должен быть уже установлен. [Python](https://www.python.org/downloads)
* Для функционирования необходим Framework Django версии 3.2
* Используйте pip для установки зависимостей: pip install -r requirements.txt
```
pip install -r requirements.txt
```

### Как запустить
Перед запуском необходимо произвести настройку переменных окружения.
в файле .env необходимо прописать переменные для доступа к БД
* SECRET_KEY
* SRV_HOST 
* SRV_PORT
* SRV_NAME
* SRV_USER
* SRV_PASSWORD
* SRV_ALLOWED_HOSTS

Запустить скрипт
```
manage.py runserver 127.0.0.1:8000
```
После активации скрипта, в любом браузере откройте 
```
127.0.0.1:8000
```

## Автор

* **Zatomis** - *Цель проекта* - Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [Devman](https://dvmn.org)
