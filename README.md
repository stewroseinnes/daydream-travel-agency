# Daydream Travel Agency - Itinerary Management Tool

## Setup
1. Install Python 3.x
2. Install dependencies: `pip install -r requirements.txt`
3. Run the application: `python src/main.py`

## Features
- Build a travel itinerary from a JSON file.
- Display the itinerary details.

daydream-travel-agency/
│
├── src/
│   ├── itinerary_builder.py    # Legacy script to build itineraries (main focus for refactoring)
│   ├── data_loader.py          # Module for loading itinerary data
│   ├── utils.py                # Utility functions (some redundant functions present)
│   ├── main.py                 # Main entry point to run the application
│
├── data/
│   ├── sample_itinerary.json   # Example itinerary data in JSON format
│
├── README.md                   # Instructions for running the project
├── requirements.txt            # Required libraries (if any)
└── .gitignore                  # Git ignored files