
def calculate_score(rpm: int, load: int, temp: int) -> float:
    """
    @file Refactored_code.py
    @brief Functions to calculate and check car health scores based on RPM, load, and temperature.
    @details
    This module provides utilities for evaluating the health of cars using sensor data.
    It includes a scoring function and a batch checker for multiple cars.
    @function calculate_score
        @brief Calculates the health score of a car.
        @param rpm Engine revolutions per minute (int).
        @param load Engine load percentage (int).
        @param temp Engine temperature in Celsius (int).
        @return Health score as a float.
    @function check_cars
        @brief Checks health scores for multiple cars and prints alerts if any are critical.
        @param rpms List of RPM values.
        @param loads List of load values.
        @param temps List of temperature values.
        @return None
    @main
        @brief Example usage of car health scoring and checking.
    """
    """Calculate the health score of a car based on rpm, load, and temperature."""
    return 100 - (rpm / 100 + load * 0.5 + (temp - 90) * 2)


def check_cars(rpms, loads, temps):
    for idx, (r, l, t) in enumerate(zip(rpms, loads, temps), start=1):
        score = calculate_score(r, l, t)
        print(f"Car {idx}: Score = {score:.2f}")
        if score < 40:
            print(" ALERT: Car health is critical!")


if __name__ == "__main__":
    rpm_values = [6500, 3000]
    load_values = [95, 40]
    temp_values = [120, 85]

    check_cars(rpm_values, load_values, temp_values)
