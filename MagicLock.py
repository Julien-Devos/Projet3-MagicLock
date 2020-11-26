from sense_hat import SenseHat
import time
from displays import *

s = SenseHat()
s.low_light = True

state = {
    "menu_index" : 0
    }

def pin():
    correct_pin = [("pressed", "up"), ("released", "up"), ("pressed", "down"), ("released", "down"),
                   ("pressed", "left"),
                   ("released", "left"), ("pressed", "right"), ("released", "right")]
    pin_correct = False
    current_pin = []

    while not pin_correct:
        s.set_pixels(screen_off)
        event = s.stick.wait_for_event()
        current_pin.append((event.action, event.direction))

        if current_pin == correct_pin:
            pin_correct = True
            print("Pin correct")
            s.set_pixels(correct)
            time.sleep(1)

        elif len(current_pin) == len(correct_pin):
            current_pin = []
            print("Wrong pin !")
            s.set_pixels(cancel)
            time.sleep(1)

    # TODO mettre un affichage de leds

def check_msg():
    with open("message", 'r') as message:
        if message.readlines() == ["\n"]:
            return True
        else:
            return False

def display_choice(menu):
    choice = menu[state["menu_index"] % len(menu)]

    s.set_pixels(choice)
    """if choice == save:
        s.set_pixels(save)

    elif choice == cancel:
        s.set_pixels(cancel)"""


def choosed_option(menu):
    choice = menu[state["menu_index"] % len(menu)]

    print("Vous avez choisis l'option n°" + str(state["menu_index"] % len(menu) + 1))

def show_menu(menu):
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


while True:
    # demande le code pin à l'utilisateur
    pin()

    if check_msg():
        """ Demander d'enregistrer un message """
        print("vide")

        menu_options = [save,cancel]

        show_menu(menu_options)



    else:
        """ propose les options du message """
        print("pas vide")
        raise SystemExit

