energia1 = {'Watt', 'Quilowatt', 'Volts', 'Ampére', 'Joule'}
energia2 = {'ºC', 'Farenheit', 'Calorias', 'KiloCalorias', 'Watt'}
energia3 = {'Kwh', 'Volts', 'Joule', 'Calorias', 'Potencia'}
energia4 = {'Kw', 'calorias', 'potencia', 'C'}
energia5 = {'Watt', 'Joule', 'Kwh','ºC', 'Farenheit'}

print(energia1 == energia5)
print(energia2 == energia1)
print(energia5 == energia4)
print(energia4 == energia2)
print(energia3 == energia3)

print(energia4 ^ energia2)
print(energia5 ^ energia4)
print(energia2 ^ energia3)
print(energia3 ^energia1)


