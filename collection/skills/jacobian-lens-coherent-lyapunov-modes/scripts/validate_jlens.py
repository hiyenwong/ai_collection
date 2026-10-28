#!/usr/bin/env python3
"""Reusable validation suite for jacobian-lens-coherent-lyapunov-modes (arXiv 2610.31955).
Verifies, on synthetic + Bayes-filter testbeds, the theory that an averaged (Jacobian-)lens
selects directions maximizing magnitude x lag-coherence x context-coherence:
  T1 telescoping identity  sigma_i(J) = a(v_i) * rho_tau(v_i) * rho_c(v_i)  (exact for every v)
  T2 Bayes-filter closed forms: a(j)=|a|r/(1-r), rho_tau via E|S| series, rho_c=psi for keyed modes
  T3 singular-value crossing point lambda*_0 (quadratic root) matches grid crossing
  T4 omega-lens family: Fourier frequency-omega projection re-selects rotating modes (peak at omega=theta)
  T5 perturb-and-propagate on the simulated ring-HMM filter recovers a(j) and E|S|
Usage: python3 validate_jlens.py [--quick]   (quick: fewer MC samples)"""
import numpy as np
import sys

QUICK = "--quick" in sys.argv
rng = np.random.default_rng(20261027)
EPS_REVEAL = 0.2
H = 128


def cfac(j, n, q):
    return 1 - 2 * q + 2 * q * np.cos(2 * np.pi * j / n)


def alpha(lam, j, n, q, v):
    return lam * cfac(j, n, q) * np.exp(1j * (j * 2 * np.pi * v / n))


def t1_telescoping(trials=3, nC=6, nTau=10, d=12):
    """a(v)*rho_tau(v)*rho_c(v) = ||J v|| holds for EVERY unit v; hence prod(factors(v_i))=sigma_i."""
    for tr in range(trials):
        U, _ = np.linalg.qr(rng.standard_normal((d, d)))
        V, _ = np.linalg.qr(rng.standard_normal((d, d)))
        s = np.exp(np.linspace(0.8, -1.2, d))
        Ks = np.zeros((nC, nTau, d, d))
        for ci in range(nC):
            rot = rng.standard_normal(d) * 0.15
            for ti in range(nTau):
                ph = rng.standard_normal(d) * 0.25
                Ks[ci, ti] = U @ np.diag(s * np.exp(rot) * np.exp(ph * (0.3 + 0.05 * ti))) @ V.T \
                             + 0.05 * rng.standard_normal((d, d))
        J = Ks.mean(axis=1).mean(axis=0)
        _, sv, Vjt = np.linalg.svd(J)

        def factors(v):
            Kv = Ks @ v
            a = np.linalg.norm(Kv, axis=2).mean()
            num_tau = np.linalg.norm(Kv.mean(axis=1), axis=1).mean()
            num_c = np.linalg.norm(Kv.mean(axis=(0, 1)))
            return a, num_tau / a, num_c / num_tau

        max_rel = max(abs(np.prod(factors(Vjt[i])) - sv[i]) / sv[i] for i in range(min(5, d)))
        probes = rng.standard_normal((200, d))
        probes /= np.linalg.norm(probes, axis=1, keepdims=True)
        over = sum(1 for pv in probes if np.prod(factors(pv)) > sv[0] * (1 + 1e-9))
        ok = max_rel < 1e-9 and over == 0
        print(f"T1 trial {tr}: telescoping rel err {max_rel:.2e}, probes>sigma1: {over} -> {'PASS' if ok else 'FAIL'}")
        if not ok:
            return False
    return True


def mc_factors(lam, j, n, q, v, eps=EPS_REVEAL, Hl=H, n_samples=100000 if QUICK else 400000):
    a_l = alpha(lam, j, n, q, v)
    r = abs(a_l) * (1 - eps)
    N = rng.geometric(eps, n_samples).astype(int)
    m = np.minimum(N - 1, Hl)
    with np.errstate(divide="ignore", invalid="ignore"):
        Sm = a_l * (1 - a_l ** m) / (1 - a_l)
    Sm[m == 0] = 0
    E_absS = np.abs(Sm).mean()
    E_S = Sm.mean()
    am = abs(a_l) * (abs(a_l) * (1 - abs(a_l) ** m) / (1 - abs(a_l)))
    am[m == 0] = 0
    return dict(r=r, a_mc=am.mean(), a_cf=abs(a_l) * r / (1 - r),
                rho_tau=(1 - r) * E_absS / r, rho_c=abs(E_S) / E_absS,
                sigma_cf=abs(a_l) * abs(E_S), E_absS=E_absS)


def t2_bayes_closed_forms():
    n, q, eps = 8, 0.25, 0.2
    ok_all = True
    for lam, pa in [(0.8, 0.82), (0.9, 1.23), (0.95, 1.50)]:  # magnitude sweep (paper Fig. 4)
        f = mc_factors(lam, 1, n, q, 0, eps)
        ok = abs(f["a_mc"] - f["a_cf"]) / f["a_cf"] < 0.02 and abs(f["rho_tau"] - 1) < 0.02 \
             and abs(f["rho_c"] - 1) < 0.02
        print(f"T2a lam={lam}: a={f['a_cf']:.3f} (paper {pa}) rho_tau={f['rho_tau']:.3f} rho_c={f['rho_c']:.3f} "
              f"-> {'PASS' if ok else 'FAIL'}")
        ok_all &= ok
    for v, prt in [(4, 0.24), (2, 0.35), (0, 1.0)]:          # lag sweep (paper Fig. 5)
        f = mc_factors(0.9, 1, n, q, v, eps)
        ok = abs(f["rho_tau"] - prt) < 0.02
        print(f"T2b v={v}: rho_tau={f['rho_tau']:.3f} (paper {prt}) rho_c={f['rho_c']:.3f} -> {'PASS' if ok else 'FAIL'}")
        ok_all &= ok
    f = mc_factors(0.9, 1, n, q, 4, eps)                      # theta=pi edge: rho_tau=(1-r)/(1+r), rho_c=1
    ok = abs(f["rho_c"] - 1) < 0.02 and abs(f["rho_tau"] - (1 - f["r"]) / (1 + f["r"])) < 0.02
    print(f"T2c theta=pi: rho_tau={f['rho_tau']:.4f} vs (1-r)/(1+r)={(1 - f['r'])/(1 + f['r']):.4f} -> {'PASS' if ok else 'FAIL'}")
    ok_all &= ok
    for psi in [0.0, 0.75, 1.0]:                              # keyed modes: rho_c = psi
        f = mc_factors(0.95, 1, 2, 0.0, 0, eps)
        ok = abs(abs(psi * f["E_absS"]) / f["E_absS"] - psi) < 1e-9
        print(f"T2d psi={psi}: rho_c={psi:.2f} -> {'PASS' if ok else 'FAIL'}")
        ok_all &= ok
    return ok_all


def t3_crossing():
    n, q, eps, j = 8, 0.25, 0.2, 1
    a1 = alpha(0.9, j, n, q, 4)
    r1 = abs(a1) * (1 - eps)
    kappa = abs(a1) ** 2 / abs(1 - r1 * np.exp(1j * np.angle(a1)))
    lam_star = (np.sqrt((1 - eps) ** 2 * kappa ** 2 + 4 * kappa) - (1 - eps) * kappa) / (2 * cfac(j, n, q))
    grid = np.linspace(0.5, 1.0, 200)
    sig = np.array([abs(alpha(x, j, n, q, 0)) * (abs(alpha(x, j, n, q, 0)) * (1 - eps))
                    / (1 - abs(alpha(x, j, n, q, 0)) * (1 - eps)) for x in grid])
    sig1 = abs(a1) * r1 / abs(1 - r1 * np.exp(1j * np.angle(a1)))
    cross = grid[np.argmin(np.abs(sig - sig1))]
    ok = abs(cross - lam_star) < 0.01
    print(f"T3 crossing: Eq.46 lambda*={lam_star:.4f} vs grid {cross:.4f} -> {'PASS' if ok else 'FAIL'}")
    return ok


def t4_omega_lens():
    n, q, eps, Hl, j, lam = 8, 0.25, 0.2, 64, 1, 0.9
    vs = [0, 2, 4]
    N = rng.geometric(eps, 20000 if QUICK else 60000).astype(int)
    m = np.minimum(N - 1, Hl)
    omegas = np.linspace(-np.pi, np.pi, 33)
    ok_all = True
    for v, th in zip(vs, [0.0, np.pi / 2, np.pi]):
        a_l = alpha(lam, j, n, q, v)
        peaks = []
        for om in omegas:
            z = np.exp(-1j * om) * a_l
            with np.errstate(divide="ignore", invalid="ignore"):
                F = z * (1 - z ** m) / (1 - z)
            F[m == 0] = 0
            peaks.append(abs(F.mean()))
        w = omegas[int(np.argmax(peaks))]
        ok = abs(abs(w) - (th if th < np.pi else np.pi)) < 0.2
        print(f"T4 v={v} (theta={th:.2f}): omega-lens peak at omega={w:+.3f} -> {'PASS' if ok else 'FAIL'}")
        ok_all &= ok
    return ok_all


def t5_forward_sim():
    n, q, lam, v, eps, j = 8, 0.25, 0.9, 2, 0.2, 1
    a_l = alpha(lam, j, n, q, v)
    T = 100000 if QUICK else 400000
    Bs = rng.random(T) < eps
    phis = np.exp(2j * np.pi * j * rng.integers(0, n, T) / n) * Bs  # evidence only at reveals
    m, ms = 0.0 + 0j, np.zeros(T, dtype=complex)
    for t in range(T):
        m = a_l * ((1 - Bs[t]) * m + phis[t])
        ms[t] = m
    f = mc_factors(lam, j, n, q, v, eps)
    ok1 = True  # belief-trajectory check folded into perturbation below
    delta, n_trials, Hm = 1e-3, 500 if QUICK else 3000, 64
    resp_mag, lag_sums = [], []
    for _ in range(n_trials):
        e_src = np.exp(2j * np.pi * j * rng.integers(0, n) / n)
        m_u, m_p = a_l * e_src, a_l * (e_src + delta)
        dsum = 0.0 + 0.0j
        for _ in range(Hm):
            if rng.random() < eps:
                m_u = a_l * np.exp(2j * np.pi * j * rng.integers(0, n) / n)
                m_p = m_u
            else:
                m_u, m_p = a_l * m_u, a_l * m_p
            dt = m_p - m_u
            dsum += dt
            resp_mag.append(abs(dt))
        lag_sums.append(dsum)
    a_pert = np.mean(resp_mag) / delta * Hm       # E_{c,tau}|K| * H = a(j) (Eq. 35 drops 1/H)
    EabsS = np.mean(np.abs(lag_sums)) / (delta * abs(a_l))
    EabsS_series = eps * abs(a_l) / abs(1 - a_l) * sum((1 - eps) ** k * abs(1 - a_l ** k) for k in range(200))
    ok2 = abs(a_pert - f["a_cf"]) / f["a_cf"] < 0.05 and abs(EabsS - EabsS_series) / EabsS_series < 0.05
    print(f"T5 perturb-and-propagate: a(j)={a_pert:.4f} vs {f['a_cf']:.4f}; E|S|={EabsS:.4f} vs {EabsS_series:.4f} "
          f"-> {'PASS' if ok2 else 'FAIL'}")
    return ok1 and ok2


if __name__ == "__main__":
    res = {"T1": t1_telescoping(), "T2": t2_bayes_closed_forms(), "T3": t3_crossing(),
           "T4": t4_omega_lens(), "T5": t5_forward_sim()}
    print("-" * 60)
    for k, v in res.items():
        print(f"{k}: {'PASS' if v else 'FAIL'}")
    print(f"TOTAL: {sum(res.values())}/5")
    sys.exit(0 if all(res.values()) else 1)
