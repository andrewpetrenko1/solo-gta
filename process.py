import psutil
from time import sleep

class Process:
  def __init__(self, process_name):
    self.process_name = process_name.lower()
    self.process = self.__getProcess()
    self.__printInfo()
  
  def __printInfo(self):
    if not self.process:
      print(f"Process {self.process_name} not found")
      return
    
    print(f"{self.process.name}\nStatus: {self.process.status()}")

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
    print(f"Pause: {result}")

  def _resume(self):
    while psutil.STATUS_STOPPED:
      self.process.resume()
      if self.process.status() == psutil.STATUS_RUNNING:
        break
    
    result = "success" if self.process.status() == psutil.STATUS_RUNNING else "fail"
    print(f"Resume: {result}")

  def _kill(self):
    if not self.process:
      return

    self.process.terminate()

  def pauseTime(self, seconds):
    if not self.process:
      return
    self._pause()
    sleep(seconds)
    self._resume()