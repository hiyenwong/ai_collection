"""Verification of the worked example in arXiv:2610.08714.

Target: q(x) = (1 + x1 x2)/4 on the diagonal domain
  Delta(A) = diag(A1, A2),  ||A_j|| <= 1   (so a = b = k = 2, f_{mu nu, j} = delta_{mu,nu} delta_{mu,j})

Reconstructs numerically (numpy only):
  1. Residual basis and coordinate matrices E, J, P, L_j (r=2, h=5)
  2. The semidefinite defect certificate (paper Eq. 3.7):
        beta^2 E^H E - P^H P = S + Phi(T),  beta = 1
  3. Douglas-factor extraction (paper Eq. 3.17-3.19):
        V = Y T0^{-1} X^H,  X = [K M_1; K M_2; E], Y = [K E_1; K E_2; P], K = T^{1/2}
     V is (bm+1)x(am+1) = 9x9; blocks A (8x8), B (8x1), C (1x8), D scalar.
     Reference values from paper Eq. 3.20 checked via coefficient generation.
  4. Coefficient generation (paper Eq. 2.20):
        q_empty = D,  q_{j1..jd} = C F_{j1} A F_{j2} ... A F_{jd} B
     must reproduce q = (1 + x1 x2)/4: q_empty = 1/4, q_{x1x2} = 1/4, all else 0.
  5. Strict contractivity ||V||^2 <= 1 - mu/t0 (Lemma 3.4).
  6. Certified norm bound: ||q(A)|| <= beta = 1 for random contractive tuples.

Letter convention here is 0-based: j=0 <-> x1, j=1 <-> x2.
"""

import itertools
import numpy as np

rng = np.random.default_rng(26100871)
ok = lambda name, cond: print(f"  [{'PASS' if cond else 'FAIL'}] {name}")

# ---------------------------------------------------------------
# 1. Residual coordinates for q(x) = (1 + x1 x2)/4
#    f = (1, x2)^T;  g = (1, x1, x1 x2, x2, x2^2)^T;  h = 5, r = 2
# ---------------------------------------------------------------
print("1. Residual basis and coordinate matrices")
h, r, k, b, a = 5, 2, 2, 2, 2          # h = 1 + k*r
m = b * r                               # multiplicity m = b*r = 4
E = np.zeros((1, h)); E[0, 0] = 1.0                 # E g = 1
P = np.zeros((1, h)); P[0, 0] = 0.25; P[0, 2] = 0.25  # P g = q
L1 = np.zeros((r, h)); L1[0, 1] = 1.0; L1[1, 2] = 1.0   # x1 f = (x1, x1 x2)
L2 = np.zeros((r, h)); L2[0, 3] = 1.0; L2[1, 4] = 1.0   # x2 f = (x2, x2^2)
J = np.zeros((r, h)); J[0, 0] = 1.0; J[1, 3] = 1.0       # f = (1, x2)
ok("g basis has h = 1 + k*r = 5 entries", h == 1 + k * r)

# ---------------------------------------------------------------
# 2. Semidefinite defect certificate (paper Eq. 3.7), beta = 1
#    E_alpha: (br x h), J in block row alpha
#    M_mu:    (br x h), sum_j f_{mu nu, j} L_j in block row nu
#    Phi(T) = sum_alpha E_alpha^H T E_alpha - sum_mu M_mu^H T M_mu
# ---------------------------------------------------------------
print("2. Semidefinite defect certificate")
T = np.diag([1.0, 8.0, 16.0, 1.0]) / 64.0
S = np.array([
    [43, 0, -4, 0, 0],
    [0,  1,  0, 0, 0],
    [-4, 0,  4, 0, 0],
    [0,  0,  0, 7, 0],
    [0,  0,  0, 0, 1],
]) / 64.0

Eblocks = [np.zeros((b * r, h)) for _ in range(b)]
for alpha in range(b):
    Eblocks[alpha][alpha * r:(alpha + 1) * r, :] = J
Mblocks = [np.zeros((b * r, h)) for _ in range(a)]
for mu in range(a):
    Mblocks[mu][mu * r:(mu + 1) * r, :] = (L1 if mu == 0 else L2)

PhiT = sum(Eb.T @ T @ Eb for Eb in Eblocks) - sum(Mb.T @ T @ Mb for Mb in Mblocks)
lhs = E.T @ E - P.T @ P
ok("certificate identity  E^H E - P^H P = S + Phi(T)",
   np.allclose(lhs - (S + PhiT), 0, atol=1e-12))
ok("S, T positive definite", np.min(np.linalg.eigvalsh(S)) > 0
   and np.min(np.linalg.eigvalsh(T)) > 0)

# ---------------------------------------------------------------
# 3. Douglas-factor extraction (Eq. 3.17-3.19)
#    X = [K M_1; K M_2; E]  ((am+1) x h = 9x5)
#    Y = [K E_1; K E_2; P]  ((bm+1) x h = 9x5)
#    V = Y T0^{-1} X^H      ((bm+1) x (am+1) = 9x9)
#    A = V[:bm,:am] (8x8), B = V[:bm, am:] (8x1), C = V[bm:, :am] (1x8), D = V[bm,am]
# ---------------------------------------------------------------
print("3. Douglas-factor extraction")
K = T ** 0.5   # T diagonal -> exact positive square root, K: (m x br)
X = np.vstack([K @ Mb for Mb in Mblocks] + [E])
Y = np.vstack([K @ Eb for Eb in Eblocks] + [P])
ok("X shape (am+1, h) = (9, 5)", X.shape == (a * m + 1, h))
ok("Y shape (bm+1, h) = (9, 5)", Y.shape == (b * m + 1, h))
T0 = X.T @ X
ok("T0 = diag(1, 1/64, 1/8, 1/4, 1/64)  (paper value)",
   np.allclose(np.diag(T0), [1, 1 / 64, 1 / 8, 1 / 4, 1 / 64], atol=1e-12)
   and np.allclose(T0, np.diag(np.diag(T0)), atol=1e-12))
V = Y @ np.linalg.inv(T0) @ X.T
Ablk = V[:b * m, :a * m]     # bm x am = 8x8
Bblk = V[:b * m, a * m:]     # bm x 1
Cblk = V[b * m:, :a * m]     # 1 x am
Dblk = V[b * m:, a * m:]     # 1 x 1
ok("V X = Y exactly", np.allclose(V @ X, Y, atol=1e-10))
ok("D block equals q_empty = 1/4", np.allclose(Dblk, 0.25, atol=1e-12))

# Reference blocks (paper Eq. 3.20), 8-dim internal coordinates:
#   A = (e2/sqrt2 + e8/4) e7^T,  B = e1/8 + e7/2,  C = e2^T/sqrt2,  D = 1/4
e = lambda i: np.eye(8)[i - 1]
A_ref = np.outer(e(2) / np.sqrt(2) + e(8) / 4, e(7))
B_ref = (e(1) / 8 + e(7) / 2).reshape(-1, 1)
C_ref = (e(2) / np.sqrt(2)).reshape(1, -1)
ok("A block matches paper Eq. 3.20", np.allclose(Ablk, A_ref, atol=1e-12))
ok("B block matches paper Eq. 3.20", np.allclose(Bblk, B_ref, atol=1e-12))
ok("C block matches paper Eq. 3.20", np.allclose(Cblk, C_ref, atol=1e-12))

# ---------------------------------------------------------------
# 4. Coefficient generation (Eq. 2.20) with F_j^(m) = [f_{mu nu,j} I_m]
#    Diagonal domain: F_1 has I_m in block (0,0); F_2 in block (1,1)  (8x8)
#    q_{j1..jd} = C F_{j1} A F_{j2} ... A F_{jd} B   (rightmost acts first)
# ---------------------------------------------------------------
print("4. Coefficient generation q_w = C F A F ... B")
F1 = np.zeros((a * m, b * m)); F1[:m, :m] = np.eye(m)
F2 = np.zeros((a * m, b * m)); F2[m:, m:] = np.eye(m)

def q_coeff(word):
    """q coefficient of the ordered word (0-based letters), via Eq. (2.20)."""
    if not word:
        return Dblk[0, 0]
    acc = Bblk                       # (bm, 1)
    for idx, j in enumerate(reversed(word)):
        acc = (F1 if j == 0 else F2) @ acc
        if idx < len(word) - 1:
            acc = Ablk @ acc
    return (Cblk @ acc)[0, 0]

ok("q_empty = 1/4", abs(q_coeff(()) - 0.25) < 1e-9)
ok("q_{x1 x2} = 1/4 (the cross term)", abs(q_coeff((0, 1)) - 0.25) < 1e-9)
max_other = max(abs(q_coeff(w)) for d in (1, 2, 3)
                for w in itertools.product(range(k), repeat=d) if w != (0, 1))
ok(f"all other generated words (d<=3) vanish (max {max_other:.2e})", max_other < 1e-9)

# ---------------------------------------------------------------
# 5. Strict contractivity:  ||V||^2 <= 1 - mu/t0  (Lemma 3.4)
# ---------------------------------------------------------------
print("5. Contractivity of V")
mu = np.min(np.linalg.eigvalsh(S))
t0 = np.max(np.linalg.eigvalsh(T0))
nrmV = np.linalg.svd(V, compute_uv=False)[0]
ok(f"||V|| = {nrmV:.6f} <= sqrt(1 - mu/t0) = {np.sqrt(1 - mu / t0):.6f}",
   nrmV <= np.sqrt(1 - mu / t0) + 1e-12)
ok("||V|| < 1 (strict contraction)", nrmV < 1 - 1e-12)

# ---------------------------------------------------------------
# 6. Certified norm bound on random noncommuting contractive tuples
#    ||q(A)|| = ||(I + A1 A2)/4|| <= beta = 1
# ---------------------------------------------------------------
print("6. Norm bound on random contractive tuples")
worst = 0.0
for _ in range(200):
    n = 4
    G1, G2 = rng.normal(size=(n, n)), rng.normal(size=(n, n))
    A1 = G1 / max(1.0, np.linalg.svd(G1, compute_uv=False)[0])
    A2 = G2 / max(1.0, np.linalg.svd(G2, compute_uv=False)[0])
    worst = max(worst, np.linalg.svd((np.eye(n) + A1 @ A2) / 4,
                                     compute_uv=False)[0])
ok(f"sup ||(I+A1 A2)/4|| = {worst:.4f} <= beta = 1", worst <= 1.0)

print()
print("All checks complete: residual basis, certificate identity, Douglas")
print("extraction (all four blocks vs paper Eq. 3.20), coefficient generation,")
print("strict contractivity, and the certified norm bound.")
