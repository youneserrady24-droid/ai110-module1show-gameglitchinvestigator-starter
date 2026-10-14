
from pathlib import Path

from streamlit.testing.v1 import AppTest

from logic_utils import check_guess

APP_PATH = str(Path(__file__).resolve().parent.parent / "app.py")

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    outcome, message = check_guess(50, 50)
    assert outcome == "Win"
    assert message == "🎉 Correct!"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"
    assert message == "📉 Go LOWER!"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"
    assert message == "📈 Go HIGHER!"

def test_new_game_button_restarts_game():
    # Put the game in a finished, mid-play state, then press "New Game"
    at = AppTest.from_file(APP_PATH).run()
    at.session_state.status = "lost"
    at.session_state.attempts = 5
    at.session_state.score = 40
    at.session_state.history = [10, 20, 30]

    new_game_button = next(b for b in at.button if b.label.startswith("New Game"))
    new_game_button.click().run()

    assert not at.exception
    assert at.session_state.status == "playing"
    assert at.session_state.attempts == 0
    assert at.session_state.score == 0
    assert at.session_state.history == []
    low, high = 1, 100  # default difficulty is Normal
    assert low <= at.session_state.secret <= high
