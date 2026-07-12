APP_NAME = "Breather"
APP_ICON = "⏳"

_MINUTES = 30, 35, 40, 45, 50, 55, 60, 65, 70, 80, 90, 100, 110, 120, 130, 140

INTERVALS = {f'{minute} minutes': minute for minute in _MINUTES}

DEFAULT_INTERVAL_KEY = "30 minutes"
TICK_INTERVAL_SECONDS = 60

NOTIFICATION_TITLE = "Time for a break!"
NOTIFICATION_MESSAGES = [
    "Stand up, stretch, give your eyes a rest 🙂",
    "Your chair misses you already... just kidding 😄",
    "Still alive? Go stretch 😅",
    "Water first. Coffee later 💧",
    "Don't become part of the chair 🪑",
    "Tiny break, big difference ✨",
    "Stretch now, thank yourself later 🙂",
    "Blink. Breathe. Move. 🌿",
    "Time for a mini adventure to the kitchen 🚶",
    "Your spine has a request 📩",
    "Go say hi to your legs 👋",
    "Move a bit. That's enough 🙂",
    "Eyes off the monitor for a minute 👀",
    "Stand up. Future you agrees 👍",
    "One glass of water won't hurt 💧",
    "Walk a little, think better 🧠",
    "Your neck called. It wants a break 📞",
    "Reset your posture 🔄",
    "Don't forget to blink 👁️",
    "Quick stretch, then back to it 🚀",
    "Break complete? See you in a while 👋",
]

SOUND_ENABLED_DEFAULT = True
SOUND_PREF_KEY = "sound_enabled"

MENU_HEADER_TEXT = "Breather"
MENU_PLACEHOLDER = "How often would you like to receive a reminder?"