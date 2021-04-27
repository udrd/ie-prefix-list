# IE community prefix list availability 
The script displays the available two-character prefix combinations that are still available and conform to the recommended format.

## Installation
Python is needed to run the script.

## How to use
* Replace the content of table.txt with the content of the two tables from http://www.blackwyrmlair.net/prefixes/ (need to wait for ad)
    * Delete the content of table.txt with a simple text editor (Notepad, etc)
    * Go to http://www.blackwyrmlair.net/prefixes/ You will be redirected and will need to click past an ad
    * Click before the first entry (0x), hold shift, click in the last cell of the first table, copy by pressing Ctrl+C
    * Paste in table.txt
    * Copy the content of the second table, and paste them in the file as well
* Run the script. Enter q to quit, number 1-3 to get specific results, or any other letter/number for full list
The output shows all available two-character prefixes of [A-Za-z][0-9A-Za-z#_!-] or [#][A-Za-z_!-] as described in the first post here http://forums.blackwyrmlair.net/index.php?showtopic=113

## Example output (out of date)
**Note:** This list is most likely out of date (2021-Jan), update table.txt and run the script for up-to-date information.

**When pressing '1':**
<samp>A: 
B: BE BF BJ BN BO BV BZ
C: CF CI CJ
D: DB DF DI DJ DN DQ
E: EB EF EH EI EJ EL EN EO ET EU EW EZ
F: FE FF FJ FO FP FV FX FY
G: GA GB GF GH GJ GK GL GN GO GQ GU GX GY GZ
H: HC HD HE HG HI HJ HL HM HN HP HQ HR HS HT HV HY HZ
I: ID IF IH IO IV IY
J: JD JE JG JI JN JO JU JV JW
K: KJ KP KQ KU KW KX KZ
L: LB LG LP LQ LT LV LX
M: ME MN
N: NC ND NG NH NK NL NN NQ NR NT NV NW NX NY NZ
O: OB OE OF OG OI OJ OK OM ON OQ OT OU OV OX OY OZ
P: PM PN PQ PR PV PZ
Q: QA QB QC QE QF QG QH QJ QK QL QM QN QO QP QR QS QV QY QZ
R: RI RP RQ RU RY
S: SY
T: TN TW TX TY
U: UA UD UE UF UG UH UI UJ UK UL UM UN UO UP UQ UR UT UV UW UX UY UZ
V: VC VD VH VJ VQ VU VV
W: WC WF WJ WN WP WU WZ
X: XA XC XF XH XJ XK XM XN XQ XR XS XU XV XW XZ
Y: YB YC YD YF YG YH YJ YK YL YM YN YP YQ YT YW
Z: ZB ZC ZD ZE ZH ZJ ZL ZM ZO ZQ ZS ZU ZW
\#: #O #U #Y</samp>

**When pressing '3':**
<samp>A: A8 A9
B: B5 B6 B8 B9
C: C9
D: D2 D3 D4 D6 D7
E: E0 E1 E2 E5 E6 E7 E8
F: F0 F2 F3 F4 F5 F6 F7 F9
G: G0 G2 G4 G5 G8 G9
H: H0 H1 H3 H4 H5 H6 H7 H8 H9
I: I2 I3 I4 I5 I6 I7 I8 I9
J: J1 J2 J4 J5 J6 J8
K: K0 K3 K4 K5 K6 K8
L: L0 L1 L2 L5 L9
M: M0 M5 M6 M8 M9
N: N0 N2 N3 N4 N5 N6 N7 N8 N9
O: O0 O4 O5 O6 O7 O8 O9
P: P0 P1 P2 P3 P6 P7 P8 P9
Q: Q0 Q2 Q3 Q4 Q5 Q7 Q8 Q9
R: R1 R3 R5 R6 R8
S: 
T: T0 T4 T5 T6 T7 T8 T9
U: U0 U1 U2 U3 U4 U5 U6 U7 U8 U9
V: V0 V1 V2 V4 V5 V6 V7 V9
W: W0 W2 W4 W6 W8 W9
X: X0 X1 X2 X4 X5 X6 X7 X9
Y: Y0 Y1 Y2 Y3 Y4 Y5 Y6 Y7 Y8 Y9
Z: Z1 Z2 Z3 Z4 Z5 Z6 Z8
\#: #0 #1 #2 #3 #4 #5 #6 #7 #8 #9</samp>

## License
MIT
