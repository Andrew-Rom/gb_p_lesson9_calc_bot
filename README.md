# Telegram Бот-Калькулятор (simple_calc_bot)

Это простой Telegram бот, который выполняет основные арифметические операции. Бот умеет складывать, вычитать, умножать, делить, возводить в степень, находить корни, вычислять остаток от деления и выполнять целочисленное деление.

## Возможности

- **Сложение**: Складывает два числа.
- **Вычитание**: Вычитает одно число из другого.
- **Умножение**: Умножает два числа.
- **Деление**: Делит одно число на другое.
- **Возведение в степень**: Возводит одно число в степень другого.
- **Нахождение корня**: Вычисляет корень заданной степени.
- **Остаток от деления**: Находит остаток от деления двух чисел.
- **Целочисленное деление**: Выполняет целочисленное деление двух чисел.

## Требования

- Python 3.7 или выше
- Токен Telegram бота (его можно получить у [BotFather](https://core.telegram.org/bots#botfather))
- Следующие Python пакеты:
  - `pyTelegramBotAPI` (для взаимодействия с Telegram API)
  - `logger` (для логирования операций)

Вы можете установить необходимые пакеты с помощью:

```bash
pip install pyTelegramBotAPI
```

## Настройка

1. Клонируйте репозиторий:

```bash
git clone https://github.com/yourusername/telegram-bot-calculator.git
cd telegram-bot-calculator
```

2. Настройте переменную окружения для токена вашего Telegram бота. Вы можете сделать это, создав файл `.env` в корневой директории проекта:

```bash
echo "BOT_TOKEN=your-telegram-bot-token-here" > .env
```

3. Запустите бота:

```bash
python main.py
```

## Как использовать

1. Начните чат с вашим ботом в Telegram.
2. Введите `/start`, чтобы увидеть приветственное сообщение.
3. Введите `/operation`, чтобы выбрать арифметическую операцию из меню.
4. Следуйте инструкциям и введите числа, которые хотите вычислить.

## Логирование

Все операции и ошибки логируются с помощью модуля `logger`. Вы можете настроить поведение логирования в файле `logger.py`.

## Участие

Не стесняйтесь форкать этот репозиторий и отправлять pull-реквесты. Любые вклады, будь то исправление ошибок, добавление новых функций или улучшение документации, приветствуются.