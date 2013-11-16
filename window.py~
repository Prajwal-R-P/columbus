import pygtk
pygtk.require('2.0')
import gtk

class TextEntry:

    def close_application(self, widget):
        gtk.main_quit()

    def __init__(self):

        # create a new window
        app_window = gtk.Window(gtk.WINDOW_TOPLEVEL)
        app_window.set_resizable(True)
        app_window.set_border_width(10)
        app_window.set_title("COLUMBUS - Discovering Composite Web Services")
        app_window.connect("delete_event", lambda w,x: gtk.main_quit())

	hbox_top = gtk.HBox(False, 0)
        vbox_a = gtk.VBox(False, 0)
        app_window.add(vbox_a)
        label_a = gtk.Label("Enter text1: ")
        label_a.show()
        vbox_a.pack_start(label_a, False, False, 0)
      

        # Generate text entry box
        entry_a = gtk.Entry()
        entry_a.set_max_length(80)
        entry_a.set_width_chars(50)
        entry_a.select_region(0, len(entry_a.get_text()))
	style = entry_a.get_style().copy()
	colour = gtk.gdk.color_parse('#9999ff')
	style.bg[gtk.STATE_NORMAL] = colour
	entry_a.set_style(style)
        entry_a.show()
        vbox_a.pack_start(entry_a, False, False, 0)



        # Text label
        vbox_b = gtk.VBox(False, 0)
        app_window.add(vbox_b)
        label_b = gtk.Label("Enter text2: ")
        label_b.show()
        vbox_b.pack_start(label_b, False, False, 0)


        # Generate text entry box
        entry_b = gtk.Entry()
        entry_b.set_max_length(80)
        entry_b.set_width_chars(50)
        entry_b.select_region(0, len(entry_b.get_text()))
	style = entry_b.get_style().copy()
	colour = gtk.gdk.color_parse('#9999ff')
	style.bg[gtk.STATE_NORMAL] = colour
	entry_b.set_style(style)
        entry_b.show()
        vbox_b.pack_start(entry_b, False, False, 0)



        # Text label
        vbox_c = gtk.VBox(False, 0)
        app_window.add(vbox_c)
        label_c = gtk.Label("Enter text3: ")
        label_c.show()
        vbox_c.pack_start(label_c, False, False, 0)


        # Generate text entry box
        entry_c = gtk.Entry()
        entry_c.set_max_length(80)
        entry_c.set_width_chars(50)
        entry_c.select_region(0, len(entry_c.get_text()))
	style = entry_c.get_style().copy()
	colour = gtk.gdk.color_parse('#9999ff')
	style.bg[gtk.STATE_NORMAL] = colour
	entry_c.set_style(style)
        entry_c.show()
        vbox_c.pack_start(entry_c, False, False, 0)



        # Text label
        vbox_d = gtk.VBox(False, 0)
        app_window.add(vbox_d)
        label_d = gtk.Label("Enter text4: ")
        label_d.show()
        vbox_d.pack_start(label_d, False, False, 0)


        # Generate text entry box
        entry_d = gtk.Entry()
        entry_d.set_max_length(80)
        entry_d.set_width_chars(50)
        entry_d.select_region(0, len(entry_d.get_text()))
	style = entry_d.get_style().copy()
	colour = gtk.gdk.color_parse('#9999ff')
	style.bg[gtk.STATE_NORMAL] = colour
	entry_d.set_style(style)
        entry_d.show()
        vbox_d.pack_start(entry_d, False, False, 0)



        # Text label
        vbox_e = gtk.VBox(True, 3)
        app_window.add(vbox_e)


        button_a = gtk.Button("close")
        button_a.connect("clicked", self.close_application)
        vbox_e.pack_start(button_a, True, True, 0)
        button_a.set_flags(gtk.CAN_DEFAULT)
        button_a.set_size_request(60,40)
        button_a.grab_default()
        button_a.show()
        halign=gtk.Alignment(1,0,0,0)
        halign.add(button_a)
        vbox_e.pack_start(halign, False, False, 3)
        self.fixed = gtk.Fixed()
        app_window.add(self.fixed)
        self.fixed.show()
        self.fixed.put(button_a,60,40)


        # Text label
        vbox_f = gtk.VBox(False, 0)
        app_window.add(vbox_f)
	image = gtk.Image()
 	pixbuf = gtk.gdk.pixbuf_new_from_file("joker.jpg")
  	scaled_buf = pixbuf.scale_simple(250,250,gtk.gdk.INTERP_BILINEAR)
  	image.set_from_pixbuf(scaled_buf)
   	image.show()
	vbox_f.pack_start(image, False, False, 0)


        # Text label
        vbox_g = gtk.VBox(False, 0)
        app_window.add(vbox_g)

        button_b = gtk.Button("close")
        button_b.connect("clicked", self.close_application)
        vbox_g.pack_start(button_b, True, True, 0)
        button_b.set_size_request(60,40)
        button_b.set_flags(gtk.CAN_DEFAULT)
        button_b.grab_default()
        button_b.show()
        vbox_g.pack_start(button_b, False, False, 0)




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