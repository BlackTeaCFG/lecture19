# BookStore Testing Project

Проект автоматизации тестирования для онлайн-магазина книг BookStore.

## Структура проекта

- `cart.py` - модуль корзины покупок
- `payment.py` - модуль обработки платежей
- `test_unit.py` - юнит-тесты для модуля корзины
- `test_integration.py` - интеграционные тесты для взаимодействия корзины и платежей
- `test_functional.py` - функциональные тесты для веб-интерфейса (требуют работающего приложения)

## Запуск тестов
python -m unittest test_unit.py
python -m unittest test_integration.py
python -m unittest test_functional.py  
### Юнит-тесты: