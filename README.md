# palindromes/semordnilaps & sator squares

### context
Sator Squares are cool elegant word puzzles. They can be read left to right, top to bottom, right to left, and bottom to top.
Making them is a fun (& time consuming) challenge. My goal with this project was to find an algorithmic way of finding/constructing [SATOR squares](https://en.wikipedia.org/wiki/Sator_Square) where you could select a palindrome and the algorithm would build a Sator square around it.

![An ancient Sator Square](https://upload.wikimedia.org/wikipedia/commons/thumb/7/71/Sator_Square_at_Opp%C3%A8de.jpg/440px-Sator_Square_at_Opp%C3%A8de.jpg)

### an approach
in order to do that, we need to do a series of operations
1. select the size of the square (n)
1. [search the dictionary](https://www.dcode.fr/semordnilap-generator) to find *palindromes* and *heteropalindromes* of length = n; this is the complete set of words that can be used to construct the Sator square.
2. choose from the list a *palidrome* to place in the center

|   |   |   |   |   |
|:-:|:-:|:-:|:-:|:-:|
|   |   | T |   |   |
|   |   | E |   |   |
| **T** | **E** | **N** | **E** | **T** |
|   |   | E |   |   |
|   |   | T |   |   |

3. place *heropalidromes* that have overlapping letters into adjacent squares, moving outward from the center or inwards from the outside are both possible

|   |   |   |   |   |
|:-:|:-:|:-:|:-:|:-:|
| **R** | **O** | T | **A** | **S** |
|   |   | E |   | **A** |
| T | E | N | E | T |
|   |   | E |   | **O** |
|   |   | T |   | **R** |

|   |   |   |   |   |
|:-:|:-:|:-:|:-:|:-:|
| R | O | T | A | S |
| O |   | E |   | A |
| T | E | N | E | T |
| A |   | E |   | O |
| S | A | T | O | R |

4. repeat until the square is complete

|   |   |   |   |   |
|:-:|:-:|:-:|:-:|:-:|
| R | O | T | A | S |
| O | **P** | E | **R** | A |
| T | E | N | E | T |
| A | **R** | E | **P** | O |
| S | A | T | O | R |

### algorithm
1. identify heteropalindromes (& the subset that are true palindromes)
2. try to fit heteropalindromes around a palindrome
