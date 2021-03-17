data = [
    "Andromeda - Shrub",
    "Bellflower - Flower",
    "China Pink - Flower",
    "Daffodil - Flower",
    "Evening Primrose - Flower",
    "French Marigold - Flower",
    "Hydrangea - Shrub",
    "Iris - Flower",
    "Japanese Camellia - Shrub",
    "Lavender - Shrub",
    "Lilac - Shrub",
    "Magnolia - Shrub",
    "Peony - Shrub",
    "Queen Anne's Lace - Flower",
    "Red Hot Poker - Flower",
    "Snapdragon - Flower",
    "Sunflower - Flower",
    "Tiger Lily - Flower",
    "Witch Hazel - Shrub",
]

flowers = []
shrubs = []

# for plant in data:
#     if "Flower" in plant:
#         flowers.append(plant)
#     elif "Shrub" in plant:
#         shrubs.append(plant)
# write your code here
for value in data:
    #print(value.split(" - "))
    if value.split(" - ")[1] == "Flower":
        flowers.append(value.split(" - ")[0])
    elif value.split(" - ")[1] == "Shrub":
        shrubs.append(value.split(" - ")[0])


else:
    print(flowers)
    print(shrubs)