volume:int = int(input("please type the volume of your tape"))
match volume:
    case 1:
        print("mute");
    case 2:
        print("very quite");
    case 3:
        print("quite");
    case 4:
        print("moderately quite");
    case 5:
        print("medium");
    case 6:
        print("not loud");
    case 7:
        print("loud");
    case 8:
        print("very loud")
    case 9:
        print("extremely laud")
    case 10:
        print("extremely laud")
    case _:
        #else
        print("Invalid volume.");