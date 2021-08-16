import threading
from process import Process
from tkinter import *
from threading import Thread
import keyboard

class GUIProcess(Process):
  def __init__(self, process_name, tk_root):
    super().__init__(process_name)
    self.root = tk_root
    self.infoVar = StringVar()
    self.var_process_name = StringVar(self.root, self.process_name)
    self.initElements()

  def __pause_resume(self):
    th1 = Thread(target=self.pauseTime, args=(10,))
    th1.start()

  def pauseTime(self, seconds):
    if not self.process:
      return
    self._pause()
    self.set_info()
    threading.Event().wait(seconds)
    self._resume()
    self.set_info()

  def kill_process(self):
    self._kill()
    self.process = None
    self.set_info()

  def set_new_name(self):
    super().__init__(self.var_process_name.get())
    self.set_info()

  def initElements(self):
    self.set_info()
    Label(self.root, 
    textvariable = self.infoVar,
    font="Arial 10"
    ).grid(row=0, columnspan=3,sticky=W+E, pady=10)
    
    Button(text="Stop and resume", command= self.__pause_resume).grid(row=1, column=0, sticky=W, padx=10, pady=5)
    Button(text="Kill", command= self.kill_process).grid(row=2, column=0, sticky=W, padx=10, pady=5)

    Entry(self.root, textvariable=self.var_process_name).grid(row=1, column=2, sticky=E, padx=10, pady=5)

    self.__callback()

  def set_info(self):
    if not self.process:
      self.infoVar.set(f"Process: {self.process_name} not found")
      return

    self.infoVar.set(f"Process: {self.process.name()}\nPid: {self.process.pid}\nStatus: {self.process.status()}")

  def __callback(self):
    self.set_new_name()
    self.root.after(2000, self.__callback)


def main():
  root = Tk()
  root.title("Process operator")
  pr = GUIProcess("gta5.exe", root)
  keyboard.add_hotkey("shift+alt+k", pr.kill_process)
  keyboard.add_hotkey("shift+alt+plus", lambda: pr.pauseTime(10))
  root.mainloop()
  

main()
