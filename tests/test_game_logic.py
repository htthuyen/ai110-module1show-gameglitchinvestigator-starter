from logic_utils import check_guess

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    outcome, hint = check_guess(50, 50)
    assert outcome == "Win"
    assert "Correct" in hint

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    outcome, hint = check_guess(60, 50)
    assert outcome == "Too High"
    assert "LOWER" in hint

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    outcome, hint = check_guess(40, 50)
    assert outcome == "Too Low"
    assert "HIGHER" in hint


def test_hint_direction_regression_for_swapped_messages():
    """Regression: too-high must say lower, too-low must say higher."""
    high_outcome, high_hint = check_guess(60, 50)
    low_outcome, low_hint = check_guess(40, 50)

    assert high_outcome == "Too High"
    assert "LOWER" in high_hint

    assert low_outcome == "Too Low"
    assert "HIGHER" in low_hint


