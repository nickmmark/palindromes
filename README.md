# palindromes

my goal was to find an algorithmic way of finding/constructing [SATOR squares](https://en.wikipedia.org/wiki/Sator_Square)

in order to do that, we need to do a series of operations
1. search the dictionary to find *palindromes* and *heteropalindromes* of the requisite length
2. place a *palidrome* in the center

|   |   |   |   |   |
|:-:|:-:|:-:|:-:|:-:|
|   |   | T |   |   |
|   |   | E |   |   |
| **T** | **E** | **N** | **E** | **T** |
|   |   | E |   |   |
|   |   | T |   |   |

3. place *heropalidromes* that have overlapping letters into adjacent squares

|   |   |   |   |   |
|:-:|:-:|:-:|:-:|:-:|
| **R** | **O** | T | **A** | **S** |
|   |   | E |   | **A** |
| T | E | N | E | T |
|   |   | E |   | **O** |
|   |   | T |   | **R** |

4. repeat until the square is complete

|   |   |   |   |   |
|:-:|:-:|:-:|:-:|:-:|
| R | O | T | A | S |
| O |   | E |   | A |
| T | E | N | E | T |
| A |   | E |   | O |
| S | A | T | O | R |

|   |   |   |   |   |
|:-:|:-:|:-:|:-:|:-:|
| R | O | T | A | S |
| O | **P** | E | **R** | A |
| T | E | N | E | T |
| A | **R** | E | **P** | O |
| S | A | T | O | R |
