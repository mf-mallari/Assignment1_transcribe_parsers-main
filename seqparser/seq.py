# DNA -> RNA Transcription


def transcribe(seq: str) -> str:
    """
    TODO: transcribes DNA to RNA by generating
    the complement sequence with T -> U replacement
    """
    # Replace all occurrences of 'T' with 'U' to transcribe DNA to RNA
    rna_sequence = seq.replace('T', 'U')

    return rna_sequence



def reverse_transcribe(seq: str) -> str:
    """
    TODO: transcribes DNA to RNA then reverses
    the strand
    """
    # Transcribe the DNA to RNA first
    transcribed_sequence = transcribe(seq)


    # Reverse the transcribed RNA sequence
    reversed_rna_sequence = transcribed_sequence[::-1]    
    
    return reversed_rna_sequence

#Transcibes DNA > RNA from a imported file
def transcribe_from_file(input_file: str, output_file: str):
    """
    Reads a DNA sequence from the input file, transcribes it to RNA,
    and writes the transcribed RNA to the output file.
    """
    # Read the DNA sequence from the input file
    with open(input_file, 'r') as file:
        dna_sequence = file.read().strip()  # Strip any extra whitespace or newlines
    
    # Transcribe the DNA sequence to RNA
    rna_sequence = transcribe(dna_sequence)
    
    # Write the RNA sequence to the output file
    with open(output_file, 'w') as file:
        file.write(rna_sequence)

#Final step: reverses the RNA seqnce to the complement
def reverse_transcribe_from_file(input_file: str, output_file: str):
    """
    Reads a DNA sequence from the input file, transcribes and reverses it,
    and writes the reversed RNA sequence to the output file.
    """
    # Read the DNA sequence from the input file
    with open(input_file, 'r') as file:
        dna_sequence = file.read().strip()  # Strip any extra whitespace or newlines
    
    # Reverse-transcribe the DNA sequence
    reversed_rna_sequence = reverse_transcribe(dna_sequence)
    
    # Write the reversed RNA sequence to the output file
    with open(output_file, 'w') as file:
        file.write(reversed_rna_sequence)





"""
#example
input_file = "test.fa"  # test file
output_file_transcribe = "rna_sequence.txt"  # File to write the transcribed RNA sequence
output_file_reverse_transcribe = "Final_output_RNA_Complement.txt"  # File to write the reversed RNA sequence

# Transcribe DNA to RNA and write to file
transcribe_from_file(input_file, output_file_transcribe)

# Reverse-transcribe DNA to RNA and write to file
reverse_transcribe_from_file(input_file, output_file_reverse_transcribe)

#Make sure to be in the correct directory to call the file
print("Transcription and reverse transcription complete. Check the output files.")

"""