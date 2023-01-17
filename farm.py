farms = [{"name": "NE Farm", "agriculture": ["sheep", "cows", "pigs", "chickens", "llamas", "cats"]},
         {"name": "W Farm", "agriculture": ["pigs", "chickens", "llamas"]},
         {"name": "SE Farm", "agriculture": ["chickens", "carrots", "celery"]}]

farm_name = input("Please select one of the following farms: NE Farm, W Farm , or SE Farm")

farm_num = 0;
if(farm_name == "NE Farm"):
    farm_num = 0
elif(farm_name == "W Farm"):
    farm_num = 1
else:
    farm_num = 2

animals = farms[farm_num]["agriculture"]

for animal in animals:
    print(animal)
