import riak

client = riak.RiakClient(pb_port=8087, protocol='pbc')

bucket = myClient.bucket('s16852')

key = "car1"

create_car(key)
get_car(key)
modify_car(key)
get_car(key)
delete_car(key)
get_car(key)

def create_car(key):
    val = {"manufacturer": "VV", "model": "Golf", "horsePower": 115, "imported": true }
    car = bucket.new(key, data=val)
    car.store()
    print("Car created.")

def get_car(key):
    car = bucket.get(key)
    print("Car: " + str(car.data) + ".")

def modify_car(key):
    car = bucket.get(key)
    car.data["horsePower"] = 145
    car.store()
    print("Car modified.")

def delete_car(key):
    car = bucket.get(key)
    car.delete()
    print("Car deleted.")
