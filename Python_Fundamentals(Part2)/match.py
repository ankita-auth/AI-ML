color=input("entre color:")

match color:
    case "Green":
        print("Go")
    case "Yellow":
        print("Wait")
    case "Red":
        print("Stop")
    case _:
        print("Wrong color!")