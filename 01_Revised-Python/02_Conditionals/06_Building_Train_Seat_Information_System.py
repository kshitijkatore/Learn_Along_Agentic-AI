seat_type =input("Enter seat type (sleeper/AC/general/luxury)").lower()

match seat_type:
    case "sleeper":
        print("Sleeper - NO AC, Beds available")
    case "ac":
        print("AC - Air conditioned, comfy ride.")
    case "general":
        print("General - Cheapest option, no reservation")
    case "luxury":
        print("Luxury - Premium seates with meals.")
    case _:
        print("Invalid seat types")
        
