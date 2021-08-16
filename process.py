import psutil
from time import sleep

class Process:
  def __init__(self, process_name):
    self.process_name = process_name.lower()
    self.process = self.__getProcess()
  
  def getInfo(self):
    if not self.process:
      return (f"Process {self.process_name} not found")
    
    return (f"{self.process.name}\nStatus: {self.process.status()}")

  def __getPid(self):
    for proc in psutil.process_iter():
      if self.process_name in proc.name().lower():
        return proc.pid

  def __getProcess(self):
    pid = self.__getPid()
    return psutil.Process(pid) if pid != None else None

  def _pause(self):
    while psutil.STATUS_RUNNING:
      self.process.suspend()
      if self.process.status() == psutil.STATUS_STOPPED:
        break

    result = "success" if self.process.status() == psutil.STATUS_STOPPED else "fail"
    return (f"Pause: {result}")

  def _resume(self):
    while psutil.STATUS_STOPPED:
      self.process.resume()
      if self.process.status() == psutil.STATUS_RUNNING:
        break
    
    result = "success" if self.process.status() == psutil.STATUS_RUNNING else "fail"
    return (f"Resume: {result}")

  def _kill(self):
    if not self.process:
      return

    self.process.terminate()

  def print_pauseTimeStatus(self, seconds):
    if not self.process:
      return
    print(self._pause())
    sleep(seconds)
    print(self._resume())
    
  def pauseTime(self, seconds):
    if not self.process:
      return
    self._pause()
    sleep(seconds)
    self._resume()