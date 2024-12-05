# Online Car Rental Platform

## Project Overview

The Online Car Rental Platform is a Python project that uses Object-Oriented Programming (OOP) concepts to simulate a car rental system. The platform allows customers to view available cars and rent them on an hourly, daily, or weekly basis. Upon returning the cars, the system automatically calculates and generates a bill based on the rental duration and type.

This project demonstrates how to manage car rental processes, including viewing the available cars, renting and returning them, and managing inventory and billing. It utilizes the `datetime` module in Python to handle rental times and calculate bills.

## Features

- **Renting cars**: Customers can rent cars on an hourly, daily, or weekly basis.
- **Car availability**: The system allows customers to check available cars before making a rental request.
- **Billing**: The platform generates a bill based on the rental time (hourly, daily, or weekly).
- **Car return**: Customers can return rented cars, and the system calculates the total bill for the rental period.

## Problem Statement

A car rental company has requested an online platform where customers can:

- View the available inventory of cars.
- Rent cars for hourly, daily, or weekly periods.
- Automatically generate a bill when the car is returned.
- Ensure that the number of requested cars is within the available stock.

## Installation

1. Clone the repository
2. Navigate to the project directory:

   ```cd online-car-rental-platform```

3. Install the required dependencies (if any).
4. Launch the project:

    - Open `car_rental_platform.ipynb` in Jupyter Notebook.
    - Run the cells to interact with the car rental platform.

## Project Structure

The project consists of the following files:

`car_rental.py`: Contains the `CarRental` and `Customer  classes. This file manages car rentals, inventory, and bill calculation.

`car_rental_platform.ipynb`: The main Jupyter Notebook where the car rental platform is executed. It interacts with the `CarRental` and `Customer` classes to run the program and handle user inputs.

## How to Use

### CarRental Class

The `CarRental` class handles the following operations:

- **display_available_cars**: Displays the current inventory of available cars.
- **rent_hourly, rent_daily, rent_weekly**: Rent cars based on the selected rental type.
- **return_car**: Calculates the rental bill based on the time the car was rented and updates the inventory.

### Customer Class

The `Customer` class allows customers to:

- **request_car**: Request cars by specifying the number and rental type.
- **return_car**: Return rented cars and get the total bill.

## Main Flow

1. **Display Available Cars**: Check how many cars are available for rent.
2. **Rent a Car**: Rent cars by specifying the rental type (hourly, daily, weekly).
3. **Return a Car**: Return rented cars and receive the bill based on the rental period.
4. **Exit**: End the program.

## Example Usage

``` bash
Options:
1. Display available cars
2. Rent a car
3. Return a car
4. Exit

Enter choice (1/2/3/4): 1
Available cars: 10

Enter choice (1/2/3/4): 2
Enter number of cars to rent: 2
Enter rental type (hourly/daily/weekly): hourly
Successfully rented 2 cars.

Enter choice (1/2/3/4): 3
Enter number of cars to return: 2
Total bill: $20
```
