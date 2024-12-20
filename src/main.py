from itinerary_builder import build_itinerary
from data_loader import load_sample_data
from utils import print_itinerary

def main():
    """
    Main function to generate and print a travel itinerary.

    This function performs the following steps:
    1. Loads sample data.
    2. Builds an itinerary based on the loaded data.
    3. Prints the generated itinerary.

    Returns:
        None
    """
    data = load_sample_data()
    itinerary = build_itinerary(data)
    print("Generated Itinerary:")
    print_itinerary(itinerary)

if __name__ == "__main__":
    main()
