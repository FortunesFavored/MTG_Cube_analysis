import requests, json, pprint

card_info = requests.get(f"https://api.scryfall.com/cards/named?fuzzy=Huntmaster of the Fells // Ravager of the Fells", auth=('user', 'pass')).json()

pprint.pprint(card_info["card_faces"][0])

with open("cube_compiled", "w") as outfile:
    json.dump(card_info, outfile)