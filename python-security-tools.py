def start_setup():
    """
    Initializes monitoring parameters and validates network segments.
    """
    print("=== SECURITY SYSTEM INITIALIZER ===")
    print("Configuring monitoring parameters...\n")

    try:
        # STEP 1: User Input & Type Conversion
        # Use .strip() to remove accidental spaces at the beginning/end
        analyst_name = input("Enter analyst name: ").strip()
        base_ip = input("Enter base IP address: ").strip()
        
        # Numeric inputs with validation
        max_attempts = int(input("Enter maximum login attempts: "))
        risk_multiplier = float(input("Enter risk multiplier (e.g., 1.5): "))

        # STEP 2: Privilege Logic
        # We use .lower() so "Admin", "ADMIN" and "admin" all work
        if analyst_name.lower() == "admin":
            is_privileged = True
        else:
            is_privileged = False

        # STEP 3: Security Calculations
        danger_threshold = max_attempts * risk_multiplier

        # STEP 4: Configuration Summary
        print("\n" + "="*30)
        print(f"Analyst: {analyst_name} (Privileged: {is_privileged})")
        print(f"Calculated Danger Threshold: {danger_threshold}")
        print("="*30)

        print("\n--- NETWORK SEGMENTATION CHECK ---")
        # STEP 5: IP Validation Logic
        if base_ip.startswith("192.168"):
            print(f"IP: {base_ip} -> Result: LOCAL NETWORK")
        elif base_ip.startswith("10.0"):
            print(f"IP: {base_ip} -> Result: CORPORATE NETWORK")
        else:
            print(f"IP: {base_ip} -> Result: EXTERNAL/PUBLIC ADDRESS")

    except EOFError:
        print("\n[!] Error: Input stream interrupted.")
        print("Tip: Run this script in a real Terminal (e.g., VS Code Terminal) to type your answers.")
    except ValueError:
        print("\n[!] Error: Please enter numeric values for attempts and multiplier.")
    except Exception as e:
        print(f"\n[!] An unexpected error occurred: {e}")

if __name__ == "__main__":
    start_setup()