try:
    command = ""
    race_started = False
    while True:
        command = input(">>>").lower()
        if(command == 'help'):
            print("""
                start - To start the race
                stop - To stop the race
                quit - To end the race.
                """)
        elif(command == "start"):
            if race_started:
                print("race already begun")
            else:
                race_started = True
                print("race has begun!")
        elif(command == "stop"):
            if not race_started:
                print("car already stopped.")
            else:
                race_started = False
                print("car has stopped.")
        elif(command == "quit"):
            print("race ended")
            break
        else:
            print
except Exception as Error:
    print(Error)