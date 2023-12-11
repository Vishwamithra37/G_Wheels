class Booking:
    def __init__(self, booking_id, cab, start_location, end_location, customer_name):
        self.booking_id = booking_id
        self.cab = cab
        self.start_location = start_location
        self.end_location = end_location
        self.customer_name = customer_name

    def cancel_booking(self):
        self.cab.is_available = True
        print(f"Booking with ID {self.booking_id} has been cancelled.")

def display_available_cabs(cabs):
    for cab in cabs:
        if cab.is_available:
            print(f"Cab ID: {cab.cab_id}")

def book_cab(bookings, cabs):
    start_location = input("Enter your pickup location: ")
    end_location = input("Enter your drop location: ")
    customer_name = input("Enter your name: ")

    for cab in cabs:
        if cab.is_available:
            cab.is_available = False
            booking = Booking(len(bookings) + 1, cab, start_location, end_location, customer_name)
            bookings.append(booking)
            print(f"Booking with ID {booking.booking_id} has been successfully made.")
            return

    print("Sorry, all cabs are currently booked.")

def main():
    cabs = [Cab(i, True) for i in range(1, 6)]
    bookings = []

    while True:
        print("\n1. Display available cabs")
        print("2. Book a cab")
        print("3. Cancel a booking")
        print("4. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            display_available_cabs(cabs)
        elif choice == 2:
            book_cab(bookings, cabs)
        elif choice == 3:
            booking_id = int(input("Enter the booking ID you want to cancel: "))
            for booking in bookings:
                if booking.booking_id == booking_id:
                    booking.cancel_booking()
                    break
            else:
                print("No booking found with the provided ID.")
        elif choice == 4:
            break
        else:
            print("Invalid choice, please try again.")


            