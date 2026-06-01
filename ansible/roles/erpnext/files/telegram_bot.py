#!/usr/bin/env python3
import logging
from datetime import datetime
FEEDBACK_FILE = "/var/log/fitness_feedback.log"

def save_feedback(user, message):
    """Сохраняет отзыв в лог-файл"""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(FEEDBACK_FILE, "a") as f:
        f.write(f"[{timestamp}] User: {user} | Feedback: {message}\n")

if __name__ == "__main__":
    print("Telegram бот для сбора отзывов готов к работе")
    print(f"Отзывы сохраняются в: {FEEDBACK_FILE}")
