"""
FASE 1 – LIVELLO INTERMEDIO
CONSEGNA: Creare un programma che gestisca una libreria usando una lista di dizionari. 
Ogni libro è rappresentato come un dizionario con chiavi: titolo, autore, anno.
Il programma deve permettere di:
- Aggiungere un nuovo libro;
- Rimuovere un libro in base al titolo;
- Cercare un libro per autore o titolo;
- Mostrare tutti i libri presenti;
Tutte queste operazioni devono essere gestite tramite funzioni.

"""

import json
import os

# creao la mia libreria
libreria =[]

# funzione per pulire lo schermo e appare all'azione successiva in modo pulito
def pulisci():
    os.system("cls" if os.name == "nt" else "clear")


# - ho messo la variabile libreria come globale per utilizzarla in questa funzione
# - questa è una funzione che usa json e volge le seguenti manzioni: crear un file json "libreira.json" e 
# lo rinomina in file. Crea una variabile libreria e gli carica il file all'interno. Se non esiste 
# manda a schermo una lista libreria vuotq #
def carica_libro() :
    global libreria
    try:
        with open("libreria.json", "r") as file:
            libreria = json.load(file)
    except FileNotFoundError:
        libreria = []


# questa funzione sovrascive il file ogni volta viene fatta una modifica, aggiunta e così via
def salva_libro() :
    with open("libreria.json", "w") as file:
        json.dump(libreria, file, indent=4)


# questa funzione chiede all'utente i dati di un libro, crea un dict con i dati inseriti dall'utente, 
# e poi aggiunge il libro nella variabile libreria.
# poi chiama la funzione per pulire lo schermo per rendere tutto più pulito e sistemato, dice che il libro
# è stato aggiunto correttamente e chiede se si vuole aggiungere un'altro libro o no  #
def aggiungi_libro():
    print("----------------")
    print("Aggiungi libro")
    print("----------------\n")
    titolo = input("Inserisci il titolo: ")
    autore = input("Inserisci l'autore: ")
    anno = input("Inserisci l'anno di pubblicazione: ")

    libro = {
        "titolo": titolo,
        "autore": autore,
        "anno": anno
    }

    libreria.append(libro)

    salva_libro()

    print("\n-------------------------------------------")
    print("Libro aggiunto correttamente alla libreria")
    print("-------------------------------------------\n")

    
    print("-------------------------------------------------")
    risposta = input("Vuoi aggiungere un altro libro?\n" \
                    "Rispondi con 'si' per aggiungere un altro libro, " \
                    "'no' per tornare al menù iniziale:\n")
    print("-------------------------------------------------\n")

    if risposta == "si":
        pulisci()
        aggiungi_libro()
    else:
        pulisci()
        menu()


def rimuovi_libro() :
    global libreria
    print("----------------")
    print("Rimuovi libro")
    print("----------------\n")

    libro_da_rimuovere = input("Inserisci il titolo del libro che desideri rimuovere:\n")

    libro_trovato = False
    for libro in libreria:
        if libro["titolo"].lower() == libro_da_rimuovere:
            conferma_rimozione = input("Vuoi davvero rimuovere questo libro?:\n")
            if conferma_rimozione == "si":
                libreria.remove(libro)

                print("\n-------------")
                print("Libro rimosso")
                print("--------------")
                salva_libro()
                libro_trovato = True

                scelta = input("\nRispondi con 'si' se vuoi continuare a riuovere un libro,\n" \
                                "Rispondi con 'no' se vuoi tornare al menù inizale:\n")
                while True:
                    if scelta == "si":
                        pulisci()
                        rimuovi_libro()
                    elif scelta == "no":
                        pulisci()
                        menu()
                    else:
                        print("Scelta non valida. Riprova!!")
    
    if not libro_trovato:
        scelta_finale = input("\nIl libro non è presente nella tua libreria!\n" \
                "\nRispondi con 'si' se vuoi riprovare a rimuovere un libro,\n" \
                "Rispondi con 'no' se vuoi tornare al menù:\n")
        while True:
            if scelta_finale == "si":
                pulisci()
                rimuovi_libro()
            elif scelta_finale == "no":
                pulisci()
                menu()
            else:
                print("Scelta non valida. Riprova!!")
                

                



def cerca_libro() :
    global libreria
    print("-------------")
    print("Cerca libro")
    print("-------------\n")

    titolo_libro_da_cercare = input("Digita il libro che desideri cercare:\n")

    libro_trovato = False
    while True:
        for libro in libreria:
            if libro["titolo"].lower() == titolo_libro_da_cercare.lower():

                print("\n-----------------")
                print("Libro trovato!")
                print("-----------------\n")

                print(f"{libro}")

                libro_trovato = True
                break
                
        
        if not libro_trovato:
            print("\n-------------------------------------------------------------------")
            print(f"Non ci sono risultati con questo titolo: {titolo_libro_da_cercare}")
            print("---------------------------------------------------------------------\n")

        scelta = input("\n\nDigita 'si' per continuare la ricerca di un libro,\n" \
                        "Digita 'no' per tornare al menù iniziale:\n")
        while True:
            if scelta == "si":
                pulisci()
                cerca_libro()
                return
            elif scelta == "no":
                pulisci()
                menu()
                return
            else:
                print("Scelta non valida. Reindirizzamento al menu principale!!")
                pulisci()
                menu()
                return
    


# in questa funzione ho dichiarato la variabile libreria globale per poterla usare.
# poi cairca il file json e per ogni libro persente nella libreria li manda a schermo con il seguente 
# formato e se la libreria è vuota manda a schermo la stirnga "nessun libro presente"#
def mostra_libro() :
    global libreria
    carica_libro()
    if libreria: 
        print("Libri presenti nella libreria:\n")
        for libro in libreria:
            print(f"- {libro['titolo']}, {libro['autore']}, {libro['anno']}")
    else:
        print("Nessun libro presente")

    while True:
        richiesta_di_continuare = input("\nRispondi con 'si' se vuoi continuare nel programma,\n" \
                                        "Rispondi con 'no' se vuoi uscire dal programma:\n")
        if richiesta_di_continuare == "si":
            pulisci()
            menu()
        if richiesta_di_continuare != "si":
            pulisci()
            break
        


# programma principale, che caricha il file json prima di essere sovrascritto e poi fa comparire un menu
# a schermo dove l'utente, tramine 1 2 3 4 può scegliere un azione da eseguire e in base le scelte che 
# vuole fare l'utente si aprono le varie funzioni per eseguire le azioni richieste e ogni volta che 
# l'utente apre una nuova scheda il programma pulisce lo schermo per rendere tutto pulito e sistemato #
carica_libro()
def menu() :
    print("--------------------")
    print("La libreria ONLINE")
    print("--------------------")

    print("\n-------------------------------------------------------------------------------------------------")
    print("Scegli una delle seguenti voci:\n")
    print("1. Aggiungi un libro")
    print("2. Rimuovi un libro")
    print("3. Cerca un libro")
    print("4. Mostra libri")
    print("5. Esci\n")
    scelta = int(input("Inserisci la tua scelta (1-4) per proseguire: "))
    print("-------------------------------------------------------------------------------------------------\n")

    if scelta == 1:
        pulisci()
        aggiungi_libro()
    elif scelta == 2:
        pulisci()
        rimuovi_libro()
    elif scelta == 3:
        pulisci()
        cerca_libro()
    elif scelta == 4:
        pulisci()
        mostra_libro()
    elif scelta == 5:
        print("Uscita dal programma")
    else: 
        print("Comando non riconosciuto! Riprova.\n")
        riprova = input("- Inserisci 'si' se vuoi continuare\n" \
                        "- Inserisci 'no' se vuoi uscire dal programma:\n" \
                        "")
        if riprova == "si":
            pulisci()
            menu()
        elif riprova == "no":
            print("Programma interrotto")


# richiamo la funzione menu per far partire il programma altrimenti non succede nulla perché il mio programma
# è all'interno della funzione menu 
menu()