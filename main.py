from game_manager import GameManager
from app_ui import AppUI, show_result

WORDS_FILE = "words.txt"
NUM_WORDS_RETRIEVE = 150
SECONDS_TO_SCROLL = 15
TEST_SECONDS = 60
timer_test = None


def stop_test() -> None:
    """
    Stops the timer, updates the UI and calls the function to show the result
    :return: it doesn't return a value
    """
    global timer_test

    screen.after_cancel(timer_test)
    screen.stop_game()
    timer_test = None

    game.check_words_against_wordlist(screen.get_typed_words())
    show_result(game.words_per_min, game.chars_per_min)
    show_result(wrong_words="\n".join(game.wrong_words))


def start_test(count: int = None) -> None:
    """
    Starts the timer of the test and keeps executing this function until the game ends or the user stop the test
    :param count: an integer with the number of seconds remaining
    :return: it doesn't return a value
    """
    global timer_test

    if timer_test:
        if count and count > TEST_SECONDS:
            screen.update_button_text(count - TEST_SECONDS)
        elif count and count == TEST_SECONDS:
            # If count it's equal to the test amount of seconds start the test
            screen.start_game(game.retrieve_words_from_file(WORDS_FILE, NUM_WORDS_RETRIEVE))
            screen.update_button_text(count - TEST_SECONDS)

        if count and count > 0:
            # If count it's greater than 0, remove a second and exec this function in 1 second
            timer_test = screen.after(1000, start_test, count - 1)
        elif count == 0 or not count:
            # If count it's equal to 0 or user pressed "Stop" button, exec stop_test function
            stop_test()

        if count and count < TEST_SECONDS and count % SECONDS_TO_SCROLL == 0:
            # Scroll the field every SECONDS_TO_SCROLL where word list is if there are many words in it
            screen.txt_words.yview_scroll(1, "units")

    else:
        # If timer is None, start the test with a 5 seconds addition
        timer_test = screen.after(1000, start_test, TEST_SECONDS + 5)


screen = AppUI(start_test)
game = GameManager()
screen.mainloop()
