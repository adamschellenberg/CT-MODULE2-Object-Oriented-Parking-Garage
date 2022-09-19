# CODING TEMPLE - MODULE 2 - BEGINNER PYTHON - OBJECT ORIENTED PARKING GARAGE

# Your assignment for today is to create a parking garage class to get more 
# familiar with Object Oriented Programming(OOP). 

# Your parking garage class should have the following methods:
# - takeTicket
# - This should decrease the amount of tickets available by 1
# - This should decrease the amount of parkingSpaces available by 1
# - payForParking
# - Display an input that waits for an amount from the user and store it in a variable
# - If the payment variable is not empty then (meaning the ticket has been paid) 
#       -> display a message to the user that their ticket has been paid and they have 15mins to leave
# - This should update the "currentTicket" dictionary key "paid" to True
# -leaveGarage
# - If the ticket has been paid, display a message of "Thank You, have a nice day"
# - If the ticket has not been paid, display an input prompt for payment
# - Once paid, display message "Thank you, have a nice day!"
# - Update parkingSpaces list to increase by 1 (meaning add to the parkingSpaces list)
# - Update tickets list to increase by 1 (meaning add to the tickets list)

# You will need a few attributes as well:
# - tickets -> list
# - parkingSpaces -> list
# - currentTicket -> dictionary

class ParkingGarage ():

    def __init__(self, number_of_parking_spaces):
        self.tickets = [x for x in range(1, number_of_parking_spaces)]
        self.parking_spaces = [x for x in range(1, number_of_parking_spaces)]
        self.current_ticket = {}

    def takeTicket (self):
        # decreases amount of tickets available by 1
        # decreases amount of parkingSpaces available by 1
        ticket_taken = self.tickets.pop()
        parking_space_taken = self.parking_spaces.pop()
        self.current_ticket.update({"ticket": ticket_taken, "parking_space": parking_space_taken, 'paid': False})
        print(f'Your ticket number is {ticket_taken}.')
        print("Stick to it, that's very important. Stick to your ticket.")

    def payForParking (self):
        # Display an input that waits for an amount from the user and stores it in a variable
        # If the payment variable is not empty (ticket has been paid) ->
            # display a message to the user that their ticket has been paid and they have 15 mins to leave
        # Update the currentTicket dictionary key "paid" to True
        paid = False
        while not paid:
            response = input('Please enter a non-zero amount to pay for your ticket ')
            if int(response) > 0:
                print('Thank you for paying. You have 15 minutes to run for your life.')
                self.current_ticket.update({'paid': True})
                paid = True

    def leaveGarage (self):
        # If ticket has been paid, display "Thank You, have a nice day"
        # Else, display an input prompt for payment
            # Once paid, display "Thank you, have a nice day!"
        # Update parkingSpaces list to increase by 1 (add to the parkingSpaces list)
        # Update tickets list to increase by 1 (add to the tickets list)
        if self.current_ticket["paid"] == True:
            print("Thank you, have a nice day!")
            self.tickets.append(self.current_ticket['ticket'])
            self.parking_spaces.append(self.current_ticket['parking_space'])
        else:
            self.payForParking()

museum_parking_garage = ParkingGarage(100)

def run ():
    running = True
    while running:
        response = input('What would you like to do? take_ticket/pay_ticket/leave_garage/quit ')
        if response.lower() == 'take_ticket':
            museum_parking_garage.takeTicket()
        if response.lower() == 'pay_ticket':
            museum_parking_garage.payForParking()
        if response.lower() == 'leave_garage':
            museum_parking_garage.leaveGarage()
            break
        if response.lower() == 'quit':
            break

run()
        