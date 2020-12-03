from sense_hat import SenseHat
import time
import displays as display # importe le fichier qui comporte toutes les listes pour l'affichage
import crypto as c

s = SenseHat()
s.low_light = True
s.set_imu_config(False,True,False)

state = {
    "menu_index" : 0,
    "message" : [],
    "save" : False
    }

def pin():
    """ Permet de dévérouiller le MagicLock en faisant la séquence contenue dans correct_pin """
    correct_pin = [("pressed", "up"), ("released", "up"), ("pressed", "down"), ("released", "down"),
                   ("pressed", "left"),("released", "left"), ("pressed", "right"), ("released", "right")]
    pin_correct = False
    current_pin = []

    while not pin_correct:
        s.set_pixels(display.screen_off)
        event = s.stick.wait_for_event()
        current_pin.append((event.action, event.direction))

        if current_pin == correct_pin:
            pin_correct = True
            s.set_pixels(display.correct)
            time.sleep(1)
            current_pin = []

        elif len(current_pin) == len(correct_pin):
            s.set_pixels(display.cancel)
            pin_was_false = True
            time.sleep(1)
            current_pin = []


def check_msg():
    """ Permet de vérifier si un message est stocké dans le fichier message """
    with open("message.txt", 'r') as message:
        if message.readlines() == ["\n"]:
            return True
        else:
            return False


def display_choice(menu):
    """ Permet d'afficher la bonne "image" sur l'écran de led en fonction de la position et
        de la liste de listes de pixels 'menu'

        Args:
            menu: list: une liste des listes de pixels qui composent l'affichage
    """
    choice = menu[state["menu_index"] % len(menu)][1]
    s.set_pixels(choice)


def choosed_option(menu):
    """ Permet de continuer le programme en fonction de l'option choisie dans le menu

        Args:
            menu: list: une liste des listes de pixels qui composent l'affichage
    """
    choice = menu[state["menu_index"] % len(menu)][0]

    # IN CASE OF DEBUG DELETE LATER
    # print("Vous avez choisis l'option n°" + str(state["menu_index"] % len(menu) + 1))

    if choice == "save":
        state["menu_index"] = 0

    elif choice == "cancel":
        s.set_pixels(display.screen_off)
        raise SystemExit

    elif choice == "save_code":
        state["menu_index"] = 0
        state["save"] = True

    elif choice == "delete":
        state["message"].pop()

    elif choice == "0":
        state["message"].append("0")

    elif choice == "1":
        state["message"].append("1")

    elif choice == "2":
        state["message"].append("2")

    elif choice == "3":
        state["message"].append("3")

    elif choice == "4":
        state["message"].append("4")

    elif choice == "5":
        state["message"].append("5")

    elif choice == "6":
        state["message"].append("6")

    elif choice == "7":
        state["message"].append("7")

    elif choice == "8":
        state["message"].append("8")

    elif choice == "9":
        state["message"].append("9")

    return (state["message"],state["save"])


def save_message():
    # Options du menu pour enregistrer un message.
    menu_options = [("0", display.num_0), ("1", display.num_1),("2", display.num_2), ("3", display.num_3),("4", display.num_4),
                    ("5", display.num_5),("6", display.num_6), ("7", display.num_7),("8", display.num_8), ("9", display.num_9),
                    ("delete", display.delete), ("save_code", display.save), ("cancel", display.cancel)]

    # Affiche le menu avec menu_options tant que le message n'est pas sauvegardé
    states = show_menu(menu_options)
    while states[1] is not True:
        states = show_menu(menu_options)
    save_floppy_disk_icon()

    # Enregirstre le message dans un string
    message_str = ""
    for i in states[0]:
        message_str += str(i)

    print("votre code: " + message_str)


def show_menu(menu):
    """ Permet d'appeller la fonction display_choice et de mettre à jour
        l'index en fonction des déplacements du joystick

        Args:
            menu: list: une liste des listes de pixels qui composent l'affichage
    """

    choosed = False
    s.set_pixels(menu[state["menu_index"] % len(menu)][1])
    while not choosed:
        events = s.stick.get_events()
        if events:
            for event in events:
                if event.action != "pressed":
                    continue

                if event.direction == 'left':
                    state["menu_index"] -= 1
                    display_choice(menu)

                elif event.direction == 'right':
                    state["menu_index"] += 1
                    display_choice(menu)

                elif event.direction == 'middle':
                    choosed = True
                    return choosed_option(menu)


def main():

    # Demande le code pin à l'utilisateur
    pin()

    # Si il n'y a pas de message
    if check_msg():
        """ Demander d'enregistrer un message """

        # Les options qui seront disponibles dans le menu
        menu_options = [("save",display.save),("cancel",display.cancel)]

        # Affiche le menu avec menu_options
        show_menu(menu_options)

        # Affiche le menu pour enregistrer un message
        message_str = save_message()

        # Demande d'enregistrer le code (combinaison de mouvements)
        code_str = save_code()

        # Chiffre les données et les retourne en tuple
        encrypted_data = encrypt_all(message_str, code_str)

        # Enregistre les données dans les fichiers respectifs
        save_encrypted_data(encrypted_data)


    # Si il y a un message
    else:
        """ Propose les options du message """

        #TODO Quand il n'y a pas de message
        print("Un message est enregistré")
        raise SystemExit


if __name__ == "__main__":
    main()
