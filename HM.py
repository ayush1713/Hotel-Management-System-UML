class Hotel:
    def __init__(self, name, location):
        self.name = name
        self.location = location
        self.rooms = []
        self.employees = []  # Consider using a separate class for users
        self.bookings = []

    def add_room(self, room):
        self.rooms.append(room)

    def remove_room(self, room):
        self.rooms.remove(room)

    # ... other functions like view_rooms, view_employees, etc.

    def add_guest(self, guest):  # New method for adding guests
        # Add logic for guest registration and validation
        self.guests.append(guest)

    def add_account(self, account):  # New method for adding accounts (optional)
        # Add logic for account creation and validation
        self.accounts.append(account)

    def add_booking(self, guest, room, booking):  # Corrected method
        self.bookings.append(booking)

class Guest:
    def __init__(self, name, address, phone_no, id_no, email):
        self.name = name
        self.address = address
        self.phone_no = phone_no
        self.id_no = id_no
        self.email = email

class Account:
    def __init__(self, id, password, account_status):
        self.id = id
        self.password = password
        self.account_status = account_status

class Room:
    def __init__(self, room_no, room_type, room_price, room_status):
        self.room_no = room_no
        self.room_type = room_type
        self.room_price = room_price
        self.room_status = room_status

class RoomBooking:
    def __init__(self, booking_id, start_date, end_date, days_duration, booking_status):
        self.booking_id = booking_id
        self.start_date = start_date
        self.end_date = end_date
        self.days_duration = days_duration
        self.booking_status = booking_status

    def add_payment(self, payment):
        # Function to add a payment to the booking
        pass

class Payment:
    def __init__(self, amount, mode_of_payment, payment_status):
        self.amount = amount
        self.mode_of_payment = mode_of_payment
        self.payment_status = payment_status

hotel = Hotel("Hotel Name", "Abu Dhabi")
hotel.guests = []  # Added a list for guests
hotel.accounts = []  # Added a list for accounts (optional)
guest1 = Guest("Suliman", "123 Main St", "555-1234", "123456789", "johndoe@example.com")
account1 = Account("suliman123", "password123", "active")  # (Optional)
room1 = Room("101", "Deluxe", 200.0, "available")
room_booking1 = RoomBooking("B123", "2024-10-01", "2024-10-05", 5, "confirmed")
payment1 = Payment(1000.0, "credit card", "successful")

# Add room to the hotel
hotel.add_room(room1)

# Add guest (implement logic in add_guest method)
hotel.add_guest(guest1)  # Call the new method

# Add account (optional, implement logic in add_account method)
hotel.add_account(account1)  # Call the new method (if used)

# Create a booking (corrected)
hotel.add_booking(guest1, room1, room_booking1)

# Add payment to the booking
room_booking1.add_payment(payment1)

# View hotel details
print(hotel.name)
print(hotel.location)

# View guest details
print(guest1.name)
print(guest1.address)

# View room details
print(room1.room_no)
print(room1.room_type)

# View booking details
print(room_booking1.booking_id)
print(room_booking1.start_date)

# View payment details
print(payment1.amount)
print(payment1.mode_of_payment)

# Print all objects
print(hotel)
print(guest1)
print(room1)
print(room_booking1)
print(payment1)