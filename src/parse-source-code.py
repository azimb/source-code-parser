# main function - this is where the program begin
# it's role is to identify if the input file exists and if the programming language of the source code is supported by the parser
def main():
    # these dictionaries/hashmaps store the corresponding comment character(s) for the 3 languages that it supports
    # hashmaps allow very efficient look up time (O(1) or constant)
    single_line_comment_syntax = {"py": "#", "java": "//", "js": "//"}
    multi_line_comment_syntax = {"py": ("'''", "'''"), "java": ("/*", "*/"), "js": ("/*", "*/")}

    # asks the user for the file name of the source file that will be parsed
    input_filename = input("Please enter the name of the source file you would like to parse. Make sure to use the correct extension: ")
    # verify that it's a not a file to be ignored
    if input_filename[0] == ".":
        raise Exception("Exception: File is being ignored as it's name starts with a period.")
    # what programming language is used in the file (using it's extension)
    language = input_filename[input_filename.rfind('.') + 1:]
    # is this a language we support? O(1) lookup in hashmap
    if language not in single_line_comment_syntax:
        raise Exception("Exception: Language not supported")

    # does the file exist?
    # handle the exception if it doesn't, and return a new exception with a more friendly error message to the user
    try:
        # read the file line by line, and store it as an array of strings (or lines)
        file_contents = open(input_filename, 'r').readlines()
    except FileNotFoundError:
        return Exception("File not found, aborting.")

    # for the programming language in subject, extract the corresponding characters for:
    #    a) single line comment
    #    b) multi line comment
    single = single_line_comment_syntax[language]
    multi_line_syntax_tuple = multi_line_comment_syntax[language]
    multi_start, multi_end = multi_line_syntax_tuple[0], multi_line_syntax_tuple[1]
    comment_syntax = [single, multi_start, multi_end]

    # this call to parse will do the actual job
    parse(file_contents, comment_syntax)

# parse function is responsible for the core functionality, which is parsing the input and generating stats
def parse(file_contents, comment_syntax):
    # dictionary to hold the stats, as key-value pairs
    # this hashmap will allow manipulation of values in constant time, and constant space ( O(1) )
    stats = {"total": 0,
             "single line comments": 0,
             "multi line comments": 0,
             "multi line comment blocks": 0,
             "code lines": 0,
             "todos": 0
             }

    # variable to keep a track we are in a block of multi line comments
    part_of_multi_line_comment = False

    # iterate over all the lines -- time complexity is O(L) where L = # of lines in the file
    for line in file_contents:
        stats["total"] +=1 # increament total number of lines

        if part_of_multi_line_comment: # are we in a block of multi line comment?
            stats["multi line comments"] += 1 # increament the number of multi line comments
            if ends_multi_line_comment(line, comment_syntax[2]): # is this is the last line of the block of multi line comments
                part_of_multi_line_comment = False # now that we are out of the block of multi line comments, flag is set to False
                stats["multi line comment blocks"] += 1 # we have seen a block, so increament it's counter in the hashmap

        elif is_single_line_comment(line, comment_syntax[0]): # is this line a single line comment
            stats["single line comments"] += 1 # increment counter for single line comments
            if has_code_before_comment(line, comment_syntax[0]): stats["code lines"] += 1 # is this code and comment, or just code?
            if has_todo(line): stats["todos"] += 1 # is this comment a todo?

        elif begins_multi_line_comment(line, comment_syntax[1]): # is this line starting a new block of multi line comments
            stats["multi line comments"] += 1 # increment the count of multi line comments
            if has_code_before_comment(line, comment_syntax[0]): stats["code lines"] += 1 # is this just a comment, or also has code before it?
            if not ends_multi_line_comment(line[line.find("'''")+1:], comment_syntax[2]): # is the multi line comment block only 1 line long?
                part_of_multi_line_comment = True # if not, set the flag to true, so that future lines are considered a part of the block
            else:
                stats["multi line comment blocks"] += 1 # if the block ended on the same line, increament the number of blocks of multi line comments

        else: # not a comment, so must be code
            if line.strip(): stats["code lines"] += 1 # verify it's not a blank line by stripping spaces
    print_stats(stats)

# helper methods to check if a line is a single line comment, if a comment has code before it, if a comment is a "todo",
#  if the line is starting or ending a new block of multi line comments
# time complexity of each of these functions is O(L), where L = length of the line

def is_single_line_comment(line, syntax): return syntax in line

def has_code_before_comment(line, syntax): return line.find(syntax) > 0

def has_todo(line): return "TODO" in line.upper()

def begins_multi_line_comment(line, syntax): return syntax in line

def ends_multi_line_comment(line, syntax): return syntax in line

# helper function to print stats from the dictionary
def print_stats(stats):
    # this chunk of code is much cleaner, but it doesn't guarantee the order
    '''
    for stat in stats: print(stat + ":" + int(stats[stat])
    '''

    print("Total lines: ", stats["total"])
    print("Total comment lines: ", stats["single line comments"] + stats["multi line comments"])
    print("Total single line comments: ", stats["single line comments"])
    print("Total multi line comments: ", stats["multi line comments"])
    print("Total multi line comment blocks", stats["multi line comment blocks"])
    print("Total todos: ", stats["todos"])
    print("Total code lines: ", stats["code lines"])

# begin the program, by calling main
main()
