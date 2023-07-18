import math

# Constants
ROOM_MATERIALS = {
    'wood': 0.02,
    'glass': 0.05,
    'bricks': 0.08,
}

HUMAN_HEARING_THRESHOLD = 140 # in decibels
simulating = True
# Function to calculate sound intensity
def calculate_sound_intensity(power, distance):
    """Takes in the power and distance and returns the sound intensity in Watts per square meter"""
    return power / (4 * math.pi * distance**2)

# Function to calculate sound level in decibels
def calculate_sound_level(intensity):
    """Takes the intensity of the sound in watts per square meter and converts it to Decibels"""
    return 10 * math.log10(intensity / 10**-12)

# Functions to simulate sound penetration
def simulate_sound_penetration_in_room(power, material, distance): #Adewale Usman
    """Takes in the power, material and distance and returns the sound level after attenuation"""
    attenuation = ROOM_MATERIALS[material]
    intensity = calculate_sound_intensity(power, distance)
    attenuated_intensity = intensity * (10**(-attenuation * distance))
    sound_level = calculate_sound_level(attenuated_intensity)
    return sound_level

def simulate_sound_level_outside(power, distance): #Olatunji Goodness
    """Takes in the power and distance and returns the sound level at a particular distance outside the classroom."""
    intensity = calculate_sound_intensity(power, distance)
    sound_level = calculate_sound_level(intensity)
    return sound_level


def main_in_room(): #Oyesiji Titilope
    """Simulates the program if the user is in the classroom"""
    # Input parameters
    lawnmower_power = float(input("Enter lawnmower power in watts: "))
    material = input("Enter the room material (wood, glass, or bricks): ")
    distance = float(input("Enter your distance from the lawnmower in meters: "))

    # Simulate sound penetration
    sound_level = math.ceil(simulate_sound_penetration_in_room(lawnmower_power, material, distance))

    # Check if sound level exceeds hearing threshold or distance threshold
    if sound_level > HUMAN_HEARING_THRESHOLD:
        print(f"The sound level reaching you in the {material} room is {sound_level}db. You are not hearing anything.")
    else:
        print(f"The sound level reaching you in the {material} room is {sound_level}db. You are hearing the noise.")

def main_outside():
    """Simulates the program if the user is outside the classroom"""
    lawnmower_power = float(input("Enter lawnmower power in watts: "))
    distance = float(input("How far are you from the lawnmower in meters: "))

    sound_level = math.ceil(simulate_sound_level_outside(lawnmower_power, distance))

    if sound_level > HUMAN_HEARING_THRESHOLD:
        print(f"The sound level at {distance}m from the lawnmower is {sound_level}db. You are not hearing anything.")
    else:
        print(f"The sound level at {distance}m from the lawnmower is {sound_level}db. You are hearing the noise.")
while simulating:
    position = input("Are you inside or outside the classroom? (in/out)  ").lower()

    if position == "in":
        main_in_room()
    elif position == "out":
        main_outside()
    else:
        print("Please pick a valid option.")
# To check if the user wants to make another simulation
    continue_simulating = input("Do you want to make another simulation? Type 'yes' or 'no'"  ).lower()

    if continue_simulating == "no":
        simulating = False

