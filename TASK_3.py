# Movie Theatre Seat Booking 

total_seats = int(input())
n = int(input())

remaining_seats = total_seats

for i in range(n):
    person, seats = map(int, input().split())
    if seats <= remaining_seats:
        print("Accepted")
        remaining_seats -= seats
    else:
        print("Rejected")
