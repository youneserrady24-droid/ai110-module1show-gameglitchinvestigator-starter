# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

- [] **Describe the game's purpose.**
  The app picks a secret number within a range set by the difficulty (Easy: 1–20, Normal: 1–100, Hard: 1–50), and the player tries to guess it within a limited number of attempts. After each guess the game gives a "Go HIGHER" / "Go LOWER" hint and updates a score that rewards winning in fewer attempts.

- [] **Detail which bugs you found.**
  1.  Guessing too high told you to "Go HIGHER", and guessing too low told you to "Go LOWER".
  2.  On even attempts the secret is passed as a string, so the old `check_guess` compared strings alphabetically (for example `"9" > "50"`), which gave wrong hints and could make a correct guess not count as a win.
  3. Entering `0` or a number above the difficulty's maximum counted as a normal guess.
  4. Typing a non-number or leaving the box empty still increased the attempt counter.
  5. New Game didn't fully reset. It only reset attempts and the secret, so after a win or loss the status stayed "won"/"lost" and the game stayed locked.
  6. The banner always said "between 1 and 100", whatever the difficulty, and the attempt counter starts at 1 instead of 0. (I noticed these but haven't fixed them.)

- [] **Explain what fixes you applied.**
  - Refactor: Moved `get_range_for_difficulty`, `parse_guess`, `check_guess`, and `update_score` out of `app.py` into `logic_utils.py`, and imported them back into the app.
  - `check_guess` now converts both values to `int` before comparing, so comparisons are numeric. It returns "Go LOWER" when the guess is too high and "Go HIGHER" when it is too low.
  -  `parse_guess` now takes `low`/`high` and rejects guesses outside the range with "Guess must be between {low} and {high}."
  -  The attempt counter now goes up only after a valid guess.
  - New Game: It now resets `status` to "playing", clears `history` and `score`, and picks the new secret from the current difficulty's range.
  
## 📸 Demo Walkthrough

A sample game on Normal difficulty (range 1–100, 8 attempts), with the secret number 58 (shown in Developer Debug Info):

1. User clicks 'New Game', so the game resets with 0 attempts and a score of 0.
2. User enters a guess of 40, and the game returns "Too Low" with the hint "📈 Go HIGHER!" (attempt 1, score −5).
3. User enters a guess of 70, and the game shows "Too High" with the hint "📉 Go LOWER!" (attempt 2, score 0).
4. User enters 150, and the game rejects it with "Guess must be between 1 and 100." The attempt isn't counted (still 2), and the score stays 0.
5. User enters a guess of 55, and the game returns "Too Low" with "📈 Go HIGHER!" (attempt 3, score −5).
6. User enters a guess of 58, and the game shows "🎉 Correct!" with balloons and "You won! The secret was 58. Final score: 45" (attempt 4, +50 points for winning).
7. The game ends. Clicking Submit again shows "You already won. Start a new game to play again." until the user clicks **New Game 🔁**.

## 🧪 Test Results

```
========================================================================================= test session starts ==========================================================================================
platform win32 -- Python 3.14.7, pytest-9.1.1, pluggy-1.6.0 -- C:\Users\errad\ai110-module1show-gameglitchinvestigator-starter\.venv\Scripts\python.exe
cachedir: .pytest_cache
rootdir: C:\Users\errad\ai110-module1show-gameglitchinvestigator-starter
plugins: anyio-4.15.1
collected 4 items                                                                                                                                                                                       

tests/test_game_logic.py::test_winning_guess PASSED                                                                                                                                               [ 25%]
tests/test_game_logic.py::test_guess_too_high PASSED                                                                                                                                              [ 50%]
tests/test_game_logic.py::test_guess_too_low PASSED                                                                                                                                               [ 75%]
tests/test_game_logic.py::test_new_game_button_restarts_game PASSED                                                                                                                               [100%]

========================================================================================== 4 passed in 1.01s ===========================================================================================
```

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, describe the Enhanced UI changes here — a screenshot is optional]
