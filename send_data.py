#***** THIS IS A TEST OF SENDING DATA TO TEXT FILE *****#

def send_data():
    file = "trial.txt"
    open(file, "w+")

    f = open(file, "a+")
    for i in range(2):
        f.write("Appended line %d\r\n" % (i + 1))
    f.close()
