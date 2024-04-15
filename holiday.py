def hotel_cost(num_nights):
    # Assuming hotel cost per night is $100
    return num_nights * 100

def plane_cost(city_flight):
    # Assuming flight costs for different cities
    if city_flight == 'London':
        return 500
    elif city_flight == 'New York':
        return 800
    elif city_flight == 'Tokyo':
        return 1000
    else:
        return 0  # Return 0 for unknown cities

def car_rental(rental_days):
    # Assuming daily rental cost is $50
    return rental_days * 50

def holiday_cost(hotel_cost, plane_cost, car_rental):
    return hotel_cost + plane_cost + car_rental

def main():
    city_flight = input("Enter the city you will be flying to (London, New York, Tokyo): ")
    num_nights = int(input("Enter the number of nights you will be staying at a hotel: "))
    rental_days = int(input("Enter the number of days for which you will be hiring a car: "))

    total_hotel_cost = hotel_cost(num_nights)
    total_plane_cost = plane_cost(city_flight)
    total_car_rental_cost = car_rental(rental_days)

    total_cost = holiday_cost(total_hotel_cost, total_plane_cost, total_car_rental_cost)

    print("\nHoliday Details:")
    print(f"City Flight: {city_flight}")
    print(f"Number of Nights: {num_nights}")
    print(f"Number of Rental Days: {rental_days}")
    print(f"Total Hotel Cost: ${total_hotel_cost}")
    print(f"Total Plane Cost: ${total_plane_cost}")
    print(f"Total Car Rental Cost: ${total_car_rental_cost}")
    print(f"Total Holiday Cost: ${total_cost}")

if __name__ == "__main__":
    main()
