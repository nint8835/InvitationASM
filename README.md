# InvitationASM
InvitationASM is an interpreter for the assembly-styled language that is used in "An Introduction to Computer Science" by G. Michael Schneider and Judith Gersting

## Requirements
Python 3.6 or later

## Usage
```bash
> python ExecuteIASM.py <file.iasm>
```

## Syntax
An InvitationASM program consists of a series of statements, containing a token corresponding with an operation, followed by a sequence of zero or more comma-separated integer arguments for the operation. Comments are denoted by starting a line with #.

## Additions
InvitationASM has several additions compared to the language used in the books. These include:
* Several new operations (indicated with *italics* in the operations list)
* Dual-usage memory: One location in memory can contain two values. An executable statement, and a numeric value.
* Register address: The register has been given a memory address of -1, allowing you to use it for operations that normally work with a memory address

## Operations

#### LOAD
Usage: `LOAD A`

Loads the value contained in memory address A into the register.

#### OUT
Usage: `OUT A`

Prints the value contained in memory address A to stdout.

#### COMPARE
Usage: `COMPARE A`

Compares the value contained in memory address A to the value in the register.
Sets the values required for JUMPGT, JUMPEQ, and JUMPLT.

#### STORE
Usage: `STORE A`

Stores the value contained in the register in memory address A.

#### *INIT*
Usage: `INIT A, B`

Initializes memory address A with value B.

#### JUMP
Usage: `JUMP A`

Jumps to the statement contained at memory address A.

#### ADD
Usage: `ADD A`

Adds the value contained at memory address A to the value in the register.

Usage: `ADD A, B`

Adds the value contained at memory address A to the value stored at memory address B, and stores it back at address B.

Usage: `ADD A, B, C`

Adds the value contained at memory address A to the value stored at memory address B, and stores it at address C.

#### SUBTRACT
Usage: `SUBTRACT A`

Subtracts the value contained at memory address A from the value in the register.

Usage: `SUBTRACT A, B`

Subtracts the value contained at memory address A from the value stored at memory address B, and stores it back at address B.

Usage: `SUBTRACT A, B, C`

Subtracts the value contained at memory address A from the value stored at memory address B, and stores it at address C.

#### *MULTIPLY*
Usage: `MULTIPLY A`

Multiplies the value in the register by the value stored at A.

Usage: `MULTIPLY A, B`

Multiplies the value stored at B by the value stored at A, and stores it back at B.

Usage: `MULTIPLY A, B, C`

Multiplies the value stored at A by the value stored at B, and stores it at C.

#### *DIVIDE*
Usage: `DIVIDE A`

Divides the value in the register by the value stored at A.

Usage: `DIVIDE A, B`

Divides the value stored at B by the value stored at A, and stores it back at B.

Usage: `DIVIDE A, B, C`

Divides the value stored at A by the value stored at B, and stores it at C.

#### HALT
Usage: `HALT`

Halts execution of the program.

#### CLEAR
Usage: `CLEAR A`

Clears the value of address A.

#### INCREMENT
Usage: `INCREMENT A`

Increments the value of address A by 1.

#### DECREMENT
Usage: `DECREMENT A`

Decrements the value of address A by 1.

#### JUMPLT
Usage: `JUMPLT A`

Jumps to address A if the last COMPARE operation set LT = 1.

#### JUMPGT
Usage: `JUMPGT A`

Jumps to address A if the last COMPARE operation set GT = 1.

#### JUMPEQ
Usage: `JUMPEQ A`

Jumps to address A if the last COMPARE operation set EQ = 1.

#### JUMPNEQ
Usage: `JUMPNEQ A`

Jumps to address A if the last COMPARE operation set EQ = 0.

#### IN
Usage: `IN A`

Reads from standard in and sets the value at A equal to what was read.

#### *ANCHOR*
Usage: `ANCHOR A`

Begins inserting new instructions from memory address A.