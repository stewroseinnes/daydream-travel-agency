def process_flight(flight):
    """
    Processes a flight event and returns a formatted string.
    
    Args:
        flight (dict): A dictionary containing flight details.
    
    Returns:
        str: A formatted string describing the flight event.
    """
    return f"Flight from {flight['from']} to {flight['to']} at {flight['time']}"

def process_hotel(hotel):
    """
    Processes a hotel event and returns a formatted string.
    
    Args:
        hotel (dict): A dictionary containing hotel details.
    
    Returns:
        str: A formatted string describing the hotel event.
    """
    return f"Stay at {hotel['name']} in {hotel['city']} for {hotel['nights']} nights"

def process_activity(activity):
    """
    Processes an activity event and returns a formatted string.
    
    Args:
        activity (dict): A dictionary containing activity details.
    
    Returns:
        str: A formatted string describing the activity event.
    """
    return f"Activity: {activity['description']} in {activity['city']} at {activity['time']}"

def build_itinerary(data):
    """
    Builds an itinerary based on the provided data.

    Args:
        data (list of dict): A list of dictionaries where each dictionary represents 
                             an event in the itinerary.
                             
    Returns:
        list of str: A list of strings where each string describes an event in the 
                     itinerary.
    """
    itinerary = []
    for event in data:
        if event["type"] == "flight":
            itinerary.append(process_flight(event))
        elif event["type"] == "hotel":
            itinerary.append(process_hotel(event))
        elif event["type"] == "activity":
            itinerary.append(process_activity(event))
        else:
            raise ValueError(f"Unknown event type: {event['type']}")
    return itinerary
