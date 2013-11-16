import pygtk
pygtk.require('2.0')
import gtk

class TextEntry:

    def close_application(self, widget):
        gtk.main_quit()

    def get_val(self):
        input = self.entry_a.get_text()
        entry_a.set_text("")
        output = self.entry_b.get_text()
        entry_b.set_text("")
        operation = self.entry_c.get_text()
        entry_c.set_text("")
        misc = self.entry_d.get_text()
        entry_d.set_text("")

    def __init__(self):

        # create a new window
        app_window = gtk.Window(gtk.WINDOW_TOPLEVEL)
        app_window.set_resizable(True)
        app_window.set_border_width(10)
        app_window.set_title("COLUMBUS - Discovering Composite Web Services")
        app_window.connect("delete_event", lambda w,x: gtk.main_quit())

	hbox_top = gtk.HBox(False, 0)
        vbox = gtk.VBox(False, 0)
        vbox_a = gtk.VBox(False, 0)
        hbox_top.add(vbox_a)
        label_a = gtk.Label("Enter text1: ")
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
        hbox_top.add(vbox_b)
        label_b = gtk.Label("Enter text2: ")
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
        hbox_top.add(vbox_c)
        label_c = gtk.Label("Enter text3: ")
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
        hbox_top.add(vbox_d)
        label_d = gtk.Label("Enter text4: ")
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
        hbox_top.add(vbox_e)


        self.button_a = gtk.Button("close")
        self.button_a.connect("clicked", self.close_application)
        vbox_e.pack_start(self.button_a, True, True, 0)
        self.button_a.set_flags(gtk.CAN_DEFAULT)
        self.button_a.set_size_request(60,40)
        self.button_a.grab_default()
        self.button_a.show()
        halign=gtk.Alignment(1,0,0,0)
        halign.add(self.button_a)
        vbox_e.pack_start(halign, False, False, 3)
        self.fixed = gtk.Fixed()
        hbox_top.add(self.fixed)
        self.fixed.show()
        self.fixed.put(self.button_a,60,40)


        # Text label
        vbox_f = gtk.VBox(False, 0)
        hbox_top.add(vbox_f)
	self.image = gtk.Image()
 	pixbuf = gtk.gdk.pixbuf_new_from_file("joker.jpg")
  	scaled_buf = pixbuf.scale_simple(250,250,gtk.gdk.INTERP_BILINEAR)
  	self.image.set_from_pixbuf(scaled_buf)
   	self.image.show()
	vbox_f.pack_start(self.image, False, False, 0)


        # Text label
        vbox_g = gtk.VBox(False, 0)
        hbox_top.add(vbox_g)

        self.button_b = gtk.Button("close")
        self.button_b.connect("clicked", self.close_application)
        vbox_g.pack_start(self.button_b, True, True, 0)
        self.button_b.set_size_request(60,40)
        self.button_b.set_flags(gtk.CAN_DEFAULT)
        self.button_b.grab_default()
        self.button_b.show()
        vbox_g.pack_start(self.button_b, False, False, 0)




        vbox_a.pack_start(vbox_b, False, False, 0)
        vbox_a.pack_start(vbox_c, False, False, 0)
        vbox_a.pack_start(vbox_d, False, False, 0)
        vbox_a.pack_start(vbox_e, False, False, 0)
        vbox_a.pack_start(vbox_f, False, False, 0)
        vbox_a.pack_start(vbox_g, False, False, 0)

	hbox_top.pack_start(vbox_a, False, False, 0)

        vbox_a.show()
        vbox_b.show()
        vbox_c.show()
        vbox_d.show()
        vbox_e.show()
        vbox_f.show()
        vbox_g.show()

	hbox_top.show()
        app_window.add(hbox_top)

	color = gtk.gdk.color_parse('#ffffff')
	app_window.modify_bg(gtk.STATE_NORMAL, color)
        app_window.show()

        self.result_label = label_a
        return

def main():
    gtk.main()
    return 0

if __name__ == "__main__":
    TextEntry()
    main()
__author__ = 'ankita'
