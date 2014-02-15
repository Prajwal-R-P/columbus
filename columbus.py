import pygtk
from lib.plotter import Plot
from lib.subPlotter import SubPlotter
import gtk
import time
class TextEntry:
    def get_SDG(self, widget):
        self.plotter.show()

    def get_sub_graph(self, widget):
        _input = self.entry_a.get_text()
        _output = self.entry_b.get_text()
        description = self.entry_c.get_text()
        #misc = self.entry_d.get_text()
        sub_plotter=SubPlotter(self.plotter,_input,_output)
        sub_plotter.show()

    @staticmethod
    def new_button(name,action):
        button = gtk.Button(name)
        button.connect("clicked", action)
        button.set_size_request(60, 40)
        button.set_flags(gtk.CAN_DEFAULT)
        button.grab_default()
        return button

    @staticmethod
    def new_entry():
        entry_a = gtk.Entry()
        entry_a.set_max_length(80)
        entry_a.set_width_chars(50)
        entry_a.select_region(0, len(entry_a.get_text()))
        style = entry_a.get_style().copy()
        colour = gtk.gdk.color_parse('#9999ff')
        style.bg[gtk.STATE_NORMAL] = colour
        entry_a.set_style(style)
        return entry_a

    def __init__(self):
        self.plotter = Plot()
        self.plotter.load_sdg()

        # create a new window
        app_window = gtk.Window(gtk.WINDOW_TOPLEVEL)
        app_window.set_resizable(True)
        app_window.set_border_width(10)
        app_window.set_title("COLUMBUS - Discovering Composite Web Services")
        app_window.connect("delete_event", lambda w, x: gtk.main_quit())

        vbox_top = gtk.VBox(False, 0)
        vbox_a = gtk.VBox(False, 0)
        vbox_top.add(vbox_a)
        #        app_window.add(vbox_a)
        label_a = gtk.Label("Inputs")

        vbox_a.pack_start(label_a, False, False, 0)


        # Generate text entry box
        self.entry_a = self.new_entry()
        vbox_a.pack_start(self.entry_a, False, False, 0)



        # Text label
        vbox_b = gtk.VBox(False, 0)
        vbox_top.add(vbox_b)
        #        app_window.add(vbox_b)
        label_b = gtk.Label("Outputs")
        vbox_b.pack_start(label_b, False, False, 0)


        # Generate text entry box
        self.entry_b = self.new_entry()
        vbox_b.pack_start(self.entry_b, False, False, 0)

        # Text label
        vbox_c = gtk.VBox(False, 0)
        vbox_top.add(vbox_c)
        label_c = gtk.Label("Description")
        vbox_c.pack_start(label_c, False, False, 0)


        # Generate text entry box
        self.entry_c = self.new_entry()
        vbox_c.pack_start(self.entry_c, False, False, 0)

        ## Text label
        #vbox_d = gtk.VBox(False, 0)
        #vbox_top.add(vbox_d)
        #label_d = gtk.Label("Clusters")
        #vbox_d.pack_start(label_d, False, False, 0)
        #
        #
        ## Generate text entry box
        #self.entry_d = self.new_entry()
        #vbox_d.pack_start(self.entry_d, False, False, 0)

         # next prev
        vbox_f = gtk.VBox(True, 0)
        vbox_top.add(vbox_f)

        hbox_f = gtk.HBox(False,0)
        button_prev = gtk.Button("<< Prev")
        button_next = gtk.Button("Next >>")

        hbox_f.add(button_prev)
        hbox_f.add(button_next)

        halign_f = gtk.Alignment(0.5,0,1,1)
        halign_f.add(hbox_f)

        vbox_f.pack_start(halign_f, False, False, 0)


        # Text label
        vbox_e = gtk.VBox(True, 3)
        vbox_top.add(vbox_e)
        #        app_window.add(vbox_e)

        self.button_a = self.new_button("Get Service Template",self.get_sub_graph)
        halign_a = gtk.Alignment(1, 0, 1, 1)
        halign_a.add(self.button_a)
        vbox_e.pack_start(halign_a, False, False, 3)


        vbox_g = gtk.VBox(True, 0)
        vbox_top.add(vbox_g)
        self.button_b = self.new_button("Get Service Dependency Graph",self.get_SDG)
        #vbox_g.pack_start(self.button_b, True, True, 0)
        halign_b = gtk.Alignment(1, 0, 1, 1)
        halign_b.add(self.button_b)
        vbox_g.pack_start(halign_b, False, False, 3)

        vbox_top.pack_start(vbox_a, False, False, 0)
        app_window.add(vbox_top)


        color = gtk.gdk.color_parse('#ffffff')
        app_window.modify_bg(gtk.STATE_NORMAL, color)
        app_window.show_all()

        return


def main():
    gtk.main()
    return 0


if __name__ == "__main__":
    TextEntry()
    main()
