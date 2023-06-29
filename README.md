# Шаблон Бота на aiogram

- [Описание](#Описание)
- [Установка](#Установка)
- [Структура](#Структура)

## Описание
Шаблон для телеграмм бота.
Библиотеки:
- aiogram
- sqlite3

## Установка
### Склонировать репозиторий
```zsh
git clone git@github.com:RG1ee/telegram-bot-template.git
# Переходим в клонированный репозиторий
```

### Создать и активировать виртуальное окружение
```zsh
 # Linux, MacOS
python -m venv .venv
. .venv/bin/activate
# Windows
python -m venv .venv
.venv\Scripts\activate.bat # Windows
```

### Создать переменные окружения и вставить свой TOKEN в .env
```zsh
cat env_sample > .env
```

### Установить зависимости
```zsh
pip install -r requirements.txt
```

## Структура
```
env_sample # Пример .env файла
src/
├── bot.py # Главный файл который нужно запускать
├── tgbot/
    ├── databases # Директория для базы данных
        ├── __init__.py
        ├── database.py # Запросы к базе данных
        ├── contextmanagers.py # Кастомные контекстные менеджеры
    ├── handlers/ # Директория для хэдлеров
        ├── __init__.py
        ├── users.py # Работа с запросами от пользователя
        ├── callback.py # Все callback функции
        ├── message.py # Все message функции
    ├── misc/ # Директория для разного
        ├── __init__.py
        ├── register_all_services.py # Регистрация всех хэндлеров
        ├── set_defaulr_command.py # Поставить комманды по умолчанию
    ├── settings/ # Директория для настроек
        ├── config.py # Настройка конфига
        ├── consts.py # Настройка глобальных констант
        ├── data.py # Настройка структуры данных для конфига
```

## Запуск
```zsh
# Linux, MacOS
python3 src/bot.py
# Windows
python src/bot.py
```
