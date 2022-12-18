import pymorphy2

morph = pymorphy2.MorphAnalyzer()

inflected = morph.parse('думающему')[0].inflect({'sing', 'nomn'}).word
print(inflected)