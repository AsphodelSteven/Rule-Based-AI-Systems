# Fief Weather Module: Triple-Cell Collision Simulator
# Created collaboratively with AI for CAP320-O Assignment 2.3

def simulate_weather():
    print("--- DnD 4X Fief Simulator: Weather Module ---")
    print("Simulating a collision between a Moving Front (Cell A) and Local Environment (Cell B).\n")

    try:
        # PART 3 REQUIREMENT: User Input
        print("Configure Cell A (The Incoming Front):")
        temp_a = input("Temperature (Cold, Mild, Hot): ").strip().lower()
        humid_a = input("Humidity (Dry, Damp, Moist): ").strip().lower()

        print("\nConfigure Cell B (The Local Terrain/Environment):")
        temp_b = input("Local Temperature (Cold, Mild, Hot): ").strip().lower()
        elevation_b = input("Elevation (Lowland, Highland, Mountain): ").strip().lower()

        print("\n--- AI Analysis of Collision Zone ---")

        # PART 3 REQUIREMENT: Rule-Based Decision Making (if-elif-else)
        
        # RULE 1: TornadoGenesis (Classic Warm/Cold front collision)
        if (temp_a == "cold" and temp_b == "hot") and humid_a == "moist":
            prediction = "SEVERE ALERT: Tornado formation likely. Warm moist air is being rapidly undercut by the cold front."
            flavor_text = "The sky turns a bruised purple and the wind begins to howl in circles."

        # RULE 2: Orographic Lift & Rain Shadow (The 'Pangaea' Mountain Logic)
        elif elevation_b == "mountain" and humid_a == "moist":
            prediction = "OROGRAPHIC LIFT: Heavy precipitation on the windward side."
            flavor_text = "Clouds snag on the peaks, dumping rain. The leeward side remains a dry rain shadow."

        # RULE 3: Flash Freeze
        elif temp_a == "cold" and temp_b == "mild" and humid_a == "moist":
            prediction = "ICE STORM: Freezing rain detected."
            flavor_text = "Rain freezes on contact with the ground. Roads and paths are treacherous."

        # RULE 4: Dust Storm (Dry/Hot collision)
        elif temp_a == "hot" and temp_b == "hot" and humid_a == "dry":
            prediction = "DUST STORM: High heat and low moisture are kicking up topsoil."
            flavor_text = "Visibility drops to zero as a wall of red sand approaches the fief."

        # RULE 5: Default/Stable Weather
        else:
            prediction = "STABLE: No severe weather fronts detected."
            flavor_text = "The weather remains calm. Ideal for travel or construction."

        # Output the result
        print(f"Status: {prediction}")
        print(f"Atmosphere: {flavor_text}")
        print("\n--- Simulation Complete ---")

    except KeyboardInterrupt:
        print("\nSimulation terminated by user.")

if __name__ == "__main__":
    simulate_weather()