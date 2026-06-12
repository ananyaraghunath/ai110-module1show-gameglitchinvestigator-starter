# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").
- When you start the game, and submit the first guess, it doesnt save to history, or count it as a guess. It saves after the next submission and starts off assuming 1 attempt already
- The hints are backwards, when should be higher, it says lower
- Upon first start up it will say 7 attempts left, but if you press new game it'll say 8 attempts left. And when new game is pressed, the history is not reset. Essentially, New Game doesn't actually reset the game.

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
| ----- | ----------------- | --------------- | ---------------------- |
| 1     | "Go Higher" hint  | "Go Lower" Hint | None                   |
| 112   | Out of bound      | "Go Higher hint | None                   |
| -1    | Out of bound      | "Go Lower" hint | None                   |

---

## 2. How did you use AI as a teammate?

I used Claude Code (Anthropic's CLI assistant) as my primary AI tool throughout this project for bug analysis, refactoring, and test generation.

**Correct AI suggestion — the even-attempt string comparison bug:**
Claude caught that on every even attempt the game was comparing numbers as text instead of as numbers, which flipped the hints. It suggested always comparing them as numbers. I wrote a test to confirm a smaller number correctly returns "Too Low" and a larger one returns "Too High" — both passed after the fix.

**Incorrect/misleading AI suggestion — scoring rule for wrong guesses:**
One area where the AI was misleading was when I asked Copilot to refactor the scoring logic — it suggested keeping the even-attempt condition but just flipping the sign, which still would have made scoring inconsistent depending on what attempt number you were on. I caught that by running a quick manual test with a few wrong guesses in a row and noticing the score was still behaving unevenly, so I ended up removing that condition entirely instead.

---

## 3. Debugging and testing your fixes

I decided a bug was truly fixed only when both the code path looked correct _and_ a targeted pytest test that could have caught the original bug now passed cleanly.

## For each bug I fixed, Claude generated a pytest case specifically designed to fail against the _original_ broken code. Claude also helped me understand _why_ one test would catch a specific bug

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
  I would explain Streamlit reruns like a robot witout memory because one you ask you get an answer an then they forget all about it or change. Then I would explain the session states like the memory of the robot because a session state remembers the information while you are using the app. This way the both work together, one runs the program and the other makes sure to remember what happened.

---

## 5. Looking ahead: your developer habits

I think one strategy I want to reuse in being methodic and organized with finding bugs and 'marking the crime scene". I believe this helpend me a lot when fixing the bugs this way I don't have to constantly memorize what to do next because it's already there. I found this strategy more effective and less time consuming. One thing I would do differently is test handeling. I want to try to create the tests on my own first and then double check with AI this way I don't feel like I can't handle testing well. Overall, for next time I want to use AI as a backup for testing instead of heavily rely on it. I found AI generated code to be effective when given the right amount of information. I also consider that it helped me learn more about effcient ways to handle testing and avoid redundant code.
