def friend(x):
    return [name for name in x if len(name) == 4]


# friend ["Ryan", "Kieran", "Mark"] `shouldBe` ["Ryan", "Mark"]

friends = ["Ryan", "Kieran", "Mark"]


def test_positive():
    assert friend(friends) == ["Ryan", "Mark"]
