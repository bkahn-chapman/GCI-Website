import tkinter as tk
from acceptURL import acceptURL
# from tkinter import font  as tkfont
# from tkinter import filedialog
class SampleApp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self._frame = None
        self.switch_frame(StartPage)

    def switch_frame(self, frame_class):
        """Destroys current frame and replaces it with a new one."""
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack()

    def resource_path(relative_path):
        if hasattr(sys, '_MEIPASS'):
            return os.path.join(sys._MEIPASS, relative_path)
        return os.path.join(os.path.abspath("."), relative_path)

class StartPage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self, text="Enter a URL").pack(pady=40)
        StartPage.url = tk.Entry(self)
        StartPage.url.pack()
        StartPage.thing = StartPage.url.get();
        tk.Button(self, text="submit", command = lambda : master.switch_frame(PageOne)).pack()

class PageOne(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self, text="Find the 'WebsiteHtml.txt' file for results.").pack(pady=40)
        tk.Button(self, text="try another", command = lambda : master.switch_frame(StartPage)).pack()
        urlGrab = acceptURL(StartPage.url.get())
        urlGrab.parseURL()
        # urlGrab.printHTMLToFile()

if __name__ == "__main__":
    app = SampleApp()
    app.title("Credibility Checker")
    app.geometry("900x600")
    app.mainloop()
