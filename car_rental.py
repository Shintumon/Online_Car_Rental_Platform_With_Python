from datetime import datetime, timedelta

class CarRental:
    def __init__(self, inventory):
        self.inventory = inventory

    def display_available_cars(self):
        print(f"Available cars: {self.inventory}")

    def rent_hourly(self, num_cars):
        return self.rent_car(num_cars, "hourly")

    def rent_daily(self, num_cars):
        return self.rent_car(num_cars, "daily")

    def rent_weekly(self, num_cars):
        return self.rent_car(num_cars, "weekly")

    def rent_car(self, num_cars, rental_type):
        if num_cars > self.inventory:
            print("Not enough cars available.")
            return None

        current_time = datetime.now()
        rental_details = {
            'rental_type': rental_type,
            'rental_period': num_cars,
            'rental_start_time': current_time
        }

        self.inventory -= num_cars
        return rental_details

    def return_car(self, rental_details):
        rental_end_time = datetime.now()
        rental_period = rental_details['rental_period']
        rental_type = rental_details['rental_type']
        rental_start_time = rental_details['rental_start_time']

        # Calculate elapsed time
        elapsed_time = rental_end_time - rental_start_time

        if rental_type == "hourly":
            bill = rental_period * 10  # Example hourly rate
        elif rental_type == "daily":
            bill = rental_period * 50  # Example daily rate
        elif rental_type == "weekly":
            bill = rental_period * 200  # Example weekly rate
        else:
            bill = 0

        # Generate detailed bill
        print(f"Number of cars returned: {rental_period}")
        print(f"Elapsed time: {elapsed_time}")
        print(f"Total bill: ${bill}")

        # Update inventory
        self.inventory += rental_period

        return bill

 
class Customer:
    def request_car(self, car_rental, num_cars, rental_type):
        if rental_type == "hourly":
            return car_rental.rent_hourly(num_cars)
        elif rental_type == "daily":
            return car_rental.rent_daily(num_cars)
        elif rental_type == "weekly":
            return car_rental.rent_weekly(num_cars)
        else:
            print("Invalid rental type.")
            return None

    def return_car(self, car_rental, rental_details):
        bill = car_rental.return_car(rental_details)
        print(f"Total bill: ${bill}")

