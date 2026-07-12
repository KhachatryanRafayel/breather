from rumps import notification
from config import NOTIFICATION_TITLE, NOTIFICATION_MESSAGES
from random import choice


def send_break_notification(sound_enabled: bool = True):
    message = choice(NOTIFICATION_MESSAGES)
    try:
        notification(
            title=NOTIFICATION_TITLE,
            subtitle="",
            message=message,
            sound=sound_enabled,
        )
    except Exception as e:
        print(f"[notifier] Не удалось отправить уведомление: {e}")