# InvitationASM
InvitationASM is an interpreter for the assembly-styled language that is used in "An Introduction to Computer Science" by G. Michael Schneider and Judith Gersting

## Usage
```bash
> python ExecuteIASM.py <file.iasm>
```

## Syntax
An InvitationASM program consists of a series of statements, containing a token corresponding with an operation, followed by a sequence of comma-separated integer arguments for the operation

## Additions
InvitationASM has several additions compared to the language used in the books. These include:
* Several new operations (indicated with *italics* in the operations list)
* Dual-usage memory: One location in memory can contain two values. An executable statement, and a numeric value.
* Register address: The register has been given a memory address of -1, allowing you to use it for operations that normally work with a memory address

## Operations

#### LOAD
Usage: `LOAD A`

Loads the value contained in memory address A into the register.

#### *PRINT*
Usage: `PRINT A`

Prints the value contained in memory address A to stdout.

#### COMPARE
Usage: `COMPARE A`

Compares the value contained in memory address A to the value in the register.
Sets MEMORY.gt to 1 if the value in the register is greater than the value in A.
Sets MEMORY.lt to 1 if the value in the register is less than the value in A.
Sets MEMORY.eq to 1 if the value in the register equals the value in A.
Used to set the values used by JUMPGT, JUMPEQ, and JUMPLT

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