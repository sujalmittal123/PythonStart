# You're building a ticket info system for a railway app. Based on seat type, show its features.
# Task:
# Input:
# "sleeper"
# 1
# 1
# "AC"
# "general",
# "luxury"
# Match using match-case
# Unknown → show: "Invalid seat type"

seat_type =input("enter the seat type(sleeper,ac,general,luxury):").lower()

match seat_type:
    case "sleeper":
        print("Sleeper: Non-AC, 3-tier, affordable")
    case "ac":
        print("AC: Air-conditioned, 3-tier/2-tier, comfortable")
    case "general":
            print("General: Non-AC, unreserved, budget-friendly")
    case "luxury":
            print("Luxury: Air-conditioned, spacious, premium")