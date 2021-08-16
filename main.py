from process import Process

def main():
  process_name = input("Process name: ")
  proc = Process(process_name)
  print(f"{proc.getInfo()}")
  proc.print_pauseTimeStatus(10)

main()
