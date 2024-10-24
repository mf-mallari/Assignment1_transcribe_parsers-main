
# Assignment 1: 

## Assignment Overview
The purpose of this assignment is to get you comfortable with:

* Reading code
* Practice Object Oriented Programming
* Using Loops, conditional statements and different data structures
* Testing your code with PyTest
* Using GitHub
* Creating a local installable package

## Objectives
    A) Write a FASTa and FASTq Parser 
    B) Write a transcription and reverse transcription function
    C) Create test cases 

# Grading (15 points total)
## Code (8 points)
    1. FASTa parser works correctly (2)
    2. FASTq parser works correctly (2)
    3. Transcription function works correctly (2)
    4. Reverse Transcription function works correctly (2)
    
    By the due date, if your FASTa parser or FASTq parser does not work, include comments on what 
    you think the solution is and what you struggled with implementing for high partial marks.

## Tests (5 points)
    5. Write Positive Case unit tests (1.5)
    6. Write Negative Case unit tests (1.5)
    7. Submit a job to GitHub Actions (1)
    8. Create a local package using flit (1)

    If your FASTa and FASTq parsers do not work, write solid test cases for both Transcription functions 
    for high partial marks.

## Documentation & GitHub (2 points)
    9. Write comments documenting your code (even if all your code works!) (1)
    10. Push your finished assignment to GitHub (1)


# Getting Started
To get started, please fork this repository onto your own GitHub. You will then work on the code base from your own repo and make changes to it in the form of commits. 

### Quick overview of Git pipline
```
# Stage changed files 
git add changed_python_file.py changed_python_file_2.py

# Stage all changed files in current directory
git add .

# Commit changed files
git commit -m "Describe your changes you've made to your python file"

# Push to your repository
git push 
```
Create a new conda environment, activate it and work from there!

After forking and creating a conda environment, go into the assignment and look at each folder and file. Figure out the purpose of each file is and which functions you need to edit. Use Main.py to test your function implementation. 

### Final Note: 
You will encounter errors on the way. Please feel free to use Google, Stack overflow, or ChatGPT to help you debug. If you remain stuck for a long time, please contact a TA. We are happy to help! 

# Reference Data 

## Test Data
The data we will be testing with will be single-line FASTA files and single-line FASTQ files. This means that the entire sequence will be on one line and you don't need to implement a multi-line FASTA/FASTQ parser. 
We've included some test data under `data/test.f[qa]` which can be used to validate your code as you are writing it. 
If you don't like these test data though you can make your own by changing the seed on the tool `data/make_seq.py` and rerunning the code.

## FASTA File Format
I am sure you have seen this before, but for those who have not, the FASTA file format is a plaintext representation of sequencing data. Some FASTA representations include multiple lines / sequence, but more often than not you will find the format only with 1 sequence per line so that is the format we will use. Here is an example of 3 sequencing records. 

### FASTA Representation
```
>Header
Sequence
```

### Example FASTA 
```
>sequence_1
ACGGACCACCATGAA
>sequence_2
ACGGACCTGAA
>sequence_3
ACGGACCGGATTAACCATGAA
```

## FASTQ File Format
The FASTQ file format is very similar to the FASTA records, but it includes 2 extra lines per record. The only added information is the quality score, which will look like a computer's stream of consciousness but is in fact the confidence that a base is the base called. If you are interested in that process, take a look at PHRED scoring, if you are not that is ok too

### FASTQ Representation
```
@Header
Sequence
+
Quality
```

### Example FASTQ
```
@seq0
TGTGGTCGTATAGTTATTGTCATAAATTACACAGAATCG
+
*540($=*,=.062565,2>'487')!:&&6=,6,*7>:
@seq1
CCCCGGACGACTGATCCCGATAGAGCTCACTCTTCGAGG
+
'(<#/0$5&!$+,:=%7=50--1;'(-7;0>=$(05*9,
@seq2
GATAAACTTCTATCACGAATACTGCGGGACCATGCAGTT
+
1,758$,:7654/7<0%5/12%-3>-2.>$$443-,'9,
```

## Transcription

### Transcription 
This process is returning the complement strand to the provided sequence. You can think of this as a mapping of complement bases, except that the `T`s are replaced with `U`s

```
input  : A C T G A A C C C
         | | | | | | | | |
output : U G A C U U G G G
```

### Reverse - Transcription
This process is used to return the reverse of the complement strand. It is equivalent to a `reverse(transcribe(seq))`

```
input       : A C T G A A C C C
              | | | | | | | | |
transcribe  : U G A C U U G G G 

output : G G G U U C A G U
```

# Github Actions 
This is a really useful tool for software development and is a good way to test if you are adding breaking changes to a code base. For this first assignment, we have created a .github/workflow/ci.yaml file for you that automatically runs pytest for you. In future assignments, you may need to create your own file. For more information, we highly recommend you check out this [blog post](https://pytest-with-eric.com/integrations/pytest-github-actions/).

# Python Modules
In the future, when you've created code that is useful for the community, you are able to share your objects in a package. To do this, we can use a package called [flit](https://flit.readthedocs.io/en/latest/index.html) that packages up your code.  Documentation on how this works is [here](https://flit.pypa.io/en/stable/). 

Note: Creating your local package using flit will be required to run your test cases and main.py.

To get started on creating your own local package. You must:
    
    1. Download flit in your conda environment
    2. Run flit init in your directory and fill in the information

To install your own package You must: 

    1. (on mac) flit install --symlink
       (on windows) flit install --pth-file

## `pyproject.toml`
When initializing flit, a pyproject.toml file will generate. Here is an example of what that would look like. 
```toml
[build-system]
requires = [
	"flit_core >=3.2,<4",
	"python_version >= '3.7'"
	]
build-backend = "flit_core.buildapi"

[project]
name = #NAME_OF_PACKAGE
authors = [{
	name = #WHO_ARE_YOU,
	email = #HOW_DO_I_YELL_AT_YOU
	}]
readme = "README.md"
license = {file = "LICENSE"}
classifiers = ["License :: OSI Approved :: MIT License"]
dynamic = ["version", "description"]
dependencies = [
	#WHAT_DOES_THIS_NEED_TO_WORK
]
```

# Unit Testing
The testing framework we are going to use in grading is pytest. We recommend you also learn how to use pytest when making your unit tests, but you can use whatever testing framework you want. pytest is easy to use though and can be setup pretty quickly. You can read the documentation for pytest [here](https://docs.pytest.org/en/6.2.x/)

The main idea is that you want to test your code with assertions. These assertions must always be true! If they are broken, then your code is not doing what it's supposed to be doing. 

Here is an example of a unit test:

```python
def add_numbers(x, y):
    return x + y

assert add_numbers(2,3) == 5
assert add_numbers(2,3) != 0
```

pytest will by default recursively search for functions to test in all `tests/test*.py` files that meet the regex `test*`.

Here is an example of a testing script that will test two functions once pytest is run:

```python
from module import add_numbers

# Positive test: Testing if the function behaves as expected.
def test_module_correct():
    assert add_numbers(2,3) == 5

# Negative test: Testing if the function behaves when something goes wrong
def test_module_incorrect():
    assert add_numbers(2,3) != 0
