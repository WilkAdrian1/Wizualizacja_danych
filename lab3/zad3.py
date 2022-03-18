produkty = {'jajka': 'sztuki', 'woda': 'butelka', 'baton': 'sztuki', 'mąka': 'kg'}

produkty_sztuki = [key for key, value in produkty.items() if value == 'sztuki']
print(produkty_sztuki)