import json
import numpy
import matplotlib
import seaborn
import matplotlib.pyplot as plt
import pandas
import warnings

#this is dev branch

class Hit:
    paese = ""
    valore = 0.0
    scambii = 0.0

    def __init__(self, paese="", valore=0.0, scambii=0.0):
        self.paese = paese
        self.valore = valore
        self.scambii = scambii

    def getPaese(self):
        return  self.paese

    def getTrend(self):
        return self.valore / self.scambii

    def to_string(self):
        print("Paese : " + str(self.paese) + "\n Valore : " + str(self.valore) + "\n Scambii : " + str(self.scambii))


hits = []

matplotlib.use("TkAgg")

with open('response.json') as f:
    jsonData = json.load(f)

jsonData = jsonData["records"]

for item in jsonData:
    hits.append([item["fields"]["cou_text_fr"], item["fields"]["i2"], item["fields"]["i1"]])

data = pandas.DataFrame(hits, columns=['Paesi', 'Valore', 'Scambii'])

print(data)

seaborn.set(style="darkgrid")
seaborn.set_style("ticks")

fig, ax = plt.subplots(1, 1)
ax.set_ylabel("Valore / Scambii")

seaborn.barplot(x=data["Paesi"], y=data["Valore"]/data["Scambii"], data=data, ax=ax)
plt.show()