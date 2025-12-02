import sys


# --- Easy Physics Formula Functions ---

def distance_speed_time():
    # Formula: d = s * t (Distance)
    print("\n--- Formula: d = s * t (Distance) ---")
    s = float(input("Enter Speed (s): "))
    t = float(input("Enter Time (t): "))
    d = s * t
    print(f"\n✨ Result: Distance (d) = **{d:.2f}**")


def work_force_distance():
    # Formula: W = F * d (Work)
    print("\n--- Formula: W = F * d (Work) ---")
    F = float(input("Enter Force (F): "))
    d = float(input("Enter Distance (d): "))
    W = F * d
    print(f"\n✨ Result: Work (W) = **{W:.2f}**")


def power_work_time():
    # Formula: P = W / t (Power)
    print("\n--- Formula: P = W / t (Power) ---")
    W = float(input("Enter Work (W): "))
    t = float(input("Enter Time (t): "))
    if t == 0:
        print("\n🛑 Error: Time (t) cannot be zero!")
        return
    P = W / t
    print(f"\n✨ Result: Power (P) = **{P:.2f}**")


def density_mass_volume():
    # Formula: ρ = m / V (Density)
    print("\n--- Formula: ρ = m / V (Density) ---")
    m = float(input("Enter Mass (m): "))
    V = float(input("Enter Volume (V): "))
    if V == 0:
        print("\n🛑 Error: Volume (V) cannot be zero!")
        return
    rho = m / V
    print(f"\n✨ Result: Density (ρ) = **{rho:.2f}**")


def pressure_force_area():
    # Formula: P = F / A (Pressure)
    print("\n--- Formula: P = F / A (Pressure) ---")
    F = float(input("Enter Force (F): "))
    A = float(input("Enter Area (A): "))
    if A == 0:
        print("\n🛑 Error: Area (A) cannot be zero!")
        return
    P = F / A
    print(f"\n✨ Result: Pressure (P) = **{P:.2f}**")


# --- Main Program Logic (One Execution) ---

def run_calculator_once():
    """Runs the calculator, executes one function, and then exits."""

    options = {
        '1': ("Distance (d = s * t)", distance_speed_time),
        '2': ("Work (W = F * d)", work_force_distance),
        '3': ("Power (P = W / t)", power_work_time),
        '4': ("Density (ρ = m / V)", density_mass_volume),
        '5': ("Pressure (P = F / A)", pressure_force_area)
    }

    print("\n--- 🧠 Easy Physics Formulas ---")
    for key, (name, _) in options.items():
        print(f"[{key}] {name}")

    choice = input("Select a number (1-5): ").strip()

    if choice in options:
        try:
            # Execute the function associated with the choice
            options[choice][1]()
        except ValueError:
            print("\n❌ Invalid input. Please enter only numerical values.")
    else:
        print("\n❌ Invalid selection. Program ending.")


if __name__ == "__main__":
    run_calculator_once()
    sys.exit()