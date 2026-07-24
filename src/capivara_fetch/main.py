import sys

import gi

gi.require_version("Gtk", "4.0")
gi.require_version("Adw", "1")
from gi.repository import Adw, Gio, Gtk  # noqa: E402

from . import const  # noqa: E402
from .window import CapivaraFetchWindow  # noqa: E402


class Application(Adw.Application):
    def __init__(self):
        super().__init__(
            application_id=const.APP_ID,
            flags=Gio.ApplicationFlags.DEFAULT_FLAGS,
        )
        self._add_action("about", self._on_about)
        self._add_action("quit", lambda *_: self.quit(), ["<primary>q"])

    def do_activate(self):
        win = self.props.active_window or CapivaraFetchWindow(application=self)
        win.present()

    def _add_action(self, name, callback, accels=None):
        action = Gio.SimpleAction.new(name, None)
        action.connect("activate", callback)
        self.add_action(action)
        if accels:
            self.set_accels_for_action(f"app.{name}", accels)

    def _on_about(self, *_):
        about = Adw.AboutWindow(
            transient_for=self.props.active_window,
            application_name=const.APP_NAME,
            application_icon=const.APP_ID,
            version=const.VERSION,
            developer_name="CapivaraOS Project",
            website=const.WEBSITE_URL,
            issue_url=const.ISSUE_URL,
            license_type=Gtk.License.GPL_3_0,
            copyright="© 2026 CapivaraOS Project",
        )
        about.present()


def main():
    app = Application()
    return app.run(sys.argv)
