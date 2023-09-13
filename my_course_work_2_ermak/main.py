from my_course_work_2_ermak.basic_word import BasicWord
from my_course_work_2_ermak.players import Player
from my_course_work_2_ermak.utils import load_random_word


def main():
    player: Player = Player(
        input("Введите имя игрока\n")
    )

    word: BasicWord = load_random_word()

    player_word = ""

    print(
        f"Привет, {player}!\n"
        f"Составьте {word.subwords_amount} слов "
        f"из слова {word}\n"
        f"Слова должны быть не короче 3 букв\n"
        f"Чтобы закончить игру, угадайте все слова "
        f"или напишите 'stop'\n"
        f"Поехали, ваше первое слово?"
    )

    while all(
            (player.words_count < word.subwords_amount,
             player_word not in ("stop", "стоп"))
    ):
        if len((player_word := input())) < 3:
            print("Слова должны быть не короче 3 букв")
            continue

        if word.is_correct(player_word):
            if not player.is_used(player_word):
                player.add(player_word)
                print("верно")
            else:
                print("уже использовано")
        else:
            print("неправильно")

    print(f"Игра завершена, вы угадали {player.words_count} слов!")


if __name__ == "__main__":
    main()
