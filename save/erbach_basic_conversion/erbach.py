def normal(n,d):
    f = 10**n
    d1 = d * f
    d1 = int(d1)
    d1 = d1/f
    return d1

# *********************************
# *INDOOR MODEL POWER REQUIREMENTS*
# *COPYRIGHT 1990 BY WALTER ERBACH*
# *********************************
import math

L=[0.06, 0.135, 0.2, 0.25, 0.3, 0.35, 0.395, 0.44,0,0,0]
D = [0.008, 0.009, 0.01, 0.012, 0.014, 0.019, 0.024, 0.0335,0,0,0]
AW=150          # WING AREA IN SQ. INCHES
SW=AW/144       # WING AREA IN SW. FEET
WC = 5.5        # WING CHORD IN INCHES
WI=2            # WING INCIDENCE, DEGREES
WH=4            # WING HEIGHT IN INCHES
W=0.070         # OVERALL WEIGHT IN OUNCE
WT=W/16         # overall weight in pounds
PCW = 0.40      # RATIO OF STAB AREA TO WING AREA.
TA = 17.0       # wing MAC to stab MAC

for H in range(1,6):  # INDEXES WING INC.
    SA = -2
    P = [0,0,0,0,0,0,0,0,0,0]
    for J in range(1,7):  # INDEXES WING ANGLE OF ATTACK.
        CG=0.3

        jw = J+int(WI/2) - 1
        js = J-1

        VE = (WT/(0.00119*SW*(L[jw]+PCW*L[js])))**0.5
        AWL=L[jw]*SW*(0.00119)*VE*VE*16
        BWD=D[jw]*SW*(0.00119)*VE*VE*16
        CTL=L[js]*SW*PCW*(0.00119)*VE*VE*16
        DTD=D[js]*SW*PCW*(0.00119)*VE*VE*16

        print()
        print()
        print("{0:2.1f} DEG. WING INCIDENCE FOR THIS RUN".format(WI))
        print("{0:2.1f} deg. body/stab  angle  of attack".format(SA))
        print(jw,js,L[jw],D[jw], L[js], D[js])
        print("{0:3.1f} DEG. WING ANGLE OF ATTACK".format(WI+SA))
        print("{0:3.1f}% STAB AREA".format(PCW*100))

        VE = normal(2,VE)
        print("{0:3.2f} FT/SEC CALC. VELOCITY".format(VE))

        # CALC. POWER FOR THIS ANG.ATTACK"
        power = VE*(BWD+DTD)*12
        P[js] = VE*(BWD+DTD)*12
        P[js] = normal(3,P[js])
        #print(power, P[js], BWD, DTD)

        print("{0:1.3f} IN OZ/SEC POWER REQUIRED".format(P[js]))
        print()
        print("CG LOCATION .  MOMENT")
        print("% WING CHORD   IN OZ")
        M = [0,0,0,0,0,0,0,0,0,0,0,0]
        for K in range(1,9): # INDEXES CG FOR MOMENT CALCULATIONS.
            ki = K -1
            DW= WC*(CG -0.25)

            #R=SA*math.pi/180.0
            R=SA*6.28/360.0
            EWLA=WH*math.sin(R)-DW*math.cos(R)
            FWDA=WH*math.cos(R)-DW*math.sin(R)
            GTLA=(TA-DW)*math.cos(R)
            HTDA=(TA-DW)*math.sin(R)

            JMWL=-AWL*EWLA
            KMWD=+BWD*FWDA
            LMTL=-CTL*GTLA
            MMTD=-DTD*HTDA
            M[ki] = JMWL+KMWD+LMTL+MMTD
            M[ki] = normal(3,M[ki])
            CO=CG*100

            print("{0:3.1f}     {1:3.6f}".format(CO, M[ki]))

            CG=CG+0.1
        SA=SA+2
    WI = WI + 2
