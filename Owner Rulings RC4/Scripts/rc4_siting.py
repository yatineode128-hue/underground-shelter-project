"""rc4_siting.py -- U4 ruled EAST.  Re-run of SG2's siting checks."""
import math
W=[]
def w(s=""): W.append(s); print(s)
def rule(t): w(); w("="*84); w("  "+t); w("="*84)

def rect(x0,y0,x1,y1): return ('R',x0,y0,x1,y1)
def circ(cx,cy,r):     return ('C',cx,cy,r)

def dist(a,b):
    """clear distance between two shapes, mm (0 if they touch or overlap)"""
    def rr(A,B):
        dx=max(A[1]-B[3], B[1]-A[3], 0.0); dy=max(A[2]-B[4], B[2]-A[4], 0.0)
        return math.hypot(dx,dy)
    def rc(R,C):
        cx,cy,r=C[1],C[2],C[3]
        dx=max(R[1]-cx, cx-R[3], 0.0); dy=max(R[2]-cy, cy-R[4], 0.0)
        return max(math.hypot(dx,dy)-r, 0.0)
    if a[0]=='R' and b[0]=='R': return rr(a,b)
    if a[0]=='R' and b[0]=='C': return rc(a,b)
    if a[0]=='C' and b[0]=='R': return rc(b,a)
    return max(math.hypot(a[1]-b[1],a[2]-b[2])-a[3]-b[3], 0.0)

def radius(sh,pin):
    """furthest point of a shape from the pin, mm"""
    if sh[0]=='C': return math.hypot(sh[1]-pin[0],sh[2]-pin[1])+sh[3]
    return max(math.hypot(x-pin[0],y-pin[1]) for x in (sh[1],sh[3]) for y in (sh[2],sh[4]))

PIN=(11000.0,3100.0)

rule("T.1  THE PIN, RECOVERED FROM SG2'S OWN ARITHMETIC")
w("""
  SG2 measures its 50 m envelope 'about the pin' and never says where the
  pin is.  Its worst case is the reserve's far corner at 42.51 m.  Solving:
""")
far=(51000.0,17500.0)
w(f"    reserve far corner ({far[0]:.0f}, {far[1]:.0f})")
w(f"    |corner - (11000, 3100)| = {math.hypot(far[0]-PIN[0],far[1]-PIN[1]):.0f} mm = "
  f"{math.hypot(far[0]-PIN[0],far[1]-PIN[1])/1000:.2f} m   <-- SG2's 42.51 m, exactly")
w(f"  THE PIN IS THE BOX CENTRE ({PIN[0]:.0f}, {PIN[1]:.0f}).  [R] recovered, not assumed.")

rule("T.2  THE SENTRY POST -- WHAT THE DRAWING ACTUALLY SAYS")
w("""
  RULING: adopt the EAST position.

  Master DR-A1-V1 records the elevation's placement as 'X 31700 - 36300'.
  A-301's OWN NOTE 2 says something different:

    'THIS SHEET DRAWS THE SENTRY POST AT X 32000-36000, WHICH IS MASTER
     A.2's ">= 10 m CLEAR OF THE SHELTER EXCAVATION" CONVENTION AND NOT A
     SITE COORDINATE'

  X 32000 - 36000 is 4000 wide, which IS the sentry post's external
  dimension (master A.4.8, 4000 x 5000).  31700 - 36300 is 4600 and matches
  nothing.  THE DRAWING IS THE PRIMARY SOURCE AND IT IS SELF-CONSISTENT.
  FINDING RC4-F1: master DR-A1-V1's X range is wrong; corrected to
  X 32000 - 36000.

  AND THE Y IS STILL MISSING.  An ELEVATION cannot give a Y -- it is a view
  along Y.  So the EAST ruling fixes X and leaves Y to be set here.
""")
sx0,sx1=32000.0,36000.0
w(f"    X {sx0:.0f} - {sx1:.0f}   = {sx1-sx0:.0f} wide   [C] from A-301 note 2")
w(f"    clear of the box east face (X 22000)  = {sx0-22000:.0f} mm = {(sx0-22000)/1000:.1f} m")
sy0,sy1=600.0,5600.0
w(f"""
  Y ADOPTED  {sy0:.0f} - {sy1:.0f}  = {sy1-sy0:.0f} deep, centred on Y 3100   [A]

    - 5000 is the sentry post's other external dimension, so the footprint
      is the real one and not a guess at proportions
    - Y 3100 is the box longitudinal centreline: the post sits square on
      the shelter's own axis, which is the only symmetry the site has
    - it keeps the post SOUTH of SG2's external works reserve (Y 6500 up),
      so the two do not occupy the same ground
""")
SENTRY=rect(sx0,sy0,sx1,sy1)

rule("T.3  THE CLASH THE MASTER PREDICTED -- AND WHY IT DOES NOT HAPPEN")
RES=rect(33000.0,6500.0,51000.0,17500.0)
w(f"""
  Master DR-A1-V1: 'SG2's external works reserve is X 33000 - 51000, so the
  elevation's placement would put the sentry post INSIDE the reserve.'

    reserve   X {RES[1]:.0f} - {RES[3]:.0f}   Y {RES[2]:.0f} - {RES[4]:.0f}
    sentry    X {sx0:.0f} - {sx1:.0f}   Y {sy0:.0f} - {sy1:.0f}

  They DO overlap in X, over X 33000 - 36000.  They do NOT overlap in Y:
    reserve south edge  Y {RES[2]:.0f}
    sentry north face   Y {sy1:.0f}
    clear gap           {RES[2]-sy1:.0f} mm = {(RES[2]-sy1)/1000:.2f} m
""")
w(f"  clear distance, sentry to reserve = {dist(SENTRY,RES)/1000:.2f} m   -- NO OVERLAP")
w("""
  FINDING RC4-F2.  THE PREDICTED CLASH RESTED ON AN ASSUMED Y.
  The master reasoned from X alone and concluded the post would land in the
  reserve.  It only would if the post's Y overlapped Y 6500-17500 -- and an
  elevation never gave a Y.  With the post on the box centreline the reserve
  DOES NOT HAVE TO MOVE.  That is the good news.  The bad news is T.5.""")

rule("T.4  THE 50 m ENVELOPE, RE-RUN")
EXC =rect(-1000.0,-1000.0,23000.0,7200.0)
SEXC=rect(8250.0,4750.0,17050.0,8750.0)
ST01=rect(36000.0,15625.0,37500.0,16375.0)
SK01=circ(44000.0,16000.0,1100.0)
SK03=circ(41400.0, 8500.0,1100.0)
SK04=circ(47800.0, 8500.0,1100.0)
for lbl,sh in (("MAIN EXCAVATION + 1000 working space",EXC),
               ("STAIRWELL EXCAVATION + working space",SEXC),
               ("SENTRY POST  --  EAST, THIS RULING",SENTRY),
               ("ST-01 SEPTIC TANK",ST01),("SK-01 FOUL SOAK PIT",SK01),
               ("SK-03 STAIRWELL SOAKAWAY",SK03),("SK-04 HEADHOUSE SOAKAWAY",SK04),
               ("EXTERNAL WORKS RESERVE, far corner",RES)):
    w(f"    {lbl:44s} {radius(sh,PIN)/1000:8.2f} m")
w(f"""
    SENTRY POST radius   NORTH assumption 17.27 m  ->  EAST ruling {radius(SENTRY,PIN)/1000:.2f} m
    WORST CASE is still the reserve at {radius(RES,PIN)/1000:.2f} m, against 50.00 m available.
    EVERYTHING STILL FITS.  The sentry post is no longer the binding element.""")

rule("T.5  THE CHECK THAT FAILS  --  SK-02 AGAINST THE EAST SENTRY POST")
SK02_old=circ(35000.0,8500.0,1100.0)
d_old=dist(SENTRY,SK02_old)
w(f"""
  IS 2470: SOAK PIT TO ANY BUILDING >= 2.0 m  [C], and the sentry post is a
  building.  SG2 never had to check this -- its sentry post was 10 m NORTH,
  nowhere near SK-02.

    SK-02 as sited by SG2   centre (35000, 8500), wall radius 1100
                            -> spans X 33900-36100,  Y 7400-9600
    sentry north face       Y {sy1:.0f}
    clear separation        {d_old:.0f} mm  =  {d_old/1000:.2f} m
""")
w(f"  *** {d_old/1000:.2f} m  vs  2.00 m REQUIRED   ->   FAIL ***")
dy=300.0
SK02=circ(35000.0,8500.0+dy,1100.0)
d_new=dist(SENTRY,SK02)
w(f"""
  THE FIX -- MOVE SK-02 {dy:.0f} mm NORTH, and nothing else.
    SK-02 (35000, {8500.0+dy:.0f}), wall radius 1100  ->  Y {8500.0+dy-1100:.0f} - {8500.0+dy+1100:.0f}
    clear separation to the sentry post = {d_new/1000:.2f} m  vs 2.00 m   PASS
  A {dy:.0f} mm nudge is the whole cost of the EAST ruling in the layout.""")

rule("T.6  EVERY CHECK SK-02'S MOVE TOUCHES, RE-RUN")
checks=[("SK-02 wall to MAIN EXCAVATION + working space", SK02, EXC, 10.0,"[A]"),
        ("SK-02 wall to STAIRWELL EXCAVATION + wk space", SK02, SEXC,10.0,"[A]"),
        ("SK-02 wall to SK-03 wall",                      SK02, SK03, 4.0,"[A]"),
        ("SK-02 wall to SK-04 wall",                      SK02, SK04, 4.0,"[A]"),
        ("SK-02 wall to SK-01 wall",                      SK02, SK01, 4.0,"[A]"),
        ("SK-01 wall to SK-02 wall  (foul to clean)",     SK01, SK02, 5.0,"[A]"),
        ("ST-01 face to SK-02 wall  (foul to clean)",     ST01, SK02, 5.0,"[A]"),
        ("SK-02 wall to the SENTRY POST",                 SK02, SENTRY,2.0,"[C]")]
nfail=0
for lbl,a,b,lim,cls in checks:
    d=dist(a,b)/1000.0; ok = d>=lim-1e-9
    nfail += (not ok)
    w(f"  {lbl:48s} {d:7.2f} m  vs {lim:5.1f} m {cls}   {'PASS' if ok else '*** FAIL ***'}")
w("")
rule("T.7  EVERY CHECK AGAINST THE SENTRY POST, WHICH SG2 NEVER RAN")
s_checks=[("ST-01 face to the SENTRY POST", ST01, 2.0),
          ("SK-01 wall to the SENTRY POST", SK01, 2.0),
          ("SK-02 wall to the SENTRY POST", SK02, 2.0),
          ("SK-03 wall to the SENTRY POST", SK03, 2.0),
          ("SK-04 wall to the SENTRY POST", SK04, 2.0)]
for lbl,sh,lim in s_checks:
    d=dist(sh,SENTRY)/1000.0; ok=d>=lim-1e-9; nfail += (not ok)
    w(f"  {lbl:48s} {d:7.2f} m  vs {lim:5.1f} m [C]   {'PASS' if ok else '*** FAIL ***'}")
d_exc=dist(SENTRY,EXC)/1000.0
w(f"  {'SENTRY POST to the MAIN EXCAVATION face':48s} {d_exc:7.2f} m  vs {10.0:5.1f} m [C]   "
  f"{'PASS' if d_exc>=10.0 else '*** FAIL ***'}")
if d_exc < 10.0:
    nfail += 1
    w(f"""
  *** AND HERE IS THE SECOND ONE. ***
  Master A.2 / A.4.8: the sentry post stands '>= 10 m CLEAR OF THE SHELTER
  EXCAVATION'.  A-301 sets X 32000, which is 10.00 m clear of the BOX FACE
  at X 22000 -- but the EXCAVATION face, with its 1000 mm working space, is
  at X 23000.  Measured from the excavation, as the rule actually reads, the
  clearance is {d_exc:.2f} m.

  FINDING RC4-F3.  A-301's convention is 10 m FROM THE BOX, not from the
  excavation, and the sheet's own note cites the excavation rule while
  applying the box face.  To satisfy the rule AS WRITTEN the post moves to
  X 33000 - 37000.""")
    SENTRY2=rect(33000.0,sy0,37000.0,sy1)
    w(f"""
  IF THE POST MOVES TO X 33000 - 37000:
    to the excavation face          {dist(SENTRY2,EXC)/1000:.2f} m  vs 10.0 m [C]   PASS
    to the external works reserve   {dist(SENTRY2,RES)/1000:.2f} m   (still no overlap in Y)
    to ST-01                        {dist(SENTRY2,ST01)/1000:.2f} m  vs  2.0 m [C]   PASS
    to SK-02 as moved               {dist(SENTRY2,SK02)/1000:.2f} m  vs  2.0 m [C]   PASS
    envelope radius                 {radius(SENTRY2,PIN)/1000:.2f} m  vs 50.00 m     PASS
  BOTH READINGS ARE RECORDED.  NEITHER IS ADOPTED OVER THE OTHER HERE --
  the ruling was 'adopt the EAST position', and the EAST position is a
  CONVENTION on a drawing, not a survey coordinate.  U4 stays [A].""")
w("")
w(f"  RESULT OF THE RE-RUN:  {len(checks)+len(s_checks)+1} checks, {nfail} failing before the fixes above.")
open("/home/user/underground-shelter-project/Owner Rulings RC4/Calculations/RC4_SITING_OUTPUT.txt",
     "w").write("\n".join(W)+"\n")
