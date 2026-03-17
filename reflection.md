# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the secret number kept changing" or "the hints were backwards").

    - The hint is implemented incorrectly. It seems displaying the hint randomly not following any logic
    - There is one attempt left, but the game exits
    - New game button doesn't work properly. It is supposed to reset the game and let the player play new game. However, when clicking on it, it keeps saying "You already won. Start a new game to play again."
---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
    - I used Copilot on this project
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
    - When finishing the game, the attempt left displayed 1. It causes confusion to the player. I used Copilot and asked what caused the issue.
    - The issue is that "attempts" is initialized as 1 and also increments 1 on every submit. 
    - The suggestion is to initialize the "attempts" = 0 and change the loss condition from >= to >, so the game ends after limit guesses, not before
    - To verify what AI suggested, I went to the file where the code is inaccurate and examine by myself. Once I agreed with the fixed suggestion, I re-runed the game and check whether the bug was fixed.
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
    - I ran the pytest and retry the game to see if the bug was successfully fixed
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
    - For the hint issues, I ran the test on both ways (pytest and mannual).
    - After successfully passing all the test cases in test_game_logic, I tried to play the game several time to make sure the bug is gone
- Did AI help you design or understand any tests? How?
    - Yes. AI helped me understand the test case. It explains to me what purpose of each cases and how it works

---

## 4. What did you learn about Streamlit and state?

- In your own words, explain why the secret number kept changing in the original app.
    - The secret number kept chaning in the original app because it was re-created with random function during each script rerun. In Streamlit, every action like clicking button or typing input will rerun the whole file. As a result, the random function will generate new secret number when an event happens
- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
    - Streamlit's rerun is like a game where there are no checkpoints. If your teammate (the user) makes a single move—like toggling a switch or clicking a button—the whole team has to start the level from the very beginning to make sure the entire game state stays in sync.
- What change did you make that finally gave the game a stable secret number?
    - I updated app.py so the secret number stays stable across Streamlit reruns by keeping it in st.session_state and only regenerating it during intentional resets. I also added difficulty-change handling with a last_difficulty state key, so when the user switches difficulty, the game resets cleanly with a new in-range secret, attempts reset, status reset to "playing", and history cleared

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
      - One habit from this project that I want to reuse in the future projects is that having a testing cases. I found it very essential and save time of debugging and testing
- What is one thing you would do differently next time you work with AI on a coding task?
      - Having a better and more structured prompt is the area I want to imporove when work with AI on a coding task. 
- In one or two sentences, describe how this project changed the way you think about AI generated code.
      - This project highlighted the importance of prompt engineering and taught me to isolate bugs into separate chat sessions. This prevents the AI from getting confused by previous context and ensures more accurate fixes.
