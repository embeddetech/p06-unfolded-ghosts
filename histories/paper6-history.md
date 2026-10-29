# Paper 6 history — "The conformal point is a phase boundary"

Release-gate ledger (publish/release-gate.md). Clean-pass counter
shown after each pass. Full details in notes.md (dated entries).

## 2026-07-12 — v0.1 drafted
9pp; science from the same day's arc: direction map
(p6_unfolding_sweep.py), divisor theorems (p6_divisor_gate/
theorem/dxd/cm_signs.py), devices (p6_d4_device.py). Four bibitems
self-flagged for audit.

## 2026-07-12 — AUDIT PASS 1 (three fresh agents). NOT CLEAN.
Counter: 0.

**Bibliography agent: 8 findings (3 MAJOR, 3 MINOR, 2 NIT).**
Majors: QubitEP2025 placeholder -> full entry (Zhang et al., PRL
135, 230203 (2025)); Starkov initial K -> G.A. (misattribution);
BGZ full entry (Ann. Phys. 492, 170569 (2026)). Minors: Chen-Ju
exact title; Smilga published title ("giving"); in-text QubitEP
characterization (non-Markovian EPs, the authors' own contrast).
Prior-art claims (a)-(d) ALL STOOD under fresh searches; zero
chimeras in 19 external refs; Rayleigh/Watson attribution verified
to page numbers.

**Numerics agent: 8 findings (3 MAJOR, 2 MINOR, 3 NIT); 85 numbers
traced clean.** Majors: (1) IK rates misattributed to "direct
integration" (they were frozen-mode eigenvalues — near-circular);
(2) the nonlinear IK reproduction existed only in a sidecar,
violating the paper's own reproducibility promise — FIXED by adding
block [3b] to p6_unfolding_sweep.py (reruns: blowups to 6 sig
digits, reldiff 4.4-4.6e-12); (3) "3% is exactly the
negativity-clean tolerance" overclaimed a sufficient condition as
a boundary (true boundary ~12%; factor-4 margin now stated).
Tolerance spot-checks PASSED (pi/Delta ratios and sqrt-3 crossing
converge under grid refinement — not artifacts).

**Claims/proofs agent: 13 findings (1 CRITICAL, 3 MAJOR, 5 MINOR,
4 NIT). All theorem algebra independently re-derived and
confirmed** (Prop 1, THM 1 series, THM 2 Hadamard + Rayleigh
values vs literature formulas at nu=0, window numerology,
Section-2 laws). CRITICAL: "complex-direction unfolding stays
negativity-free" was a FALSE CONVERSE — the negativity-free set is
the purely imaginary ray (and the EP) only; general split
delta = a+ib with a != 0 has non-monotone cascade ratio
(derivative changes sign; verified: monotone at split phase 90 deg
only, 0 decreasing intervals vs 919-1049 at other phases — new
script block [6] in p6_divisor_theorem.py). The corrected
statement SHARPENS the result: the divisor reads out Re(delta).
D5 device cases survive (both purely imaginary). Majors: abstract/
caption conflated the family oscillatory set (real axis) with the
generic one (single ray phi=0); "depth-three cascades" needed the
Jordan qualifier (reducible counterexample); dictionary IK-row
"negativity-free cascade" asserted an unproven depth-4 claim
(removed). Minors/nits: rescaled-variable pole statement; ratio
convergence scoped to rho=2,6; Rayleigh precision range corrected;
0.48/2.15-cm onsets flagged as finite-step protocol values;
"every t" -> "t>0"; strictly positive diagonal; theorem extended
to any eigenvalue.

ALL FINDINGS FIXED same-day; manuscript recompiled. Errors-with-
detectors logged in notes.md. PASS 2 (three fresh agents against
the corrected manuscript) required before counter can advance.

## 2026-07-12 — AUDIT PASS 2 (three fresh agents). NOT CLEAN.
Counter: 0.

Bibliography: 4 findings (1 MAJOR-process: push-hold must lift
before circulation; 1 MINOR fixed: dedicated home repos for
Companion2/3; 2 no-action nits). Zero accuracy errors; Eq.(58)
cross-numbering verified by direct count.

Numerics: 6 findings (1 MINOR, 5 NIT), 43/44 traced clean, all
grid-artifact spot-checks passed. Fixes: eta/J boundary made
script-traceable (measured ~13%: z* = 6.3/6.0/5.8 cm at 12/13/14%);
t_c precision restated ~1e-6; Rayleigh bound 3e-15; vacuous
worst_diag control repaired (now certifies 1.8e-2/8.5e-3/5.3e-3);
per-bond range 0.9982-0.9995; z* scoped to finite-step offset.

Claims/proofs: 7 findings (1 CRITICAL, 3 MINOR, 3 NIT). ALL
theorems/proposition re-verified sound. THE CRITICAL: pass-1's own
correction was STILL a false "exactly" — the scan sampled split
phases 0-180 deg only and was generalized; for Im(delta) < 0 an
open SILENT CONE hugging the lower real axis is negativity-free
(agent proved monotonicity for delta = 0.2-0.6i three ways).
Fixed with full-circle scan + bisection in the public script:
cone boundary 195.345 deg (15.345 deg from the real axis; mirror
344.655 deg), matching the agent's ~15.3. Manuscript now states
the half-plane law + silent cone as a sharp-threshold result the
paper owns. Minors fixed: intro kind-dependent oscillatory set;
omega_2^2 > 0 guard in abstract + caption; "prove" -> dominant-pole
"show" for the bands. Nits fixed: c_3 positivity now via exact
factorization 36 c_3 = (rho-1)(rho^2 - 8 rho + 19), negative
discriminant; (m+1)-th superdiagonal label; arXiv Eq.(3.24)
cross-reference.

LESSON (added to release-gate checklist candidates): scans over a
phase-like parameter must cover the FULL domain — two consecutive
false-converse criticals came from half-domain scans generalized.

## 2026-07-12 — AUDIT PASS 3 (three fresh agents). NOT CLEAN.
Counter: 0.

Bibliography: 3 findings (1 moderate, 2 minor), all wording —
zero external-record errors for the SECOND consecutive pass.
Fixed: Companion4/prop repository pointers made explicit; abstract
over-attribution of the (sqrt3/2)gamma_b rate to IK corrected
("the rate their equations imply").

Numerics: 6 findings (3 minor, 3 info), 50 traced clean; cone
boundary independently pinned 195.34485 deg on four grids +
tangency solve; seeds robust. Fixed: 15.345 (double rounding);
sigma_1 5.1e-12; discrete |Delta| points; protocol step stated at
onset ratios; 13-14% grid caveat; Eq.(3.24) item superseded (see
below).

Claims/proofs: 6 findings (1 MAJOR, 3 minor, 2 nits) — theorems
all sound again; NO third half-domain generalization found under
the explicit quantifier probe. THE MAJOR: silent-cone GEOMETRY
DESCRIBED BACKWARDS ("hugging the lower real axis" — the cone is
centered on the -i ray, spanning 195.345-344.655 deg; the wedges
near the real axis are the RECURRENT ones). Numbers were right,
picture inverted; abstract/body/intro corrected. Minors: zero-step
onset is 0.486 not ~0.50 (verified by convergence 0.4722->0.4858
before editing; paper 4's 0.50 was its dt=0.05 protocol value —
paper 4 line fixed too, audit counter note: paper 4 already reset
this session); eta/J boundary convention stated (agent's
window-aligned convention differs by one grid step — both now
disclosed); (3.24) arXiv parenthetical DROPPED (two agents gave
conflicting arXiv numbering testimony — only the agreed Eq. 58
retained). Nits: pi/|Delta| absolute values (5 places); z* offset
identified as exactly tau/2 (6.158/3.802 quoted).

Both papers recompiled clean. Counter: 0. PASS 4 launching.

## 2026-07-12 — AUDIT PASS 4 (three fresh agents). NOT CLEAN.
Counter: 0. First pass with ZERO criticals AND zero majors in
claims/proofs; zero accuracy errors in bibliography (3rd straight).

Bibliography: 4 findings (1 minor style — arXiv IDs added to
Klauck/Hatano-Nelson; 3 no-action informationals: Smilga title
variant, push-hold gate, self-declared device citation gap).
All 20 bibitems PASS; IK rate-attribution language verified clean.

Numerics: 3 findings (1 MAJOR: incomplete-fix propagation — the
0.486 correction had not reached p6_d4_device.py (still printed
"0.50/(2J) = 1.000") or proposal v1.1; both fixed, script rerun
prints 0.486/(2J) = 0.972; FIX-PROPAGATION added to the gate
checklist. 1 minor: same proposal line. 1 nit: stale cm_signs
docstring numbers.) 50 traced clean; tau/2 offset law verified at
three steps; cone brackets re-confirmed sharp + scale-invariant.

Claims/proofs: 7 findings (0 critical, 0 major, 3 minor, 4 nit).
All 12 verification items re-derived clean; NO residue of any of
the three historical criticals (explicit probes). Fixed: onset-
ratio protocol fully specified (0.02 pair step + 0.01 base grid,
detection = first grid point past pi/|Delta| - tau/2 — reconciles
the two sections); wedge dynamics corrected recurrent->TRANSIENT
(finitely many windows; spectrometer readable only early there —
genuine physics sharpening); abstract clause split (blowup
reproduction vs frozen-mode rate); open->closed cone (threshold
tangency is silent); exact time grid stated for interval counts;
conjugation-symmetry clause closes the family-sweep half-domain
residue; 0.48 protocol + both-direction rounding explained; D5
detunings restated at point of use.

Trend: findings 29 -> 17 -> 12 -> 14 (but severity collapsed:
criticals 1->1->0->0, majors 3+3+3 -> 1+3 -> 1 -> 1-process/1-prop).
Counter: 0. PASS 5 launching against the corrected manuscript.

## 2026-07-12 — AUDIT PASS 5 (three fresh agents). NOT CLEAN.
Counter: 0. Totals: 14 findings (biblio 6: 1 med/2 low/3 note;
numerics 4: 1 med/2 low/1 info; claims 4: 1 minor/3 nit). Zero
theorem errors for the FIFTH consecutive derivation; zero
bibliography accuracy errors for the fourth.

Substantive catches this pass: BARANDES NAMED-BUT-UNCITED (missed
by four prior passes — bibitem added, plus Stelle, Maldacena,
Merlin-coinage companion, NM-EP nearest-neighbor acknowledgment);
wedge gloss "single window over most of the wedge" untraceable
and wrong (measured: single-window regime = outer ~6 deg / 39% of
wedge; text now carries measured counts and the script counts
WINDOW RUNS, wedge phases added to the printed scan); stale
0.50/c comment (fix-propagation residue); both scan grids stated;
strict-count 1050 tolerance note; imperfection split-convention
stated in paper 6 + proposal; D4 kappa disambiguated; z* center
parenthetical. One bibitem (NMEPtheory 2406.18362) carries an
explicit author-list-to-verify marker for pass 6.

Severity trajectory (crit/major per pass): 1+3 -> 1+3 -> 0+1 ->
0+1(process) -> 0+0-with-2-mediums. PASS 6 LAUNCHING — first
plausible clean candidate.

## 2026-07-12 — AUDIT PASS 6 (three fresh agents). NOT CLEAN.
Counter: 0. Totals: 6 findings (biblio 2, numerics 3, claims 1).
Sixth consecutive derivation with zero theorem errors; fifth with
zero bibliography accuracy errors.

Biblio: 2 (1 major = the planted NMEPtheory author-list marker,
RESOLVED with verified record Lin-Kuo-Lambert-Miranowicz-Nori-Chen
Nat. Commun. 16, 1289 (2025); 1 minor = Barandes PoP volume 3(1),8
added). Merlin coinage placement verified by full-text search of
both DM PDFs.

Numerics: 3 (1 moderate + 2 low) — the 189-deg wedge endpoint
(I'd stated "1 window at 189-195" but 189 has 2 windows); fixed by
quoting only SAMPLED phases (190/193=1, 188=2, 181/185=4) and
covering the cone interior by the proved bisection instead of
scan-range phrasing; garbled D4 parenthetical rewritten. 51
traced clean.

Claims: 1 (major) — the SAME 189-deg endpoint, caught
independently; already resolved by the numerics fix (both agents
saw the pre-fix text; the sampled-phases rewrite covers it). All
theorems re-verified a sixth time; no residue of any of the four
historical failure modes.

The 189-deg finding = the generalize-beyond-measurement disease at
DEGREE granularity (half-plane -> wedge -> single degree across
passes). Systemic fix now in the text: quote sampled phases only,
never interpolated ranges. Counter: 0. PASS 7 launching — first
pass starting from a manuscript with NO known open items and six
clean derivation sweeps behind it.

## 2026-07-12 — AUDIT PASS 7 (three fresh agents, FIRST CROSS-MODEL
pass: agents now Opus 4.8 after Fable credit exhaustion; paper is
Fable-authored). NOT CLEAN but AT THE FLOOR.
Counter: 0. Totals: 7 findings, ALL nit/trivial/no-action.

Biblio (2): Smilga "giving"->"give" (Opus agent contradicted pass-6
agent; resolved by DIRECT arXiv fetch = "give"), DM serial comma.
All substantive entries re-confirmed a 2nd time cross-model; zero
accuracy errors (6th straight); no placeholders remain.

Numerics (3): ALL info/no-action ("no fix required"); cross-model
confirmation that paper 6's 0.486/base-grid diagnosis is the
numerically correct account. 48 traced clean.

Claims (2 nit): theorems re-derived a 7TH time, all sound. (1) my
"919-1049" interval count is implementation-noise at tol 1e-12
(agent's independent script: 1047; mine: 1049; only the strict
1050 is robust) -> reworded to quote the robust values (919, 953,
strict-1050) with the tail-sensitivity flagged. (2) "210-330 deg"
range-under-sampled-phases-label -> reworded (interior to proven
cone). No half-domain/inverted/propagation/interpolation residue.

CROSS-MODEL SIGNIFICANCE: an independent architecture (Opus)
adversarially re-verifying Fable-authored math + numerics + refs
found ZERO substantive defects and only 4 wording/formatting nits
across three agents. Strong evidence the manuscript is at its
quality floor and model-robust.

Provenance: commit trailer switched to Opus 4.8 from the swap point
(papers stay Fable-authored; audit-fix commits are Opus work).
Counter: 0. Assessment: at the floor. Launching pass 8; if pass 8
is likewise nit-only, HOLD per the stall valve and surface to
user (release-grade final pass reserved for Fable's return).

## 2026-07-12 — AUDIT PASS 8 (three fresh agents, cross-model Opus;
fresh-eyes + regression framing). NOT CLEAN but NEAR FLOOR.
Counter: 0. Totals: 5 findings (biblio 0 CLEAN, numerics 1 low,
claims 4: 2 minor 2 nit). Theorems re-derived 8th time, all sound.

Biblio: 0 findings - FULLY CLEAN (first fully-clean lane); both
prior title fixes confirmed vs source; no failure modes/placeholders.
Numerics: 1 low (reproducibility) - public script now prints strict
(<0) interval count so paper's strict-1050 reproduces from the
unmodified artifact. 48 traced clean.
Claims (fresh-eyes): found a REAL conceptual item six checklist
passes missed - MINOR #1: "complex-direction unfolding" mislabeled
the Ilhan-Kovner corner (which the paper's OWN taxonomy places at
phi=pi = REAL direction, imaginary SPLIT because omega_2^2<0),
risking conflation with the genuinely-complex Merlin row. Fixed in
all 3 places -> "imaginary-split unfolding (phi=pi, omega_2^2<0)".
Vindicates the fresh-eyes reframing: the gate still caught a
substantive taxonomic inconsistency at pass 8. Also fixed: #2
"the line"->"the exceptional line" (abstract); #3 500/500 attached
to "either way" -> scoped to the generic-ray sampling; #4 "all
deformation directions"->"the finite-frequency family's" (the k=0
corner is quartic-generic, not classified).

Since pass 8 found a SUBSTANTIVE (if minor) item, we are NOT at two
consecutive floor passes - loop continues. User (2026-07-12)
authorized continuing to apply trivial fixes on Opus + eventually
running the OTHER papers through the audit cycle. Provenance stays
clean (papers Fable-authored; Opus applies audit-driven
corrections + runs cross-model verification). PASS 9 to launch.

## 2026-07-12 — AUDIT PASS 9 (cross-model Opus; skeptical-referee +
regression framing). PIVOTAL: substantive claim-overstatement found.
Counter: 0. NOT clean; paper needs a THESIS RESCOPING, not polish.

Biblio: 0 (fully clean, 2nd straight; body edits didn't orphan cites).
Numerics: 3, ALL info/no-action (30 traced clean; no regression from
pass-8 edits).
Claims (SKEPTICAL REFEREE): 12 findings (1 CRITICAL, 3 MAJOR, 5 minor,
3 nit) - all CLAIM/SCOPE, zero calculational (theorems re-derived,
sound). Nine checklist passes missed these because they checked
correctness, not calibration-of-claims. Vindicates K>1 + varied
framing.

SUBSTANTIVE (QUEUED for user/Fable, NOT applied on Opus - thesis/
title-level authorship):
 F1 CRIT: "divisor reads out the direction" oversold. Negativity
   reads only Re(delta)/oscillatory-vs-not; +i (growing) and -i
   (decaying) both negativity-FREE. IK blowup = pure imaginary split
   = in the negativity-free set => the "spectrometer" may not detect
   the program's flagship ghost via negativity. (Whether the M2/
   mass-creation channel catches the size-4 corner is UNVERIFIED -
   needs computation.) Title "reads them out" needs rescoping.
 F2 MAJOR: "conditional mass creation" (column-sum crossing) is
   sigma_max-normalization-DEPENDENT (negativity is invariant, column
   sum is scaled by sigma_max^2(s)/sigma_max^2(s+tau)). Presented as
   physics + D5 lab signal w/o flagging convention; sigma_max never
   defined in-text. *** PROPAGATES TO PAPER 4 *** (its k=2 central
   result IS conditional mass creation) - paper-4 audit now running
   is directly relevant.
 F3 MAJOR: D5 observable not intensity-only (sigma_max needs complex
   U/phase); feasibility citation still a promissory note.
 F4 MAJOR: "stacked sectors mixed-mechanism as a theorem" assumes
   Smilga tower has IRREDUCIBLE k>=3 blocks - cited, not established
   here; "as a theorem" overreaches.

TRIVIAL-ISH (also HELD, to be reworked coherently with F1-F4 by
Fable, since they touch the same rescoped passages):
 F5 phi = phase-of-Delta (Layer1) vs phase-of-split (Layer2) differ
   at corner - state the Delta->sqrt map. F6 "predicts...no free
   params" oversells (map ingests IK's Delta_eff; nonlinear
   integration is the real corroboration). F7 "measured" used for
   SIMULATION throughout incl. abstract - reserve for the lab. F8
   band-convergence "we show...converge" is asymptotic+numerical,
   label as such vs Thms 1-2. F9 z_c +-0.015 finer than convention
   shift 0.06. F10 restate inherited conventions (sigma_max, beable
   basis, |U|^2). F11 "phase boundary" interpretive (title). F12
   provenance note shifts burden to proofs.

DECISION: HOLD entire revision for Fable + user (thesis/title
rescoping + F2 cross-paper coordination); paper-6 loop PAUSES pending
it. The theorems and every number stand; only the framing/claims
need rescoping. This is the session's most important audit outcome.

## 2026-07-12 — PASS-9 RESCOPING APPLIED (Fable resumed). v0.2.
Counter: 0 (content change). All 12 findings addressed:

F2 (sigma_max, SHARED with paper 4): resolved once for both papers —
conventions paragraph in Sec. 3 (definition; minimal-contraction
justification: sigma_max is the pointwise-least normalization
admitting a unitary dilation, the unique one discarding no survival
probability beyond what the dynamics loses); M1 signs
convention-FREE vs M2 column sums convention-RELATIVE; NEW
minimality dichotomy (crossing-free renormalization requires
c^2 >= c^2(0) e^{kappa^2 t^2}, Gaussian conditioning vs polynomial
dynamics, divergent overhead — verified in p6_divisor_gate.py [4],
t4_jordan_process.py [3b]). Also discharges F10.

F1 (CRIT, the thesis): resolved by a NEW COMPUTATION
(p6_m2_channel.py) rather than by softening alone:
 - the column-sum (M2) channel fires at EVERY split phase incl. the
   entire M1-silent set (onsets 0.30-0.68 over the full circle at
   |delta|=0.6), with an ASYMMETRIC onset on the imaginary axis
   (0.68 growing vs 0.30 decaying; robust at |delta|=0.3 and pair
   step 0.02): the second channel resolves exactly the sign
   negativity cannot.
 - the IK corner was never a bond: it is a SIZE-4 Jordan block, so
   Thm k2 (k>=3) makes it negativity-bearing REGARDLESS of
   direction — M1 onset = first grid point past the theorem's
   short-step boundary tau/(sqrt3-1) at both tau tested (0.07 vs
   0.0683; 0.03 vs 0.0273), identical for pure corner / phi=pi /
   phi=0, while M2 onsets differ by direction (0.80/0.91/0.73).
 Title rescoped: "a photonic device that reads them out" -> "a
 two-channel photonic readout". Abstract + intro Layer-2 + new
 Sec-3 paragraph ("The second channel, and the corner") reconcile
 Sec 2 with Sec 3; "direction spectrometer" now always scoped to
 the negativity channel + real part.

F3: sigma_max is INTENSITY-ACCESSIBLE for the triangular device
(U^dag U eigenvalues from measured Ghat alone; exact at
triangularity 6e-16, Weyl-bounded by sqrt(Ghat11 Ghat12) under
imperfection, rel 5e-3 at eta=3%J; p6_d4_device.py [1c]) — the
observable half dissolved. Feasibility half: promissory note
replaced by verified citation Weidemann et al., Science 368, 311
(2020) (HN anisotropic coupling realized in a photonic mesh
lattice; Szameit school) + honest transfer statement.

F4: "as a theorem" now properly anchored — the tower's M-quantum
sector is a single IRREDUCIBLE Jordan block of size M+1 by the
sector-tower proposition of Companion4 (constructive form of
Smilga); premise cited where proven, theorem chain closed.

F5: Delta -> sqrt(Delta) phase-halving map stated in Sec 2 (why a
real phi=pi family deformation arrives as an imaginary split).
F6: "predicts" -> "returns ... algebra once Delta_eff is given";
no-free-parameters weight moved to the nonlinear reproduction.
F7: measured -> computed/simulated for all simulation claims
(lab-context "measured/measurable" retained deliberately).
F8: band statements labeled dominant-pole asymptotics, explicitly
below Thm 1-2 strength (abstract + body).
F9: z_c +-0.015 scoped as statistical-at-fixed-protocol, with the
0.06 convention shift named part of the observable.
F11: "phase boundary" flagged as EP-sense analogy in Discussion.
F12: no action (honest disclosure stands); version line updated to
v0.2 "under audit; not yet released".

Recompiled clean (13 pp). PASS 10 (three fresh agents) to launch
against v0.2.

## 2026-07-12 — AUDIT PASS 10 (three fresh Fable agents). NOT CLEAN.
Counter: 0. Totals: 14 findings (biblio 1 NIT; numerics 1 MAJOR +
2 MINOR + 2 NIT; claims 1 MAJOR + 3 MINOR + 4 NIT). Theorems
re-derived a TENTH time, all sound; ~141 numbers traced by
numerics agent (all reproduce), ~60 by claims agent; both novelty
claims survive a sixth fresh search; biblio zero accuracy errors.

THE MAJOR (numerics; found independently in diagnostic form by my
own pre-verification): the D5 MC least-squares fit was
UNINFORMATIVE for J/Gd/eta on the balanced device — outputs pinned
at initialization (corr(etahat,eta)=0.024, corr(Jhat,J)=0.18
agent; 0.05/0.06 my replication at a different seed), so the
quoted "eta resolved to +-0.0075 (3% of J)" and "z_c +-0.015" were
ECHOES OF THE INJECTED PRIORS. Fix: balanced-device estimators
replaced by CLOSED-FORM CALIBRATION-FREE ones (Gd from
dark-subtracted log-slope of Ghat11; J+Gd from
sqrt(Ghat21/Ghat11)/z — calibration cancels exactly in the ratio).
New honest numbers (seeded rerun): J recovered +0.5%+-1.7%, corr
0.74 (printed as a control); z_c +-0.040 cm; z* +-0.22 unchanged
(Delta genuinely recovered by the retained LSQ fit, corr 0.88);
eta NOT resolved at 3% (Ghat12 signal at dark floor) — certified
via window cleanliness (<13%), z* re-entry for larger eta (6.9 cm
at 10%), and the [1c] Weyl residual; the non-recovery
corr(etahat,eta)=0.04 is now a PERMANENT PRINTED CONTROL.
Propagated to proposal (which also had a z*=pi/Delta mislabel of
finite-step values — fixed to the protocol-labeled form).
GATE-CHECKLIST CANDIDATE: MC "resolution" claims must be backed by
truth-vs-estimate CORRELATIONS, not by spreads (a spread can be a
prior echo).

The claims MAJOR (quantifier): "fires on every direction" rested
on a 30-deg scan. Fixed by DENSIFYING the public scan (5-deg grid,
72 phases: 0 silent, onsets exactly [0.30, 0.68] — the agent's own
independent 5-deg scan agreed) and wording all such claims as
sampled. Corner direction-independence now split honestly: theorem
for the corner block itself; computed at 12 sampled unfolding
phases at |Delta|=0.36 (onset 0.070 at every phase — new script
scan). Other fixes: "proven silent cone" -> computed; "as a matter
of theorem" -> the exact Sec-4 phrasing (negativity half only);
"throughout 210-330" -> sampled phases; abstract generic-ray
attribution (exact Puiseux eigenvalues, sampling only for the
probability-one part); det-fingerprint scoped to "this pair";
intro band sentence carries the asymptotic label; corner base grid
0.002 stated, onsets requoted at script precision (0.070/0.028;
M2 0.800/0.906/0.728); zero-step 0.486 now EMITTED by
p6_divisor_gate.py [4] (root of 2 k^2 t sigma^2 = (sigma^2)',
prints 0.4859) closing the reproducibility gap; ghost-turned-
tachyon hyphenated per the IK title; Smilga bibitem set to the
PUBLISHED "Giving" title after direct Crossref verification (DOI
10.1007/s10773-014-2404-2) — reverses pass-7's arXiv-based choice
with a stronger primary source; % comment in the bibitem records
the evidence.

All fixes applied; scripts rerun; recompiled clean (13 pp).
Counter: 0. PASS 11 launching.

## 2026-07-12 — AUDIT PASS 11 (three fresh Fable agents). NOT CLEAN
## but the closest yet: biblio CLEAN, numerics CLEAN (first
## double-clean lanes), claims 2 MINOR + 7 NIT (wording/hygiene only).
Counter: 0. Theorems re-derived an ELEVENTH time (sympy-grade), all
sound; numerics traced ~150/150; biblio verified all 25 entries incl.
the new Weidemann/Smilga entries, Eq. 58 re-confirmed with an
independent re-derivation of the Delta_eff translation; novelty
claims survive a seventh adversarial search. The repaired MC was
explicitly verified compliant with the new correlation rule.

Fixes applied (all wording/hygiene): code-availability scoped
(Merlin-row numbers reproduce from Companion4) + D4 divisor-det
print added to p6_d4_device.py [3] (first negative 2.11 cm, min
-28.6); "deep cascade" -> "deep JORDAN cascade" (2 places, the
detuned-cascade sign map does depend on detunings); Thm 2 carries
the any-eigenvalue clause its proof uses; abstract probability-one
statement re-graded exact-by-eigenvalues (sampling = corroboration);
corner +i parenthetical marked principal-branch + outside-bond-
classification; "fifth paper"/paper6-slot reconciled; "existing
platforms" -> "demonstrated platform capabilities"; D4 negativity
onset de-symboled (no t_c collision with the convention-relative
t_c); p6_unfolding_sweep worst-statistic now excludes phi=0,pi
explicitly (float sin(pi) junk-term guard). PLUS cross-paper title
propagation from the p5 pass-3 biblio: IK published title
"Ghost-turned tachyon" (Crossref-verified; bibitem + both in-text
coinages; reverses the pass-10 arXiv-based hyphenation with the
stronger source, % comment records the evidence).

Recompiled clean (13 pp). Counter: 0. PASS 12 launching (Opus
agents per the new model policy; Fable reserved for the K-1
confirming pass).

## 2026-07-12 — AUDIT PASS 12 (three fresh OPUS agents). NOT CLEAN
## by four sentences: biblio CLEAN, numerics CLEAN (~120 traced,
## robustness holds under refinement+reseeding, MC correlation gate
## explicitly satisfied), claims 2 MINOR + 2 NIT.
Counter: 0. Theorems re-derived a TWELFTH time (sympy), all sound;
the pass-11 Crossref title corrections were independently
re-verified by the biblio agent against the publisher records
(instructed not to trust the % comments).

Fixes applied:
- "fires everywhere" -> "fires at every sampled direction" (the one
  stray universal; script verdict line likewise re-worded).
- corr(Dhat, Delta) now PRINTED by p6_d4_device.py (0.86, genuine
  recovery control for the detuned/spectroscopy fit -- the agent
  verified 0.86 independently before we added the print; the z*
  +-0.22 claim now cites it in-text). Closes the last MC loop.
- Abstract no-free-parameters clause split so it attaches only to
  the nonlinear reproduction ("...while the map's frozen-mode rate
  ... is the rate their equations imply once their effective
  detuning is ingested").
- Body upgraded the generic-direction probability-one statement to
  its true analytic strength (exact Puiseux eigenvalues; sampling
  = corroboration), fixing an abstract-vs-body UNDERSELL.
Recompiled clean (13 pp). Counter: 0.

PASS 13 NOT YET LAUNCHED (user hold: session limit approaching; no
new passes). On resume: launch pass 13 with OPUS agents (counter
still 0; the Fable pass is reserved for counter = K-1).

## 2026-07-13 — AUDIT PASS 13 (three fresh Opus agents). NOT CLEAN
## by one notation item: biblio CLEAN, numerics CLEAN (~78/78,
## fresh-seed 7885/7885 sign-law robustness, MC correlation gate
## satisfied incl. corr(Dhat,Delta)=0.86), claims 1 MINOR + 2 NIT.
Counter: 0. Theorems re-derived a THIRTEENTH time, all sound; the
biblio agent re-verified both %-commented title decisions
independently and confirmed the Eq.-58 check again.

THE MINOR (a genuine 13-pass survivor): Delta means SQUARED-
frequency detuning in Sec. 2 (omega_2^2 = omega^2 + Delta) but
FREQUENCY split in Sec. 3+ (Delta = omega_1 - omega_2 = Sec. 2's
delta), and Table 1's Stelle row mixed both symbols for the same
quantity ("cost 2/delta; returns at pi/|Delta|") — quantitatively
misleading by a factor 2*omega to a reader carrying Sec. 2's
meaning. FIXED: explicit one-sentence notation map added after the
conventions paragraph (delta ~= Delta/2omega on the finite-
frequency line; both usages standard in their arenas); Stelle row
unified to delta. NITs: intro silent-set wording corrected to the
full silent SET (+i ray + cone, not "imaginary directions");
abstract "measures" -> "would measure" (proposal, not
measurement). Plus the numerics agent's no-action observation
acted on: p6_divisor_gate.py docstring R4 conjecture now
explicitly marked REFUTED by its own printouts (same docstring-
vs-data disease as the t4 pass-3 catch, preempted).

Optional hardening noted, not applied (pure suggestion, no
finding): cite Mandal arXiv:2603.25603 (Hessenberg-form Puiseux
classification, no divisibility content) near novelty claim A.
Holding for the next round's biblio agent to adjudicate as a
proper finding if warranted.

Recompiled clean (14 pp). Counter: 0. PASS 14 launching (Opus).

## 2026-07-13 — AUDIT PASS 14 (three fresh Opus agents). NOT CLEAN.
Counter: 0. Numerics CLEAN (~85/85, third consecutive clean
numerics lane); biblio 1 MAJOR (the Mandal adjudication, ordered
explicitly this pass: CITE — the directional-Puiseux half of
novelty claim A is anticipated by Mandal arXiv:2603.25603
(Hessenberg-form classification, sensing applications, zero
divisibility content); the compound claim survives literally but
brushed past the closest prior art while citing less-close 2026
work); claims 1 MINOR + 2 NIT (the Delta overload again — the
pass-13 notation map judged insufficient, full rename demanded;
slot-sentence copyedit; abstract cone precision).

Fixes applied:
- Mandal2026 CITED (arXiv record self-verified: I. Mandal, exact
  title) at the head of the Puiseux-literature sentence with the
  no-divisibility-content delimiter; novelty claim A narrowed to
  rest on the divisor sign-and-column-sum image ("the directional
  Puiseux classification itself has independent precedent
  [Mandal2026], and the divisor image is what is new here").
- FULL Delta->delta RENAME for the frequency split across
  abstract, intro, Sec 3, Sec 5 (13 edits; pi/|delta_i|, r(t)
  formula, onset laws, D5 spectroscopy delta=0.5/0.8); notation
  paragraph rewritten to the single-symbol rule (delta = frequency
  split everywhere; Delta = the omega^2 family detuning; corner
  map delta = sqrt(Delta) kept). The corner unfolding circle
  |Delta|=0.36 correctly RETAINED as family detuning. RIPPLE: the
  proposal's D5 paragraph renamed to match (3 sites; Delta-z the
  protocol step is a distinct symbol, kept).
- Slot sentence copyedited; abstract cone thresholds to ~195.3deg
  (precise values + bisection method remain in Sec 3).

Recompiled clean (14 pp paper6, 4 pp proposal). Counter: 0.
PASS 15 launching (Opus). NOTE: p5 reached counter 1 this same
session (its pass 7); p6's blockers remain wording-grade only.

## Pass 15 — 2026-07-13 (Opus x3; applied by Fable)

- Bibliography: CLEAN (all records re-verified vs Crossref/arXiv;
  no chimera; Mandal characterization confirmed).
- Claims: 1 MINOR — the provenance pledge said "every numerical
  claim is reproducible from the public scripts" but the Merlin
  row of the dictionary section reproduces from the revised
  companion's scripts, not this repo's. FIX: pledge now discloses
  the one exception inline.
- Numerics: 1 LOW — scripts still labeled the frequency split
  "Delta" in docstrings/prints after pass 14's manuscript-wide
  Delta->delta rename (p6_divisor_theorem, p6_divisor_dxd,
  p6_d4_device, p6_unfolding_sweep). FIX: 27 label edits, labels
  only; all four scripts rerun — numeric outputs unchanged
  (onsets/ratios identical); corr print now "corr(deltahat,
  delta)". Also corr(\hat\Delta,\Delta) -> corr(\hat\delta,\delta)
  in the manuscript at the device-fit control sentence.
- BOILERPLATE (no counter effect, rule-3 exception, logged): the
  audit-gate provenance sentence added to the page-2 pledge
  (identical across papers; AUDIT.md + histories/ pointer).

Recompiled clean (14 pp). Counter: 0. GATE CHANGE this pass:
K = 2 -> 3 (user accepted the escalation, 2026-07-13); model
policy: counter 1 and 2 confirming passes run on Fable, routine
passes on Opus. PASS 16 launching (Opus — counter 0).

BOILERPLATE LOG (2026-07-13, rule-3 exception, no counter effect):
the audit-gate provenance sentence now reads "repeated adversarial
audit passes" (user request — the sentence should say the agents
are prompted as hostile referees, which they are); identical edit
across all seven papers, recompiled clean.

## Pass 16 — 2026-07-13 overnight (Opus x3) — CLEAN (counter 1)

FIRST FULLY-CLEAN PASS for paper 6.
- Claims: CLEAN. Every theorem/prop re-derived independently
  (Prop 1 sign law, Thm 1 k=2-only with the s*=tau/(sqrt3-1)
  identity, Thm 2 Rayleigh alternation vs 2e5 J0-zeros, famlaw/
  genlaw/corner/IK). The one universal-over-directions claim
  (closed-UHP negativity-free set = +i ray + EP, exactly) verified
  as PROVED over its full domain; cone thresholds reproduced by
  the agent's own scan to 1e-3 deg. Notation reservation
  (delta/Delta) checked at every site — holds. +i/-i labeling
  cross-section consistent. Two no-action observations logged
  (gamma_b vs gamma_0 both defined; M2 sign-resolution correctly
  filed as computed).
- Numerics: CLEAN. ~61 numbers traced, all match; silent-cone
  boundary + Rayleigh sums independently re-derived; MC claims all
  carry printed truth-vs-estimate correlations; full-circle scans
  confirmed full-circle. Two no-action NITs (5e-12 rounding of
  4.6e-12; median ~sqrt(eps) tilde) — no change needed, logged.
- Bibliography: CLEAN. All 23 external records re-verified vs
  Crossref/arXiv (incl. independent re-confirmation of IK
  "Ghost-turned" and Smilga "Giving" %-comments); quotations
  verbatim; prior-art sweep (topic/author-cluster/recent listings
  through July 2026) found no anticipation of the two-channel
  divisor readout; nearest neighbors all cited and scoped.

Counter: 1 of K=3. PASS 17 launching on FABLE (counter-1
confirming pass per the 2026-07-13 model policy).

## Pass 17 — 2026-07-13 overnight (FABLE x3, counter-1 confirming)

COUNTER RESET 1 -> 0, and ESCALATION TRIGGER #2 (chronologically
the first of the night): the claims MAJOR below existed during
declared-clean pass 16. K stays 3 pending the user's morning
ruling.

- Claims (Fable): 1 MAJOR + 1 MINOR — the confirming pass earned
  its keep. MAJOR: "negativity-cleanliness of a 6 cm window
  bounds |eta|/J below the ~13% boundary" is FALSE on half its
  domain — negativity reads only eta>0 (real split); eta<0 gives
  a purely imaginary split that is negativity-silent at ANY
  magnitude (agent computed -14%/-20%/-50%/-100%: all clean; I
  independently re-verified with the paper's device model before
  accepting — +14% fires at -2.26, all negative etas at +0.0).
  The paragraph's own closing sentence even said so. FIX: the
  certification is now stated as explicitly two-channel —
  negativity bounds the eta>0 side (13-14% boundary), the silent
  eta<0 side is bounded by the sign-blind Weyl residual
  sqrt(Ghat11*Ghat12) [1c]; margin sentence updated; PROPAGATED
  to p6_d4_device.py docstring (same one-sided claim) and
  proposal/main.tex. MINOR: wedge window counts "4 within t<=40"
  depend on |delta| (6 at |delta|=1); now qualified "at
  |delta|=0.6" with completed-total counts marked
  scale-invariant. Everything else re-derived clean, incl. the
  full Hadamard/Rayleigh chain and Eq.-58 numbering
  independently.
- Bibliography (Fable): CLEAN (all records incl. GitHub repo
  existence for the Companion cites; Eq.-58 APS renumbering
  independently reconstructed; prior-art clean).
- Numerics (Fable): LANE ABORTED — the agent hit a scratch-path
  environment failure, lost its run outputs, went quiet for ~70
  minutes, and was killed after a nudge (its restart plan would
  have re-run everything from zero). The pass verdict (NOT
  CLEAN, counter 0) was already fixed by the claims MAJOR;
  numerics coverage is carried by pass 16's clean Opus lane and
  will be re-established fresh on the CURRENT text by pass 18.
  No partial numbers from the aborted lane were used.

Paper 6 + proposal recompiled clean (14 pp / 4 pp). Counter: 0 of
K=3. PASS 18 launching (Opus x3).

## Pass 18 — 2026-07-13 overnight (Opus x3)

- Claims: CLEAN. All three formal results + every in-text
  computation re-derived from scratch; silent-cone threshold
  independently re-bisected to 195.34485 deg; window counts
  1/1/2/4/4 independently reproduced; sign-domain and
  quantifier probes all pass (the b>=0 "exactly" iff proven both
  directions). Two no-action NITs logged (2/sqrt-delta generic
  contrast wording; c_m dimensionful-vs-rescaled normalization,
  explicitly disambiguated in-text).
- Bibliography: CLEAN. All records re-verified (Klauck page 883
  confirmed against a bad intermediate fetch; high-numbered 2026
  IDs all real); prior-art sweep clean; Barandes 2507.21192
  assessed optional.
- Numerics: 1 MAJOR + 1 NIT — the traceability gap in MY OWN
  pass-17 fix: the manuscript's "(computed: no in-window
  negativity at eta/J=-14% through -100%)" was verified in
  scratch but NOT emitted by the committed script (p6_d4_device
  [1b] scanned only -3% on the negative side) — violating the
  reproducibility pledge. FIX: [1b] frac tuple extended with
  -0.14/-0.30/-0.50/-1.00; script rerun — emits the silence
  lines (-100%: window min entry +0.0, z* > 30 cm), numbers
  unchanged. The agent independently confirmed the physics to
  -200% and located the true boundary at 13.5-13.8% (quoted
  13-14% grid claim stands). NIT: "1% scan grid" phrasing now
  "1% grid near the boundary". ~78 numbers traced, ~77 exact,
  ZERO wrong.

Recompiled clean (14 pp). Counter: 0 of K=3. PASS 19 launching
(Opus x3).

## Pass 19 — 2026-07-13 overnight (Opus x3) — CLEAN (counter 1)

- Claims: CLEAN. Every result re-derived from scratch; the
  sign-domain quantifiers explicitly probed (family both-signs
  vs generic positive-ray asymmetry verified exact; the b>=0
  "exactly the +i ray and the EP" iff confirmed analytically;
  cone thresholds independently re-bisected to 195.34485 deg).
  Two no-action NITs (median ~sqrt(eps) tilde; phi as arg-Delta
  vs arg-delta reading hazard, already flagged in-text).
- Numerics: CLEAN, 67/67 exact. The pass-18 eta-sweep fix traces
  perfectly ([1b] emits both the +13/14% boundary and the
  -14..-100% silence); adversarial probes (1-deg phase grid, 4
  seeds, tolerance sweeps) STRENGTHENED the sampled claims; the
  Merlin-row exemption honored as the single disclosed
  exception. Two no-action NITs (D4 onset gap loosest agreement,
  honestly framed; Merlin-row out-of-set by design).
- Bibliography: CLEAN (third consecutive; all records +
  characterizations re-verified).

Counter: 1 of K=3. PASS 20 launching on FABLE (counter-1
confirming pass per model policy).

## Pass 20 — 2026-07-13 ~02:50 (FABLE x3, counter-1 confirming) — INCOMPLETE

- Numerics (Fable): CLEAN (106/106; cone boundary re-bisected at
  5 grid/tolerance combos to 1e-6 deg; eta boundary probed at 3
  window grids — 13% clean at all, factor-four margin stands;
  every "exactly" re-derived as genuine algebra).
- Bibliography (Fable): 1 MAJOR (release-checklist, NO text
  change: the five self-citation bibitems + the provenance note
  assert public records that are true only after the
  publish-hold-lift GitHub sync — repos currently 163 commits
  behind / placeholder READMEs; made an explicit pre-circulation
  gate step), 1 MINOR (add Wong-Zeng-Li, npj Quantum Inf. 12, 63
  (2026), DOI 10.1038/s41534-026-01205-2 — channel-level EPs
  explicitly violating CP-divisibility — to the "closest
  EP-divisibility contact" sentence; VERIFY the record per rule 7
  before applying), 1 NIT (Pimenta arXiv title capitalization
  "Stochastic-Quantum"). PENDING APPLICATION after reset.
- Claims (Fable): LANE DIED MID-RUN — session limit. RELAUNCH
  after reset. Pass verdict HELD OPEN; counter remains 1 pending.

## Pass 20 — CLOSED 2026-07-13 morning (claims lane relaunched post-limit)

COUNTER RESET 1 -> 0; ESCALATION TRIGGER #7 (findings existed
during declared-clean pass 19).
- Numerics (Fable): CLEAN 106/106 (ledgered at checkpoint).
- Bibliography (Fable): 1 MINOR + 1 NIT, applied post-reset:
  Wong-Zeng-Li npj QI 12, 63 (2026) added to the EP-divisibility
  sentence (Crossref-verified); Pimenta title capitalization per
  the arXiv record. Plus the public-repo-sync MAJOR logged as a
  pre-circulation checklist item (no text change).
- Claims (Fable relaunch): 1 MINOR + 3 NIT. MINOR: the
  renormalization-necessity "only if" was attributed to script
  block [4], which verifies only the column-sum law and the
  envelope's SUFFICIENCY; the necessity needs a telescoping
  argument the text never gave. The agent supplied and verified
  it (pairwise bound + refinement of the partition -> Gaussian);
  the text now states the telescoping inline and scopes the
  block-[4] attribution correctly. NITs: Gamma_M defined at first
  use (pole width as a frequency, gamma/m_r, Companion4's
  convention); p6_unfolding_sweep.py's stale summary prose
  tightened (oscillatory set = family real axis + generic
  positive ray ONLY; mixed complex splits get transient M1
  windows, not M1-freedom) — rerun, labels-only change verified;
  cond(V) -> cond(S) to clear the collision with Prop 1's
  V(t)=|U(t)|^2. Everything else re-derived clean (the agent's
  own 1491-configuration adversarial ensemble; 0.05-deg cone
  interior sweep found zero negativity pockets; full
  eta-certification table reproduced from its own device model).

Recompiled clean (14 pp). Counter: 0 of K=3. PASS 21 launching
(Opus x3).

## Pass 21 — 2026-07-13 morning (Opus x3) — CLEAN (counter 1)

- Claims: CLEAN. Every result re-derived (sympy-symbolic where
  possible); the NEW telescoping-necessity argument verified
  valid ("sup attained since refinement increases the product");
  the b>=0 iff checked on both branches; cone boundary
  independently reproduced. Two NITs explicitly no-change
  (delta first-use forward-reference optional; c_m dual
  normalization already disambiguated in-text — logged so no
  future editor "unifies" them).
- Numerics: CLEAN, ~85/85; four highest-risk claims re-probed
  under perturbed tolerances/grids/parameters (decay-split
  M1-freeness at 18 parameter combos; c3 positivity on 50k
  points; M2 asymmetry sign robust at a third |delta| and three
  taus; cone boundary grid-independent).
- Bibliography: CLEAN (all records incl. WongZengLi2026 and the
  Pimenta capitalization %-comment re-verified; the optional
  Barandes 2507.21192 add no-actioned a third time — no
  exhaustiveness claim in tension).

Counter: 1 of K=3. PASS 22 launching on FABLE (counter-1
confirming pass per model policy).

## Pass 22 — 2026-07-13 morning (FABLE x3, counter-1 confirming)

COUNTER RESET 1 -> 0; ESCALATION TRIGGER #9 (finding existed
during declared-clean pass 21).
- Numerics (Fable): CLEAN 98/98 (perturbed grids/tolerances; both
  eta sign domains from [1b]; Merlin-row exception honored).
- Bibliography (Fable): CLEAN, zero findings (Eq.-58 APS
  renumbering independently reconstructed a second time: 34+24;
  Merlin coinage verified in the PRL full text; all %-comments
  re-held; WongZengLi preprint ID 2507.16049 noted as optional
  polish).
- Claims (Fable): 1 MINOR — ONE WORD: intro line 186 said "a
  deep cascade's divisor" where Theorem 2 delivers only the
  JORDAN cascade (the general detuned cascade oscillates at
  pi/|delta_i| instead, as the same paragraph states); the body
  carries the qualifier at both other sites. Fixed: "a deep
  Jordan cascade's divisor". Deep no-action set logged: the
  Weyl-bound exactness re-derived (triangle inequality makes it
  exact, not just Weyl-generic); the generic-direction claim
  hostile-tested beyond its declared model (real perturbations
  of the physical companion: 2000/2000 growing); "total
  positivity" phrasing noted nonstandard-but-recoverable.

Recompiled clean (14 pp). Counter: 0 of K=3. Next pass HELD
pending the user's Opus-vs-Fable policy ruling (as is paper 4's
pass 23).

## Pass 23 — 2026-07-13 (Opus x3) — CLEAN (counter 1)

- Claims: CLEAN (all theorems re-derived; the telescoping
  necessity re-verified with the supremum argument; two
  no-action observations — crossing-column phrasing, D5
  lower-vs-upper triangular orientation).
- Numerics: CLEAN 47/47 (negative-eta silence extended to -200%;
  eta boundary refined to (13.5%, 14%] — manuscript conservative).
- Bibliography: CLEAN — with a RULE-7 REJECTION: the agent
  claimed Stelle 1977's published title is unhyphenated; the raw
  Crossref title field carries the hyphen ("higher-derivative"),
  bibitem correct. Logged in auditor-error-log. WongZengLi
  arXiv-ID add remains optional no-action; Eq.-58 numbering
  already twice independently reconstructed.

Counter: 1 of K=3 (fourth return). OPUS DRY STREAK = 3 (passes
19, 21, 23 — one short of retirement under the N=4 rule). PASS
24 launching on FABLE (counter-1 confirming pass).

## Pass 24 — 2026-07-13 (FABLE x3) — INCOMPLETE (wind-down kill)

- Numerics (Fable): CLEAN, ~130 traced, zero mismatches (finer
  eta-grid puts the true boundary at ~13.3%, inside the stated
  13-14%; all probes passed).
- Bibliography (Fable): 1 MAJOR = the reorg URL sweep not yet
  applied to paper 6 — APPLIED (counter-neutral per the rule-3
  reorg exception): Companion/2/3 -> p01/p02/p03, provenance +
  Companion4/3prop routing -> ghosts-program hub. WongZengLi
  arXiv-ID NIT raised a third time, still optional no-action.
- Claims (Fable): KILLED mid-run at the user's wind-down (account
  switch). Its last report confirmed a typo at line 284 —
  "genericially" -> "generically", VERIFIED and FIXED. Any
  further findings it had are lost; pass 24 is INCOMPLETE and
  does not adjudicate. Counter remains 1 (pass 23) pending a
  fresh Fable confirming pass next session.

Recompiled clean (14 pp).

## Rescope-integrity re-audit — 2026-07-13 (Opus x1, UNCOUNTED)

User-directed confirmation of the pass-9 rescope (v0.2), NOT a counter
pass — counter stays 1 (pass 23). One hostile-referee agent, no
histories/notes access, the four original pass-9 findings supplied
verbatim as the checklist; re-derived the fix sites and re-ran the p6_*
scripts. ALL FOUR RESOLVED:
- F1 (CRIT): title "two-channel photonic readout"; negativity scoped to
  Re(delta) + explicit silent sector; IK/+i in the silent set; M2
  channel re-run fires at every sampled phase (+i 0.68 / -i 0.30 / EP
  0.48; 72-phase scan 0 silent); size-4 corner Thm-k2 onset 0.070 at
  every unfolding; "sampled" hedge present throughout.
- F2 (MAJOR): sigma_max defined + pointwise-least justification correct;
  convention flagged at every M2 site incl. D5.
- F3 (MAJOR): Weidemann Science 368 at the load-bearing site; triangular
  intensity-accessibility argument given + algebra verified +
  p6_d4_device.py reproduces (6e-16 / 5.1e-3 vs Weyl 5.39e-3).
- F4 (MAJOR): "as a matter of theorem" scoped to a single irreducible
  block; reducible carve-out stated; irreducibility an honest imported
  premise (permitted).
No new oversold phrasing. No edits applied (nothing to fix). Verdict:
rescope sound; theses established-not-asserted.

## Pass 25 — 2026-07-13 (FABLE x3) — NOT CLEAN (counter 1 -> 0 on fix apply)

- Numerics: CLEAN. Every number traced to fresh p6_*.py output (0
  mismatches), 7/7 rc=0, boundaries robust under perturbed
  tol/grid/seed; eta/J first-negativity +13.6% => manuscript's
  "13-14%" is CONSERVATIVE.
- Claims: 3 findings, all VERIFIED then FIXED (rule 7):
    F1 (NIT) T used at ~:381 before its only definition (Thm 2,
      :559). Grep-confirmed no earlier def; s+tau already in use
      (:350/:375/:413/:418). FIX: introduced "T=s+\tau" at first
      use (:381).
    F2 (MINOR) xi, N_eff used at :711-717, defined nowhere in p6
      (grep-confirmed: only occurrences). FIX: pinned "in the
      notation of the revised \cite{Companion4}" at first use;
      did NOT fabricate their definitions.
    F3 (NIT) varphi=0 corner mislabeled "oscillatory" (:536) —
      EOM d^2(d^2+Delta)x=0 -> {1,t,e^{+-i sqrt(Delta) t}}, so a
      secular (1,t) doublet persists (not purely oscillatory).
      FIX: "oscillatory one" -> "imaginary-split one", which names
      the character of the varying pair (parallel to varphi=pi's
      real split) without overclaiming and without the agent's
      wrong "non-growing" (the (1,t) doublet IS boundary-
      polynomial-growing). Aligns with the paper's own "real part
      / imaginary directions of the split" language (:541-542).
- Bibliography: 2 findings applied:
    F1 (counter-NEUTRAL, rule-3 reorg exception) Companion* repo
      pointers reconciled to OPTION A (USER DECISION 2026-07-13):
      each paper -> its OWN pNN- repo, no cross-pointing into p01.
      Companion2 -> p02 (dropped "source in main program repo"),
      Companion3 -> p03 (same), Companion4 hub -> p04-choosing-
      ghosts, Companion3prop -> p06-unfolded-ghosts source in
      proposal/. SUPERSEDES the pass-24 hub-routing note for
      Companion4/3prop.
    F2 (MINOR) Maldacena2011 (:1066) missing year. FIX: added
      "(2011)" to "arXiv:1105.5632" (verified: 1105.5632
      "Einstein Gravity from Conformal Gravity", Maldacena 2011).
- REJECTED leads (already correct, logged to auditor-error-log):
  IK2014 "Ghost-turned tachyon" hyphenation, Smilga2014
  "Giving"/(2015), Donoghue-Menezes serial comma — all match
  published Crossref.

Counter: reset 1 -> 0 (claims F1/F2/F3 + biblio F2 are counter-
resetting). ALL-FABLE pass, so the Opus dry streak (3 of 4) is
untouched. Recompiled clean (14 pp); log shows no errors, no
undefined refs/citations.

## Pass 26 — 2026-07-13 (OPUS x3) — NOT CLEAN (counter stays 0)

Opus dry streak does NOT advance (Opus lane produced accepted
findings) -> Opus retirement (N=4) NOT triggered; streak resets to 0.

- Numerics: CLEAN. 90/90 traced (89 to p6 scripts + Merlin row to
  disclosed companion), all 7 scripts rc=0; MC correlations genuine
  and seed-robust incl. the non-recovery control corr(etahat,eta);
  silent-cone boundary independently re-bisected to 195.3449 deg;
  every "exact/zero" structural not epsilon; prior half-domain scan
  confirmed now full-circle. Two no-action INFO (sigma_1 5.1e-12 is
  tail-correction-assisted, already disclosed "analytic tail
  correction"; median rate ~0.7 sqrt(eps) under the "~", defensible).
- Bibliography: CLEAN. All 27 bibitems verified vs Crossref/arXiv;
  both %-commented published-title cases (Smilga "Giving", IK
  "Ghost-turned") re-confirmed correct; "Eq. (58) of IK2014" correct;
  both sharpest novelty claims survive a fresh sweep. INFO only.
- Claims: 3 findings VERIFIED then FIXED (rule 7), 1 no-action, 1
  reorg-class:
    F1 (MINOR, counter-resetting) REVERSES pass-25's own F3 fix.
      Pass 25 changed varphi=0 "oscillatory" -> "imaginary-split"
      (:537); that was WRONG. At the corner delta=sqrt(Delta), so
      varphi=0 (Delta>0) gives delta REAL = oscillatory/real split;
      varphi=pi (Delta<0) gives the imaginary split (the IK blowup).
      Pass 25 conflated the persistent {1,t} secular doublet (present
      for ALL corner unfoldings) with the SPLIT character. Confirmed
      by p6_m2_channel.py [2], which labels the varphi=0 case
      "(oscillat.)" with M2 onset 0.728 -- exactly the manuscript's
      "0.728 respectively" for varphi=0. FIX: "imaginary-split one"
      -> "real-split one" (names the split's real character without
      the bare "oscillatory" pass 25 rightly avoided for the doublet).
    F2 (MINOR, counter-resetting) "spectrometer for / reads out the
      real part of the split" overstates by a sign: the negativity
      channel reads |Re delta|, blind to sign(Re delta). Confirmed by
      p6_divisor_theorem.py [6]: 30/150 deg both 919 decreasing
      intervals, 60/120 deg both 1049 -- identical across sign(Re)
      flips at equal |Re|,Im. FIX: "the real part" -> "the magnitude
      of the real part" at all 4 readout sites (abstract, intro,
      Prop-region, body); added one clause noting sign(Re delta) is a
      residual ambiguity of the negativity channel. ("paced by the
      real part" left as-is: a pace is a magnitude, not flagged.)
    F3 (NIT, counter-resetting) intro dropped "the EP" from the
      M1-silent set (abstract :79-80 and body :468 list it). FIX:
      added "the EP" to the intro list.
    F4 (NIT, NO ACTION) undefined xi/N_eff/m_r in the Merlin
      paragraph -- already pinned "in the notation of the revised
      \cite{Companion4}" by pass 25, and m_r defined via M^2=m_r^2+i
      gamma; adequately disclosed (the Merlin exception). No change.
    F5 (NIT, counter-NEUTRAL rule-3 reorg exception) intro repo-slot
      sentence claimed "the standing experimental proposal occupies
      the intervening slot" -- false: per publish/repo-reorg.md the
      proposal ships INSIDE p06, and slot p05 is paper7
      (renormalized-ghosts). FIX: adopted paper7's sibling phrasing
      ("repository slot paper6, the program's numbering being fixed
      at drafting time"), dropping the wrong proposal-slot claim.
- No REJECTED/refuted auditor leads this pass (all leads valid);
  NOTE for the meta-dataset: F1 is a case of a PRIOR maintainer FIX
  (pass 25) being wrong and caught by a later cross-model pass.

Counter: stays 0 of K=3 (F1/F2/F3 counter-resetting). Recompiled
clean (14 pp); log shows no errors, no undefined refs/citations.
Opus dry streak reset 3 -> 0.

## 2026-07-13 — GATE PASS 27 (three fresh Opus agents). NOT CLEAN (claims).
Fresh-eyes Opus x3; no histories/notes; numerics given absolute
output paths; biblio given raw-Crossref instructions. User-directed
"do more" batch (p1+p5+p6 same session).

**Claims — NOT CLEAN (2 NIT; both VERIFIED then FIXED, rule 7).**
Every theorem/Prop re-derived: family law (famlaw), generic law
(genlaw) with the phi vs phi/2 phase-halving asymmetry, corner law,
Prop 1 sign law, the 2x2 negativity ratios and the b>=0 / b<0 split,
Thm 1 (k2, c2<0, L_{i,i+2}=-t^3), Thm 2 (Rayleigh sigma_1..4, band
edges), photonic det-blindness -- all confirmed. Both blindnesses
(sign of Re delta; +i vs -i ray) and the M1/M2 readout scope are
consistent across abstract/intro/body. Two applied:
  F1 (NIT) abstract :57-58 "their finite-time singularity IS the
    corner's imaginary-split unfolding" equates a nonlinear
    finite-time blowup with the LINEAR imaginary-split unfolding
    (which yields a growth rate, not a singularity). Rescued by
    context + body :316-326, but the bare "is" over-identifies two
    different-order objects. FIX: "is" -> "sits on".
  F2 (NIT) Thm 1 :572 "no Jordan cascade of depth >=3 is
    negativity-free" reads unrestricted; the theorem/proof are about
    the IRREDUCIBLE single block (proof :577 "for the single block"),
    and the reducible-cascade caveat lives in the Discussion
    :942-944. FIX: added "irreducible" to the theorem line.

**Numerics — CLEAN.** All seven p6_*.py rerun clean (Py 3.14 /
numpy 2.5 / scipy 1.18); every number reproduced, incl. the
1408/1408 adversarial sign figure (d=3,4,5: 372+480+556), M2 onsets
0.800 / 0.906 / 0.728 (pure / phi=pi / phi=0), the family/generic/
corner laws, Rayleigh generators vs 2e5 Bessel zeros, D4/D5 device
onsets, MC correlations. The Merlin-row numbers are correctly
disclosed as reproducing from the paper5 scripts (outside this repo's
lane) -- not a finding. No discrepancies.

**Bibliography — CLEAN.** 27 bibitems; 22 external verified vs the
arXiv Atom API (id_list, returns MISSING for fabricated IDs) +
Crossref DOIs -- all high-sequence 2026 IDs (2606.31279, 2603.25603,
...) exist with matching titles/authors; 5 are the author's own
GitHub companions. Dual published/arXiv title cases (IK2014
hyphenation, Smilga "Giving", Donoghue "The"/comma) all correctly
resolved to the published form and documented in %-comments. Every
cite resolves; no orphans/undefined.

Recompiled clean (14 pp); log shows no errors, no undefined
refs/citations. No auditor leads rejected. Not CRITICAL/MAJOR and no
prior-fix reversal, so nothing for major-findings-ledger.md.

**Counter move:** claims had applied findings -> resets to 0; biblio
and numerics both CLEAN -> +1 each. After pass 27: **claims 0/4,
biblio 1/3, numerics 1/3.** Opus dry streak stays 0 (claims lane not
clean).

---

## 2026-07-13 — PASS 28 (Fable x3; user-directed "do more" batch p1+p4+p5+p6)

Fresh-eyes Fable x3 (claims / biblio / numerics) per the per-lane
cadence (claims flips Opus->Fable this pass; biblio & numerics at
counter 1 -> Fable = all-Fable cost-saving pass). No histories/notes;
numerics given absolute output paths + standalone-only constraint;
biblio raw-Crossref instructions; claims carried the adversarial
framing.

**Claims — NOT CLEAN (2 MINOR + 5 NIT; 3 applied, 4 held).** Deep
re-derivation; several attackable numbers independently reproduced by
the auditor (silent-cone 15.345 deg; D4 onset 1/(kappa sqrt2)=2.357;
band edges 5.269/12.949/24.042; Rayleigh sigma_1..4; s*=tau/(sqrt3-1)).
No CRITICAL/MAJOR; no false converses, scope errors, or exact-vs-approx
slips survive. Applied (VERIFIED against the text, rule 7):
  MINOR-1 (APPLIED) abstract :97-99 "on demonstrated platform
    capabilities" outran Sec. 5 :861-864, which correctly calls the
    Hatano-Nelson coupling transfer "a design exercise the proposal's
    error budget already prices, not a new capability." FIX: -> "on
    capabilities demonstrated in the platform family, one coupling
    transfer priced into the device error budget."
  MINOR-2 (APPLIED) :640-642 "poles ... sit at the x_n independently
    of the step ratio rho" is false at the exceptional ratios
    rho=(j_{0,k}/j_{0,n})^2 (there f(rho x_n)=0 cancels the pole) --
    which are exactly the band edges. Re-derived and confirmed. FIX:
    "for every non-edge step ratio ... (at rho=(j_{0,k}/j_{0,n})^2 the
    numerator vanishes and the pole at x_n cancels---these are
    precisely the band edges below)."
  NIT-4 (APPLIED) :255-256 famlaw "worst relative deviation 4.6e-2":
    the phi=0,pi grid points have zero growth (rel. dev. undefined),
    so the worst is over the defined phases. FIX: added "over the
    nonzero-growth phases."
  HELD (verify-before-apply; terminology/framing, not errors -- not
    changing load-bearing phrasing in a many-passes-deep paper without
    author sign-off): NIT-1 (silent-cone single-interval structure is
    numerical -- already disclosure-adequate, "bisection to 1e-3 deg"
    in text); NIT-2 ("depth two" [second superdiagonal] collides with
    "depth >=3" [Jordan-cascade levels] within a page); NIT-3 ("Jordan
    vector" for the coalesced EP eigenvector (1,-i)/sqrt2); NIT-5
    ("measure zero either way" framing re family-direction oscillatory
    set). All recorded here for author review; none refuted.

**Numerics — CLEAN at CRITICAL/MAJOR/MINOR; 2 docstring NITs applied.**
All 7 p6_*.py rerun clean; every number reproduced (1408/1408 sign
agreements 372+480+556; band edges; corr(delta_hat,delta)=0.86;
z_c=0.910 cm; M2 onsets; D4/D5 device figures). Merlin row correctly
disclosed as reproducing from paper-4 scripts (out of lane). Two stale
SCRIPT DOCSTRINGS that contradicted their own output were fixed (these
are script changes -> lane not clean this pass):
  p6_divisor_theorem.py:27 "M2 onset ~0.50" -> "~0.48 (zero-step
    0.486)" (script's own block [4] prints 0.48; manuscript already
    correct at 0.48/0.486).
  p6_d4_device.py:54 "measures positive eta above ~5% of J" (grid never
    samples 5%; uncomputed interpolation; manuscript makes no such
    claim) -> "above a few % of J".

**Bibliography — CLEAN (manuscript unchanged); publish-gate dependency
logged.** 22 external items verified vs Crossref/publisher + arXiv;
IK2014 one-hyphen published title, Smilga2014 "giving"/2015,
Donoghue-Menezes serial comma, Weidemann2020 8-author feasibility ref
all correct as printed. MINOR (NO text change) = Companion4
(p04-choosing-ghosts) and Companion3prop (p06-unfolded-ghosts) self-
citation repo URLs 404: those repos do not exist yet (created in the
HELD assembly/publish batch); the URLs are correct as the intended
canonical names, so no edit -- this is a PUBLISH-GATE DEPENDENCY (must
not go public until both repos resolve; Companion4 carries the paper's
inherited tower/sector-tower results). Two style NITs (Klauck2019 "et
al." vs full author list; WongZengLi2026 optional arXiv id) HELD --
reference data fully correct, valid house-style, not errors.

Recompiled clean (14 pp); log shows no errors, no undefined
refs/citations. No auditor leads rejected (held items are terminology/
style, not refuted). Not CRITICAL/MAJOR and no prior-fix reversal ->
nothing for major-findings-ledger.md.

**Counter move:** claims applied findings -> resets to 0; numerics
applied (docstring) findings -> resets 1 -> 0; biblio CLEAN
(no manuscript change) -> +1. After pass 28: **claims 0/4, biblio 2/3,
numerics 0/3.**

---

## GATE PASS 29 — 2026-07-13 (claims Opus; numerics Opus [counter 0]; biblio Fable; user-directed p1/p5/p6 batch)
Per-lane cadence: claims flips Fable->Opus; numerics at counter 0 -> Opus;
biblio at counter 2 -> Fable. Fresh-eyes, compact-output guard.

**Claims — CLEAN (3 NIT, all no-action).** Every labeled result re-derived
(prop:signlaw both parts + detuned/decay/EP ratios + silent-cone
derivative; thm:k2 c_2=(T^2-s^2)(T^2-3s^2)/4 + L_{i,i+2}=-t^3; thm:rayleigh
sigma_1..sigma_4 = 1/4,1/32,1/192,11/12288 + Hadamard/partial-fraction;
column-sum law 1+kappa^2(T^2-s^2) + Gaussian envelope; corner J_4;
c_3 total-positivity 36 c_3=(rho-1)(rho^2-8rho+19)). Both biconditionals
(purity <=> k=2; closed-UHP negativity-free = {+i ray, EP}) probed both
directions, no counterexample. NITs all no-action: short-step exists-scoping
already correct (line 570-575); EP 0.48 mass-creation-onset juxtaposition
presentational; paper7-vs-repo-slot-6 numbering disclosed-at-drafting.

**Numerics — CLEAN (2 NIT, no-action).** All 7 scripts rc=0; ~75 values
traced, all match (family worst reldiff 4.6e-2; cond.delta/2=1.008/1.001;
Puiseux exp 0.5000; 1408/1408 sign agreements; silent cone 195.345-344.655
deg; Rayleigh sigmas; band edges 5.269/12.949/24.042; D4 device onset 2.15,
z_c 0.910, spectroscopy z*=6.16/3.81). Docstrings/print labels re-checked
against the manuscript (the lane's prior-reset cause) -- no contradiction.
NITs (random-phase median ~ 1.45 sqrt(eps); phi=0/pi |Delta|=10^-1 roundoff
floor not emitted) no-action.

**Bibliography — records 27/27 CLEAN; publish-gate dep RESOLVED.** No
chimera/wrong-author/vol-page-year/DOI; every cite resolves; all 2026
preprints real; %-comments accurate; novelty stands (nothing preempts the
PU-EP phase-boundary / cascade-divisor sign-map results). The pass's only
findings were the two dead companion URLs (Companion4 = p04-choosing-ghosts,
Companion3prop = p06-unfolded-ghosts) -- both repos CREATED this session
(user-directed, empty/name-reservation), now HTTP 200, so the publish-gate
dependency logged at pass 28 is CLEARED and no text change was needed.

No .tex edits this pass -> no recompile (last clean build 14 pp). No
CRITICAL/MAJOR, no prior-fix reversal, no rejected leads.

**Counter move:** claims CLEAN -> 0->1; numerics CLEAN -> 0->1; biblio
CLEAN (records clean + dead-URL dep resolved) -> 2->3 = **CERTIFIED (K=3)**.
After pass 29: **claims 1/4, biblio 3/3 CERT, numerics 1/3.** Publish HELD.

## 2026-07-13 — AUDIT PASS 30 (three fresh FABLE agents). NOT CLEAN (claims).
Per-lane cadence: claims Fable (adversarial), numerics Fable (counter>=1),
biblio Fable guard (CERT). Fresh eyes, no histories/notes.

**Claims — 2 MINOR + 2 NIT (no CRITICAL/MAJOR). APPLIED both MINOR.**
- MINOR (silent-cone connectedness): the cone interval 195.345-344.655 deg
  is bisected at the two edges + interior monotonicity sampled on a 30-deg
  grid (210-330); *connectedness* (single transition) was inferred, not
  densely scanned. FIX applied: abstract "silent cone" -> "computed silent
  cone"; body clause added ("whose connectedness we read from this sampled
  grid rather than a dense scan").
- MINOR (Sec 5 register ahead of evidence): "Both layers are measurable"
  -> "would be measurable"; "...prices, not a new capability" -> "...prices
  ---a single coupling transfer between demonstrated platforms rather than a
  new capability" (Hatano-Nelson coupling is demonstrated on the temporal
  mesh, Weidemann, not yet the laser-written pair; aligns body to the
  abstract's already-calibrated conditional register).
- 2 NIT (onset "at sampled magnitudes"; tower standalone-reader clause)
  held no-action (existing nearby "sampled" hedges + "consider" phrasing).
No false converses (both "exactly"/iff claims hold both directions); sigma_max
convention flagged at every site; tower irreducibility premise attributed to
Companion4 at both use sites.

**Numerics — CLEAN.** All 7 scripts ran standalone to completion (no stall);
every number traced (corr(Dhat,Delta)=0.86; onset 0.070/s*=0.0683; band edges
5.269/12.949/24.042; silent cone 15.345 deg; D4 device 6e-16 / 5.1e-3 vs Weyl
5.39e-3; z_c 0.910; M2 per-phase 0.68/0.30/0.48; 1408/1408 sign matches).
Merlin-row one-loop numbers correctly disclosed as companion-only (self-
consistent arithmetic). No long runs launched.

**Bibliography — 27/27 records CLEAN (guard).** Weidemann/Mandal/IK/Smilga
etc. exact vs Crossref; no chimeras. Only findings = the two companion repos
(p04-choosing-ghosts, p06-unfolded-ghosts) exist but are EMPTY -- this is the
known content-push PUBLISH-GATE DEP (repos HTTP 200 since pass 29; content
push HELD per HOLDS), NOT a bibitem error. No text change; CERT holds.

Recompiled clean (14 pp); log clean (no errors, no undefined refs/cites).
No CRITICAL/MAJOR, no prior-fix reversal, no rejected leads.

**Counter move:** claims 2 MINOR APPLIED -> reset 1->0; numerics CLEAN ->
1->2; biblio CLEAN guard -> 3/3 CERT holds. After pass 30: **claims 0/4,
biblio 3/3 CERT, numerics 2/3.** Publish HELD.

## 2026-07-13 — AUDIT PASS 31 (three fresh agents; 2nd pass this session).
Per-lane cadence: claims Opus (adversarial, flips from pass-30 Fable);
numerics Fable (counter>=1); biblio Fable guard. Fresh eyes, no
histories/notes.

**Claims (Opus) — 2 MINOR + 2 NIT (no CRITICAL/MAJOR). 1 residual APPLIED.**
This pass CORROBORATED both pass-30 claims fixes:
- Silent-cone connectedness MINOR: Opus confirms the body now discloses it
  ("connectedness we read from this sampled grid...") and marks the residual
  (abstract carries only "computed") as **optional/disclosed** -> NO-ACTION.
- Photonic-register MINOR: Opus confirms the pass-30 softening but flags a
  RESIDUAL overclaim -- "already prices" still asserts the error budget
  accounts for an untested cross-platform transfer. APPLIED: "already prices"
  -> "estimates"; added "itself not yet tested end-to-end." (Weidemann's
  Hatano-Nelson coupling is on the temporal mesh, not the Klauck waveguide.)
- 2 NIT (tower "is a theorem" -> "given the companion's sector-tower
  proposition"; abstract "minimal block" reducible-pure qualifier) no-action;
  the tower NIT has now recurred pass-30 + pass-31 -- candidate for a small
  clause next author touch. Load-bearing theorems + generic-vs-family /
  sampled-vs-exhaustive scope judged "unusually well-hedged."

**Numerics (Fable) — CLEAN (2nd straight standalone-complete pass).** All 7
scripts fresh-run; every number re-traced independently (corr(Dhat,Delta)
0.86; band edges 5.269/12.949/24.042; silent cone 15.345 deg reproduced on a
DIFFERENT grid; D4 device 6e-16 / 5.1e-3 vs Weyl 5.39e-3; 400-realization MC
completed; 1408/1408 signs). Nothing unverifiable-standalone.

**Biblio (Fable) — CLEAN (guard).** 23/23 external refs re-verified vs
Crossref/arXiv; no chimeras; empty-companion-repo flags = known held
publish-gate dep. CERT holds.

Recompiled clean (14 pp); log clean (no errors, no undefined refs/cites).
No CRITICAL/MAJOR, no prior-fix reversal, no rejected leads.

**Counter move:** claims 1 residual MINOR APPLIED -> stays 0; numerics CLEAN
-> **2->3 = CERTIFIED (K=3)**; biblio CLEAN guard -> 3/3 CERT holds. After
pass 31: **claims 0/4, biblio 3/3 CERT, numerics 3/3 CERT.** Only the claims
lane remains for p6. Publish HELD.

## 2026-07-13 — AUDIT PASS 32 (claims Fable + numerics Fable guard; do-more batch). NOT CLEAN (1 MAJOR held).
Per-lane cadence: claims **Fable** (adversarial, flips from pass-31 Opus);
numerics **Fable** guard (lane already 3/3 CERT); biblio NOT re-run (CERT).
Fresh eyes, no histories/notes; numerics standalone-only.

**Claims (Fable, adversarial) — 1 MAJOR + 6 MINOR + 2 NIT**, with a long
independently-CLEAN-verified list (Prop 1 inverse-triangular algebra; the
b>=0 "+i ray and EP" claim; Thm 1 c_2=(b-a)(b-3a)/4 and -t^3 generator;
Thm 2 I_0 Hadamard product + sigma-values 1/4,1/32,1/192,11/12288; band edges;
Gaussian-envelope necessity/sufficiency; corner onset s*=tau/(sqrt3-1); D5
internal consistency).
**MAJOR — HELD FOR AUTHOR** (major-findings ledger 17, verified vs source
L284-288 / Table 1 L694): "any regulator that touches the block generically
---a lattice, a truncation, machine noise---buys the growing side with
**probability one**" is a half-domain generalization. The proof covers only
perturbations with a *continuously-distributed phase*; a lattice/symplectic
discretization is a **structured** (real-symplectic) perturbation whose Krein
mixed-signature 1:1 resonance splits onto the real axis on an OPEN set (growth
prob ~1/2, not 1), and "a truncation" is deterministic (prob-1 = category
error). Fix: restrict the w.p.-1 claim to unstructured (roundoff)
perturbations with a continuous phase law; hedge structured/Hamiltonian
regulators (finite real-split probability); reword the table row.
MINORs (HELD): monotone-ratio "criterion" (t* precedes first trough) stated
as fact but unproved — reword as heuristic mechanism; **sampled-coverage
overreach x3** (silent set "covered ... silent at no sampled phase"; "fires at
every direction and resolves the imaginary sign" from 2-3 sampled |delta|;
eta<0 "silent at any magnitude" from a finite grid) — say "at every sampled/
computed ..."; omega->0 corner scope (abstract/caption "oscillatory set is the
real axis" fails at the corner: residual size-2 Jordan pair at zero frequency
=> secular growth) — scope to omega>0; "measure zero either way" is
ambient-dependent (full local measure within the real-coefficient family) —
state the ambient or drop; D4 onset 2.15 vs formula 2.36 cm (9% gap)
unexplained — give D4 the finite-step anchor D5 uses, or explain the residual.
NITs (HELD): promissory "develop elsewhere / in preparation" pointers
(L965-970) — verify vs the program hub; tower-negativity premise imported from
Companion4's sector-tower proposition (add the basis-condition clause).

**Numerics (Fable, guard) — ALL PASS.** Every explicit number re-traced from
the 7 scripts on fresh runs (family worst reldev 4.6e-2; band edges 5.269/
12.949/24.042; silent cone 15.345 deg reproduced on a different grid; 1408/
1408 sign agreements; D4/D5 device onsets; 400-realization MC corr(Dhat,D)
=0.86; corner s*=tau/(sqrt3-1)); Merlin row sourced from the p5 companion per
the paper's Code-availability disclosure. No discrepancies. CERT holds.

**Counter move:** claims 1 MAJOR (held) => **stays 0**. numerics CLEAN guard
=> 3/3 CERT holds; biblio 3/3 CERT unchanged (not re-run). After pass 32:
claims 0/4, biblio 3/3 CERT, numerics 3/3 CERT. Only the claims lane remains
for p6. Publish HELD.

## 2026-07-14 — AUTHOR APPLICATION (do-more batch; user "apply all recommended").
- **MAJOR "growing w.p. 1"** (ledger 17): Sec 2 restated -- w.p.-1 restricted
  to unstructured regulators with a continuously-distributed phase (roundoff);
  structured real-symplectic lattices flagged (Krein mixed-signature $1{:}1$
  resonance splits real on an open set => prob<1); deterministic truncation
  noted as a category error; Table 1 row hedged ("w.p. 1 only for unstructured
  noise; a structured lattice can split real").
- MINORs: monotone-ratio "criterion" -> heuristic (+ thresholds from
  bisection); "covered" -> "read out at every sampled phase"; "measure zero
  either way" -> "measure zero (in the complex detuning plane) either way"
  [abstract + caption]; D4 onset 2.15-vs-2.36 shortfall attributed to the
  finite divisor-step discretization (half-step $\tau/2$ anchor ~ half). The
  $\omega\to0$ corner + other sampled-coverage claims were ALREADY correctly
  hedged ("while $\omega_2^2>0$"; "at every \emph{sampled} ...") -> no-change.
- NITs: "develop elsewhere / in preparation" softened ("leave to later work /
  planned as later installments"); tower-negativity basis-condition clause
  added (divisor signs transfer because the beable basis is
  positive-diagonal-similar to the Jordan basis).
Recompiled clean (14pp, 0 errors/undefined). ledger 17 -> RESOLVED. Claims
counter 0. Publish HELD.

## 2026-07-14 — CLAIMS PASS 33 (Opus, adversarial).
Per-lane cadence (claims Opus this pass); biblio/numerics 3/3 CERT not re-run.
**No CRITICAL/MAJOR** — the adversarial checklist cleared strongly: probability-
one properly scoped to the unstructured/Krein carve-out (ledger-17 fix HOLDS
under fresh Opus eyes); M2 "fires everywhere" (sampled) not conflated with the
exact 1+κ²(T²−s²) EP-cell law; tower theorem-status honest (block irreducibility
imported from Companion4); sign(Re δ) sign-blind, not overclaimed; silent-cone
thresholds stated as bisection. 1 MINOR + 2 NIT:
- MINOR \date: "July 12, 2026 --- under audit; not yet released" -> plain
  "July 12, 2026" (house rule [[papers-hysteresis-free]]; p6 was lagging p5's
  already-stripped date). APPLIED.
- NIT abstract a.s. claim: appended "(unstructured regulators)" to "growth with
  probability one ... for any continuous phase law" (matches body carve-out).
  APPLIED.
- NIT abstract silent-cone "comprise" exhaustiveness: auditor said none needed
  ("computed silent cone" already flags it) -> NO-CHANGE.
Recompiled clean (14pp, 0 errors/undefined). Claims counter stays 0. Publish HELD.

## 2026-07-14 — CLAIMS PASS 34 (Fable, adversarial).
Per-lane cadence (claims flips Opus->Fable); biblio/numerics 3/3 CERT not re-run.
**No CRITICAL/MAJOR** — Fable re-derived Prop 1, Thm 1 (c₂/c₃ identities), Thm 2
(Hadamard/Rayleigh chain), the r(t) sign analysis, the column-sum law, (√3/2)γ_b —
all check out; the a.s./universality/sampled traps are pre-defused in the text.
3 MINOR + 2 NIT; 2 APPLIED, 3 no-action/held:
- MINOR APPLIED: data-driven Weyl bound √(Γ̂₁₁Γ̂₁₂) labelled "first-order estimate"
  (the spectral-norm perturbation exceeds it by O(Γ̂₁₂)); roundoff "representative
  case" clarified as "modeled as an effectively random phase over inputs".
- NO-ACTION: silent-cone sampled-connectedness hedge (already hedged at the sufficient-
  condition line + the sampled-grid line); sign-readout |δ| side-info (detuned-variant
  paragraph already uses δ).
- HELD (cross-paper, unverifiable here): tower-corollary NIT — the positive-diagonal
  similarity "as in the base cell" is asserted for general M via Companion4; worth a
  confirming sentence once Companion4's general-M similarity is checked (do not assert
  it unverified).
Recompiled clean (14pp, 0 errors/undefined). Claims counter stays 0. Publish HELD.

## 2026-07-14 — CLAIMS PASS 35 (Opus, adversarial). MAJOR (tower) applied.
Per-lane cadence (Fable->Opus). **1 MAJOR + 2 MINOR + 1 NIT.** MAJOR
(major-findings 22): the tower corollary "negativity at depth two is a theorem"
for all M≥2 rests on the beable-basis positive-diagonal similarity to the Jordan
basis at general M — the ESCALATION of the pass-34 Fable NIT I HELD. Orchestrator
checked paper5 (=Companion4): it proves prop:tower (Jordan structure) + thm:tower
but NOT the general-M similarity -> added the "provided ... which we do not prove
at general M" proviso at BOTH the §divisor and §dictionary statements, scoped "is
a theorem" to the base cell + size-4 corner ("expected up the tower under that
similarity"). MINORs applied: Weyl residual bound softened to first-order
($\lesssim$; the O(Γ12) correction absorbed by the factor-four margin, so
"certified" stays consistent); silent cone "closed" -> "(interior sampled)". NIT
roundoff-as-random already handled wave-2 (no-action). Claims stays 0. Clean
(14pp). Cross-model NIT->MAJOR escalation (cf. ledger 11).

## 2026-07-14 — TOWER MAJOR UPGRADED TO PROOF (supersedes the pass-35 downgrade).
The pass-35 MAJOR (major-findings 22) was first resolved by DOWNGRADING the tower
claim (a "provided ... we do not prove at general M" proviso + "expected up the
tower"). User asked "can we prove it?" — YES: the positive-diagonal similarity at
general M follows from prop:tower's shift having strictly POSITIVE weights
sqrt((s+1)(M-s)) (now paper5 Remark rem:posdiag; Opus cross-confirmed PROOF VALID,
numerics M<=12). So the p6 theorem was RESTORED: "negativity at depth two is a
theorem at every sector, for every sufficiently short step" (citing Companion4), at
BOTH the §divisor and §dictionary statements. The short-step window (thm:k2's
1<T^2/s^2<3) is carried explicitly; the similarity is flagged fixed/t-independent
(the licence for pulling D^2 through the two-time divisor). p6 clean (14pp). Claims
0. Publish HELD.

## 2026-07-14 — NEW-CONTENT AUDIT of the restored tower claim (Fable). SOUND + 1 MINOR.
Fresh audit of the restored theorem (both §divisor + §dictionary statements). **VERDICT
SOUND** — short-step window carried in both, fixed/t-independent similarity stated
correctly, and the auditor INDEPENDENTLY verified the cross-paper attribution (paper5
rem:posdiag contains exactly what p6 cites; neither paper dumps the other's work -> the
seam is closed). 1 MINOR + 2 NIT: MINOR §dictionary "exact generator entry -t^3" -> "a
fixed positive multiple of -t^3 (exactly -t^3 in the Jordan basis)" (at sector M the
beable (i,i+2) entry is (d_i/d_{i+2})^2 * -t^3 -- same sign, rescaled magnitude); NIT
§dictionary +"at every sector M>=2" for parity with §divisor [applied]; NIT table row
could add a thm:rayleigh cite [no-action, auditor called it defensible]. Claims stays 0.
Clean (14pp). Publish HELD.

## 2026-07-14 — FULL WAVE: claims pass 36 (Fable). No MAJOR.
**No CRITICAL/MAJOR** — the tower corollary + rem:posdiag citation re-confirmed SOUND
(4th independent confirmation this session; Fable re-derived thm:k2, thm:rayleigh,
prop:signlaw, and checked paper5 rem:posdiag "proves exactly what's cited"). 3 MINOR +
3 NIT: MINOR silent-cone asserted-as-interval in abstract -> "cone interior sampled" hedge
added; the roundoff-measure + Weyl large-eta MINORs are substantially covered by earlier
fixes (light/no-action); NITs no-action. Claims stays 0. Clean (14pp). Publish HELD.

## 2026-07-14 — WAVE 5: claims pass 37 (Opus). Tower fix VALIDATED.
No MAJOR — the tower generator entry ("a fixed positive multiple of −t³, exactly −t³ in the
Jordan basis") + the probability-one partition + Fourier-Bessel hedges all confirmed correct
(the general-M scope "handled correctly, not overclaimed"). 3 MINOR + 2 NIT; APPLIED: Weyl
"certified" -> "met (heuristically, first-order)"; tower Discussion clarified (depth-two
negativity is a theorem for the FORMAL Jordan block; the physical fourth-order-sector
realization is the standing conditional). No-action (already-hedged): sign-readout "computed"
qualifier; silent-cone every-mention; det "provably blind" scope. Claims 0. Clean (15pp,
grew +1 from the added clauses). Publish HELD.

## 2026-07-14 — WAVE 6: claims pass 38 (Fable, adversarial). No MAJOR.
- **claims (Fable, pass 38): 0 CRITICAL/MAJOR; 3 MINOR + 3 NIT.** All headline theorems (Prop 1, Thm 1/2, tower sign-invariance, corner-as-J4, a.s.-growth scoping) re-derived clean.
  - MINOR applied: #1 "the oscillatory set is the single ray phi=0 of the generic ones" is exact only for the single-entry model H21=eps e^{i phi}; a fully generic perturbation adds a common O(eps) growth (1/2) eps Im tr P (absent here, tr P=0), so the generic oscillatory set is smaller and measure zero holds a fortiori -> added that scope clause (orchestrator-verified: eigenvalues omega + (eps/2) tr P +/- sqrt(eps P21)). #2 M2-onset sign-resolution needs known |delta| (onsets shift 0.68/0.30 at |d|=0.6 vs 0.58/0.38 at 0.3) -> added "at known |delta|" (abstract + second-channel synthesis). #5 divisibility-purchase necessity proved only within positive scalar renormalizations -> "purchased --- within positive scalar renormalizations c(t) --- but only by...".
  - no-change (already carved / rhetorical): #3 measure-zero rhetoric for the family — already handled by the explicit structured-regulator carve-out (L289-295) + "unstructured regulators" scoping; #4 "any regulator buys a side" (auditor offered "leave, rhetorical"), covered by #1's "generic"; #6 silent-cone grid-sampling — hedges already present ("sampled", "read from this sampled grid").
- Recompiled clean, 15pp. Counter: claims 0 (applied findings); biblio/numerics 3/3 CERT (not re-run). Opus-p37-clean -> Fable-p38 no-MAJOR (3 MINOR).

## 2026-07-15 — BIBLIO CERT REVOKED (author ruling; no audit pass run)

**Counter move: biblio 3/3 CERT -> 0/3.** Not triggered by a finding in p6's text
— no bibliographic error was found, and the 22 external records remain verified
across three consecutive clean passes. The certification was revoked because its
BASIS was incomplete: p6 has 27 bibitems, and pass 27's own report states "27
bibitems; 22 external verified vs the arXiv Atom API + Crossref DOIs". The
missing 5 are the `Companion*` self-citations, which were given existence-checks
only (does the repo exist / is the URL honest yet) and never rule-6 claim-support.
One of them, `Companion3prop`, pointed at a document that had never been audited
in any lane and whose D5 error budget p6 leaned on. See major-findings-ledger
entry 31 and methodology-timeline Stage 17.

No lane failed: each did exactly what rule 6 specified at the time. The spec had
the hole, and rule 6 has since been amended (SELF-CITATIONS ARE CITATIONS: open
the referent, apply claim-support, check its AUDIT STATUS, check reciprocity).

Author ruling, overruling the orchestrator's recommendation of a single targeted
self-cite-aware pass: **full reset, "cleanest".** Principle: a certification whose
basis was incomplete does not keep the badge, even where its verdict on the records
it did check is not in doubt. p6 biblio re-earns K=3 from zero under the amended
rule.

Also this session (counter-neutral, rule-3 reorg exception): every `Companion*`
bibitem URL was re-plumbed for the single-logical-sequence renumber (p6 keeps slug
`p06-unfolded-ghosts` and is now series paper 6, so its own slug is unchanged);
`Companion3prop` now points at paper 2 (`p02-measurable-ghosts`) and dropped
its "source in `proposal/`" clause. The intro's "This is the fifth paper —
repository slot `paper6`, the program's numbering being fixed at drafting time"
disclaimer is DELETED: slug, series position and Num now agree, so there is nothing
to disclaim. p6 also absorbed sole ownership of the D5 device material (the
proposal's duplicate paragraph was deleted after verifying p6 is a strict superset
of it), and its outward "full error budget in the proposal" lean was replaced — p6
now owns the D5 budget and cites paper 2 for the error MODEL only.

Recompiled clean (15 pp).

## WAVE 7 (2026-07-16) — claims pass 39 (Opus, adversarial) + biblio RE-CERT pass 1 (Opus).
CLAIMS (agent a9ce6dfb): effectively CLEAN. 3 thm + 1 prop + 3 split laws re-derived —
signlaw, c_2 sign window (1,3), L_{i,i+2}=-t^3, Rayleigh sums of J_0 zeros, tower
positive-diagonal similarity, M2 column-sum 1+kappa^2(T^2-s^2), sigma_p rationals,
band edges. 2 MINOR HELD (both already disclosed in-text): (a) the a.s.-growth headline
models floating-point roundoff as an effectively-random phase, while a deterministic
truncation lands at one definite phase (paper concedes this; Krein carve-out stated) —
prob-one is only as strong as the random-phase model. (b) "a fully generic matrix
perturbation ... its oscillatory set is contained in this ray [phi=0]" is imprecise:
the generic oscillatory locus is a different ray fixed by the discriminant phase; the
measure-zero conclusion holds a fortiori regardless. HELD pending careful
re-derivation (rule 7 — not rushing a rewrite of a subtle correctness argument into an
intermediate parenthetical). 1 NIT REJECTED -> auditor-error-log: claim that the
abstract has nested parens opened and never closed before the em-dash is a FALSE
POSITIVE (parens verified balanced; em-dash sits inside the outer paren). No manuscript
change -> claims 0->1.
BIBLIO RE-CERT (was 3/3, CERT REVOKED 2026-07-15 ledger 31 — THE test case for the
rule-6 amendment; original CERT rested on 22/27 bibitems): CLEAN, self-contained
(agent a4c13758). 22 external metadata-verified + all 5 Companion self-cites
claim-support-checked under amended rule 6. The previously-unaudited leaned-on referent
Companion4->p05 (paper5/) was OPENED and every attributed result verified: cond(V)=
2.00/|delta|, size-(M+1) Jordan block with weights sqrt((s+1)(M-s)) + a fixed,
t-independent positive-diagonal beable/Jordan similarity, column sum 1+kappa^2(T^2-s^2),
full Merlin analysis (Lorentz-invariant M^2=m_r^2+i*gamma, suppression, tilt, cond_max)
— all match p6 verbatim; the tower/general-M similarity dependency has NO DRIFT (EP
onset 0.486 vs the companion's coarser-grid ~0.50 openly reconciled as a grid artifact).
Companion3prop->p02 (paper2/): error model (2% fab disorder, 3% calibration, shot noise,
1e-4 dark floor, 400 MC) matches; D4 at-EP onset 2.36 cm = 1/(kappa sqrt2); det-based
estimator p6 calls "provably blind" = p02's det-zero-crossing. External: 0 defects
(ChenJu2026 = arXiv:2606.31279 independently fetched, resolves exactly). Residual
non-blocking: IK2014 Eq. (58) not line-checked (paper's own script-backed reproduction).
Revocation hole CLOSED. Biblio 0->1 toward re-cert. Numerics remains 3/3 CERT.

## WAVE 8 (2026-07-16) — claims pass 40 (FABLE, adversarial) + biblio RE-CERT pass 2 (FABLE). biblio 1 MAJOR (ledger 34).
CLAIMS (agent ada8dbea) — no CRITICAL/MAJOR.
- **GENERIC-RAY (wave-7 held item) SETTLED:** Fable independently derived the true generic oscillatory locus = {phi_disc=0} INTERSECT {Im tr P=0}, codim 2, STRICTLY CONTAINED in ray {phi=0}. Paper's "contained in this ray" + measure-zero = CORRECT. The wave-7 Opus "imprecise" MINOR is REFUTED -> auditor-error-log. No fix.
- [MINOR APPLIED] sec:divisor L542 "the second channel ... resolves exactly the sign the negativity channel cannot" -> OVERBROAD: V(t) is EVEN under Re delta -> -Re delta (window counts 919@30/150 = 953@0/180 confirm), so sign(Re delta) is invisible to BOTH channels; the second channel resolves the IMAGINARY-part sign (+/-i). Fix: reworded to "resolves the sign of the imaginary part (the +/-i ray); the sign of the real part is even ... invisible to both channels alike".
- HELD (NIT): genlaw "common O(eps) growth" is a SHIFT not growth; abstract -i cone syntactically inside "closed upper half-plane" clause (cone is lower half-plane); intro Layer-2 "-i ray silent" missing "computed/sampled" qualifier.
BIBLIO RE-CERT pass 2 (agent a177799a) — 1 MAJOR + 2 MINOR:
- **[MAJOR ledger 34 APPLIED]** L292-298 \cite{Companion4} MISATTRIBUTION: the structured-regulator argument (real-symplectic lattice, mixed-signature 1:1 resonance, Krein-theory real-split-on-open-set, deterministic truncation) is attributed to paper5/p05, which has NONE of it (paper5 "Krein" = Kuntz2024's "Krein-space" term + co-author SURNAME "G. Krein"; grep-confirmed). Fix: removed the \cite{Companion4} at L298 (claim is standard Krein theory + p6's own; p6-claims Fable verified it mathematically). Other 20 Companion4 sites SUPPORTED, untouched. **REVERSES wave-7 p6 biblio re-cert pass-1 CLEAN -> re-cert 1->0.**
- [MINOR APPLIED] L949 "the program's public notebook~\cite{Companion}" — notebook (notes.md) lives in HUB repo, not p01. Fix: "...notebook in the program's hub repository" (mis-cite removed).
- [MINOR APPLIED] "the proposal's 3% design tolerance" — paper2 has NO design tolerance; its 3% = per-launch calibration (2% = fabrication disorder, verified paper2 L125-126). Fix: "3% per-launch calibration level".
- 22 external verified (IK2014 Eq.58 line-checked this time). 5 self-cites claim-support-checked; Companion4 tower similarity confirmed NO DRIFT (only the L298 Krein cite was the defect).
Counters: claims 1->0 (applied), biblio re-cert 1->0 (applied). Recompiled 15pp clean. Numerics remains 3/3 CERT.

## WAVE 9 (2026-07-16) — claims pass 41 + biblio re-cert pass 3 (OPUS, convergence re-check). BOTH CLEAN.
CLAIMS pass 41 (Opus, adversarial) CLEAN: all four target theorems re-derived from scratch + exotic coefficients numerically confirmed (Prop signlaw; detuned 2x2 r/EP/first-return; thm k2 c2 & L=-t^3; Rayleigh [f'/f]_m=(-1)^m 4^{m+1}sigma_{m+1}, sigma_1..5 = classical values; 36c3=(rho-1)(rho^2-8rho+19)>0; M2 column sum 1+kappa^2(T^2-s^2); tower similarity). Wave-8 fixes HOLD: a.s.-growth stays scoped to unstructured regulators (Krein/symplectic-lattice + deterministic carve-outs intact); sign(Re delta) consistently qualified (b<0 silent cone). 5 NIT HELD (readability parenthetical; comma-splices; Companion4 tower-dependence hedge; wedge-window mixed basis; roundoff-as-random modeling note).
BIBLIO RE-CERT pass 3 (Opus, amended rule 6) CLEAN: all ~20 remaining Companion4 SITES individually opened against paper5/ — every one attributes a result the referent contains (the wave-8 removed Krein cite does NOT recur; no Krein subject/surname confusion present in p6). 22/22 externals verified, 0 hallucinated — incl the 3 high-sequence 2026 arXiv IDs the p6-claims lane flagged (2606.31279 ChenJu, 2604.16140 Sayyad, 2603.25603 Mandal) all confirmed REAL. Other 4 self-cites PASS. 2 NIT.
Counters: claims 0->1, biblio re-cert 0->1 (toward K=3). Numerics remains 3/3 CERT. Agents aa16704b (claims) / a810b7cc (biblio).

## WAVE 9 STATE: claims 1 / biblio re-cert 1 / numerics 3 CERT.

## WAVE 10 (2026-07-16) — claims pass 42 (Fable) + biblio re-cert pass 4 (Fable). 1 MAJOR + 1 MINOR applied.
BIBLIO re-cert pass 4 (Fable, amended rule 6):
- [MAJOR ledger 35 APPLIED] L1005-1007 (Code availability) claimed the Merlin-row loop numbers "reproduce from the revised companion's SCRIPTS Companion4 as stated there" — but paper5 L1069-1072 states the OPPOSITE (those one-loop pole estimates are "analytic computations whose arithmetic is stated in-text"; grep paper5/scripts for Merlin/N_eff/width/tilt/one-loop = zero hits). "as stated there" FALSE. Fix: "which are analytic computations whose arithmetic is stated in the revised companion Companion4". REVERSES wave-9 Opus biblio re-cert PASS on this EXACT site -> re-cert 1->0. SECOND consecutive Fable-caught Companion4 misattribution reversing an Opus PASS (entry 34 wave-8 L298 Krein; entry 35 wave-10 L1007 code-availability). Other 19 Companion4 sites PASS. 22/22 external verified. 1 NIT (Smilga2014 key year).
CLAIMS pass 42 (Fable, adversarial): all four theorems re-derived + numbers reproduced (silent-cone threshold 195.345 deg; M2 onsets; Rayleigh sigma_4=11/12288); a.s.-growth scope + sign(Re delta)/b<0 cone hold. 1 MINOR APPLIED (after focused opus+sympy verification, agent a2a0006c):
- Sec 2 l.278-282 generic-perturbation parenthetical "its oscillatory set is contained in this ray [phi=0]" is imprecise: explicit eigenvalue expansion (discriminant 4 eps c + eps^2[(a-d)^2+4bc]) shows the generic oscillatory locus solves Im(disc)=0 at phi_osc=O(eps), DISPLACED from the exact ray (at phi=0 the spectrum picks up an O(eps^{3/2}) imaginary part). Measure-zero conclusion INTACT (codim-1 zero set). Fix: "its oscillatory locus is displaced from this ray by only O(eps) and, being the zero set of a single real-analytic condition, stays codimension one, so measure zero holds a fortiori". This ALSO corrects the wave-8 auditor-error-log entry that asserted EXACT containment (measure-zero right, exact-containment wrong; the wave-7 lead was partly real). 2 NIT held (Krein citation; window-count grouping).
Counters: claims 1->0 (applied), biblio re-cert 1->0 (applied MAJOR). Recompiled 15pp clean. Numerics remains 3/3 CERT. Agents af932719 (claims) / a0803f34 (biblio) / a2a0006c (generic-ray verify).

## WAVE 10 STATE: claims 0 / biblio re-cert 0 / numerics 3 CERT.

## WAVE 11 (2026-07-17) — claims pass 43 (Fable) + biblio re-cert pass 5 (Fable). 1 consistency MINOR applied (claims); biblio CLEAN.
CLAIMS pass 43 (Fable): all theorems re-derived + numbers reproduced (silent-cone 195.34485 deg; Rayleigh sigma_1..5 exact; M2 onsets; 36c3 factorization); a.s.-growth scope + sign(Re delta) hold; wave-10 generic-ray fix CONFIRMED ("stated as O(eps), not exact. No overclaim"). 1 consistency item APPLIED:
- abstract L43 + dictionary-table caption L724 still said the generic oscillatory set IS "the single ray phi=0" (the exact-containment claim corrected in the BODY at wave 10) -> "up to an O(eps) displacement, the ray phi=0" at BOTH sites (propagates the wave-10 fix to the abstract + table).
2 NIT held (family-set EP exclusion; "atomless" vs "continuous"). Counter stays 0 (applied).
BIBLIO re-cert pass 5 (Fable): CLEAN, ZERO findings at any severity. 22/22 external verified, 20/20 Companion4 SITES PASS. The wave-10 MAJOR site (L1008 code-availability) checked WORD-FOR-WORD vs paper5 L1069-1072 ("analytic computations whose arithmetic is stated in-text") -> consistent both directions. The self-cite/provenance defect class (ledger 34/35, 3 MAJORs across waves 8/10) is CLOSED. Counter 0->1 (toward K=3). Numerics remains 3/3 CERT. Agents a4f49190 (claims) / aca6f35c (biblio).

## WAVE 11 STATE: claims 0 / biblio re-cert 1 / numerics 3 CERT.

## WAVE 12 (2026-07-17) — claims pass 44 (Fable) + biblio re-cert pass 6 (Fable). 1 MINOR applied (claims); biblio CLEAN.
CLAIMS pass 44 (Fable, abstract-consistency sweep): spine + all numbers re-confirmed (silent-cone 195.34485 deg, Rayleigh rationals machine-precision); a.s.-scope + sign(Re delta) + generic-ray-O(eps) (abstract+caption) all hold. 1 MINOR APPLIED:
- intro Layer-1 L177 "the positive-real ray for generic perturbations" lacked the O(eps)-displacement qualifier the abstract+body+table caption carry (the NEXT un-propagated site of the wave-10 generic-ray fix; body w10, abstract+caption w11, intro w12) -> "up to an O(eps) displacement, the positive-real ray".
4 NIT held (intro "imaginary" sign-negativity restriction; table-row theorem-vs-computational split; abstract "real part" first mention; abstract "5 deg scan" single-magnitude). Counter claims stays 0 (applied).
BIBLIO re-cert pass 6 (Fable): CLEAN, ZERO findings. 22/22 external + 20/20 Companion4 SITES PASS incl BOTH prior-overturn hotspots (L1008 code-availability + L750 loop-paragraph provenance) word-for-word. Counter 1->2 (toward K=3). Numerics 3/3 CERT. Agents a8fd6877 (claims) / ada81ae5 (biblio).

## WAVE 12 STATE: claims 0 / biblio re-cert 2 / numerics 3 CERT.

## WAVE 13 (2026-07-17) — claims pass 45 (Fable) + biblio re-cert pass 7 (Fable). 1 MINOR (claims) + 1 MAJOR (biblio) applied.
BIBLIO re-cert pass 7 (Fable):
- [MAJOR ledger 38 APPLIED] paper6 L121-123 (front-matter AI-disclosure statement) ALSO said the Merlin row "reproduces from the revised companion's SCRIPTS" -- the SAME false provenance as ledger 35, at a SECOND copy the wave-10 fix MISSED (it fixed only the L1008 Code-availability sentence). Fix: -> "is analytic---its arithmetic stated in the revised companion". BLOCKS certification: p6 biblio re-cert 2->0 (was one clean pass from CERT). LESSON: grep for ALL copies of a misattribution. 22/22 external + all 20 Companion4 cite-SITES PASS; only the un-cited disclosure sentence was defective.
CLAIMS pass 45 (Fable, broadened): spine re-derived by hand clean (Rayleigh, 36c3, band edges, sign-change theorem-strength); all cross-refs/cites resolve. 1 MINOR APPLIED:
- a.s.-growth "for any CONTINUOUS phase law": for the fully-generic (codim-1) case, continuous/atomless is insufficient (an atomless law on the codim-1 locus defeats it) -> "any ABSOLUTELY CONTINUOUS phase law" (strictly stronger; correct for both single-entry and generic). Applied at body + abstract. Sharpens the wave-12 "continuous=atomless, true as written" NIT.
4 NIT held (s/sigma overloads -> notation pass; recurring "sign is even" category slip; column-sum "crossing column"). Counter claims stays 0. Recompiled 15pp clean. Agents a39fd8e4 (claims) / ae7a88d1 (biblio).

## WAVE 13 STATE: claims 0 / biblio re-cert 0 / numerics 3 CERT.

## WAVE 14 (2026-07-17, conv 9fa0e0c5): CLAIMS pass 46 OPUS + BIBLIO re-cert pass 8 FABLE.
CLAIMS: ZERO MAJOR -- signlaw/k2/rayleigh re-derived from scratch by Opus; growth-w.p.1 scoping (absolutely-continuous phase law, unstructured-regulator caveat), generic-ray O(eps) hedge, band theorem-vs-asymptotics status, sign(Re delta) invisibility all consistent across abstract/intro/body/table. 2 MINOR applied:
- [MINOR APPLIED] "(Krein theory) ... growing side has probability strictly below one" -> BOTH halves fixed: (a) prob-clause "strictly between zero and one (an open band of oscillatory directions survives)" -- the real-symplectic lattice retains an open oscillatory band, so prob in (0,1), not merely <1; (b) CITATION: "(Krein theory)" was invoked with NO reference -> added \bibitem{KreinTheory} = M.G. Krein 1950 (Dokl. Akad. Nauk SSSR 73, 445) + R.S. MacKay 1986 (Nonlinear Phenomena and Chaos, ed. Sarkar, Adam Hilger, pp.254-270), cited at L296. Metadata VERIFIED by the biblio agent vs primary sources (MacKay MR854706 confirmed twice; Krein vs citing literature); 28-entry bibliography confirmed still CLEAN. (DO-IT-NOW CORRECTION: this citation was initially parked to "protect the cert basis" -- wrong call per investigate-don't-defer; resolved in-session by having the biblio agent verify the single addition so the 0->1 pass covers the COMPLETE bibliography, not a stale 27-entry one.)
- [MINOR APPLIED] tower "negativity at depth two is a theorem at every sector" -> qualified "given the companion's sector-tower structure" (foregrounds the Companion4 out-of-paper premise; second site L761 already carried "with its premise supplied by the companion").
- [NIT HELD] abstract w.p.1 sentence near-unparseable (triple-nested parens; content correct); O(eps) "oscillatory locus" loose when tr P != 0 (model uses tr P=0). Both readability-only, HELD for the owed notation/polish micro-pass (logged, not dropped).
BIBLIO re-cert pass 8 (Fable): CLEAN -> counter 0->1 (on the COMPLETE 28-entry bibliography incl. the verified Krein/MacKay addition). All 5 self-cites SUPPORTED at 26 body cite-sites (referents opened: Companion->paper1/, Companion2->paper3/, Companion3->paper4/, Companion4->paper5/, Companion3prop->paper2/; every quoted number traced incl. Merlin arithmetic, 0.486 onset, 2/delta law, M+1 sector tower, sqrt((s+1)(M-s)) weights). All external refs verified (7x 2026 + 2x 2025 high-risk arXiv IDs live-resolved). ledger-38 THIRD-COPY grep-check PASSED (no third Merlin-scripts attribution; both provenance sites read "analytic"). NOTE: the Krein title is a translation of a Russian original -- future passes should not flag translation-wording variants as a metadata error.
Counter claims stays 0 (2 MINOR applied); biblio re-cert 0->1. Recompiled 15pp clean. Agents a4f5ad82 (claims) / a061eade (biblio + Krein-add verification).

## WAVE 14 STATE: claims 0 / biblio re-cert 1 / numerics 3 CERT.

## WAVE 15 (2026-07-17, conv 9fa0e0c5): CLAIMS pass 47 FABLE + BIBLIO re-cert pass 9 FABLE.
CLAIMS: ZERO MAJOR -- signlaw/k2/rayleigh + Gaussian gate + IK corner + D5 reconstruction all re-derived from scratch SOUND; growth-w.p.1 scoping, generic-ray O(eps), Krein claim, sector-M foregrounding all confirmed. 4 MINOR + 2 NIT applied:
- [MINOR APPLIED] F1 "precisely the band edges": cancellation ratios (j_0k/j_0n)^2 are two-index; only the n=1 dominant-pole subfamily are edges -> restricted to x_1 ("cancellations at a subdominant x_n shift only subleading terms"). F2 generic-locus: "zero set of a single condition, codim one" -> "contained in the zero set of a single condition (the imaginary discriminant), measure zero a fortiori" (true locus is codim TWO; O(eps) displacement confirmed correct -- also settles the wave-14 held NIT-4). F3 abstract "without leaving the exceptional line" -> "without imposing a detuning floor on the approach" (the dressed pair is OFF the line at every finite k). F4 "Jordan cascade" defined ("an equal-diagonal, nearest-neighbor bidiagonal chain, the physical object throughout").
- [NIT APPLIED] F5 "total positivity of c_3" -> "positivity of c_3 at every step ratio"; F6 "theorem at every sector" -> "at every sector M>=2".
BIBLIO re-cert pass 9 (Fable): CLEAN -> counter 1->2. The wave-14-added KreinTheory (Krein 1950 + MacKay 1986) claim-supported with verified metadata; all 5 self-cites SUPPORTED at 26 sites; all externals verified; Merlin third-copy grep PASS. **One clean pass from K=3 CERT.**
Counter claims stays 0; biblio 1->2. Recompiled 15pp clean. Agents a1d9ac65 (claims) / a7c5c53a (biblio).

## WAVE 15 STATE: claims 0 / biblio re-cert 2 / numerics 3 CERT.

## WAVE 16 (2026-07-17, conv 9fa0e0c5): CLAIMS pass 48 FABLE + BIBLIO re-cert pass 10 FABLE.
CLAIMS: ZERO MAJOR; wave-15 fixes VALIDATED (O(eps)/codim, Jordan-cascade class, M>=2, Krein carve-out all re-derived sound). signlaw/k2/rayleigh + Gaussian gate + IK corner re-derived SOUND. 1 MINOR + 1 NIT applied:
- [MINOR APPLIED] "growth with probability one" is exact only for the PHASE-ONLY (traceless) model; full-matrix AC noise (Im tr P != 0) opens a DECAYING band of width O(sqrt eps) -> added the qualifier ("probability 1-O(sqrt eps) -> 1 as eps->0") + softened the Discussion "sits on one side or the other" to name the decaying side. Counterexample verified.
- [NIT APPLIED] "oscillatory set is the WHOLE real axis" -> "punctured real axis (Delta != 0)" (the EP Delta=0 is secular, not oscillatory).
BIBLIO re-cert pass 10 (Fable): CLEAN -> 2->3 = **CERTIFIED K=3.** The 2026-07-15 ledger-31 revocation FULLY RE-EARNED; the Krein/MacKay add claim-supported; all 5 self-cites SUPPORTED at all sites; all externals verified; Merlin third-copy PASS.
Counter claims stays 0; **biblio 2->3 CERT.** Recompiled 15pp clean. Agents af625b7e (claims) / a6e8097d (biblio).

## WAVE 16 STATE: claims 0 / biblio 3 CERT / numerics 3 CERT.

## WAVE 17 (2026-07-17, conv 9fa0e0c5): CLAIMS pass 49 FABLE. ZERO MAJOR; wave-15/16 fixes re-derived SOUND (punctured real axis, O(eps)/codim, Krein, M>=2); signlaw/k2/rayleigh + Gaussian gate + IK corner all re-derived. 3 MINOR applied:
- [MINOR] the wave-15 "Jordan cascade" class broadening exposed that Thm 1/Thm 2's EXACT formulas ("-t^3", "2(-1)^m 4^{m+1} sigma_{m+1} t^{2m+1}") hold only in the JORDAN BASIS (unit couplings); general chains carry a positive bond factor |c_i..c_{i+m}|^2, only the SIGNS are class-invariant -> scoped both formulas "in the Jordan basis" + bond-factor note.
- [MINOR] Thm 1 proof widened its conclusion to the chain class without the positive-diagonal-similarity bridge -> added the V=D^-1 f(t^2 N) D sentence.
- [MINOR] abstract "growth with probability one (unstructured regulators)" -- wave-16 fixed only the BODY; abstract copy still lacked the traceless qualifier (grep-all-copies miss) -> "(unstructured, traceless/phase-only; fully generic noise 1-O(sqrt eps))".
Counter claims stays 0. Recompiled 15pp clean. Agent a874c1f0.

## WAVE 17 STATE: claims 0 / biblio 3 CERT / numerics 3 CERT.

## WAVE 18 (2026-07-17, conv 954cb52d) — notation pass + Fable claims pass 50
NOTATION: Rayleigh sums sigma_p->R_p (frees sigma_max), divisor coefficients c_m->h_m (frees bond coupling c_i), IK singularity t_c->t_sing (frees mass-creation onset t_c), ladder index s->nu, Delta-sigma error term rewritten in prose (respects reserved Delta). CLAIMS: spine SOUND -- Prop signlaw, thm:k2 (h_2 window), thm:rayleigh (R_p Rayleigh values, Hadamard factorization), bond sign law + silent cone, Gaussian envelope, probability-one scoping (all copies correctly hedged), corner, photonics all re-derived. ZERO new structural MAJOR. Fix-propagation sibling applied: "punctured real axis (Delta!=0)" was in abstract+caption but stale ("whole real axis") in intro L178 + Sec 2 L261 -> both punctured (Delta=0 is the EP, secular not oscillatory). NIT: h_3(rho) rescaled convention explicit; imaginary-split negativity-silence given analytic reason (det>=1). Notation pass verified clean by the claims lane. Recompiled 15pp clean. Counter claims 0.

## WAVE 19 (2026-07-17, conv 954cb52d) — Fable claims pass 51
Spine SOUND (signlaw/k2/rayleigh/bond-cone/band asymptotics all re-derived); sibling sweep CLEAN (wave-18 punctured-real-axis fix confirmed in every copy). 0 MAJOR. MINOR: generic decaying band opens only when the common term damps (Im tr P<0) -- added condition. NIT: measure-zero "detuning plane"->"complex plane" (both copies). Left defensible: a,b=s^2,T^2 reuse (alpha/beta already used 11x; inline-defined). Recompiled 15pp clean. Counter claims 0.

## WAVE 20 (2026-07-17, conv 954cb52d) — Fable claims pass 52
Spine SOUND; punctured-real-axis confirmed all copies. MAJOR (sibling): intro Layer 1 listed "lattice discretizations" among generic (measure-zero-oscillatory) perturbations but a structured real-symplectic lattice is Krein with an OPEN band (body/table had the carve-out) -> "generic UNSTRUCTURED perturbations ... structured lattice the exception". MINOR: Table w.p.-1 row -> "unstructured phase-only ... fully generic 1-O(sqrt eps)". NIT: "lower real axis"->"real axis (from below)" both copies. Recompiled 15pp clean. Counter claims 0.

## WAVE 21 (2026-07-17, conv 954cb52d) -- OPUS cross-model claims pass 53
CROSS-MODEL: no CRITICAL/MAJOR; thm:k2 tower + thm:rayleigh + bond cone + all numerics re-derived SOUND. PRIOR-FIX REVERSAL (ledger 48): generic-ray "O(eps) displacement" (wave-10 opus+sympy verifier) is WRONG -> O(sqrt eps) angular, matching the body band width; VERIFIED numerically+analytically (phi-star/sqrt eps -> 2.46 const); fixed all 3 sibling copies (abstract/map/caption). Recompiled 15pp clean. Counter claims 0.

## WAVE 22 (2026-07-17, all-lane all-Fable; user: "run until Fable returns NOTHING 3x each lane")
- CLAIMS (Fable): no CRITICAL/MAJOR (all theorems re-derived sound; the 400-run MC + all closed forms confirmed). 3 MIN applied: (1) ledger 54 -- oscillatory-set DISPLACEMENT O(sqrt eps)->O(eps) at abstract/intro/Table-1-caption (REVERSES the wave-21 ledger-48 over-correction; there are two objects -- locus displacement O(eps), decaying-band width O(sqrt eps); orchestrator-verified via p6_two_loci.py, band boundary phi*/sqrt(eps)->1.0); (2) Krein structured-regulator quantifier "absolutely continuous" -> "full support"; (3) +-i growing/decaying ray labels anchored to the symmetric split convention omega_{1,2}=omega +- delta/2.
- NUMERICS (Fable): 1 MIN -- same O(eps)/O(sqrt eps) displacement issue (cross-lane with claims). Everything else reproduced (7 scripts run in full incl. the 400-run device MC).
- BIBLIO (Fable): CLEAN -- all external bibitems + all ~20 Companion4 self-cite sites claim-support-checked; verbatim quotes + 2026 arXiv IDs confirmed. Fable-clean 1/3.
- Recompiled 15pp clean. Counters: claims 0; numerics CERT->0; biblio CERT + Fable-clean 1/3. Fable-clean streak: biblio 1/3, claims 0/3, numerics 0/3.

## WAVE 23 (2026-07-18, all-lane all-Fable)
- CLAIMS (Fable): no MAJOR (spine sound; wave-22 ledger-54 two-loci fix + Krein full-support + symmetric-split convention all re-validated). 3 MIN, all finer precision in the O(eps)/O(sqrt eps) passage: the "1-O(sqrt eps)" RATE qualified to "phase densities bounded near the band" (a.c. alone gives only ->1) at 3 sites; the "displaced ray by O(eps)" softened to containment ("within an O(eps) neighborhood") + explicit "empty once Im tr P != 0" note (2+1 sites).
- NUMERICS (Fable): CLEAN -> Fable-clean 1/3. INDEPENDENT re-validation of ledger-54: fresh from-scratch construction gave band width 1.998*sqrt(eps) [O(sqrt eps)] and traceless oscillatory locus at phi*=-0.5*eps [O(eps)] -- "no mislabeling."
- BIBLIO (Fable): CLEAN -> Fable-clean 2/3 (all 27 bibitems + ~20 Companion4 sites re-confirmed).
- Recompiled 15pp clean. Counters: claims 0/3, numerics 1/3, biblio 2/3.


## WAVE 24 (2026-07-18, all-lane all-Fable)
- CLAIMS (Fable): CLEAN -> Fable-clean 1/3. The O(eps)/O(sqrt eps) hot-spot passage (worked waves 10/21/22/23) is now airtight and re-validated: "O(eps) locus displacement at Im tr P=0, empty for Im tr P!=0, O(sqrt eps) decaying band -- each object correctly attributed; a.c.->w.p.1, bounded-density->rate 1-O(sqrt eps), full-support->strictly-between." It stopped attracting findings.
- NUMERICS (Fable): CLEAN -> Fable-clean 2/3 (full 400-run MC + all scripts reproduce; the two-loci scalings independently re-derived from scratch). NOTE: this lane returned an interim note first and was RESUMED via SendMessage to get its verdict once the background MC finished.
- BIBLIO (Fable): 1 NIT -- Krein 1950 title translation "several investigations" -> "certain investigations" (standard rendering of "nekotorykh"; "several"=neskolko is a different word). Resets biblio 2/3 -> 0/3 (one clean pass short of converging -- a textbook demonstration of the strict "nits count" criterion).
- Recompiled 15pp clean. Counters: claims 1/3, numerics 2/3, biblio 0/3.

## WAVE 25 (2026-07-18, all-lane all-Fable) -- NUMERICS LANE CONVERGED
- CLAIMS (Fable): no MAJOR. 1 MIN: intro "growth everywhere else" given the decaying-band qualifier (for net-damping fully generic noise an O(sqrt eps) decaying band intervenes; growth there only w.p. 1-O(sqrt eps)) -- the abstract/Discussion already carried it. The O(eps)/O(sqrt eps) passage re-validated airtight.
- NUMERICS (Fable): CLEAN -> **Fable-clean 3/3 CONVERGED** (clean waves 23/24/25; ran the 400-run MC in background and gave its verdict in one pass -- no resume needed).
- BIBLIO (Fable): 1 MIN + 1 NIT applied, 1 NIT REJECTED. Applied: Sec-5 "two-device ... own extension" reworded (D4 already exists in the cited proposal paper2; only D5 is new + a new guide-basis negativity readout on D4); WongZengLi2026 given its arXiv:2507.16049. REJECTED: Krein-title synonym swap "certain"->"some" (defensible translation; see auditor-error-log).
- Recompiled 15pp clean. Counters: claims 0/3, numerics 3/3 CONVERGED, biblio 0/3.

## WAVE 26 (2026-07-18, all-OPUS cross-model check; numerics SKIPPED as converged 3/3)
- CLAIMS (Opus): CLEAN -- every theorem re-derived; the O(eps)/O(sqrt eps) two-loci + empty-set caveat + distribution hypotheses all validated cross-model; two suspected errors (15.345 silent-cone threshold; D5 re-entry factor-2) investigated and confirmed correct. (Noted a stale CODE COMMENT in p6_d4_device.py as an explicit no-action observation, not a finding.)
- BIBLIO (Opus): 1 NIT REJECTED (DonoghueMenezes titles -- auditor compared to arXiv, but rule 6 = publisher governs; bibitem correct; see auditor-error-log). Otherwise clean; all self-cite claim-support re-validated.
- NUMERICS: SKIPPED (Fable-converged 3/3).
- No manuscript edits (claims clean, biblio NIT rejected). Fable-clean streaks: claims 0/3, biblio 1/3, numerics 3/3 CONVERGED. Claims + biblio now Opus-cross-model-validated.

## WAVE 27 (2026-07-18, all-OPUS cross-model check, 2nd consecutive; numerics SKIPPED as converged 3/3)
- CLAIMS (Opus): CLEAN. Adversarial from-scratch re-derivation of all three theorems (per-bond sign law, k2-only purity h2=(T^2-s^2)(T^2-3s^2)/4, Rayleigh sign law via I_0(2sqrt x) Hadamard product); all numerics reproduced independently (Rayleigh sums, band edges, 36 h3 discriminant, silent-cone thresholds 195.34485/344.65515 deg = 15.345 deg reproduced to the digit, corner s*=tau/(sqrt3-1), Puiseux/IK rates). Scope/quantifier probes all adequately hedged. Zero findings.
- BIBLIO (Opus): CLEAN -- 1 LOW flag REJECTED after primary-source verification. The recurring DonoghueMenezes serial-comma flag re-appeared on a NEW premise (this wave: "published PRD also has no comma"); orchestrator WebFetch'd Crossref (DOI 10.1103/PhysRevD.100.105006) = title WITH the serial comma, matching the bibitem -> flag is a misread, item CLOSED against the publisher record (see auditor-error-log). All 23 external bibitems + high-sequence 2026 arXiv IDs re-verified; WongZengLi now published (npj QI 12, 63 (2026)); all self-cites claim-support + reciprocity confirmed.
- NUMERICS: SKIPPED (Fable-converged 3/3).
- No manuscript edits (claims clean, biblio flag rejected). Fable-clean streaks: claims 0/3, biblio 1/3, numerics 3/3 CONVERGED. Claims + biblio Opus-cross-model-validated a 2nd time.


## SESSION 2026-07-18/19 (numbering unification + claim-support + rotation-four Fable)
- Folder unchanged (paper6, series 6); cite keys -> codenames; earlier prose "paper~4" -> "the conformal-gravity paper \cite{choosing}"; release-gate leak + biblio %-comment notes removed.
- Claim-support (Opus): CLEAN; IK2014 Eq.58/t_sing verbatim, all EP/non-Hermitian + 2026 refs SUPPORTED.
- Rotation-four Fable: BIBLIO CLEAN (23 refs, all three checks: metadata + arXiv-ID-resolves + claim-support; DonoghueMenezes serial-comma guard honored; the high-sequence 2026 EP arXiv IDs all resolve). CLAIMS 1 MINOR x2 sites -- stale pre-cutover ordinals "The fourth paper"/"the paper-4 statement" for choosing (now series 5) -> codename phrasing; the ordinal-word/hyphenated variants the original unification sweep (paper~N only) missed. Corpus sibling-sweep -> no other residue. Fresh streaks: biblio 1/3, claims 0/3.

## FABLE CLAIMS PASS 2026-07-19 (Fable-spend rotation-four wave, Wave 2)
- **SOUND: zero CRITICAL/MAJOR/MINOR** (2 NITs only). Auditor re-derived every spine AND independently reproduced the headline numerics from scratch (own scripts): famlaw/genlaw eigenvalues; corner rates 0.433/0.866/1.732; Prop 1 sign law (605/605 fresh triangular checks, zero residual); k=2 thm h₂=(b-a)(b-3a)/4; Rayleigh f=I₀(2√x) genus-0 + R₁..R₄; finite-step bands edge-march →(j₀₂/j₀₁)²=5.26894; divisor gate column sum 1+κ²(T²-s²); D5 construction one-way at J=Γ_d, estimator J+Γ_d; Merlin tilt. **Historically-fraught spots CLEAN: the two loci NOT conflated** (oscillatory displacement O(ε), measure-zero, "empty once Im tr P≠0" exact via trace reality; decaying-band width O(√ε), positive measure -> "1-O(√ε)"); **silent-cone threshold re-derived to 195.34487° vs paper 195.345°** (10⁻³-deg claim confirmed); Krein full-support hedge sufficient; ω₂²>0 clause present everywhere. Applied 2 NITs: abstract/table "ray φ=0 of the generic ones" -> "(the single-entry-model reference direction)" (for general P the ref ray is −arg P₂₁; body already anchored this); D5 η-imperfection re-entry lengths (6.9/12.7cm, verified correct) + a clause that the imperfect H₁₂≠0 device is non-triangular so the π/|δ| bond rule no longer governs (forestalls misapplying the paper's own spectrometer formula).
- Streak: p6-claims had findings (2 NITs) -> NOT a clean-streak pass, but zero MINOR-or-worse (closest to clean of the four). Recompiled clean; both gates PASS.

## FABLE BIBLIO PASS 2026-07-19 (Fable-spend rotation-four wave, biblio round 2) -- CLEAN
- **23/23 external bibitems CLEAN, 0 fix-needed.** Publisher-governs cases all confirmed toward the published form (Smilga2014 "Giving", IK2014 un-hyphenated, DM-PRL drops arXiv "The"); the recurring DonoghueMenezes comma correctly NOT raised (closed false positive). Verified by direct source quote: Merlin coinage attribution (PRD footnote -> PRL paper), Klauck fs-laser platform, WongZengLi CP-divisibility. 2 LOW machine-read caveats (IK2014 Eq.(58) is the paywalled PRD numbering; Pimenta2025 trace-preserving claim abstract-only) -- neither a defect.
- **CLEAN pass -> advances the p6-biblio Fable-clean streak.** No manuscript change.

## OPUS CROSS-MODEL WAVE 2026-07-20 (Wave A; claims + numerics; biblio skipped -- Fable cleared 23/23 this session)
- **FULLY CONVERGED: claims SOUND (Opus, confirms Fable) + numerics CLEAN (Opus, first run this session).** Claims: full spine re-derived (famlaw/genlaw, the TWO loci confirmed NOT conflated -- O(ε) oscillatory displacement vs O(√ε) band; silent-cone derivative; k=2 h₂; Rayleigh f=I₀(2√x); D5 non-triangular clause SOUND). Numerics: all 7 p6_* scripts reproduce every value (silent-cone 195.345°, Prop-1 1408/1408 bonds residual 0, k=2 flip at √3, R₁..R₄=1/4,1/32,1/192,11/12288, edge-march →(j₀₂/j₀₁)²=5.269, two-loci growth √ε exp 0.5000, D5 re-entry 6.0/6.9/12.7cm, corner rates); deterministic (all RNG seeded, no PYTHONHASHSEED). No CRITICAL/MAJOR/MINOR either lane. Notes (not defects): Merlin row is disclosed non-scripted/analytic (Code-availability carve-out); D5 0.91cm (finite-step protocol) vs 0.97cm (zero-step 0.486/2J) correctly distinguished in-line. Skipped 1 style nit (abstract nested-parenthetical readability, auditor said not required). No manuscript change.

## OPUS DEEP CLAIMS 2026-07-20 (Wave D; Nth adversarial pass) -- SOUND
- no C/M/MINOR; two-loci logic verified airtight for FULLY GENERIC P (Im tr P≠0 => oscillatory set empty; traceless => measure-zero O(ε) curve inside positive-measure O(√ε) band); silent-cone/Krein/D5-certification all held via honest hedging; ChenJu2026 high-id already biblio-confirmed real. No manuscript change.

## OPUS DEEP CLAIMS 2026-07-20 (hunt-what-was-rationalized wave, p5-p8) -- SOUND, 2 MINOR + 1 NIT applied
- No CRITICAL/MAJOR; theorem spines (h_2/h_3 divisors, Rayleigh identity, detuned 2x2 ratio, column-sum law, band edges, corner rate) re-derived; the O(ε)/O(√ε) two-loci logic verified airtight in the body.
- Applied: (MINOR, Krein attribution §"Structured regulators") SHARPENS Wave-D's "Krein held via honest hedging". Original: "a mixed-signature $1{:}1$ resonance, whose Hamiltonian unfoldings split onto the ... oscillatory axis on an open set of directions (Krein theory)". Defect: a mixed-signature (Krein-)collision is precisely the UNSTABLE case (Krein's positive/strong-stability result is the DEFINITE-signature case), and Krein signature is UNDEFINED at the defective (Jordan/EP) point; the open oscillatory set is a property of the real-symplectic DEFECTIVE unfolding (MacKay, bundled in \cite{KreinTheory}), not of a Krein signature. Recast: "a defective $1{:}1$ resonance, whose Hamiltonian unfoldings keep an open set of directions oscillatory (a property of the real-symplectic unfolding, not of a Krein signature---undefined at the defective point~\cite{KreinTheory})". **NOT a reversal** -- the conclusion (open oscillatory set survives) was always correct; only the cited justification was backwards. (MINOR, intro) "$O(\epsilon)$ neighborhood ... for generic perturbations" dropped the traceless hypothesis (body: empty once Im tr P≠0) -> "for traceless-shift perturbations". (NIT) false-causal "so" linking the common $O(\epsilon)$ growth to the $O(\epsilon)$ ray displacement -> "; the oscillatory locus is instead displaced ... through the sub-leading discriminant correction".
- HELD/reported (NIT, not applied): abstract triple-nested parenthetical -- parentheses balanced, readability only.
- Recompiled 15pp, 0 undefined. Both gates PASS. No MAJOR.

## RE-VERIFY 2026-07-20 (adversarial Opus check of the Krein recast) -- CONFIRMED, no change
- Fresh Opus verifier confirmed the Krein-attribution recast is mathematically CORRECT on every point (PU 1:1 resonance genuinely defective/Jordan-EP; Krein signature undefined there; the open oscillatory set is a real-symplectic/MacKay property; normal form (0 1;−k 0) oscillatory for k>0 = open half) and COMPLETE (sibling sweep clean: "mixed-signature" now absent everywhere; the 3 structured-lattice sites at L170/L297/L738 all consistent; \cite{KreinTheory} does bundle MacKay). Verdict "ship it". No further change.

## OPUS NUMERICS 2026-07-20 (Wave 6; reproduce-from-scripts) -- CLEAN (1 defensible NIT)
- Ran all 7 scripts. Every script-backed number reproduces to the quoted digits: h2=1/4(T^2-s^2)(T^2-3s^2) (5.9e-13), 36h3=(rho-1)(rho^2-8rho+19) (SymPy), Rayleigh R1..R4, L=2t/-t^3, band edges 5.269/12.949/24.042, -0.691660, corner rate 0.433/0.866/1.732, column-sum law, detuned r(t) to 1e-15, 500/500 draws, 1408/1408 sign agreements, silent-cone 15.345deg, full D4/D5 device chain. NIT held-defensible (#47): the fully-generic O(sqrt eps) band / prob 1-O(sqrt eps) claims are analytic with no dedicated script (only the traceless model is exercised) -- defensible under the Code-availability "numerical claims" scoping. The old phi*/sqrt-eps=1.000000 figure is (correctly) absent now that the two-loci result is analytic.
- No manuscript change.

## FABLE CLAIMS 2026-07-20 (cross-model diversity wave, p1/p3/p5/p6) -- 1 MINOR + 2 NIT applied
- Fable re-derived divisor coeffs h_2/h_3 (+ h_4/h_5 in closed form BEYOND the paper, confirming the m=5 odd window), Rayleigh algebra, two-loci orders (NOT swapped), tower similarity, D5 reconstruction. Zero CRITICAL/MAJOR, zero false converses. **Independently CONFIRMED the session's Krein recast is CORRECT PHYSICS** (re-derived the Hamiltonian-Hopf structure: mixed-signature = unstable-necessary; signature undefined/degenerate at the defective point; open oscillatory set = MacKay real-symplectic-unfolding property).
- Applied: (MINOR #59) abstract dangling appositive "the sign negativity cannot see" (comma splice) -> "---a sign the negativity channel cannot see;". (NIT #60) **self-edit** this session's "traceless-shift perturbations" coinage -> "traceless perturbations". (NIT #61) measure-zero syllogism proviso "not identically vanishing in the phase" added.
- HELD: Krein "undefined" -> optional precision "degenerate (eigenvector symplectically isotropic)" -- recast confirmed correct, "undefined" defensible; left.
- Recompiled 15pp, 0 undefined. Both gates PASS. No MAJOR.

## OPUS CLAIMS AUDIT 2026-07-23 (fresh, not in prior waves) — CLEAN
- NOTHING at MINOR+. Two-loci O(eps)/O(sqrt eps) correct on the right object at every site (the historically-reversed seam, ledger 48/54); silent-cone 15.345 deg verified; k=2 purity h2=1/4(T^2-s^2)(T^2-3s^2) + Rayleigh sign law (R2/R3/R4, even-m march 3.000->5.269) re-derived exact; Krein invocation defensible (signature undefined at the defective point). IK Eq.58 machine-provisional but self-checked to 1e-6.

## W22 WIDE-OPEN AUDIT 2026-07-26 (Opus, adversarial; claims+numerics+biblio) — essentially CLEAN; 1 NIT applied
- **CLAIMS CLEAN:** full spine re-derived from scratch + attacked with the AUDITOR's OWN adversarial examples (not the paper's): Prop 1 sign law (0/8942 sign mismatches on random triangular d=2-6); Thm 1 h₂=(T²−s²)(T²−3s²)/4 + J₄/J₅ complex-eigenvalue sign-flip at ratio 3; Thm 2 Hadamard R₁..R₄; h₃ 36h₃=(ρ−1)(ρ²−8ρ+19) disc<0; bond taxonomy silent-cone 195.3449°/344.6551° (independent bisection); symplectic exception/Krein. No false universals/converses; "sampled" qualifiers honest. **NUMERICS CLEAN:** all 7 scripts reproduce every number (family 4.6e-2, IK rates, band-edge march, R-sums ≤3e-15, D4/D5 device numbers, symplectic-vs-non-symplectic labeling correct). **BIBLIO CLEAN:** 25 cites defined/cited, balanced; Smilga2014 "Giving" convention holds (W21 #79); 2026 arXiv IDs reconcile to research/p6_prior_art_resweep.md (provenance-tracked, standing human-PDF).
- **NIT applied (precision):** abstract L44 + Table caption L752 "within an $O(\epsilon)$ neighborhood of the ray $\varphi=0$ ... of the generic ones---measure zero (in the complex plane) either way" — the O(ε) neighborhood has positive area, juxtaposed with "measure zero" it risks a momentary misread (the measure-zero object is the RAY/curve, the O(ε) is its numerical resolution). Reworded BOTH sites (sibling-swept): "the ray $\varphi=0$ (... resolved to within $O(\epsilon)$) of the generic ones---measure zero either way" (matches the body L287 "zero set of a single real-analytic condition"). **NIT (readability, split the 12-line abstract sentence) REJECTED — pure style on technically-correct text.**
- Recompiled 15pp, 0 undefined, 0 overfull >10pt. Both gates PASS. **p6 -> 0/3 (took a precision NIT; manuscript otherwise clean).**

## W23 CROSS-PAPER BIBLIO CORRECTION 2026-07-31 (orchestrator, Crossref-verified) - 2 fixes; counter reset
- IK2014 carried "Conformal gravity redux: **Ghost-turned-Tachyon**"; Crossref (10.1103/PhysRevD.89.104015) gives "Conformal gravity redux: **Ghost-turned tachyon**" - the 07-24 Opus biblio wave had introduced BOTH a spurious hyphen and a spurious capital T from the arXiv form. Corrected. Also Smilga2014's stray mid-title capital ("order Giving") harmonized to house sentence-case "giving" (the WORD stays per major-ledger #79 / auditor-error-log; only the case changed). **major-ledger #84.** Corpus re-grepped: zero stale copies. Rebuilt clean (2 overfull, both <6pt), both gates PASS.
- NOTE: resets p6's counter. The rest of the paper was not re-audited this wave.

## W25 WIDE-OPEN AUDIT 2026-08-01 (Fable, adversarial) - NO MAJOR; NUMERICS CLEAN (7/7 scripts, nothing skipped); 1 MINOR + 1 NIT applied, both script-side; counter -> 0
- **Every proposition and theorem re-derived independently**, including both branches of the sign law, the k=2-only theorem by series inversion, the Rayleigh/Hadamard construction with recomputed band edges, the silent cone and its scale invariance, and -- notably -- the O(eps) vs O(sqrt eps) exponents derived by **explicit expansion rather than by analogy**, which is where an earlier wave (ledger #48) went wrong. Measure-zero and genericity language checks out; the punctured axis correctly handles the Delta=0 EP.
- **MINOR + NIT applied, both text-vs-script with the PAPER on the correct side:** p6_unfolding_sweep.py's printed MAP claimed mixed complex splits give "transient M1 windows, then silence". Re-derivation of dr/dt shows the envelope sqrt(a^2+b^2) exceeds the decaying b*exp(-b t) for all t, so UPPER-half-plane mixed splits recur INDEFINITELY -- exactly what main.tex L520-522 and p6_divisor_theorem.py block [6] already state. Only the lower-half wedges go transient. The same printout omitted the Delta=0 puncture. p6_divisor_theorem.py's docstring carried the matching error ("EP or complex split"). Both corrected to the paper's (correct) statement; script re-run exit 0.
- **REJECTED:** the DonoghueMenezes PRL title re-flag (Crossref lacks the leading "The"). **The user confirmed this against the actual PDF on 2026-07-24**; a human read of the published article outranks a Crossref metadata record, which is supplier-provided and known to drop leading articles. See auditor-error-log for the asymmetry with #84. minor-ledger #171.
