# write tests for transcribes
from seqparser import (
        transcribe,
        reverse_transcribe)
    
def test_freebie_transcribe_1():
    """
    This one is a freebie
    DO NOT MODIFY TIS FUNCTION
    """
    assert True


def test_freebie_transcribe_2():
    """
    This too is a freebie
    DO NOT MODIFY THIS FUNCTION
    """
    assert 1 != 2

        
def test_transcribe():
    """
    TODO: Write your unit test for the
    transcribe function here.
    """
    pass


def test_reverse_transcribe():
    """
    TODO: Write your unit test for the
    reverse transcribe function here.
    """
    pass

   
def test_transcription():
    # List of individual DNA bases and their expected RNA bases
    test_cases = [
        ('A', 'A'), 
        ('T', 'U'),  # Should not see Thymine in result
        ('G', 'G'),  
        ('C', 'C'),  
    ]

    # Loop through each base
    for dna_base, expected_rna_base in test_cases:
        transcribed_base = transcribe(dna_base)
        # Check if the transcribed base matches the expected RNA base
        assert transcribed_base == expected_rna_base, (
            f"Test failed for base {dna_base}: Expected {expected_rna_base}, but got {transcribed_base}"  )
        


def test_all_thymine_sequence():
    dna_sequence = "TTTT"
    expected_rna_sequence = "UUUU"
    transcribed_sequence = transcribe(dna_sequence)
    
    assert transcribed_sequence == expected_rna_sequence, f"Expected {expected_rna_sequence}, but got {transcribed_sequence}"

def test_lowercase_input():
    dna_sequence = "atgc"
    expected_rna_sequence = "AUGC"  
    transcribed_sequence = transcribe(dna_sequence.upper())  # Convert input to uppercase if needed
    
    assert transcribed_sequence == expected_rna_sequence, f"Expected {expected_rna_sequence}, but got {transcribed_sequence}"
    print("Lowercase input test passed.")