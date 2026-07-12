import rumps
import AppKit
from Foundation import NSAttributedString, NSUserDefaults
from config import *
from notifier import send_break_notification
from timer_manager import TimerManager


def make_gray_header(text: str) -> rumps.MenuItem:
    header = rumps.MenuItem(text)
    header.set_callback(None)

    attributes = {
        AppKit.NSForegroundColorAttributeName: AppKit.NSColor.secondaryLabelColor(),
        AppKit.NSFontAttributeName: AppKit.NSFont.menuFontOfSize_(12),
    }
    attributed_title = NSAttributedString.alloc().initWithString_attributes_(
        text, attributes
    )
    header._menuitem.setAttributedTitle_(attributed_title)
    return header


class BreatherApp(rumps.App):
    def __init__(self):
        super().__init__(name=APP_NAME, icon="assets/icon.png", template=True, quit_button="Quit")

        self.defaults = NSUserDefaults.standardUserDefaults()
        self.sound_enabled = self._load_sound_pref()

        self.timer_manager = TimerManager(
            interval_minutes=INTERVALS[DEFAULT_INTERVAL_KEY],
            on_interval_reached=self.trigger_notification,
        )

        header = make_gray_header(MENU_HEADER_TEXT)

        interval_menu = rumps.MenuItem(MENU_PLACEHOLDER)
        self.interval_items = {}
        for name in INTERVALS:
            item = rumps.MenuItem(name, callback=self.set_interval)
            item.state = (name == DEFAULT_INTERVAL_KEY)
            self.interval_items[name] = item
            interval_menu.add(item)

        self.sound_item = rumps.MenuItem("Notification Sound", callback=self.toggle_sound)
        self.sound_item.state = self.sound_enabled

        self.menu = [
            header,
            rumps.separator,
            interval_menu,
            self.sound_item,
            rumps.separator,
        ]

        self.rumps_timer = rumps.Timer(self.on_tick, TICK_INTERVAL_SECONDS)
        self.rumps_timer.start()

    def _load_sound_pref(self) -> bool:
        if self.defaults.objectForKey_(SOUND_PREF_KEY) is None:
            return SOUND_ENABLED_DEFAULT
        return bool(self.defaults.boolForKey_(SOUND_PREF_KEY))

    def toggle_sound(self, sender):
        self.sound_enabled = not self.sound_enabled
        sender.state = self.sound_enabled
        self.defaults.setBool_forKey_(self.sound_enabled, SOUND_PREF_KEY)

    def set_interval(self, sender):
        for item in self.interval_items.values():
            item.state = False
        sender.state = True

        minutes = INTERVALS[sender.title]
        self.timer_manager.set_interval(minutes)

    def trigger_notification(self):
        send_break_notification(sound_enabled=self.sound_enabled)

    def on_tick(self, _):
        self.timer_manager.tick(minutes_passed=1)


if __name__ == "__main__":
    BreatherApp().run()