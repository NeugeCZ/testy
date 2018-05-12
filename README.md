# Upravené funkce + testy

Pár slov k původním funkcím:

abc_random_string: Fce vracela hrubý převod sekvence bytů - tato konverze do str z mého pohledu není vhodným zp. generování (prediktabilita začátku s b' a lomítek, proměnná délka řetězce). Pro zachování krypto-friendly řešené nechávám základ a konvertuji do hexu. Length jsem pochopil jako délku celého str vč. 'abc'.

is_prime: Upraveno tak, aby fce správně klasifikovala č. menší než 2 + celočíselné floaty.

print_next_prime: Taktéž upraveno pro celočíselné floaty + snížená náročnost pro vyhledávání ze záp. čísel, při kterém není nutné lézt do cyklu. 

Pár slov k testům:

Z hlediska těch dvou číselných fcí nedělám pro každý subproblém zvlášťní test, všechny potenciální (výše vytčené/odstraněné) problémy se snažím, pokud možno, pokrýt v jedné sadě testů s parametrize.
