# main.py
#
# Copyright 2020 Dave Patrick
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Gio

class Window(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title='Calculator')
        self.set_border_width(10)

        grid = Gtk.Grid()
        grid.set_row_spacing(5)
        grid.set_column_spacing(5)
        self.add(grid)

        self.expression = ""

        but1 = Gtk.Button(label='1')
        but2 = Gtk.Button(label='2')
        but3 = Gtk.Button(label='3')
        but4 = Gtk.Button(label='4')
        but5 = Gtk.Button(label='5')
        but6 = Gtk.Button(label='6')
        but7 = Gtk.Button(label='7')
        but8 = Gtk.Button(label='8')
        but9 = Gtk.Button(label='9')
        but0 = Gtk.Button(label='0')
        butc = Gtk.Button(label='C')
        butdot = Gtk.Button(label='.')
        butplus = Gtk.Button(label='+')
        butminus = Gtk.Button(label='-')
        buttimes = Gtk.Button(label='*')
        butdivide = Gtk.Button(label='/')
        butpercent = Gtk.Button(label='%')
        butequal = Gtk.Button(label='=')
        butback = Gtk.Button()
        icon = Gio.ThemedIcon(name="edit-clear-symbolic")
        image = Gtk.Image.new_from_gicon(icon, Gtk.IconSize.BUTTON)
        butback.add(image)

        but1.connect("clicked", self.one)
        but2.connect("clicked", self.two)
        but3.connect("clicked", self.three)
        but4.connect("clicked", self.four)
        but5.connect("clicked", self.five)
        but6.connect("clicked", self.six)
        but7.connect("clicked", self.seven)
        but8.connect("clicked", self.eight)
        but9.connect("clicked", self.nine)
        but0.connect("clicked", self.zero)
        butc.connect("clicked", self.clear)
        butdot.connect("clicked", self.dot)
        butplus.connect("clicked", self.addition)
        butminus.connect("clicked", self.subtract)
        buttimes.connect("clicked", self.multiply)
        butdivide.connect("clicked", self.divide)
        butequal.connect("clicked", self.equal)
        butback.connect("clicked", self.backspace)
        butpercent.connect("clicked", self.percent)

        grid.attach(but1, 0, 4, 1, 1)
        grid.attach(but2, 1, 4, 1, 1)
        grid.attach(but3, 2, 4, 1, 1)
        grid.attach(but4, 0, 3, 1, 1)
        grid.attach(but5, 1, 3, 1, 1)
        grid.attach(but6, 2, 3, 1, 1)
        grid.attach(but7, 0, 2, 1, 1)
        grid.attach(but8, 1, 2, 1, 1)
        grid.attach(but9, 2, 2, 1, 1)
        grid.attach(but0, 0, 5, 2, 1)
        grid.attach(butc, 0, 1, 1, 1)
        grid.attach(butdot, 2, 5, 1, 1)
        grid.attach(butplus, 3, 4, 1, 1)
        grid.attach(butminus, 3, 3, 1, 1)
        grid.attach(buttimes, 3, 2, 1, 1)
        grid.attach(butdivide, 3, 1, 1, 1)
        grid.attach(butequal, 3, 5, 1, 1)
        grid.attach(butback, 1, 1, 1, 1)
        grid.attach(butpercent, 2, 1, 1, 1)

        but1.set_hexpand(True)
        but2.set_hexpand(True)
        but3.set_hexpand(True)
        butplus.set_hexpand(True)

        but7.set_vexpand(True)
        but4.set_vexpand(True)
        but1.set_vexpand(True)
        butc.set_vexpand(True)
        butequal.set_vexpand(True)

        box = Gtk.Box()
        box.set_border_width(5)
        grid.attach(box, 0, 0, 4, 1)
        self.result = Gtk.Label()
        self.result.set_label("")
        box.pack_start(self.result, True, True, 0)


    def one(self, widget):
        self.expression += '1'
        self.result.set_label(str(self.expression))


    def two(self, widget):
        self.expression += '2'
        self.result.set_label(str(self.expression))


    def three(self, widget):
        self.expression += '3'
        self.result.set_label(str(self.expression))


    def four(self, widget):
        self.expression += '4'
        self.result.set_label(str(self.expression))


    def five(self, widget):
        self.expression += '5'
        self.result.set_label(str(self.expression))


    def six(self, widget):
        self.expression += '6'
        self.result.set_label(str(self.expression))


    def seven(self, widget):
        self.expression += '7'
        self.result.set_label(str(self.expression))


    def eight(self, widget):
        self.expression += '8'
        self.result.set_label(str(self.expression))


    def nine(self, widget):
        self.expression += '9'
        self.result.set_label(str(self.expression))


    def zero(self, widget):
        self.expression += '0'
        self.result.set_label(str(self.expression))


    def dot(self, widget):
        self.expression += '.'
        self.result.set_label(str(self.expression))


    def addition(self, widget):
        self.expression += '+'
        self.result.set_label(str(self.expression))


    def subtract(self, widget):
        self.expression += '-'
        self.result.set_label(str(self.expression))


    def multiply(self, widget):
        self.expression += '*'
        self.result.set_label(str(self.expression))

    def divide(self, widget):
        self.expression += '/'
        self.result.set_label(str(self.expression))


    def percent(self, widget):
        self.expression += '*0.01'
        self.percentequaled = ""
        if self.expression != "":
            try:
                self.percentequaled = eval(self.expression)
                self.expression = str(self.percentequaled)
                self.result.set_label(str(self.percentequaled))
            except:
                self.expression = ""

    def backspace(self, widget):
        self.expression = self.expression[:-1]
        self.result.set_label(str(self.expression))

    def clear(self, widget):
        self.expression = ""
        self.result.set_label(str(self.expression))


    def equal(self, widget):
        self.equaled = ""
        if self.expression != "":
            try:
                self.equaled = eval(self.expression)
                self.expression = str(self.equaled)
            except:
                self.equaled = "ERROR"
                self.expression = ""
        self.result.set_label(str(self.equaled))


window = Window()
window.connect("delete-event", Gtk.main_quit)
window.show_all()
Gtk.main()
