from kata import three_kata


def test_three_kata_ok():
    dna = "GACCGCCGCC"
    result = three_kata.dna_to_rna(dna)
    assert result == "GACCGCCGCC"
