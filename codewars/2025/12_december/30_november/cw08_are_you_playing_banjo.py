def are_you_playing_banjo(name):
    if name[0].lower() == 'r':
        return f"{name} plays banjo"
    else:
        return f"{name} does not play banjo"

def test_delete_nth():
    assert are_you_playing_banjo("Robert") == "Robert plays banjo"
    assert are_you_playing_banjo("Jack") == "Jack does not play banjo"