import os

def main() -> None:
    if os.path.exists("/tmp/fifo"):
        file = open("/tmp/fifo", "r")
        for line in file:
            print(line)
    else:
        print("Error reading the pipe!")

if __name__=="__main__":
    main()