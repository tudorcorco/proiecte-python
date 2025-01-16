import pandas as pd
import os


desktop_path = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
file_path = os.path.join(desktop_path, 'inventar_depozit.xlsx')


if not os.path.exists(file_path):
    print("Eroare: Fișierul inventar_depozit.xlsx nu există pe desktop.")
    exit()


def scade_inventar(cod_produs, cantitate):
    inventar_df = pd.read_excel(file_path)

    if cod_produs in inventar_df['CodProdus'].values:
        index_produs = inventar_df.loc[inventar_df['CodProdus'] == cod_produs].index[0]
        disponibil = inventar_df.at[index_produs, 'Cantitate']
        if cantitate <= disponibil:
            inventar_df.at[index_produs, 'Cantitate'] -= cantitate
            print(f"Ați luat {cantitate} bucăți din produsul cu codul {cod_produs}.")
            print(f"Cantitate disponibilă rămasă pentru produsul cu codul {cod_produs}: {inventar_df.at[index_produs, 'Cantitate']}")

            inventar_df.to_excel(file_path, index=False)
        else:
            print("Eroare: Cantitatea cerută este mai mare decât cantitatea disponibilă.")
    else:
        print("Eroare: Codul produsului nu există în inventar.")


while True:
    try:
        cod_produs_ales = int(input("Introduceți codul produsului pe care doriți să-l luați sau '0' pentru a ieși: "))
    except ValueError:
        print("Eroare: Codul produsului trebuie să fie o valoare numerică.")
        continue

    if cod_produs_ales == 0:
        break

    cantitate_alesa = input("Introduceți cantitatea pe care doriți să o luați: ")

    if not cantitate_alesa.isdigit() or int(cantitate_alesa) <= 0:
        print("Eroare: Cantitatea introdusă trebuie să fie un număr întreg pozitiv.")
        continue

    cantitate_alesa = int(cantitate_alesa)
    scade_inventar(cod_produs_ales, cantitate_alesa)
