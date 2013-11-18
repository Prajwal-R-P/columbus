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
        operation = self.entry_c.get_text()
        misc = self.entry_d.get_text()
        sub_plotter=SubPlotter(self.plotter,_input,_output)
        sub_plotter.show()

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
        label_a.show()
        vbox_a.pack_start(label_a, False, False, 0)


        # Generate text entry box
        self.entry_a = gtk.Entry()
        self.entry_a.set_max_length(80)
        self.entry_a.set_width_chars(50)
        self.entry_a.select_region(0, len(self.entry_a.get_text()))
        style = self.entry_a.get_style().copy()
        colour = gtk.gdk.color_parse('#9999ff')
        style.bg[gtk.STATE_NORMAL] = colour
        self.entry_a.set_style(style)
        self.entry_a.show()
        vbox_a.pack_start(self.entry_a, False, False, 0)



        # Text label
        vbox_b = gtk.VBox(False, 0)
        vbox_top.add(vbox_b)
        #        app_window.add(vbox_b)
        label_b = gtk.Label("Outputs")
        label_b.show()
        vbox_b.pack_start(label_b, False, False, 0)


        # Generate text entry box
        self.entry_b = gtk.Entry()
        self.entry_b.set_max_length(80)
        self.entry_b.set_width_chars(50)
        self.entry_b.select_region(0, len(self.entry_b.get_text()))
        style = self.entry_b.get_style().copy()
        colour = gtk.gdk.color_parse('#9999ff')
        style.bg[gtk.STATE_NORMAL] = colour
        self.entry_b.set_style(style)
        self.entry_b.show()
        vbox_b.pack_start(self.entry_b, False, False, 0)



        # Text label
        vbox_c = gtk.VBox(False, 0)
        vbox_top.add(vbox_c)
        #        app_window.add(vbox_c)
        label_c = gtk.Label("Operations")
        label_c.show()
        vbox_c.pack_start(label_c, False, False, 0)


        # Generate text entry box
        self.entry_c = gtk.Entry()
        self.entry_c.set_max_length(80)
        self.entry_c.set_width_chars(50)
        self.entry_c.select_region(0, len(self.entry_c.get_text()))
        style = self.entry_c.get_style().copy()
        colour = gtk.gdk.color_parse('#9999ff')
        style.bg[gtk.STATE_NORMAL] = colour
        self.entry_c.set_style(style)
        self.entry_c.show()
        vbox_c.pack_start(self.entry_c, False, False, 0)



        # Text label
        vbox_d = gtk.VBox(False, 0)
        vbox_top.add(vbox_d)
        #        app_window.add(vbox_d)
        label_d = gtk.Label("Clusters")
        label_d.show()
        vbox_d.pack_start(label_d, False, False, 0)


        # Generate text entry box
        self.entry_d = gtk.Entry()
        self.entry_d.set_max_length(80)
        self.entry_d.set_width_chars(50)
        self.entry_d.select_region(0, len(self.entry_d.get_text()))
        style = self.entry_d.get_style().copy()
        colour = gtk.gdk.color_parse('#9999ff')
        style.bg[gtk.STATE_NORMAL] = colour
        self.entry_d.set_style(style)
        self.entry_d.show()
        vbox_d.pack_start(self.entry_d, False, False, 0)



        # Text label
        vbox_e = gtk.VBox(True, 3)
        vbox_top.add(vbox_e)
        #        app_window.add(vbox_e)


        self.button_a = gtk.Button("Get Service Template")
        self.button_a.connect("clicked", self.get_sub_graph)
        vbox_e.pack_start(self.button_a, True, True, 0)
        self.button_a.set_size_request(60, 40)
        self.button_a.set_flags(gtk.CAN_DEFAULT)
        self.button_a.grab_default()
        self.button_a.show()
        halign_a = gtk.Alignment(1, 0, 0, 0)
        halign_a.add(self.button_a)
        vbox_e.pack_start(halign_a, False, False, 3)


        # Text label
        #vbox_f = gtk.VBox(False, 0)
        #vbox_top.add(vbox_f)
        #self.image = gtk.Image()
        #pixbuf = gtk.gdk.pixbuf_new_from_file("joker.png")
        #scaled_buf = pixbuf.scale_simple(650, 500, gtk.gdk.INTERP_BILINEAR)
        #self.image.set_from_pixbuf(scaled_buf)
        #self.image.show()
        #vbox_f.pack_start(self.image, False, False, 0)

        vbox_g = gtk.VBox(True, 3)
        vbox_top.add(vbox_g)
        #        app_window.add(vbox_g)


        self.button_b = gtk.Button("Get Service Dependency Graphy")
        self.button_b.connect("clicked", self.get_SDG)
        vbox_g.pack_start(self.button_b, True, True, 0)
        self.button_b.set_size_request(60, 40)
        self.button_b.set_flags(gtk.CAN_DEFAULT)
        self.button_b.grab_default()
        self.button_b.show()
        halign_b = gtk.Alignment(1, 0, 0, 0)
        halign_b.add(self.button_b)
        vbox_g.pack_start(halign_b, False, False, 3)

        vbox_a.pack_start(vbox_b, False, False, 0)
        vbox_a.pack_start(vbox_c, False, False, 0)
        vbox_a.pack_start(vbox_d, False, False, 0)
        vbox_a.pack_start(vbox_e, False, False, 0)
        #vbox_a.pack_start(vbox_f, False, False, 0)
        vbox_a.pack_start(vbox_g, False, False, 0)

        vbox_top.pack_start(vbox_a, False, False, 0)
        app_window.add(vbox_top)

        vbox_a.show()
        vbox_b.show()
        vbox_c.show()
        vbox_d.show()
        vbox_e.show()
        #vbox_f.show()
        vbox_g.show()

        vbox_top.show()

        color = gtk.gdk.color_parse('#ffffff')
        app_window.modify_bg(gtk.STATE_NORMAL, color)
        app_window.show()

        #self.result_label = label_a
        return


def main():
    gtk.main()
    return 0


if __name__ == "__main__":
    TextEntry()
    main()
