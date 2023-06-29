from tgbot.databases.contextmanagers import database_connection


# Главный класс для работы с базой данных
class DataBaseHelper:
    def __init__(self, db_name: str) -> None:
        self.db_name: str = db_name

    # Пример функции для создания таблицы с пользователями
    @property
    def create_all_tables(self):
        with database_connection(self.db_name) as cursor:
            cursor.execute(
                """
                CREATE TABLE IF NOT EXISTS user
                (
                    telegram_id INTEGER PRIMARY KEY,
                    first_name TEXT,
                    last_name TEXT,
                    age INTEGER
                );
                """
            )
