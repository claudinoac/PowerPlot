EESchema Schematic File Version 4
LIBS:P_SUPPLY-cache
EELAYER 26 0
EELAYER END
$Descr User 5846 8268
encoding utf-8
Sheet 1 1
Title "SADAMAP POWER SUPPLY"
Date "2018-01-31"
Rev "2"
Comp "LAPMA/CTA - IF/UFRGS"
Comment1 "All resistors are 1/4W"
Comment2 "The transformer 12+12 should have 800mA minimum current"
Comment3 "Designed by: Alisson Claudino"
Comment4 ""
$EndDescr
$Comp
L P_SUPPLY-rescue:CONN_01X02 P1
U 1 1 5A4B779A
P 1500 1250
F 0 "P1" H 1650 1250 50  0000 C CNN
F 1 "127VAC" H 1500 1400 50  0000 C CNN
F 2 "Connectors:bornier2" H 1500 1250 50  0001 C CNN
F 3 "" H 1500 1250 50  0000 C CNN
	1    1500 1250
	-1   0    0    1   
$EndComp
$Comp
L P_SUPPLY-rescue:F_Small F2
U 1 1 5A4B77B2
P 3450 1000
F 0 "F2" H 3410 1060 50  0000 L CNN
F 1 "1A" H 3330 940 50  0000 L CNN
F 2 "Fuse_Holders_and_Fuses:Fuseholder5x20_horiz_SemiClosed_Casing10x25mm" H 3450 1000 50  0001 C CNN
F 3 "" H 3450 1000 50  0000 C CNN
	1    3450 1000
	1    0    0    -1  
$EndComp
$Comp
L P_SUPPLY-rescue:GND #PWR01
U 1 1 5A4B77B3
P 3200 1500
F 0 "#PWR01" H 3200 1250 50  0001 C CNN
F 1 "GND" H 3200 1350 50  0000 C CNN
F 2 "" H 3200 1500 50  0000 C CNN
F 3 "" H 3200 1500 50  0000 C CNN
	1    3200 1500
	1    0    0    -1  
$EndComp
$Comp
L P_SUPPLY-rescue:CP C2
U 1 1 5A4B77BA
P 1700 4250
F 0 "C2" H 1725 4350 50  0000 L CNN
F 1 "1000u" H 1450 4150 50  0000 L CNN
F 2 "Capacitors_THT:CP_Radial_D10.0mm_P5.00mm" H 1738 4100 50  0001 C CNN
F 3 "" H 1700 4250 50  0000 C CNN
	1    1700 4250
	1    0    0    -1  
$EndComp
$Comp
L P_SUPPLY-rescue:GND #PWR02
U 1 1 5A4B77BB
P 2550 4500
F 0 "#PWR02" H 2550 4250 50  0001 C CNN
F 1 "GND" H 2550 4350 50  0000 C CNN
F 2 "" H 2550 4500 50  0000 C CNN
F 3 "" H 2550 4500 50  0000 C CNN
	1    2550 4500
	1    0    0    -1  
$EndComp
$Comp
L P_SUPPLY-rescue:CP C4
U 1 1 5A4B77BC
P 2050 4250
F 0 "C4" H 2075 4350 50  0000 L CNN
F 1 "100u" H 2100 4150 50  0000 L CNN
F 2 "Capacitors_THT:C_Rect_L7.0mm_W2.0mm_P5.00mm" H 2088 4100 50  0001 C CNN
F 3 "" H 2050 4250 50  0000 C CNN
	1    2050 4250
	1    0    0    -1  
$EndComp
$Comp
L P_SUPPLY-rescue:CP C5
U 1 1 5A4B77BD
P 3050 4250
F 0 "C5" H 3075 4350 50  0000 L CNN
F 1 "10u" H 3100 4150 50  0000 L CNN
F 2 "Capacitors_THT:CP_Radial_D5.0mm_P2.50mm" H 3088 4100 50  0001 C CNN
F 3 "" H 3050 4250 50  0000 C CNN
	1    3050 4250
	1    0    0    -1  
$EndComp
$Comp
L P_SUPPLY-rescue:+5V #PWR03
U 1 1 5A4B77BE
P 3050 4000
F 0 "#PWR03" H 3050 3850 50  0001 C CNN
F 1 "+5V" H 3050 4140 50  0000 C CNN
F 2 "" H 3050 4000 50  0000 C CNN
F 3 "" H 3050 4000 50  0000 C CNN
	1    3050 4000
	1    0    0    -1  
$EndComp
$Comp
L P_SUPPLY-rescue:PWR_FLAG #FLG04
U 1 1 5A4B77BF
P 2050 4000
F 0 "#FLG04" H 2050 4095 50  0001 C CNN
F 1 "PWR_FLAG" H 2050 4180 50  0000 C CNN
F 2 "" H 2050 4000 50  0000 C CNN
F 3 "" H 2050 4000 50  0000 C CNN
	1    2050 4000
	1    0    0    -1  
$EndComp
$Comp
L P_SUPPLY-rescue:PWR_FLAG #FLG05
U 1 1 5A4B77C0
P 3800 4350
F 0 "#FLG05" H 3800 4445 50  0001 C CNN
F 1 "PWR_FLAG" H 3800 4530 50  0000 C CNN
F 2 "" H 3800 4350 50  0000 C CNN
F 3 "" H 3800 4350 50  0000 C CNN
	1    3800 4350
	1    0    0    -1  
$EndComp
$Comp
L P_SUPPLY-rescue:Led_Small D2
U 1 1 5A4B77D3
P 3450 4250
F 0 "D2" H 3300 4200 50  0000 L CNN
F 1 "+5V" H 3400 4350 39  0000 L CNN
F 2 "LEDs:LED_D5.0mm" V 3450 4250 50  0001 C CNN
F 3 "" V 3450 4250 50  0000 C CNN
	1    3450 4250
	0    1    -1   0   
$EndComp
$Comp
L P_SUPPLY-rescue:R R2
U 1 1 5A4B77D4
P 3250 4050
F 0 "R2" V 3330 4050 50  0000 C CNN
F 1 "1k" V 3250 4050 50  0000 C CNN
F 2 "w_pth_resistors:RC03" V 3180 4050 50  0001 C CNN
F 3 "" H 3250 4050 50  0000 C CNN
	1    3250 4050
	0    -1   1    0   
$EndComp
$Comp
L P_SUPPLY-rescue:F_Small F1
U 1 1 5A4B77D9
P 1950 1200
F 0 "F1" H 1910 1260 50  0000 L CNN
F 1 "100mA" H 1830 1140 50  0000 L CNN
F 2 "Fuse_Holders_and_Fuses:Fuseholder5x20_horiz_SemiClosed_Casing10x25mm" H 1950 1200 50  0001 C CNN
F 3 "" H 1950 1200 50  0000 C CNN
	1    1950 1200
	1    0    0    -1  
$EndComp
$Comp
L P_SUPPLY-rescue:CONN_01X02 P2
U 1 1 5A4B77DA
P 1500 1650
F 0 "P2" H 1650 1650 50  0000 C CNN
F 1 "ON/OFF SW" H 1500 1800 50  0000 C CNN
F 2 "Connectors:bornier2" H 1500 1650 50  0001 C CNN
F 3 "" H 1500 1650 50  0000 C CNN
	1    1500 1650
	-1   0    0    1   
$EndComp
$Comp
L P_SUPPLY-rescue:D_Small D3
U 1 1 5A4B77E4
P 3700 1300
F 0 "D3" H 3850 1300 50  0000 L CNN
F 1 "1N4001" H 3600 1400 50  0000 L CNN
F 2 "Diodes_THT:D_DO-35_SOD27_P7.62mm_Horizontal" V 3700 1300 50  0001 C CNN
F 3 "" V 3700 1300 50  0000 C CNN
	1    3700 1300
	-1   0    0    -1  
$EndComp
$Comp
L P_SUPPLY-rescue:D_Small D5
U 1 1 5A4B77E5
P 4000 1300
F 0 "D5" H 3750 1300 50  0000 L CNN
F 1 "1N4001" H 3800 1400 50  0000 L CNN
F 2 "Diodes_THT:D_DO-35_SOD27_P7.62mm_Horizontal" V 4000 1300 50  0001 C CNN
F 3 "" V 4000 1300 50  0000 C CNN
	1    4000 1300
	-1   0    0    -1  
$EndComp
$Comp
L P_SUPPLY-rescue:D_Small D4
U 1 1 5A4B77E6
P 3700 1600
F 0 "D4" H 3850 1600 50  0000 L CNN
F 1 "1N4001" H 3550 1500 50  0000 L CNN
F 2 "Diodes_THT:D_DO-35_SOD27_P7.62mm_Horizontal" V 3700 1600 50  0001 C CNN
F 3 "" V 3700 1600 50  0000 C CNN
	1    3700 1600
	-1   0    0    -1  
$EndComp
$Comp
L P_SUPPLY-rescue:D_Small D6
U 1 1 5A4B77E7
P 4000 1600
F 0 "D6" H 3750 1600 50  0000 L CNN
F 1 "1N4001" H 3800 1500 50  0000 L CNN
F 2 "Diodes_THT:D_DO-35_SOD27_P7.62mm_Horizontal" V 4000 1600 50  0001 C CNN
F 3 "" V 4000 1600 50  0000 C CNN
	1    4000 1600
	-1   0    0    -1  
$EndComp
Text Notes 3700 1500 0    47   ~ 0
BRIDGE\n
$Comp
L P_SUPPLY-rescue:LM7805CT U2
U 1 1 5A4B77E8
P 2550 4100
F 0 "U2" H 2350 4300 50  0000 C CNN
F 1 "LM7805CT" H 2550 4300 50  0000 L CNN
F 2 "Power_Integrations:TO-220" H 2550 4200 50  0001 C CIN
F 3 "" H 2550 4100 50  0000 C CNN
	1    2550 4100
	1    0    0    -1  
$EndComp
$Comp
L P_SUPPLY-rescue:+12V #PWR06
U 1 1 5A4B7FC7
P 4200 1450
F 0 "#PWR06" H 4200 1300 50  0001 C CNN
F 1 "+12V" H 4200 1590 50  0000 C CNN
F 2 "" H 4200 1450 50  0000 C CNN
F 3 "" H 4200 1450 50  0000 C CNN
	1    4200 1450
	0    1    1    0   
$EndComp
$Comp
L P_SUPPLY-rescue:+12V #PWR07
U 1 1 5A4B8325
P 1700 4000
F 0 "#PWR07" H 1700 3850 50  0001 C CNN
F 1 "+12V" H 1700 4140 50  0000 C CNN
F 2 "" H 1700 4000 50  0000 C CNN
F 3 "" H 1700 4000 50  0000 C CNN
	1    1700 4000
	1    0    0    -1  
$EndComp
$Comp
L P_SUPPLY-rescue:LM7808CT U1
U 1 1 5A4B869C
P 1550 2700
F 0 "U1" H 1350 2900 50  0000 C CNN
F 1 "LM7808CT" H 1450 2900 50  0000 L CNN
F 2 "Power_Integrations:TO-220" H 1550 2800 50  0001 C CIN
F 3 "" H 1550 2700 50  0000 C CNN
	1    1550 2700
	1    0    0    -1  
$EndComp
$Comp
L P_SUPPLY-rescue:+12V #PWR08
U 1 1 5A4B8AE8
P 1100 2600
F 0 "#PWR08" H 1100 2450 50  0001 C CNN
F 1 "+12V" H 1100 2740 50  0000 C CNN
F 2 "" H 1100 2600 50  0000 C CNN
F 3 "" H 1100 2600 50  0000 C CNN
	1    1100 2600
	1    0    0    -1  
$EndComp
$Comp
L P_SUPPLY-rescue:GND #PWR09
U 1 1 5A4B8BB8
P 1550 3100
F 0 "#PWR09" H 1550 2850 50  0001 C CNN
F 1 "GND" H 1550 2950 50  0000 C CNN
F 2 "" H 1550 3100 50  0000 C CNN
F 3 "" H 1550 3100 50  0000 C CNN
	1    1550 3100
	1    0    0    -1  
$EndComp
$Comp
L P_SUPPLY-rescue:CP C3
U 1 1 5A4B8CA8
P 2050 2850
F 0 "C3" H 2075 2950 50  0000 L CNN
F 1 "22u" H 2100 2750 50  0000 L CNN
F 2 "Capacitors_THT:CP_Radial_D5.0mm_P2.50mm" H 2088 2700 50  0001 C CNN
F 3 "" H 2050 2850 50  0000 C CNN
	1    2050 2850
	1    0    0    -1  
$EndComp
$Comp
L P_SUPPLY-rescue:+8V #PWR010
U 1 1 5A4B8F03
P 2050 2600
F 0 "#PWR010" H 2050 2450 50  0001 C CNN
F 1 "+8V" H 2050 2740 50  0000 C CNN
F 2 "" H 2050 2600 50  0000 C CNN
F 3 "" H 2050 2600 50  0000 C CNN
	1    2050 2600
	1    0    0    -1  
$EndComp
$Comp
L P_SUPPLY-rescue:TRANSFO4 T1
U 1 1 5A4B9023
P 2600 1450
F 0 "T1" H 2600 1150 50  0000 C CNN
F 1 "127:12" H 2600 1750 50  0000 C CNN
F 2 "Transformers_THT:12V_transformer-3T" H 2600 1450 50  0001 C CNN
F 3 "" H 2600 1450 50  0000 C CNN
	1    2600 1450
	-1   0    0    1   
$EndComp
$Comp
L P_SUPPLY-rescue:-12V #PWR14
U 1 1 5A4BA189
P 3500 1450
F 0 "#PWR14" H 3500 1550 50  0001 C CNN
F 1 "-12V" H 3500 1600 50  0000 C CNN
F 2 "" H 3500 1450 50  0000 C CNN
F 3 "" H 3500 1450 50  0000 C CNN
	1    3500 1450
	0    -1   -1   0   
$EndComp
$Comp
L P_SUPPLY-rescue:CP C1
U 1 1 5A4BB159
P 1100 2850
F 0 "C1" H 1125 2950 50  0000 L CNN
F 1 "100u" H 1150 2750 50  0000 L CNN
F 2 "Capacitors_THT:C_Rect_L7.0mm_W2.0mm_P5.00mm" H 1138 2700 50  0001 C CNN
F 3 "" H 1100 2850 50  0000 C CNN
	1    1100 2850
	1    0    0    -1  
$EndComp
$Comp
L P_SUPPLY-rescue:GND #PWR011
U 1 1 5A4BB415
P 3550 3100
F 0 "#PWR011" H 3550 2850 50  0001 C CNN
F 1 "GND" H 3550 2950 50  0000 C CNN
F 2 "" H 3550 3100 50  0000 C CNN
F 3 "" H 3550 3100 50  0000 C CNN
	1    3550 3100
	1    0    0    -1  
$EndComp
$Comp
L P_SUPPLY-rescue:CP C7
U 1 1 5A4BB41B
P 4050 2850
F 0 "C7" H 4100 2750 50  0000 L CNN
F 1 "22u" H 4100 2950 50  0000 L CNN
F 2 "Capacitors_THT:CP_Radial_D5.0mm_P2.50mm" H 4088 2700 50  0001 C CNN
F 3 "" H 4050 2850 50  0000 C CNN
	1    4050 2850
	1    0    0    1   
$EndComp
$Comp
L P_SUPPLY-rescue:CP C6
U 1 1 5A4BB431
P 3100 2850
F 0 "C6" H 3100 2750 50  0000 L CNN
F 1 "100u" H 3150 2950 50  0000 L CNN
F 2 "Capacitors_THT:C_Rect_L7.0mm_W2.0mm_P5.00mm" H 3138 2700 50  0001 C CNN
F 3 "" H 3100 2850 50  0000 C CNN
	1    3100 2850
	1    0    0    1   
$EndComp
$Comp
L P_SUPPLY-rescue:LM7908CT U3
U 1 1 5A4BB509
P 3550 2700
F 0 "U3" H 3350 2500 50  0000 C CNN
F 1 "LM7908CT" H 3450 2500 50  0000 L CNN
F 2 "Power_Integrations:TO-220" H 3550 2600 50  0001 C CIN
F 3 "" H 3550 2700 50  0000 C CNN
	1    3550 2700
	-1   0    0    1   
$EndComp
$Comp
L P_SUPPLY-rescue:-12V #PWR10
U 1 1 5A4BB582
P 3100 2600
F 0 "#PWR10" H 3100 2700 50  0001 C CNN
F 1 "-12V" H 3100 2750 50  0000 C CNN
F 2 "" H 3100 2600 50  0000 C CNN
F 3 "" H 3100 2600 50  0000 C CNN
	1    3100 2600
	1    0    0    -1  
$EndComp
$Comp
L P_SUPPLY-rescue:-8V #PWR16
U 1 1 5A4BB5C0
P 4050 2600
F 0 "#PWR16" H 4050 2700 50  0001 C CNN
F 1 "-8V" H 4050 2750 50  0000 C CNN
F 2 "" H 4050 2600 50  0000 C CNN
F 3 "" H 4050 2600 50  0000 C CNN
	1    4050 2600
	1    0    0    -1  
$EndComp
$Comp
L P_SUPPLY-rescue:F_Small F3
U 1 1 5A4BB7E0
P 3450 1850
F 0 "F3" H 3410 1910 50  0000 L CNN
F 1 "1A" H 3330 1790 50  0000 L CNN
F 2 "Fuse_Holders_and_Fuses:Fuseholder5x20_horiz_SemiClosed_Casing10x25mm" H 3450 1850 50  0001 C CNN
F 3 "" H 3450 1850 50  0000 C CNN
	1    3450 1850
	1    0    0    -1  
$EndComp
$Comp
L P_SUPPLY-rescue:Led_Small D7
U 1 1 5A4BBCC1
P 4550 2850
F 0 "D7" H 4400 2800 50  0000 L CNN
F 1 "-8V" H 4450 2950 39  0000 L CNN
F 2 "LEDs:LED_D5.0mm" V 4550 2850 50  0001 C CNN
F 3 "" V 4550 2850 50  0000 C CNN
	1    4550 2850
	0    1    1    0   
$EndComp
$Comp
L P_SUPPLY-rescue:R R3
U 1 1 5A4BBCC7
P 4350 2650
F 0 "R3" V 4430 2650 50  0000 C CNN
F 1 "1k" V 4350 2650 50  0000 C CNN
F 2 "w_pth_resistors:RC03" V 4280 2650 50  0001 C CNN
F 3 "" H 4350 2650 50  0000 C CNN
	1    4350 2650
	0    -1   1    0   
$EndComp
$Comp
L P_SUPPLY-rescue:Led_Small D1
U 1 1 5A4BD57D
P 2550 2850
F 0 "D1" H 2400 2800 50  0000 L CNN
F 1 "-8V" H 2450 2950 39  0000 L CNN
F 2 "LEDs:LED_D5.0mm" V 2550 2850 50  0001 C CNN
F 3 "" V 2550 2850 50  0000 C CNN
	1    2550 2850
	0    1    -1   0   
$EndComp
$Comp
L P_SUPPLY-rescue:R R1
U 1 1 5A4BD583
P 2350 2650
F 0 "R1" V 2430 2650 50  0000 C CNN
F 1 "1k" V 2350 2650 50  0000 C CNN
F 2 "w_pth_resistors:RC03" V 2280 2650 50  0001 C CNN
F 3 "" H 2350 2650 50  0000 C CNN
	1    2350 2650
	0    -1   1    0   
$EndComp
Wire Wire Line
	3000 1650 3050 1650
Wire Wire Line
	3050 1650 3050 1850
Wire Wire Line
	3050 1250 3000 1250
Wire Wire Line
	3050 1000 3050 1250
Wire Wire Line
	1700 4050 2050 4050
Wire Wire Line
	2550 4350 2550 4450
Wire Wire Line
	2050 4000 2050 4050
Connection ~ 2050 4050
Wire Wire Line
	2050 4400 2050 4450
Connection ~ 2050 4450
Wire Wire Line
	3050 4000 3050 4050
Wire Wire Line
	2950 4050 3050 4050
Wire Wire Line
	3050 4450 3050 4400
Connection ~ 2550 4450
Connection ~ 3050 4050
Wire Wire Line
	1700 4400 1700 4450
Connection ~ 3050 4450
Wire Wire Line
	3450 4150 3450 4050
Wire Wire Line
	3450 4050 3400 4050
Wire Wire Line
	3450 4450 3450 4350
Wire Wire Line
	2100 1650 2200 1650
Wire Wire Line
	1800 1600 1700 1600
Wire Wire Line
	3800 1300 3850 1300
Connection ~ 3850 1300
Wire Wire Line
	3600 1300 3550 1300
Wire Wire Line
	3550 1300 3550 1450
Wire Wire Line
	3550 1600 3600 1600
Wire Wire Line
	3800 1600 3850 1600
Wire Wire Line
	4150 1600 4100 1600
Wire Wire Line
	4150 1300 4150 1450
Wire Wire Line
	4150 1300 4100 1300
Wire Wire Line
	4200 1450 4150 1450
Connection ~ 4150 1450
Wire Wire Line
	3500 1450 3550 1450
Connection ~ 3550 1450
Connection ~ 3850 1600
Wire Wire Line
	3850 1850 3850 1600
Wire Wire Line
	3550 1000 3850 1000
Wire Wire Line
	3850 1000 3850 1300
Wire Wire Line
	1700 1700 2100 1700
Wire Wire Line
	2100 1700 2100 1650
Wire Wire Line
	1100 2600 1100 2650
Wire Wire Line
	1100 2650 1150 2650
Wire Wire Line
	1550 2950 1550 3050
Wire Wire Line
	1100 3050 1550 3050
Wire Wire Line
	2050 3050 2050 3000
Connection ~ 1550 3050
Wire Wire Line
	2050 2600 2050 2650
Wire Wire Line
	1950 2650 2050 2650
Connection ~ 2050 2650
Wire Wire Line
	3200 1500 3200 1450
Wire Wire Line
	3200 1450 3000 1450
Wire Wire Line
	3050 1000 3350 1000
Connection ~ 1100 2650
Wire Wire Line
	1100 3000 1100 3050
Wire Wire Line
	3100 2600 3100 2650
Wire Wire Line
	3100 2650 3150 2650
Wire Wire Line
	3550 2950 3550 3050
Wire Wire Line
	4050 3050 4050 3000
Connection ~ 3550 3050
Wire Wire Line
	4050 2600 4050 2650
Wire Wire Line
	3950 2650 4050 2650
Connection ~ 4050 2650
Connection ~ 3100 2650
Wire Wire Line
	3050 1850 3350 1850
Wire Wire Line
	3550 1850 3850 1850
Wire Wire Line
	4550 2750 4550 2650
Wire Wire Line
	4550 2650 4500 2650
Wire Wire Line
	4550 3050 4550 2950
Wire Wire Line
	1700 4450 2050 4450
Wire Wire Line
	3800 4450 3800 4350
Connection ~ 3450 4450
Wire Wire Line
	3100 3050 3550 3050
Connection ~ 4050 3050
Wire Wire Line
	3100 3000 3100 3050
Wire Wire Line
	2550 2750 2550 2650
Wire Wire Line
	2550 2650 2500 2650
Wire Wire Line
	2550 3050 2550 2950
Connection ~ 2050 3050
Wire Wire Line
	1700 4000 1700 4050
Connection ~ 1700 4050
Wire Wire Line
	1700 1200 1850 1200
Wire Wire Line
	2050 1200 2150 1200
Wire Wire Line
	2150 1200 2150 1250
Wire Wire Line
	2150 1250 2200 1250
Wire Wire Line
	1800 1600 1800 1300
Wire Wire Line
	1800 1300 1700 1300
Text Notes 1600 2150 0    60   ~ 0
TRANSFORMER MODULE W/ DIODE BRIDGE AND FUSES\n
Wire Notes Line
	1100 800  1100 2250
Wire Notes Line
	1100 2250 4500 2250
Wire Notes Line
	4500 2250 4500 800 
Wire Notes Line
	4500 800  1100 800 
Text Notes 2000 4850 0    60   ~ 0
+5V REGULATOR W/ LED INDICATOR
Wire Notes Line
	1400 4950 4050 4950
Wire Notes Line
	4050 4950 4050 3700
Wire Notes Line
	4050 3700 1400 3700
Wire Notes Line
	1400 3700 1400 4950
Text Notes 1000 3500 0    60   ~ 0
+8V REGULATOR W/ LED INDICATOR\n
Text Notes 2950 3500 0    60   ~ 0
-8V REGULATOR W/ LED INDICATOR
Wire Notes Line
	2750 2350 2750 3600
Wire Notes Line
	900  2350 900  3600
Wire Notes Line
	900  2350 2750 2350
Wire Notes Line
	2850 2350 2850 3600
Wire Notes Line
	4750 2350 4750 3600
Wire Notes Line
	4750 2350 2850 2350
$Comp
L P_SUPPLY-rescue:CONN_01X02 P4
U 1 1 5A4C0021
P 3700 5400
F 0 "P4" H 3700 5550 50  0000 C CNN
F 1 "+5V OUTPUT" V 3800 5400 50  0000 C CNN
F 2 "Connectors:bornier2" H 3700 5400 50  0001 C CNN
F 3 "" H 3700 5400 50  0000 C CNN
	1    3700 5400
	1    0    0    -1  
$EndComp
$Comp
L P_SUPPLY-rescue:+5V #PWR012
U 1 1 5A4C00F6
P 3350 5300
F 0 "#PWR012" H 3350 5150 50  0001 C CNN
F 1 "+5V" H 3350 5440 50  0000 C CNN
F 2 "" H 3350 5300 50  0000 C CNN
F 3 "" H 3350 5300 50  0000 C CNN
	1    3350 5300
	1    0    0    -1  
$EndComp
Wire Wire Line
	3350 5300 3350 5350
Wire Wire Line
	3350 5350 3500 5350
$Comp
L P_SUPPLY-rescue:GND #PWR013
U 1 1 5A4C020F
P 3350 5500
F 0 "#PWR013" H 3350 5250 50  0001 C CNN
F 1 "GND" H 3350 5350 50  0000 C CNN
F 2 "" H 3350 5500 50  0000 C CNN
F 3 "" H 3350 5500 50  0000 C CNN
	1    3350 5500
	1    0    0    -1  
$EndComp
Wire Wire Line
	3350 5500 3350 5450
Wire Wire Line
	3350 5450 3500 5450
$Comp
L P_SUPPLY-rescue:CONN_01X03 P3
U 1 1 5A4C0356
P 2900 5450
F 0 "P3" H 2900 5650 50  0000 C CNN
F 1 "SYMMETRIC 8V OUT" V 3000 5450 50  0000 C CNN
F 2 "Connectors:bornier3" H 2900 5450 50  0001 C CNN
F 3 "" H 2900 5450 50  0000 C CNN
	1    2900 5450
	1    0    0    -1  
$EndComp
Wire Wire Line
	2600 5600 2600 5550
Wire Wire Line
	2250 5550 2600 5550
$Comp
L P_SUPPLY-rescue:GND #PWR014
U 1 1 5A4C062F
P 2550 5450
F 0 "#PWR014" H 2550 5200 50  0001 C CNN
F 1 "GND" H 2550 5300 50  0000 C CNN
F 2 "" H 2550 5450 50  0000 C CNN
F 3 "" H 2550 5450 50  0000 C CNN
	1    2550 5450
	0    1    1    0   
$EndComp
Wire Wire Line
	2550 5450 2700 5450
$Comp
L P_SUPPLY-rescue:-8V #PWR8
U 1 1 5A4C080C
P 2600 5600
F 0 "#PWR8" H 2600 5700 50  0001 C CNN
F 1 "-8V" H 2600 5750 50  0000 C CNN
F 2 "" H 2600 5600 50  0000 C CNN
F 3 "" H 2600 5600 50  0000 C CNN
	1    2600 5600
	-1   0    0    1   
$EndComp
$Comp
L P_SUPPLY-rescue:+8V #PWR015
U 1 1 5A4C0858
P 2600 5300
F 0 "#PWR015" H 2600 5150 50  0001 C CNN
F 1 "+8V" H 2600 5440 50  0000 C CNN
F 2 "" H 2600 5300 50  0000 C CNN
F 3 "" H 2600 5300 50  0000 C CNN
	1    2600 5300
	1    0    0    -1  
$EndComp
Text Notes 2350 6050 0    60   ~ 0
POWER SUPPLY OUTPUTS
Wire Notes Line
	1950 5050 1950 6150
Wire Notes Line
	900  3600 2750 3600
Wire Notes Line
	4750 3600 2850 3600
$Comp
L P_SUPPLY-rescue:PWR_FLAG #FLG016
U 1 1 5A4C6095
P 2250 5600
F 0 "#FLG016" H 2250 5695 50  0001 C CNN
F 1 "PWR_FLAG" H 2250 5780 50  0000 C CNN
F 2 "" H 2250 5600 50  0000 C CNN
F 3 "" H 2250 5600 50  0000 C CNN
	1    2250 5600
	-1   0    0    1   
$EndComp
Wire Wire Line
	2250 5600 2250 5550
Connection ~ 2600 5550
Wire Wire Line
	2600 5300 2600 5350
Wire Wire Line
	2600 5350 2700 5350
Wire Notes Line
	1950 6150 3950 6150
Wire Notes Line
	3950 6150 3950 5050
Wire Wire Line
	2050 4050 2150 4050
Wire Wire Line
	2050 4050 2050 4100
Wire Wire Line
	2050 4450 2550 4450
Wire Wire Line
	2550 4450 2550 4500
Wire Wire Line
	2550 4450 3050 4450
Wire Wire Line
	3050 4050 3050 4100
Wire Wire Line
	3050 4050 3100 4050
Wire Wire Line
	3050 4450 3450 4450
Wire Wire Line
	3850 1300 3900 1300
Wire Wire Line
	4150 1450 4150 1600
Wire Wire Line
	3550 1450 3550 1600
Wire Wire Line
	3850 1600 3900 1600
Wire Wire Line
	1550 3050 1550 3100
Wire Wire Line
	1550 3050 2050 3050
Wire Wire Line
	2050 2650 2050 2700
Wire Wire Line
	2050 2650 2200 2650
Wire Wire Line
	1100 2650 1100 2700
Wire Wire Line
	3550 3050 3550 3100
Wire Wire Line
	3550 3050 4050 3050
Wire Wire Line
	4050 2650 4050 2700
Wire Wire Line
	4050 2650 4200 2650
Wire Wire Line
	3100 2650 3100 2700
Wire Wire Line
	3450 4450 3800 4450
Wire Wire Line
	4050 3050 4550 3050
Wire Wire Line
	2050 3050 2550 3050
Wire Wire Line
	1700 4050 1700 4100
Wire Wire Line
	2600 5550 2700 5550
Wire Notes Line
	1950 5050 3950 5050
$EndSCHEMATC
