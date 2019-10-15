# source-code-parser

=======================================================
Author: Azim Baghadiya
======================================================

Overview:
---------
- A python program is provided, that performs the desired task.
- Each part of the code is crisp, and outlines the approach clearly with the help of comments.
- Any functionality that is reusable, will be found as a function. This modularization is done to avoid duplication of code and effective debugging.
- Data structures like hashmaps (or dictionaries in Python) are used when applicable, to optimize the algorithm.
  (these also make the code scalable, and maintainable)
- Time and space complexity are discussed along with the core chunks of the algorithm, to outline how efficiently the program computes the result when the input becomes very large.
- Program currently supports parsing source code files for Java, Python, and JavaScript.
- For Java and Pyton, sample test files have been created and the program result has been verified
  (these tests and their results can be found in the "test-file" directory)

Assumptions:
------------
- A blank line within a commented block will be counted as a multi line comment.
- TODOs are used in single line comments only.
- A valid filename will be provided, for instance, no exmpty strings
  (However, these scenarios are handled: file starts with a period, or a file other than Java/Python/Js) 

Testing:
--------
The test files make sure to produce not only the usual scenarios, but also exhaust all possible edge cases I could think of.
The content of the test files exactly list what scenarios (especially the corner cases) they produce.

Limitations:
------------
- Python mutli line comments can use ''' or """. The program assumes that ''' will be used.
- Didn't implement the feature of giving input_file name as a command line argument.
- While exceptional handling has been performed and edge cases are often checked, one area where this program lacks
	robuestness is when a character that is used for commenting, is used for another purpose.
   	
	For example, if the file contains the following code:	my_regex("[#abcd");
	the program will treat everything after # ( ie "abcd");" ) as a comment.

	While this edge case is not being handled by the program, it's been highlighted to identify shortcomings of the program.
- If the extension of the file is of language A and the actual source code is of language B, this could lead to incorrect results

Instructions:
-------------
- (The only) source file is available in the "src" directory
- The two test files (for Python and Java) are available in the "test-files" directory
- Please place either of the two test files (or both) in the directory of the source file to test it
  (as the program assumes that the input file lives in the same directory)
- Run the program, and when it prompts, please provide the file that you would like to test
  (please make sure to provide the correction extension)
- Results will be computed and printed to the console
