# write tests for parsers
import io

from seqparser import (
        FastaParser,
        FastqParser)



def test_freebie_parser_1():
    """
    This one is a freebie
    DO NOT MODIFY THIS FUNCTION
    """
    assert True


def test_freebie_parser_2():
    """
    This too is a freebie
    DO NOT MODIFY THIS FUNCTION
    """
    assert 1 != 2


def test_freebie_parser_1():
    """
    This one is a freebie
    DO NOT MODIFY THIS FUNCTION
    """
    assert True


def test_freebie_parser_2():
    """
    This too is a freebie
    DO NOT MODIFY THIS FUNCTION
    """
    assert 1 != 2


def test_fastq_all_elements_present():
    parser = FastqParser('data/test.fq')  # Assuming FastqParser reads from a file
    for record in parser:
        # Check if all elements (header, sequence, and quality) are present in the record
        header, sequence, quality = record
        
        assert header, "Header is missing in the FASTQ record"
        assert sequence, "Sequence is missing in the FASTQ record"
        assert quality, "Quality scores are missing in the FASTQ record"
    
                    