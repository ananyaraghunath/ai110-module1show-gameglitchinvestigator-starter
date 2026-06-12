from logic_utils import (
    check_guess,
    get_range_for_difficulty,
    update_score,
    parse_guess,
)




def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    outcome, _ = check_guess(50, 50)
    assert outcome == "Win"


def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    outcome, _ = check_guess(60, 50)
    assert outcome == "Too High"


def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    outcome, _ = check_guess(40, 50)
    assert outcome == "Too Low"


# --- Bug-targeting tests added after fixing each bug ---


def test_check_guess_hint_direction_not_reversed():
    # BUG #8: original messages were reversed ("Too High" said "Go HIGHER!").
    # A guess that is too high should tell the player to go LOWER, and vice versa.
    _, high_msg = check_guess(60, 50)
    _, low_msg = check_guess(40, 50)
    assert "LOWER" in high_msg
    assert "HIGHER" in low_msg


def test_check_guess_handles_large_numbers_as_ints():
    # BUG #1:  9 vs 10 must be "Too Low" (numeric), not "Too High".
    outcome, _ = check_guess(9, 10)
    assert outcome == "Too Low"
    # And 100 vs 20 must be "Too High" numerically 
    outcome, _ = check_guess(100, 20)
    assert outcome == "Too High"


def test_hard_is_harder_than_normal():
    # BUG #2: "Hard" returned a SMALLER range (1-50) than "Normal" (1-100),
    # making it easier. Hard's range must be at least as wide as Normal's.
    _, normal_high = get_range_for_difficulty("Normal")
    _, hard_high = get_range_for_difficulty("Hard")
    assert hard_high > normal_high


def test_win_on_first_attempt_scores_full_points():
    # BUG #7a: win points used (attempt_number + 1), so a first-guess win scored
    # less than 100. A win on attempt 1 should add the full 100 points.
    assert update_score(0, "Win", 1) == 100


def test_wrong_guess_penalty_is_symmetric():
    # BUG #7b: "Too High" awarded +5 on even attempts while "Too Low" subtracted
    # 5 -> a wrong guess could RAISE your score. Both directions must penalize
    # equally regardless of attempt number.
    assert update_score(100, "Too High", 2) == update_score(100, "Too Low", 2)
    assert update_score(100, "Too High", 3) == update_score(100, "Too Low", 3)


