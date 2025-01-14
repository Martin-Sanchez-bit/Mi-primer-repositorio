meme_dict = {"CRINGE": "Algo excepcionalmente raro o embarazoso", "LOL": "Una respuesta común a algo gracioso o league of legends", "XD": "risa", "NTP": "no te preocupes"}
word = input("Escribe una palabra que no entiendas (¡con mayúsculas!): ")
if word in meme_dict.keys():
    print(meme_dict[word])
else:
    print("no se encontro esa palabra")
