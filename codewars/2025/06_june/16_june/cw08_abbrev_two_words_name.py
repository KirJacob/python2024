def abbrev_name(name):
    return ".".join(list(map(lambda name: name[0].capitalize(), name.split(" "))))


def test_abbrev_name():
    assert abbrev_name("Sam Harris") == "S.H"
    assert abbrev_name("patrick feenan") == "P.F"
    assert abbrev_name("Evan C") == "E.C"
