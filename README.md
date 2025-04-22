[![Maintainability](https://api.codeclimate.com/v1/badges/e4fc64c03c925cc836b0/maintainability)](https://codeclimate.com/github/FrostEasy54/connect_4/maintainability)

# Connect 4 Game

Веб-приложение для игры "Четыре в ряд" с поддержкой двух игроков в реальном времени через WebSocket.  
Бэкенд реализован на Python, фронтенд — на Next.js.

## 🧩 Описание

Этот проект позволяет двум игрокам подключаться к игре и соревноваться друг с другом в режиме реального времени.  
Используется WebSocket для обеспечения мгновенного обмена данными между клиентами и сервером.

## 🚀 Технологии

- **Бэкенд:** Python
- **Фронтенд:** Next.js (TypeScript)
- **WebSocket:** для двусторонней связи в реальном времени
- **Docker:** для контейнеризации приложения

## 📦 Установка и запуск

1. Клонируйте репозиторий:

   ```bash
   git clone https://github.com/FrostEasy54/connect_4.git
   cd connect_4
   ```
2. Запустите приложение с помощью `Docker Compose`:
   ```bash
   docker-compose up --build
   ```
3. Откройте браузер и перейдите по адресу `http://localhost:3000`
4. 📁 Структура проекта
   ```bash
   connect_4/
    ├── backend/        # Серверная часть на Python
    ├── frontend/       # Клиентская часть на Next.js
    ├── .gitignore
    ├── README.md
    └── docker-compose.yml

   ```
## 📌 Особенности
* Реализация игры "Четыре в ряд" с возможностью игры между двумя пользователями
* Использование WebSocket для обеспечения реального времени
* Модульная архитектура с разделением на клиентскую и серверную части
