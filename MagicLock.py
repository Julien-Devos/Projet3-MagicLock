def main():
    # Le nom du fichier de QCM à utiliser
    filename = 'QCM2.txt'

    try:
        # Load questions from file
        questions = load_questions(filename)

        # User choose the score mode
        scores = select_rating_mode()

        print("Bienvenu(e) dans notre programme de QCM !"
              "\n\tPour répondre aux questions, rentrez la lettre associée aux propositions de réponses."
              "\n\tSi vous pensez qu'il y a plusieurs réponses, écrivez les en séparant chaque réponse par une virgule !\n"
              "\n********************************\n")

        qcm_loop(questions, scores)

        print("\nLe questionnaire est terminé !")

    except OSError:
        print("Il y a un problème avec le fichier de questionnaire !")