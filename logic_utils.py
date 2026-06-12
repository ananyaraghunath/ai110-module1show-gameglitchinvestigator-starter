import random


def get_range_for_difficulty(difficulty: str):
    """Return (low, high) inclusive range for a given difficulty."""
    # FIX: Refactored from app.py into logic_utils.py using agent mode.
    # Bug was inverted difficulty: "Hard" returned 1-50 (a SMALLER range than
    # "Normal" 1-100), making Hard easier. AI suggested ordering the ranges so
    # each tier is strictly wider than the previous one.
    if difficulty == "Easy":
        return 1, 20
    if difficulty == "Normal":
        return 1, 100
    if difficulty == "Hard":
        return 1, 200
    return 1, 100


def parse_guess(raw: str):
    """
    Parse user input into an int guess.

    Returns: (ok: bool, guess_int: int | None, error_message: str | None)
    """
    # FIX: Refactored verbatim from app.py into logic_utils.py using agent mode.
    # Logic was already correct, so we kept the behavior (including truncating
    # "3.9" -> 3) and only moved it out of the UI layer.
    if raw is None:
        return False, None, "Enter a guess."

    if raw == "":
        return False, None, "Enter a guess."

    try:
        if "." in raw:
            value = int(float(raw))
        else:
            value = int(raw)
    except Exception:
        return False, None, "That is not a number."

    return True, value, None


def check_guess(guess, secret):
    """
    Compare guess to secret and return (outcome, message).

    outcome examples: "Win", "Too High", "Too Low"
    """
    # FIX: Refactored into logic_utils.py and removed the headline glitch using
    # agent mode.
    """
    Compare guess to secret and return (outcome, message).
    FIX: Hints were inverted. Fixed comparison logic.
    FIX: Always cast to int to avoid string comparison bug.
    """
    secret = int(secret)

    if guess == secret:
        return "Win", "🎉 Correct!"
    if guess > secret:
        return "Too High", "📈 Go LOWER!"
    return "Too Low", "📉 Go HIGHER!"


def update_score(current_score: int, outcome: str, attempt_number: int):
    """Update score based on outcome and attempt number."""
    # FIX: Refactored into logic_utils.py and fixed scoring using agent mode.
    # Two bugs: (1) win points used `attempt_number + 1` even though attempts is
    # already incremented before this call, double-penalizing the player;
    # (2) "Too High" awarded +5 on even attempts (rewarding a wrong guess) while
    # "Too Low" always subtracted 5. AI suggested a consistent rule: first-guess
    # win = 100, each later attempt costs 10 (floored at 10), and any wrong guess
    # costs a flat 5 regardless of direction.
    if outcome == "Win":
        points = 100 - 10 * (attempt_number - 1)
        if points < 10:
            points = 10
        return current_score + points
    if outcome == "Too High":
        return current_score - 5
    if outcome == "Too Low":
        return current_score - 5
    return current_score
