### Learning c from zero to hero!

#### Day 1

1. Used vim to write a simple c file that prints "Hello World" 
2. Complied the file with gcc(`gcc hello.c`); which produced a new file `a.out`.
3. To print the Strign to the screen I run the the produced file by calling it directly `./a.out`

#### How it works under the hood

- **Compilation isn't one step.** `gcc hello.c` actually runs four stages behind the scenes: preprocessing (handles lines starting with `#`), compiling (C code -> assembly), assembling (assembly -> machine code / object file), and linking (combines object code with library code into one executable). The end result is `a.out`.
- **`#include <stdio.h>`** pulls in the declarations for the standard I/O library, which is where `printf` comes from. Without it, the compiler wouldn't know what `printf` is.
- **`int main()`** is the entry point — the OS starts running your program here. The `int` means it returns a number when it finishes.
- **`return 0;`** sends an exit code back to the OS. `0` conventionally means "success"; anything non-zero usually signals an error.
- **`./a.out`** — the `./` is needed because, unlike some other OSes, the shell doesn't search the current directory for programs by default. You have to point directly at the file.
- **The trailing `%`** you sometimes see after running `./a.out` isn't from your program — it's zsh flagging that the output didn't end with a newline (`printf("Hello world")` has no `\n`).


