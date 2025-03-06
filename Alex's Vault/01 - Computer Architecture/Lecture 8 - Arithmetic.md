## MIPS Multiplication Instructions

Two 32-bit registers for product:

- HI: most-significant 32 bits
- LO: least-significant 32-bits

![[image 9.png|image 9.png]]

## Division

![[image 1 6.png|image 1 6.png]]

### Binary Division

- Example divide 1001010 by 1000
- Check for 0 divisor
- Long division approach
    - If divisor ≤ dividend bits
        - 1 bit in quotient, subtract
    - Otherwise
        - 0 bit in quotient, bring down next dividend bit
- Restoring division
    - Do the subtract, and if remainder goes < 0, add divisor back
- Signed Division
- Divide using absolute values
- Adjust sign of quotient and remainder as required

### Faster Division

Do not use parallel hardware as in multiplier

- Subtraction is conditional on sign of remainder

Faster dividers generate multiple quotient bits per step

- Still require multiple steps
- Solution currently uses future prediction and correction strategy.

## MIPS Division Instructions

- Use HI/LO registers for result
    - HI: 32-bit remainder
    - LO: 32-bit quotient
- Instructions
    - div rs, rt / divu rs, rt
    - No overflow or divide-by-0 checking
        - Software must perform checks if required
    - Use mfhi

==*** ***==

## Floating Point Number Representation

### Floating Point

- Representation for non-integral numbers
    - Including very small and very large numbers
- Types float and double
- Like scientific notation
    - $-2.34\times10^{56}$﻿
    - $0.002\times10^{-4}$﻿
    - $987.02\times10^{9}$﻿
- In binary
    - Labelled binary point

$-5.25 = -101.01$

## Floating Point Standard

- Single precision (32-bit) - Float
- Double Precision (64-bit) - Double

![[image 2 6.png|image 2 6.png]]

### Excess Representation

Exponent = yyyy + Bias

- 127 for single
- 1023 for double

Biased exponent is unsigned

Exponents, 00…0000 and 1111…11 reserved

## Floating Point Example

![[image 3 5.png|image 3 5.png]]

![[image 4 5.png|image 4 5.png]]

## Accurate Arithmetic

![[image 5 4.png|image 5 4.png]]