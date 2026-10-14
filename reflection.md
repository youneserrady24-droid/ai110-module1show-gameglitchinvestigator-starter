# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?

The game displays a prompt asking the player to guess a number within a specified range. Below the prompt, there is a text box where the player can enter their guess. The interface also includes a checkbox that can be selected to enable hints, along with two buttons: "New Game" and "Submit a Guess."

A sidebar on the left allows the player to select the desired difficulty level.

- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").

 1. New Game button does not refresh the game
 2. Out-of-range guesses are accepted
 3. Hints provide incorrect information
 4. Incorrect number of attempts at the start of the game
 5. The info banner always says "between 1 and 100" whatever the difficulty

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input   | Expected Behavior   | Actual Behavior            | Console Output / Error |
|---------|---------------------|----------------------------|------------------------|
| 0       | Number out of range |Accepts it as a valid guess |app.py:14-29            |
|New Game | Starts a new game   |Doesn't refresh, gets stuck |app.py:134-138          |
| Hint    | Gives a correct hint|Hints give incorrect answer |app.py:37-40            |

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
I used Claude and ChayGpt 
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
The fix for when the "New Game" button is pressed by the user but doesn't refresh, the claude agent added new line on the check_guess() function to set the game back to "playing" status and not just stop it
- Give one example of an AI suggestion you did not accept as written (including what the AI suggested, why you rejected or changed it, and how you verified your version). It does not have to be a suggestion that was wrong: over-engineered, out of scope, harder to read, or a poor fit for this codebase all count.
I rejeted its pytest since it didn't run correctly, it was checking if the guesses were correct, too high or too low icorrectly. Instead of asserting the output of check_guess method with a tuple, it checked it using a string only.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
I checked it in the game directly.
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
  I tested the New Game button manually and it showed me that the code now starts a new session and takes on new guesses like it was supposed to.
- Did AI help you design or understand any tests? How?
Yes, it helped with the fixes and explained them, also the tests it ran were easy to understand and follow while also being effictive. 

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
  I want to reuse the habit of running tests after making changes to catch bugs early and make sure the code still works as expected. I also want to use Git to track my changes and commit my work regularly.

- What is one thing you would do differently next time you work with AI on a coding task?
  Next time, I would ask the AI to explain the changes it makes and work on smaller parts of the code at a time. This would help me understand the code better and identify mistakes more easily.

- In one or two sentences, describe how this project changed the way you think about AI generated code.
  This project taught me that AI-generated code can be helpful, but it is not always correct and can introduce bugs. I learned that I need to review the code, understand how it works, and test it before trusting it.