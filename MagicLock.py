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

def view(message):
    s.show_message("Message: " + message, scroll_speed=0.06)

def delete_all():
    with open("message.txt", 'w') as message_file:
        message_file.write("")
    with open("code.txt", 'w') as code_file:
        code_file.write("")

def choosed_option(menu):
    """ Permet de continuer le programme en fonction de l'option choisie dans le menu

        Args:
            menu: list: une liste des listes de pixels qui composent l'affichage
    """
    choice = menu[state["menu_index"] % len(menu)][0]
    option = None

    # IN CASE OF DEBUG DELETE LATER
    # print("Vous avez choisis l'option n°" + str(state["menu_index"] % len(menu) + 1))

    if choice == "save":
        state["menu_index"] = 0
        option = 'save'

    elif choice == "cancel":
        s.set_pixels(display.screen_off)
        raise SystemExit

    elif choice == "save_code":
        state["menu_index"] = 0
        state["save"] = True

    elif choice == "decode":
        state["menu_index"] = 0

    elif choice == "delete":
        state["message"].pop()

    elif choice == "message_delete":
        option = 'message_delete'

    elif choice == "view":
        option = 'view'

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

    return (state["message"],state["save"],option)


def save_message():
    """ Affiche le menu qui permet d'enregistrer le message

        Returns:
            message_str: str: le message enregistré sous forme de string
    """

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
    return message_str


def code_help():
    """ Affiche les messages d'aide sur l'écran de led du MagicLock """
    s.show_message("Pour enregistrer le code, bougez le MagicLock et validez en pressant le joystick. |", scroll_speed=0.06)
    s.show_message("Pour enregistrer le code allez vers la gauche avec le joystick. |", scroll_speed=0.06)
    s.show_message("Le code doit être composé de mouvements de 90° vers la droite ou la gauche.", scroll_speed=0.06)


def save_floppy_disk_icon():
    """ Permet d'afficher le 'floppydisk' qui clignotte """
    s.set_pixels(display.floppy_disk)
    time.sleep(0.5)
    s.set_pixels(display.screen_off)
    time.sleep(0.5)
    s.set_pixels(display.floppy_disk)
    time.sleep(0.5)
    s.set_pixels(display.screen_off)
    time.sleep(0.5)
    s.set_pixels(display.floppy_disk)
    time.sleep(0.5)
    s.set_pixels(display.screen_off)


def save_code():
    """ Permet d'enregistrer le code (suite de mouvement)

        Returns:
            code_str: str: le code enregistré sous forme de string (right ou left)
    """

    #TODO il faut le décommenter avec la fin
    #s.show_message("Pour l'aide allez vers la droite avec le joystick", scroll_speed=0.06)

    code_list = []
    saved = False
    while not saved:
        s.set_pixels(display.code)
        gyro = s.get_gyroscope()
        events = s.stick.get_events()
        if events:
            for event in events:
                if event.action != "pressed":
                    continue

                if event.direction == 'left':
                    if len(code_list) == 0:
                        continue
                    else:
                        saved = True
                        save_floppy_disk_icon()

                elif event.direction == 'right':
                    code_help()

                elif event.direction == 'up':
                    s.set_pixels(display.delete)
                    time.sleep(0.5)
                    s.set_pixels(display.screen_off)
                    raise SystemExit

                elif event.direction == 'middle':
                    s.set_pixels(display.save)
                    time.sleep(0.5)
                    s.set_pixels(display.screen_off)
                    code_list.append([["pitch",gyro['pitch']],["roll",gyro['roll']],["yaw",gyro['yaw']]])

    for i in range(len(code_list)):
        for j in range(len(code_list[i])):
            code_list[i][j][1] = round(code_list[i][j][1], 2)

    code_str = code_list_to_str(code_list)
    return code_str


def code_list_to_str(code_list):
    """ Permet de transformer une liste de code en string

        Returns:
            code_str: str: une représentation du code sous forme de str (right ou left)
    """
    code_str = ""
    curr = code_list[0]
    #[[['pitch', 70.4], ['roll', 332.88], ['yaw', 81.13]], [['pitch', 338.07], ['roll', 298.1], ['yaw', 328.45]], [['pitch', 299.45], ['roll', 258.01], ['yaw', 321.3]], [['pitch', 350.57], ['roll', 84.53], ['yaw', 88.07]]]
    for pos in range(len(code_list)):
        for value in range(len(code_list[pos])):
            if 45 < code_list[pos][value][1] <= 115:
                code_str += code_list[pos][value][0]+"90"
            elif 115 < code_list[pos][value][1] <= 205:
                code_str += code_list[pos][value][0]+"180"
            elif 205 < code_list[pos][value][1] <= 295:
                code_str += code_list[pos][value][0]+"270"
            elif 295 < code_list[pos][value][1] <= 360 or 0 <= code_list[pos][value][1] <= 45:
                code_str += code_list[pos][value][0]+"360"
    return code_str


def encrypt_all(message_number_str,code_str):
    """ Permet de chiffrer le message et le code

        Returns:
            hashed_code: str: le code sous forme hachée
            encoded_message: str: le message sous forme chiffrée
    """
    alphabet = ["a","b","c","d","e","f","g","h","i","j"]
    hashed_code = c.hashing(code_str)
    message_letter_str = ""

    for i in message_number_str:
        message_letter_str += alphabet[int(i)]

    encoded_letter_message = c.encode(code_str,message_letter_str)

    print(hashed_code,encoded_letter_message)
    return (hashed_code,encoded_letter_message)


def save_encrypted_data(encrypted_data):
    """ Permet de sauvegarder le message et le code dans les fichiers respectifs """
    code, message = encrypted_data

    with open("message.txt", 'w') as message_file:
        message_file.write(message)

    with open("code.txt", 'w') as code_file:
        code_file.write(code)


def decode_all(code_str_tried):
    """ Permet de décoder le message enregistré si le code fourni est correct.

        Args:
            code_str_tried: str: le code entré par l'utilisateur pour décoder le message

        Returns:
            retourne le message décodé si le code code_str_tried est correcte et False si non
    """

    hashed_code_tried = c.hashing(code_str_tried)

    with open("code.txt", 'r') as code_file:
        correct_hashed_code = code_file.readline().strip()

    if hashed_code_tried == correct_hashed_code:
        print("correct code")

        with open("message.txt", 'r') as message_file:
            correct_coded_message = message_file.readline().strip()
        print(code_str_tried, correct_coded_message)

        decoded_letter_message = c.decode(code_str_tried,correct_coded_message)

        # SECURITE EN PLUS
        letters = [("0","a"), ("1","b"), ("2","c"), ("3","d"), ("4","e"), ("5","f"), ("6","g"), ("7","h"), ("8","i"), ("9","j")]
        message_number_str = ""

        for i in decoded_letter_message:
            for j in range(10):
                if letters[j][1] == i:
                    message_number_str += letters[j][0]

        return message_number_str

    return False


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


def wrong_code_display():
    """ Affiche à l'écran les 'logos' qui signifient un mauvais code et la suppression des fichiers"""
    s.set_pixels(display.cancel)
    time.sleep(0.3)
    s.set_pixels(display.delete)
    time.sleep(0.3)
    s.set_pixels(display.cancel)
    time.sleep(0.3)
    s.set_pixels(display.delete)
    time.sleep(0.3)
    s.set_pixels(display.cancel)
    time.sleep(0.3)
    s.set_pixels(display.delete)
    time.sleep(0.3)
    s.set_pixels(display.cancel)
    time.sleep(0.3)
    s.set_pixels(display.delete)
    time.sleep(0.3)
    s.set_pixels(display.cancel)
    s.set_pixels(display.screen_off)


def main():
    """ Fonction principale du programme qui appelle les bonnes fonctions au bon moment """
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

        menu_options = [("view",display.view),("save",display.save),("message_delete",display.delete)]

        saved = False
        while not saved:
            # Affiche le menu avec menu_options
            option = show_menu(menu_options)

            # Si l'option est choisie on affiche le message
            if option[2] == 'view':
                view(message_str)

            elif option[2] == 'save':
                s.set_pixels(display.correct)
                time.sleep(0.5)
                saved = True

            # Si l'option est choisie on supprime les fichiers
            elif option[2] == 'message_delete':
                s.show_message("Message supprimes", scroll_speed=0.06)
                raise SystemExit


        # Roll 315 - 45  Pitch 330 - 30


        #TODO Affiche le message un menu pour garder ou réenregistrer

        # Demande d'enregistrer le code (combinaison de mouvements)
        code_str = save_code()

        # Chiffre les données et les retourne en tuple
        encrypted_data = encrypt_all(message_str, code_str)

        # Enregistre les données dans les fichiers respectifs
        save_encrypted_data(encrypted_data)


    # Si il y a un message
    else:
        """ Propose les options du message """

        # Les options qui seront disponibles dans le menu
        menu_options = [("decode",display.decode),("cancel",display.cancel)]

        # Affiche le menu avec menu_options
        show_menu(menu_options)

        # Permet d'enregistrer le code entré dans code_str
        code_str = save_code()

        # Permet d'essayer 3 fois de rentrer un code pour décoder le message enregistré
        tries = 1
        decoded_message = decode_all(code_str)

        while decoded_message is False and tries < 3:
            s.set_pixels(display.cancel)
            time.sleep(0.5)
            code_str = save_code()
            decoded_message = decode_all(code_str)
            tries += 1

        # Si au bout de 3 essais le code est toujours
        # erroné on appelle wrong_code_display() et on supprime les fichiers
        if tries == 3:
            wrong_code_display()
            delete_all()

        #Si le message est décodé on affiche les options disponibles
        if decoded_message is not False:
            s.set_pixels(display.correct)
            time.sleep(0.5)
            # Les options qui seront disponibles dans le menu
            menu_options = [("view",display.view),("message_delete",display.delete),("cancel",display.cancel)]

            while True:
                # Affiche le menu avec menu_options
                option = show_menu(menu_options)

                # Si l'option est choisie on affiche le message
                if option[2] == 'view':
                    view(decoded_message)

                # Si l'option est choisie on supprime les fichiers
                elif option[2] == 'message_delete':
                    delete_all()
                    s.show_message("Message et code supprimes", scroll_speed=0.06)
                    break


if __name__ == "__main__":
    # Appelle la fonction qui lance le programme
    main()
