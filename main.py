meme_dict = {
            "CRINGE": "Garip ya da utandırıcı bir şey",
            "LOL": "Komik bir şeye verilen cevap",
            "BOOMER": "Yaşlı bireylere verilen isim.",
            "FPOON": "Çatal-Kaşık karışımı aletin kısa ismi",
            "AURA": "Kişinin verdiği hisse denir, genellikle çok havalı ise yüksek 'aura puanına' sahip olursunuz"
            }

word = input("Anlamadığınız bir kelime yazın (hepsini büyük harflerle yazın!): ")

if word in meme_dict.keys():
    print(meme_dict[word])
else:
    print("???")
