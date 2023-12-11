import dataclasses


class available_vehicles:
# Vehicles data
   data = {'vehicle_type': ['Bike', 'Scooter', 'Car'],
        'passenger_capacity': [1, 1, 4]}

# Creating a DataFrame from the above dictionary
df = dataclasses.df(dataclasses)
def filter_vehicles_by_type(vehicle_type):
    filtered_vehicle_df = df.loc[[vehicle_type]]
    return filtered_vehicle_df

# Example usage: filter available vehicles by type 'Car'
print(filter_vehicles_by_type('Car'))

# Setting 'vehicle_type' as index
df.set_index('vehicle_type', inplace=True)

def available_vehicles():
    available_vehicle_list = ['Bike', 'Scooter', 'Car']
    available_vehicle_df = df.loc[available_vehicle_list]
    return available_vehicle_df

print(available_vehicles())