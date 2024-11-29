def CustomerState(collection):
    states = list(collection.find({}, {"State": 1, "_id": 0}))
    states = [item['State'] for item in states]
    states = set(states)
    return states
def CustomerCity(collection):
    cities = list(collection.find({}, {"City": 1, "_id": 0}))
    cities = [item['City'] for item in cities]
    cities = set(cities)
    return cities