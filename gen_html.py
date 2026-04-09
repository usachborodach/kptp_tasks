#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import yaml
from jinja2 import Template
from datetime import datetime

def load_tasks_from_yaml(file_path):
    """Загружает список задач из YAML-файла."""
    with open(file_path, 'r', encoding='utf-8') as f:
        tasks = yaml.safe_load(f)
    # tasks должен быть списком строк
    if not isinstance(tasks, list):
        raise ValueError("YAML-файл должен содержать список задач")
    return tasks

def render_html(tasks, current_time):
    """Генерирует HTML-страницу с помощью Jinja2 шаблона."""
    # Шаблон в виде строки (можно вынести в отдельный файл)
    template_str = """
<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Задачи КПТП Дубровка (поле)</title>
    <link rel="icon" type="image/x-icon" href="favicon.ico">
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            background-color: #121212;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            padding: 2rem;
            color: #e0e0e0;
        }

        .container {
            max-width: 1200px;
            margin: 0 auto;
        }

        /* Заголовок */
        .header {
            background-color: #1e1e1e;
            border-radius: 12px;
            padding: 1.5rem 2rem;
            margin-bottom: 2rem;
            box-shadow: 0 4px 10px rgba(0,0,0,0.3);
            border-left: 5px solid #4caf50;
        }

        .header h1 {
            font-size: 1.8rem;
            font-weight: 500;
            margin-bottom: 0.5rem;
            color: #ffffff;
        }

        .update-date {
            font-size: 1rem;
            color: #aaaaaa;
            display: flex;
            align-items: center;
            gap: 0.5rem;
        }

        .update-date::before {
            content: "🕒";
            font-size: 1.1rem;
        }

        /* Список задач */
        .tasks-list {
            display: flex;
            flex-direction: column;
            gap: 1rem;
        }

        .task-card {
            background-color: #1e1e1e;
            border-radius: 12px;
            padding: 1.2rem 1.5rem;
            transition: transform 0.2s, background-color 0.2s;
            border: 1px solid #2c2c2c;
            box-shadow: 0 2px 5px rgba(0,0,0,0.2);
        }

        .task-card:hover {
            background-color: #2a2a2a;
            transform: translateX(5px);
            border-color: #4caf50;
        }

        .task-text {
            font-size: 1rem;
            line-height: 1.4;
            color: #e0e0e0;
            word-break: break-word;
        }

        /* Счётчик задач */
        .counter {
            background-color: #2d2d2d;
            display: inline-block;
            padding: 0.2rem 0.8rem;
            border-radius: 20px;
            font-size: 0.85rem;
            margin-top: 0.5rem;
            color: #bbbbbb;
        }

        footer {
            margin-top: 2rem;
            text-align: center;
            font-size: 0.8rem;
            color: #6c6c6c;
            border-top: 1px solid #2c2c2c;
            padding-top: 1.5rem;
        }
    </style>
</head>
<body>
<div class="container">
    <div class="header">
        <h1>📋 Задачи КПТП Дубровка (поле)</h1>
        <div class="update-date">Актуализировано: {{ current_time }}</div>
    </div>

    <div class="tasks-list">
        {% if tasks %}
            {% for task in tasks %}
            <div class="task-card">
                <div class="task-text">{{ task | trim }}</div>
            </div>
            {% endfor %}
        {% else %}
            <div class="task-card">
                <div class="task-text">✅ На данный момент активных задач нет.</div>
            </div>
        {% endif %}
    </div>

    <div class="counter">
        Всего задач: {{ tasks|length }}
    </div>
</div>
</body>
</html>
    """
    template = Template(template_str)
    return template.render(tasks=tasks, current_time=current_time)

def main():
    # 1. Загружаем задачи
    try:
        tasks = load_tasks_from_yaml("tasks.yml")
    except Exception as e:
        print(f"Ошибка чтения tasks.yml: {e}")
        return

    # 2. Текущее время в нужном формате
    now = datetime.now()
    current_time_str = now.strftime("%Y.%m.%d %H:%M")

    # 3. Генерируем HTML
    html_content = render_html(tasks, current_time_str)

    # 4. Записываем index.html
    with open("index.html", "w", encoding="utf-8") as f:
        f.write(html_content)

    print(f"✅ Страница index.html успешно создана. Задач: {len(tasks)}")
    print(f"   Дата актуализации: {current_time_str}")

if __name__ == "__main__":
    main()
