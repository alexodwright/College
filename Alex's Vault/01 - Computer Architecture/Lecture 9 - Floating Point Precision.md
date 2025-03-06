Relative precision:

- Single: approx $2^{-23}$﻿
    - Equivalent to 23 x $log_{10}2 \approx 2.3 \times 0.3 \approx$﻿ 7 decimal digits of precision
- Double: approx $2^{-52}$﻿
    - Equivalent to 52 $\times \\log_{10}2 \approx 52 \times 0.3 \approx$﻿ 16 decimal digits of precision

==Precision-range trade off==

- Fraction field controls precision while exponent field controls range
- Fraction bits + exponent bits = fixed number (e.g., 31 bits in single precision)

## Floating-Point MIPS Instruction

- Separate FP processor (CP!)
- Separate FP registers
    - 32 single-precision: $f0, $f1, … $f31
    - Pared for double-precision: $f0/$f1, $f2/$f3, …
        - Release 2 of MIPs ISA supports 32 x 64-bit FP reg’s
- FP instructions operate only on FP registers
    - Programs generally don’t do integer ops on FP data, or vice versa
    - More registers with minimal code-size impact.

## MIPS FP Instructions

- Arithmetic
    
    - Single: add.s, sub.s, mul.s, div.s
        - e.g., add.s $f0, $f1, $f6
    - Double: add.d, sub.d, mul.d, div.d
        - e.g., mul.d $f4, $f4, $f6
    
    MIPS floating-point instructions do not have immediate operands
    
    ### Load and Store Instructions
    
    Single: lwc 1, swc1
    
    Double: ldc 1, sdc 1
    
    e.g. ldc 1 $f8, 32($sp)
    
    ### Register Transfer
    
    ==TO== cp1: mtc1 $t0, $f0
    
    ==FROM== cp1: mfc1 $t0, $f0
    
- Comparison
    
    - c.xx.s, c.xx.d (xx is eq, ,lt, le, …)  
        Sets or clears FP condition-code bit  
        
    - e.g. c.lt.s $f3, $f4
    
    Branching
    
    - bclt label
    
    Conversion
    
    - cvt.x.y $f0, $f1 ==# cvt.to.from==
        
        x & y could be {s, d, w}
        
    - e.g. cvt.d.w $f0, $f2 ==# int_to_double==

## FP Example $\degree$﻿F to $\degree$﻿C

C code:

```C
float f2c (float fahr) {
	return ((5.0/9.0)*(fahr-32.0));
}
```

- Fahr in $f12, result in $f0
    
    literals in global memory space
    
    - Note that fahr is obtained using syscall 6 for single.
    

NOTE: The code above does not follow good programming practice as it uses magic numbers!

MIPS code:

```Assembly
# the constants are defined using .float
f2c: lwc1 $f16, const5
lwc1 $f18, const9
div.s $f16, $f16, $f18
lwc1 $f18, const32
sub.s $f18, $f12, $f18
mul.s $f0, $f16, $f18
jr $ra
```

Coding for performance

- Smaller data units (e.g., Int vs long or single vs. double) require ==smaller storage== and are ==processed faster==.
- Floating point operations are slower than integer operations.
- The choice of data type significantly impact the performance and this is evident in data intensive applications, such as data science and game development.

## Example Question:

10 in binary is 1010 → 1.010 * $2^3$﻿

sign = 0

exponent = 127 (single point precision) + 3 (exponent) = 130 = 1000 0010

mantissa = 0100 0000 0000 0000 0000 000

## FP Adder Hardware

![[image 10.png|image 10.png]]

## Multidimensional Arithmetic

![[image 1 7.png|image 1 7.png]]

![[image 2 7.png|image 2 7.png]]

### Matrix storage

- Storing two-dimensional data in one dimensional (linear) memory.

![[image 3 6.png|image 3 6.png]]