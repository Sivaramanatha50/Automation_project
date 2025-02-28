# import json
#
import requests
from RPA.JSON import JSON
import json

conn = requests.get("https://opentdb.com/api.php?amount=10")
#data = {"response_code":0,"results":[{"type":"multiple","difficulty":"medium","category":"Entertainment: Film","question":"Johnny Depp made his big-screen acting debut in which film?","correct_answer":"A Nightmare on Elm Street","incorrect_answers":["My Bloody Valentine","Halloween","Friday the 13th"]},{"type":"multiple","difficulty":"hard","category":"Geography","question":"The Andaman and Nicobar Islands in South East Asia are controlled by which country?","correct_answer":"India","incorrect_answers":["Vietnam","Thailand","Indonesia"]},{"type":"multiple","difficulty":"easy","category":"Entertainment: Video Games","question":"In World of Warcraft the default UI color that signifies Druid is what?","correct_answer":"Orange","incorrect_answers":["Brown","Green","Blue"]},{"type":"multiple","difficulty":"medium","category":"Vehicles","question":"What do the 4 Rings in Audi&#039;s Logo represent?","correct_answer":"Previously independent automobile manufacturers","incorrect_answers":["States in which Audi makes the most sales","Main cities vital to Audi","Countries in which Audi makes the most sales"]},{"type":"multiple","difficulty":"easy","category":"Entertainment: Video Games","question":"Which Animal Crossing game was for the Nintendo Wii?","correct_answer":"Animal Crossing: City Folk","incorrect_answers":["Animal Crossing: New Leaf","Animal Crossing: Wild World","Animal Crossing: Population Growing!"]},{"type":"multiple","difficulty":"hard","category":"Science: Computers","question":"Which of these was the name of a bug found in April 2014 in the publicly available OpenSSL cryptography library?","correct_answer":"Heartbleed","incorrect_answers":["Shellshock","Corrupted Blood","Shellscript"]},{"type":"multiple","difficulty":"medium","category":"Entertainment: Film","question":"In the 1979 British film &quot;Quadrophenia&quot; what is the name of the main protagonist?","correct_answer":"Jimmy Cooper","incorrect_answers":["Pete Townshend","Franc Roddam","Archie Bunker"]},{"type":"multiple","difficulty":"hard","category":"Entertainment: Video Games","question":"In Diablo lore, this lesser evil spawned from one of the seven heads of Tathamet, and was known as the Maiden of Anguish.","correct_answer":"Andariel","incorrect_answers":["Valla","Malthael","Kashya"]},{"type":"multiple","difficulty":"hard","category":"Science &amp; Nature","question":"How many protons are in an oxygen atom?","correct_answer":"Eight","incorrect_answers":["Four","Two","Six"]},{"type":"boolean","difficulty":"easy","category":"Geography","question":"Toronto is the capital city of the North American country of Canada.","correct_answer":"False","incorrect_answers":["True"]}]}
data = conn.json()
questions = JSON().get_values_from_json(data,"$..question")
#answers = JSON.get_values_from_json(conn,"$response_code..correct_answer")
# for i in questions:
#     print(i)

# import re
#
# expres = '[A-Za-z]+[0-9]+@+[A-Za-z]+.+([A-Za-z]{2})'
#
# data = "sivaram031@gmail.com"
#
#
# if re.findall(expres,data):
#     print(True)
# else:
#     print(False)

# l = "I felt happy because I saw the happy others were happy and because I knew I should feel happy but I happy wasnt really happy"
# d = {}
# for i in l.split():
#     d[i] = d.get(i,0)+1
# print(d)

from collections import defaultdict

# Sample dictionary
data = {
    "a": "apple",
    "b": "banana",
    "c": "apple",
    "d": "cherry",
    "e": "banana",
    "f": "apple"
}
value_to_keys = defaultdict(list)
for key, value in data.items():
    value_to_keys[value].append(key)

# Step 2: Swap keys and values, keeping lists for duplicate values
swapped_dict = {value: keys for value, keys in value_to_keys.items()}

#print(swapped_dict)

# f = {'name':"siva",'age':30,'addres':{'village':"banglore","town":'tadipatri'}}
#
# for k in f.keys():
#     print(k.__getitem__('addres'))

s = "hi how are"

print(' '.join(s.split(' ')[::-1]))

