class TimerManager:
    """
    Отвечает только за логику отслеживания времени.
    Ничего не знает про UI (rumps) или про способ уведомления —
    просто вызывает on_interval_reached(), когда время истекло.
    """

    def __init__(self, interval_minutes: int, on_interval_reached):
        self.interval_minutes = interval_minutes
        self.elapsed_minutes = 0
        self.on_interval_reached = on_interval_reached  # callback

    def set_interval(self, minutes: int):
        self.interval_minutes = minutes
        self.reset()

    def reset(self):
        self.elapsed_minutes = 0

    def tick(self, minutes_passed: int = 1):
        """Вызывается каждый раз, когда rumps.Timer тикает."""
        self.elapsed_minutes += minutes_passed
        if self.elapsed_minutes >= self.interval_minutes:
            self.reset()
            self.on_interval_reached()