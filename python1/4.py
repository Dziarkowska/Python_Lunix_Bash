
kod_wlasciwy = input('Podaj swoj nowy kod:\n')
liczba_dostepnych_prob = 3

while liczba_dostepnych_prob > 0:
	print("Masz",liczba_dostepnych_prob,"proby\n")
	kod_podany = input("podaj kod:\n")
	if kod_wlasciwy == kod_podany:
		print("dobry kod")
		break
	else:
		print("zly kodd")
		liczba_dostepnych_prob -= 1