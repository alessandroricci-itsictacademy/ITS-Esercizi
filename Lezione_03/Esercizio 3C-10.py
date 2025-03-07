""" Esercizio 3C-10. Scrivere un programma in Python che permetta all'utente di inserire una data (giorno e mese espressi in forma numerica), salvi la data in una tupla e utilizzi un match statement per verificare se la data corrisponde a una festività o a un evento speciale:
- Capodanno → 1 Gennaio → "Capodanno"
- San Valentino → 14 Febbraio → "San Valentino"
- Festa della Repubblica Italiana → " Giugno → "Festa della Repubblica Italiana"
- Ferragosto → 15 Agosto → "Ferragosto"
- Halloween → 31 Ottobre → "Halloween"
- Natale → 25 Dicembre → "Natale"
- Altro caso → "Nessuna festività importante in questa data."
Expected Output:
Inserisci il giorno: 25
Inserisci il mese: 12
Output: Il 25/12 è Natale!
- - - - - - - - - - - - - - -
Inserisci il giorno: 5
Inserisci il mese: 3
Output: Nessuna festività importante in questa data. """

giorno = int(input("Inserisci il giorno: "))
mese = int(input("Inserisci il mese: "))

data = (giorno, mese)

giorni_del_mese: list = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

match data:
    case data if giorno < 1 or giorno > giorni_del_mese[mese] - 1 or mese < 1 or mese > 12:
        print("La data inserita non è valida.")
    case data if giorno == 1 and mese == 1:
        print(f"Il {data} è Capodanno!")
    case data if giorno == 14 and mese == 2:
        print(f"Il {data} è San Valentino!")
    case data if giorno == 2 and mese == 6:
        print(f"Il {data} è Festa della Repubblica Italiana!")
    case data if giorno == 15 and mese == 8:
        print(f"Il {data} è Ferragosto!")
    case data if giorno == 31 and mese == 10:
        print(f"Il {data} è Halloween!")
    case data if giorno == 25 and mese == 12:
        print(f"Il {data} è Natale!")
    case _:
        print(f"Nessuna festività importante in questa data.")