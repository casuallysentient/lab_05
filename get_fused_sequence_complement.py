def get_fused_sequence_complement(sequence_a, sequence_b):
    """
    This function receives two sequences of DNA and combines them, iterating over
    the two sequences and alternating between characters from each one. If one
    sequence is longer than the other, it will only add characters from both until
    the shorter sequence runs out of characters, at which point it will simply add
    the characters from the longer string onto the end. After it has completed
    this, it passes the combo string to get_complement, which returns a complement
    DNA string that this function then returns to its reference in main().

    :param sequence_a: the first of the two sequences passed
    :param sequence_b: the second of the two sequences passed
    :return: the complement of the combo of the two strings received
    """
    combo_sequence = ""
    if len(sequence_a) >= len(sequence_b):
        longer_sequence = sequence_a
    else:
        longer_sequence = sequence_b
    for x in range(len(longer_sequence)):
        if len(sequence_a) > x:
            if sequence_a[x] in ("A", "T", "C", "G"):
                combo_sequence = combo_sequence + sequence_a[x]
        if len(sequence_b) > x:
            if sequence_b[x] in ("A", "T", "C", "G"):
                combo_sequence = combo_sequence + sequence_b[x]
    comp_sequence = get_complement(combo_sequence)
    return comp_sequence


def get_complement(combo_sequence):
    """
    This function receives a combined DNA strand from get_fused_sequence_complement
    and iterates over the string, constructing a new string where each character
    is the pairing nucleotide to the original character.

    :param combo_sequence: the already-combined sequence of the two initial
    sequences
    :return: the complement sequence to the one passed in
    """
    comp_sequence = ""
    for x in range(len(combo_sequence)):
        char = combo_sequence[x]
        if char == "A":
            comp_sequence += "T"
        elif char == "C":
            comp_sequence += "G"
        elif char == "T":
            comp_sequence += "A"
        elif char == "G":
            comp_sequence += "C"
    return comp_sequence


def main():
    """
    Just some sample behavior. Feel free to try your own!
    """
    sequence_a = "XXATGTGT"
    sequence_b = "ACGTGTATGCTGTGTGTACGTGTGATCG"
    fused_sequence_complement = get_fused_sequence_complement(sequence_a, sequence_b)
    print(fused_sequence_complement)


# DO NOT WRITE CODE BELOW THIS LINE

if __name__ == '__main__':
    main()
