# Импортируем библиотеку для логирования
from loguru import logger
# Импортируем библиотеку для валидации данных
from pydantic import BaseModel, ValidationError

# Создаем модель данных с помощью Pydantic
class Polzovatel(BaseModel):
    imya: str
    vozrast: int

def main():
    # Логируем начало работы программы
    logger.info("Программа запущена...")
    
    try:
        # Позитивный сценарий: корректные данные
        polzovatel1 = Polzovatel(imya="Ахмет", vozrast=25)
        logger.success(f"Пользователь успешно проверен: {polzovatel1}")
        
        # Негативный сценарий: некорректный тип данных (ожидается int, передается str)
        logger.warning("Ввод некорректных данных...")
        Polzovatel(imya="Мехмет", vozrast="двадцать")
        
    except ValidationError as e:
        # Логируем ошибку валидации
        logger.error(f"Ошибка валидации данных: {e}")
    
    # Логируем завершение работы программы
    logger.info("Программа завершена.")

if __name__ == "__main__":
    main()