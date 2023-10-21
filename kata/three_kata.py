# https://www.codewars.com/kata/5556282156230d0e5e000089/train/python

def dna_to_rna(dna: str):
    """
    Translate DNA to RNA
    :param dna: str
    :return: rna: str
    """

    if all(letter in ("G", "C", "A", "T") for letter in dna):
        return dna.replace("T", "U")
    return "Bad DNA"
