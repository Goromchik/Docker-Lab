# Docker-Lab
## Запуск
```bash
docker compose up -d --build
docker compose ps
```
## Тестирование
Открыть в браузере http://localhost:8000/notes

## Проверка сохранности данных
```bash
docker compose down
docker compose up -d
```
После этого http://localhost:8000/notes по-прежнему показывает все записи.

## Остановка
```bash
docker compose down
```
