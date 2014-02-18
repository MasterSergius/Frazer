#-*- coding: utf-8 -*-
import os
import sys
import time
import ConfigParser
from Tkinter import *

class TkinterMessage():
    def __init__(self):
        self._get_config()
        self.phrase_window = Tk()
        self.frame = Frame(self.phrase_window)
        self.phrase_label = Label(self.frame)

    def _get_config(self):
        self.config = ConfigParser.ConfigParser()
        self.config.read(os.path.join(os.environ['PRODROOT'],'etc/message.cfg'))
        self.font = self.config.get('text','font')
        self.font_size = int(self.config.get('text', 'font_size'))
        self.font_color = self.config.get('text', 'font_color')
        self.background_color = self.config.get('text', 'background_color')
        self.text_margin = int(self.config.get('text','margin'))
        self.window_position_x = self.config.get('window', 'position_x')
        self.window_position_y = self.config.get('window', 'position_y')
        self.window_margin_x = int(self.config.get('window', 'margin_x'))
        self.window_margin_y = int(self.config.get('window', 'margin_y'))
        self.window_max_width = int(self.config.get('window', 'max_width'))
        self.window_border_width = int(self.config.get('window', 'border_width'))
        self.window_border_color = self.config.get('window', 'border_color')
        self.window_delay_displaying = int(self.config.get('window', 'delay_displaying'))

    def show_message(self, phrase):
        self.frame.config(bd=self.window_border_width, bg=self.window_border_color)
        self.frame.pack()
        self.phrase_label.config(text=phrase,
                                 font=(self.font, self.font_size),
                                 bg=self.background_color, fg=self.font_color,
                                 wraplength=self.window_max_width, justify=LEFT,
                                 padx=self.text_margin, pady=self.text_margin)
        self.phrase_label.pack()
        window_width = self.phrase_label.winfo_reqwidth()
        window_height = self.phrase_label.winfo_reqheight()
        if self.window_position_x == 'LEFT':
            window_x = self.window_margin_x
        else:
            window_x = self.phrase_window.winfo_screenwidth() - window_width - self.window_margin_x
        if self.window_position_y == 'TOP':
            window_y = self.window_margin_y
        else:
            window_y = self.phrase_window.winfo_screenheight() - window_height - self.window_margin_y
        self.phrase_window.geometry('%dx%d+%d+%d' % (window_width, window_height, window_x, window_y))
        self.phrase_window.overrideredirect(True)
        self.phrase_window.after(self.window_delay_displaying, lambda: self.phrase_window.destroy())
        self.phrase_window.mainloop()

if __name__ == '__main__':
    msg = sys.argv[1]
    Tmsg = TkinterMessage()
    Tmsg.show_message(msg)
