def calculate_score(rpm: int, load: int, temp: int) -> float:
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
