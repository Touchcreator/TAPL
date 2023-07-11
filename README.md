# TAPL
## Why You Should Use TAPL:
- ~~I made it~~
- The syntax is pretty simple
- You don't need to worry about formatting
## How to use:
TAPL is a stack based programming language, so data is stored in the background and you can run a command to use the data.
### Running:
Windows: `py tapl.py {filename}.tapl` or `tapl {filename}.tapl`

Unix-based OS: `python3 tapl.py {filename}.tapl`
### Simple Commands:
`"<data>"` - This command stores a string.

`[<data>]` - This command stores an integer.

`p` - This command prints the latest data.

`j` - This command joins the 2 latest data pieces as a string. It starts from the second latest data piece to the latest.

`r` - This command is the same as `j` but in reverse.

`i` - This command asks for input and stores the input in a data piece.

`+` - This command adds the 2 latest numbers in the data set.

`-` - This command subtracts the two latest numbers in the dataset. It starts from the second latest data piece to the latest.

`*` - This command multiplies the two latest numbers in the dataset.

`/` - This command divides the two latest numbers in the dataset. It starts from the second latest number to the latest.

`{<code>}` - This command runs Python code, incase you ever need to.

`>` - This command compares the two latest numbers. It goes from the second latest number to the latest. If true, it adds the value `True` to the dataset, if false, it adds `False`

`<` - The same as the above command, but its less than.

`=` - This command checks if the two latest values are the same, if so, it adds `True` to the dataset, if not, it adds `False`.

### Complicated Commands:
`t`: Lets say you had a program like this: `"hi" "hi2" "hi3" "hi4"`, and you wanted to print hi. Right now, you can't, because its buried in the dataset. However, if you added `[4] t` to the program, making it `"hi" "hi2" "hi3" "hi4" [4] t`, now, "hi" is at the front of the data, and all you need to do is add `p` to print it. Making the full command `"hi" "hi2" "hi3" "hi4" [4] tp`

`:`: In order to use this command, you must have a number before it. If the second latest value in the dataset is equal to `True`, then nothing happens, but if the second latest value is equal to `False`, it skips the amount of characters equivalent to the first number in the dataset.

`;`: The opposite of `:`

# Compiling:
After 1 billion years, you've finally finished your program. But your friend doesn't have TAPL installed! (what a loser) This is OK though. As TAPL 0.3.0 and above come with a converter to Python. In order to convert, you would run `py compile.py <yourcode>.tapl <target>.py`. The issue however, is that the `:` and `;` commands break when you use this method. If your code has an if command, you must manually fix the code. Once you are done, you can use a tool such as Pyinstaller to convert to an EXE.


