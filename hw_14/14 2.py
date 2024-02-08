import json


def make_json_file(path, file) -> str:
    """ამ ფუნქციით ვქმნით ახალ JSON ფაილს"""
    file_path = f"{path}/{file}.json"

    try:
        with open(file_path, mode="x", encoding="utf-8"):
            pass
        # file = open(file_path, mode='x', encoding='utf-8')
        # file.close()
    except FileExistsError as ex:
        print(f'Faili arsebobs: "{file_path}"')
        print("Gaagrdzele mushaoba...\n")

    return file_path


def write_content_json(path, json_data):
    """JSON ფაილში მონაცემების შეტანა, მიუთითეთ ფაილის მისამართი და შესატანი JSON მონაცემები"""
    with open(path, mode="w", encoding="utf-8") as file:
        file.write(json.dumps(json_data))


def read_json_file(path):
    """მიანიჭეთ სანახავი JSON ფაილის მისამართი"""
    with open(path, mode="r", encoding="utf-8") as fin:
        return json.loads(fin.read())


def edit_content(path, id, key_to_edit, new_value):
    """JSON ფაილში მონაცემების რედაქტირებისათვის მიუთითეთ: ფაილის მისამართი, ID თუ რომელ ჩანაწერშია ცვლილება გასაკეთებელი, KEY სადაცაა ცვლილება განსახორციელებელი, ჩაწერეთ ახალი მნიშვნელობა"""
    with open(path, mode="r", encoding="utf-8") as file:
        data = json.load(file)

    for item in data:
        if item["id"] == id:
            item[key_to_edit] = new_value
        # else:
        #     print(f'Key {key_to_edit} ver moidzebna failshi')

    with open(path, mode="w", encoding="utf-8") as file:
        file.write(json.dumps(data))
        print(f"Monacemebi ID: {id} Key {key_to_edit} warmatebit ganakhlda")


def update_json_file(path, new_data):
    """JSON ფაილში ჩანაწერების დასამატებლად მიუთითეთ ფაილის მისამართი, list-ში კი დასამატებელი JSON მონაცემები"""
    players_list = read_json_file(path)

    for item in new_data:
        players_list.append(item)
        # print(item)

    with open(path, mode="w", encoding="utf-8") as fin:
        fin.write(json.dumps(players_list))


# ================================

chess_players = [
    {"id": 19, "name": "Jobava", "country": "Georgia", "rating": 2588, "age": 41},
    {"id": 28, "name": "Caruana", "country": "USA", "rating": 2781, "age": 32},
    {"id": 35, "name": "Giri", "country": "Netherlands", "rating": 2771, "age": 30},
    {"id": 84, "name": "Carlsen", "country": "Norway", "rating": 2864, "age": 34},
    {"id": 118, "name": "Ding", "country": "China", "rating": 2799, "age": 32},
    {"id": 139, "name": "Karjakin", "country": "Russia", "rating": 2747, "age": 35},
    {"id": 258, "name": "Duda", "country": "Poland", "rating": 2731, "age": 31},
    {
        "id": 301,
        "name": "Vachier-Lagrave",
        "country": "France",
        "rating": 2737,
        "age": 34,
    },
    {"id": 403, "name": "Nakamura", "country": "USA", "rating": 2768, "age": 36},
]

file_path = make_json_file("files/jsons", "data2")

# make_json_file('file_path', 'data_1') # ფაილის შექმნა

# write_content_json(file_path, chess_players) # ფაილში მონაცემების შეტანა

data = read_json_file(file_path)  # ფაილის ნახვა/ წაკითხვა
print(data)
print(len(data))

# # არსებულ ფაილში მონაცემების რედაქტირება
# edit_content(file_path, 403, 'name', 'Hikaru Nakamura')


# არსებულ ფაილში ახალი კონტენტის დამატება
# new_data = [
#   {'id': 568, 'name': 'Kasparov', 'country': 'Russia', 'rating': 2705, 'age': 56},
#   {'id': 189, 'name': 'Karpov', 'country': 'Russia', 'rating': 2698, 'age': 59},
# ]
# update_json_file(file_path, new_data)
