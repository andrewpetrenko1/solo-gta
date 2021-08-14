from process import Process
from time import sleep
PROCESS_NAME = "steam.exe"

def main():
  proc = Process(PROCESS_NAME)
  proc.pauseTime(10)
  sleep(5)

main()
