from sense_hat import SenseHat
import time
import displays as display  #importe le fichier qui comporte toutes les listes pour l'affichage
import crypto as c

s = SenseHat()
s.low_light = True

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
            print("Pin correct")
            s.set_pixels(display.correct)
            time.sleep(1)

        elif len(current_pin) == len(correct_pin):
            current_pin = []
            print("Wrong pin !")
            s.set_pixels(display.cancel)
            time.sleep(1)


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
    print("Vous avez choisis l'option n°" + str(state["menu_index"] % len(menu) + 1))

    if choice == "save":
        save_code()

    elif choice == "cancel":
        raise SystemExit


def choosed_option_message(menu):
    """ Permet de continuer le programme en fonction de l'option choisie dans le menu

        Args:
            menu: list: une liste des listes de pixels qui composent l'affichage
    """
    choice = menu[state["menu_index"] % len(menu)][0]
    print("Vous avez choisis l'option n°" + str(state["menu_index"] % len(menu) + 1))

    if choice == "save_code":
        state["save"] = True

    elif choice == "cancel":
        raise SystemExit

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

    returns = (state["message"],state["save"])
    return returns


def save_code():
    menu_options = [("0", display.num_0), ("1", display.num_1),("2", display.num_2), ("3", display.num_3),("4", display.num_4),
                    ("5", display.num_5),("6", display.num_6), ("7", display.num_7),("8", display.num_8), ("9", display.num_9),
                    ("delete", display.delete), ("save_code", display.save), ("cancel", display.cancel)]

    # Permet d'afficher le menu des options -> (numéros de 0 à 9 et del save cancel)
    message = show_menu(menu_options,2)
    while message[1] is not True:
        message = show_menu(menu_options, 2)
    message_str = ""
    for i in message[0]:
        message_str += str(i)
    print("votre code: " + message_str)

def show_menu(menu,menu_number):
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
                    if menu_number == 1:
                        choosed_option(menu)
                    elif menu_number == 2:
                        return choosed_option_message(menu)


def main():
    while True:
        #demande le code pin à l'utilisateur
        pin()

        if check_msg():
            """ Demander d'enregistrer un message """
            print("Pas de message enregistré")

            menu_options = [("save",display.save),("cancel",display.cancel)]

            #Permet d'afficher le menu des options -> (Enregistrer un message ou annuler et revérouiller le MagicLock)
            show_menu(menu_options,1)
            state["menu_index"] = 0

        else:
            """ Propose les options du message """
            print("Un message est enregistré")
            raise SystemExit


if __name__ == "__main__":
    main()
