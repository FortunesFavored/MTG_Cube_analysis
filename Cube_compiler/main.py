import pandas as pd
import requests
import time
import re
import json

cube_info = pd.read_csv("TCGplayer.csv")

cube_compiled = {}

for i in cube_info["Name"]:
    # print(i)
    i = re.sub("\(([\w\s]+)\)" , "", i)
    print(i)
    time.sleep(0.005)
    api_call = False
    try:
        card_info = requests.get(f"https://api.scryfall.com/cards/named?fuzzy={i}", auth=('user', 'pass')).json()
        api_call = True
    except:
        ...  
    if api_call == True:
        try:
            cube_compiled[card_info["name"]]={
                "mana_cost":card_info.get("mana_cost"),
                "cmc":card_info.get("cmc"),
                "type":card_info.get("type_line"),
                "keywords":card_info.get("keywords"),
                "colors":card_info.get("colors"),
                "rarity":card_info.get("rarity"),
                "oracle_text":card_info.get("oracle_text"),
                "image_link_normal":card_info.get("image_uris").get("normal"),
                "promo":card_info.get("promo"),
                "reprint":card_info.get("reprint"),
                "artist":card_info.get("artist"),
                "flavor_text":card_info.get("flavor_text"),
            }
        except:
            try:
                cube_compiled[card_info["card_faces"][0]["name"]]={
                    "mana_cost":card_info["card_faces"][0].get("mana_cost"),
                    "cmc":card_info.get("cmc"),
                    "type":card_info["card_faces"][0].get("type_line"),
                    "keywords":card_info.get("keywords"),
                    "colors":card_info["card_faces"][0].get("colors"),
                    "rarity":card_info.get("rarity"),
                    "oracle_text":card_info["card_faces"][0].get("oracle_text"),
                    "image_link_normal":card_info["card_faces"][0].get("image_uris").get("normal"),
                    "promo":card_info["card_faces"][0].get("promo"),
                    "reprint":card_info["card_faces"][0].get("reprint"),
                    "artist":card_info["card_faces"][0].get("artist"),
                    "flavor_text":card_info["card_faces"][0].get("flavor_text"),
                    "Transform":card_info["card_faces"][1]["name"],
                }
                cube_compiled[card_info["card_faces"][1]["name"]]={
                    "mana_cost":card_info["card_faces"][1].get("mana_cost"),
                    "cmc":card_info["card_faces"][1].get("cmc"),
                    "type":card_info["card_faces"][1].get("type_line"),
                    "keywords":card_info.get("keywords"),
                    "colors":card_info["card_faces"][1].get("colors"),
                    "rarity":card_info.get("rarity"),
                    "oracle_text":card_info["card_faces"][1].get("oracle_text"),
                    "image_link_normal":card_info["card_faces"][1].get("image_uris").get("normal"),
                    "promo":card_info["card_faces"][1].get("promo"),
                    "reprint":card_info["card_faces"][1].get("reprint"),
                    "artist":card_info["card_faces"][1].get("artist"),
                    "flavor_text":card_info["card_faces"][1].get("flavor_text"),
                    "Transform":card_info["card_faces"][0]["name"],
                }
            except:
                print("\n")
                print(card_info["name"])
        ...

with open("cube_compiled", "w") as outfile:
    json.dump(cube_compiled, outfile)