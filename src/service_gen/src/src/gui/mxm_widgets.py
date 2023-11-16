from tkinter import (
    Button,
    Entry,
    Label,
    Frame,
    DISABLED,
    filedialog,
    ACTIVE,
    NORMAL,
    StringVar,
    Toplevel,
)
from tkinter.tix import Balloon

from src.common.look_and_feel import *


def on_enter(e):
    e.widget["background"] = MXM_GREEN_LIGHT


def on_leave(e):
    e.widget["background"] = MXM_GREEN


def on_clc(e):
    e.widget.master.focus()


class MXMButton(Button):
    def __init__(self, master, text, command):
        Button.__init__(
            self,
            master,
            text=text,
            command=command,
            font=MXM_FONT,
            height=1,
            relief="flat",
            activebackground=MXM_GREEN_LIGHT,
        )
        self.bind("<Enter>", on_enter)
        self.bind("<Leave>", on_leave)


class MXMEntry(Entry):
    def __init__(self, master, textvariable, width, state, tooltip=None):
        Entry.__init__(
            self,
            master,
            textvariable=textvariable,
            highlightthickness=1,
            width=width,
            state=state,
        )
        CreateToolTip(self, tooltip)
        self.bind("<Return>", on_clc)


class MXMLabel(Label):
    def __init__(self, master, text, width):
        Label.__init__(
            self,
            master,
            text=text,
            font=MXM_FONT,
            background="#FFFFFF",
            width=width,
            anchor="w",
        )


class MXMLabeledEntry(Frame):
    def __init__(self, master=None, tooltip=None, browse_name="---"):
        Frame.__init__(self, master, background="#FFFFFF")
        self.relative_path = StringVar(value="enter relative path for .h")
        self.user_name = MXMLabel(self, text=browse_name, width=18)
        self.user_name.grid(row=1, column=0, sticky="W")
        self.user_entry = MXMEntry(
            self,
            textvariable=self.relative_path,
            width=50,
            state=NORMAL,
            tooltip=tooltip,
        )
        self.user_entry.grid(row=1, column=1, ipady=2, padx=15, sticky="W")


class MXMBrowseWidget(Frame):
    DIR_BROWSE = "askdirectory"
    FILE_BROWSE = "askopenfilename"

    def __init__(
        self, master=None, tooltip=None, browse_name="---", browse_type=DIR_BROWSE
    ):
        Frame.__init__(self, master, background="#FFFFFF")
        self.folder_path = StringVar()
        self.browse_type = browse_type
        self.user_name = MXMLabel(self, text=browse_name, width=18)
        self.user_name.grid(row=1, column=0, sticky="W")
        self.user_entry = MXMEntry(
            self,
            textvariable=self.folder_path,
            width=50,
            state=DISABLED,
            tooltip=tooltip,
        )
        self.user_entry.grid(row=1, column=1, ipady=2, padx=15, sticky="W")
        self.browse_button = MXMButton(
            self, text="Browse", command=self.__folder_path_callback
        )
        self.browse_button.grid(row=1, column=2)

    def __folder_path_callback(self):
        if self.browse_type == MXMBrowseWidget.DIR_BROWSE:
            folder_selected = filedialog.askdirectory()
        else:
            folder_selected = filedialog.askopenfilename()
        self.folder_path.set(folder_selected)

    def get_selected_path(self):
        return self.folder_path.get()


class CreateToolTip(object):
    """
    create a tooltip for a given widget
    """

    def __init__(self, widget, text="widget info"):
        self.waittime = 500  # miliseconds
        self.wraplength = 250  # pixels
        self.widget = widget
        self.text = text
        self.widget.bind("<Enter>", self.enter)
        self.widget.bind("<Leave>", self.leave)
        self.widget.bind("<ButtonPress>", self.leave)
        self.id = None
        self.tw = None

    def enter(self, event=None):
        self.schedule()

    def leave(self, event=None):
        self.unschedule()
        self.hidetip()

    def schedule(self):
        self.unschedule()
        self.id = self.widget.after(self.waittime, self.showtip)

    def unschedule(self):
        id = self.id
        self.id = None
        if id:
            self.widget.after_cancel(id)

    def showtip(self, event=None):
        x = y = 0
        x, y, cx, cy = self.widget.bbox("insert")
        x += self.widget.winfo_rootx() + 25
        y += self.widget.winfo_rooty() + 20
        # creates a toplevel window
        self.tw = Toplevel(self.widget)
        # Leaves only the label and removes the app window
        self.tw.wm_overrideredirect(True)
        self.tw.wm_geometry("+%d+%d" % (x, y))
        label = Label(
            self.tw,
            text=self.text,
            justify="left",
            background="#ffffff",
            relief="solid",
            borderwidth=1,
            wraplength=self.wraplength,
        )
        label.pack(ipadx=1)

    def hidetip(self):
        tw = self.tw
        self.tw = None
        if tw:
            tw.destroy()
