import random, time
print("Waiting to send number...")
while True:
    try:
        file = open("treat.txt", 'r')
        file.close()

    except: 
        time.sleep(1)

    else:
        file = open("treat.txt", "r")
        run = file.readline()
        if run == "run":
            file2 = open("choice.txt", 'w')
            choice = str(random.randint(0,9))
            file2.write(choice)
            file2.close()
            file.close()
            print("\nNumber sent")
            break



