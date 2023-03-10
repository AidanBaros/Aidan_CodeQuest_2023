"""System Module"""
import sys
import math

def better_round(val:float, n_digits:int = 0):
    val *= 10**n_digits
    result = int(val + (0.5 if val >= 0 else -0.5))
    return result / 10**n_digits

def main():

    cases = int(sys.stdin.readline().rstrip())
    for _ in range(cases):
        line = sys.stdin.readline().rstrip()
        diameter, motor_revolutions, power_required, rpm, available_capacity, voltage, distance = (float(val) for val in line.split(" "))

        circumference = math.pi*diameter
        cm_distance = distance*100
        rotations_of_wheel = cm_distance / circumference
        revolutions_of_motor = motor_revolutions * rotations_of_wheel
        time = revolutions_of_motor/rpm
        total_power = revolutions_of_motor * power_required
        amps = total_power / voltage
        ampere = amps * time
        ampere_hours = ampere/60
        if ampere_hours < available_capacity:
            print(f"Success {better_round(time,4):.4f}")
        else:
            print("Fail")





main()