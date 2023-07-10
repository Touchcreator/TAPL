# TAPL
## How to use:
TAPL is a stack based programming language, so data is stored in the background and you can run a command to use the data.
### Running:
Windows: `py tapl.py {filename}.tapl` or `tapl {filename}.tapl`

Unix-based OS: `python3 tapl.py {filename}.tapl`
### Simple Commands:
`"{data}"` - This command stores a string.

`[{data}]` - This command stores an integer.

`p` - This command prints the latest data.

`j` - This command joins the 2 latest data pieces as a string. It starts from the second latest data piece to the latest.

`r` - This command is the same as `j` but in reverse.

`i` - This command asks for input and stores the input in a data piece.

`+` - This command adds the 2 latest numbers in the data set.

`-` - This command subtracts the two latest numbers in the dataset. It starts from the second latest data piece to the latest.

`*` - This command multiplies the two latest numbers in the dataset.

`/` - This command divides the two latest numbers in the dataset. It starts from the second latest number to the latest.

### Complicated Commands:
`t`: Lets say you had a program like this: `"hi" "hi2" "hi3" "hi4"`, and you wanted to print hi. Right now, you can't, because its buried in the dataset. However, if you added `[4] t` to the program, making it `"hi" "hi2" "hi3" "hi4" [4] t`, now, "hi" is at the front of the data, and all you need to do is add `p` to print it. Making the full command `"hi" "hi2" "hi3" "hi4" [4] tp`


