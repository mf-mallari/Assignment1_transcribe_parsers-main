import io
from typing import Tuple, Union


class Parser:
    """
    Base Class for Parsing Algorithms
    """
    def __init__(self, filename: str):
        """
        Initialization to be shared by all inherited classes.
        
        # Recall that this is where we store baseline attribute of a class. For example:
            class Cat: 
                def __init__(self, weight: float, breed: str, food: str):
                    self.weight = weight
                    self.breed = breed
                    self.food = food
                    
        # What attributes are we initializing here in Parser? 
        """
        self.filename = filename  # Path to the file
        self.file_object = None  # File object after opening the file
        self.current_record = None  # The current record being processed
        self.sequence_format = None  # File format, e.g., 'FASTA', 'FASTQ'


    def get_record(self, f_obj: io.TextIOWrapper) -> Union[Tuple[str, str], Tuple[str, str, str]]:
        """
        Returns a sequencing record that will either be a tuple of two strings (header, sequence)
        or a tuple of three strings (header, sequence, quality). 

        """
        return self._get_record(f_obj)

    #Allows the parser to be used as an iterator to yield records one by one
    def __iter__(self):
       
        with open(self.filename, "r") as f_obj:  # Open the file here
            while True:
                try:
                    rec = self.get_record(f_obj)  # Pass the file object to get_record
                    yield rec  # Yield the record
                except StopIteration:
                    break  # Stop the loop when no more records are available       
    

    def _get_record(self, f_obj: io.TextIOWrapper) -> Union[Tuple[str, str], Tuple[str, str, str]]:
        """
        a method to be overridden by inherited classes.
        """
        raise NotImplementedError(
                """
                This function is not meant to be called by the Parser Class.
                It is expected to be overridden by `FastaParser` and `FastqParser`
                """)

# Reads the next FASTA record from the file object and returns a 2-tuple (header, sequence).
class FastaParser(Parser):
    """
    Fasta Specific Parsing.
    """
    def _get_record(self, f_obj: io.TextIOWrapper) -> Tuple[str, str]:
        header = f_obj.readline().strip()
            
        if not header:  # End of the file
            raise StopIteration
        
        # Check if the header starts with '>', if not, add it
        if not header.startswith(">"):
            print(f"Warning: Header does not start with '>'. Adding '>' to: {header}")

        # Initialize an empty list to collect sequence lines
        sequence_lines = []
        # Read the sequence lines until the next header or end of the file
        while True:
            line = f_obj.readline().strip()
            if not line or line.startswith(">"):
                    # If we hit a new header or the end of the file, stop reading
                    f_obj.seek(f_obj.tell() - len(line))  # Rewind to the start of the new header
                    break
            sequence_lines.append(line)

        # Join the sequence lines into a single string and return the header and sequence
        return header, "".join(sequence_lines)

class FastqParser(Parser):
    """
    Fastq Specific Parsing 
    """
    def _get_record(self, f_obj: io.TextIOWrapper) -> Tuple[str, str, str]:
        # Read the header line (starts with '@')
        header = f_obj.readline().strip()
        if not header:  # End of the file
            raise StopIteration
        if not header.startswith("@"):
            raise ValueError("FASTQ format error: Header does not start with '@'")

        # Read the sequence
        sequence = f_obj.readline().strip()

        # Read the plus line (must be '+')
        plus_line = f_obj.readline().strip()
        if plus_line != "+":
            raise ValueError("FASTQ format error: Missing '+' separator")

        # Read the quality line (same length as the sequence)
        quality = f_obj.readline().strip()

        if len(sequence) != len(quality):
            raise ValueError("FASTQ format error: Sequence and quality scores must be the same length")

        return header, sequence, quality

"""
fastq_parser = FastqParser("test.fq")

# Iterate over the records in the FASTQ file and print them
for record in fastq_parser:
    print(record)

# Test the FastaParser
if __name__ == "__main__":
    fasta_parser = FastaParser("test.fa")
    for record in fasta_parser:
        print(record)
"""