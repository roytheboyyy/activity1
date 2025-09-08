def shutdown():
    option = input("Shut down? Y/N: ").upper()
    if option == "Y":
        print("Shutting down...")
    elif option == "N":
        print("Shutdown cancelled.")
    else:
        print("Invalid input")
        shutdown()

shutdown()
