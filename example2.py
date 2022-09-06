from datetime import datetime

log_file =  "example2.log"

def read_log(log):
    # Open the logfile and print contents to the terminal
    with open(log, "r") as f:
        print(f.read())

def write_log(log, name):
    # Add a new logfile entry with datstamp

    # Get current date and time
    log_time = str(datetime.now())
    with open(log, "a") as f:
        f.writelines("Entry logged at: {} by {}\n".format(log_time, name))

# Entry point for program
if __name__ == '__main__':
    # Get users name
    name = input("What is your name? ")

    # Add entry to log file
    print("Adding new log entry")
    write_log(log_file, name)
    print("")

    # Access Starting log file
    print("Log file contents")
    print("-----------------")
    read_log(log_file)