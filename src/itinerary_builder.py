def build_itinerary(data):
    """
    Builds an itinerary based on the provided data.

    Args:
        data (list of dict): A list of dictionaries where each dictionary represents 
                             an event in the itinerary. Each dictionary must have a 
                             "type" key with a value of either "flight", "hotel", or 
                             "activity". Depending on the type, other required keys 
                             are:
                             - "flight": "from", "to", "time"
                             - "hotel": "name", "city", "nights"
                             - "activity": "description", "city", "time"

    Returns:
        list of str: A list of strings where each string describes an event in the 
                     itinerary.
    """
    itinerary = []
    for i in range(len(data)):
        if data[i]["type"] == "flight":
            itinerary.append(f"Flight from {data[i]['from']} to {data[i]['to']} at {data[i]['time']}")
        elif data[i]["type"] == "hotel":
            itinerary.append(f"Stay at {data[i]['name']} in {data[i]['city']} for {data[i]['nights']} nights")
        elif data[i]["type"] == "activity":
            itinerary.append(f"Activity: {data[i]['description']} in {data[i]['city']} at {data[i]['time']}")
    return itinerary
