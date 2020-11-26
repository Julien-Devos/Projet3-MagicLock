from sense_hat import SenseHat
import time
import displays as display  #importe le fichier qui comporte toutes les listes pour l'affichage

s = SenseHat()
s.low_light = True

state = {
    "menu_index" : 0
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
    choice = menu[state["menu_index"] % len(menu)]
    s.set_pixels(choice)


def choosed_option(menu):
    """ Permet de continuer le programme en fonction de l'option choisie dans le menu

        Args:
            menu: list: une liste des listes de pixels qui composent l'affichage
    """
    choice = menu[state["menu_index"] % len(menu)]

    print("Vous avez choisis l'option n°" + str(state["menu_index"] % len(menu) + 1))


def show_menu(menu):
    """ Permet d'appeller la fonction display_choice et de mettre à jour
        l'index en fonction des déplacements du joystick

        Args:
            menu: list: une liste des listes de pixels qui composent l'affichage
    """
    choosed = False

    s.set_pixels(menu[0])
    while not choosed:
        events = s.stick.get_events()
        if events:
            for event in events:
                if event.action != "pressed":
                    continue

                if event.direction == 'left':
                    state["menu_index"] += 1
                    display_choice(menu)

                elif event.direction == 'right':
                    state["menu_index"] -= 1
                    display_choice(menu)

                elif event.direction == 'middle':
                    choosed = True
                    choosed_option(menu)


def main():
    while True:
        #demande le code pin à l'utilisateur
        pin()

        if check_msg():
            """ Demander d'enregistrer un message """
            print("Pas de message enregistré")

            menu_options = [display.save,display.cancel]

            #Permet d'afficher le menu des options -> (Enregistrer un message ou annuler et revérouiller le MagicLock)
            show_menu(menu_options)


        else:
            """ Propose les options du message """
            print("Un message est enregistré")
            raise SystemExit


if __name__ == "__main__":
    main()