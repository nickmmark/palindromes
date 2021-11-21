# palindromes

Sator Squares are cool elegant word puzzles. Making them is a fun (& time consuming) challenge.
My goal with this project was to find an algorithmic way of finding/constructing [SATOR squares](https://en.wikipedia.org/wiki/Sator_Square)

[![An ancient Sator Square](https://upload.wikimedia.org/wikipedia/commons/thumb/7/71/Sator_Square_at_Opp%C3%A8de.jpg/440px-Sator_Square_at_Opp%C3%A8de.jpg)

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

3. place *heropalidromes* that have overlapping letters into adjacent squares

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
