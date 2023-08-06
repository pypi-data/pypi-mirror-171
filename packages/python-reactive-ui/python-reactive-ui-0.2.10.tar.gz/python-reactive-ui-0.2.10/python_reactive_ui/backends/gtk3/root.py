from python_reactive_ui import Component
from python_reactive_ui.lib.core import Root

# fmt: off
import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk
# fmt: on


class Gtk3Root(Root):
    def __init__(self, root: Gtk.Container):
        self.root = root
        self.tree = None

    def render(self, component: Component):
        component.mount(self.root.add, self.root.remove)
        self.root.show_all()


def create_root(root):
    return Gtk3Root(root)
