# Тестовое задание: upTrader

# Установка и запуск #


## Установка и запуск

1. Клонируйте репозиторий:

    ```bash
    git clone https://github.com/DarthZiel/upTrader.git
    cd upTrader
    ```


2. pip install poetry

3. Создайте таблицы
    ```bash
    poetry run python manage.py migrate
    ```

4. Загрузите тестовоые данные:
     ```bash
    poetry run python manage.py loaddata data.json
    ```

5. Создайте суперюзера:
    
    ```bash
    poetry run python manage.py createsuperuser
    ```
    
6. Запустите сервер:
    
    ```bash
    poetry run python manage.py runserver
    ```


 
