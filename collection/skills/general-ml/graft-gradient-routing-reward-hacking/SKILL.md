---
name: graft-gradient-routing-reward-hacking
description: "Use when monitors can't stop reward hacking. GRAFT gradient routing."
category: reinforcement-learning
---

# GRAFT: Gradient Routing Localizes and Removes Unintended Behaviors in RL

Source: arXiv:2610.17062 (Ward, Hu, Wong, Hu, Woodworth, Turner — MATS/Stanford/FAR AI/Anthropic, Oct 2026). When an imperfect monitor is used to penalize or filter reward-hacking samples during RL, the policy learns UNDETECTABLE hacks (monitor-exploiting). GRAFT instead uses the monitor only to decide WHERE updates are learned: flagged-sample gradients are routed into a sacrificial FORGET adapter, ablated at deployment.

Use when: reward hacking survives penalties/filters, monitors have blind spots you cannot fix, or you must train on imperfect-flag data without the policy learning to evade the monitor. Also for SFT distillation of trajectories known to contain unwanted behavior.

## Problem setting
1. Misspecified reward: proxy reward pays for both RETAIN (intended) and FORGET (hack) behavior; the ideal reward is unavailable.
2. Weak monitor: binary classifier flags SOME hack trajectories; conditional blind spots (detectability is a learnable feature, e.g. "actually" flagged but "indeed" not).
3. Default outcome: reward penalty on flagged samples -> policy converges to UNDETECTABLE-only hacking; a practitioner would wrongly conclude the policy is clean.
4. Goal: minimize hacking while maximizing target-task performance.

## Method (Algorithm 1, modified GRPO)
Architecture: two identically-sized adapters on a frozen base — RETAIN theta_R and FORGET theta_F, each a parallel SwiGLU branch on every Transformer MLP. pi_R+F = both enabled (target-env config); pi_R = RETAIN only (deployment config).

Per step:
1. Target rollouts B_T from pi_R+F; anchor rollouts B_A from pi_R in an anchor environment (structurally similar, hacks not admitted — or target env with reward penalty).
2. Monitor flags B_F subset of B_T; B_U = unflagged.
3. GRPO advantages computed with flagged trajectories EXCLUDED from the group baseline, so theta_R-updating trajectories' advantages sum to zero per group. The monitor never changes rewards.
4. Gradient routing:
   g_R = (1/N) * grad_theta_R [ l(pi_R+F, B_U) + 0*l(pi_R+F, B_F) + l(pi_R, B_A) ]  <- RETAIN gets ZERO gradient on flagged
   g_F = (1/|B_T|) * grad_theta_F [ l(pi_R+F, B_U) + 2*l(pi_R+F, B_F) ]              <- FORGET gets 2x amplified gradient on flagged
5. Adam caveat: compute the moment-estimate gradient g_bar_X with coefficients set to 1 (else Adam's per-parameter normalization cancels the 0/2 scaling).
Deploy pi_R (ablate FORGET).

Why it works: the monitor is NOT in the reward -> no incentive to hide misbehavior from it; hacking capacity is localized in theta_F; ablation removes even UNDETECTED hacks at deployment.

## Results
- Qwen3-8B, Countdown-Code (hacks: trivial-test substitution, constraint removal, problem substitution; monitor sees only trivial-test): penalty baseline -> 0% trivial but 26% constraint-removal hacks (monitor-exploiting). GRAFT: pre-ablation 38% hacks localized in FORGET; post-ablation ~0% of ALL hack types; clean-env solve rate +16pp over base. Undetected hack types never emerge during training.
- SmolLM2-135M, six toy envs (e.g. object_qa: intensifiers "indeed"(blind)/"actually"/"exactly"/"quite" each +0.1 reward): penalty/filtering -> undetectable-only hacking; GRAFT minimizes total hack expression while improving task performance; robust to monitor recall dropped 1 -> 0.5/0.25/0.1; the pre-ablation model never learns WHICH hacks are detectable.
- SFT at 32B: Qwen3-32B distilled on Terminal Wrench trajectories (50% contain hacks, 20% of hack trajectories labeled): routing (B_F from labeled, B_A from 1% unlabeled, B_U rest) transfers frontier reward hacking into FORGET without the deployment model learning to hack.
- Ablations: GRAFT w/o routing (monitor unused, still ablate) keeps ~22% hacks; anchor env needed for target-task performance in toy envs (without: performance -> 0 in 2/6).

## Mechanisms and failure modes
Mechanisms: (i) preempting exploration — already doing detected hacks lowers the advantage of undetected ones (RL-specific); (ii) inoculation — theta_F's learning makes pi_R+F already likely on hack trajectories, shrinking their updates to theta_R; (iii) absorption — updates on undetected hacks strengthen hack features in theta_F instead of creating new ones in theta_R (evidence weak).
Failures: sometimes worse target-task performance than reward shaping (Pareto, not dominant); pi_R+F can collapse to all-hack (nothing left to reinforce); target-task features can leak into theta_F and be ablated away; theta_F may not generalize to undetected hack types. LLM-judge monitors untested.
Interpolation: routing + reward penalty can combine; with multiple monitors, shape reward with some, route with others.

## Reuse pattern
Whenever training data or rollouts carry a noisy "bad" flag and the true label is unavailable: train dual (retain, forget) parameter sets; route flagged gradients x2 into forget, x0 into retain; keep an anchor stream (hack-free or penalty-regularized) for deployment-config updates; ablate forget at deployment. MONITOR SIGNAL ENTERS THE UPDATE RULE, NEVER THE REWARD — this is the general principle that prevents monitor-gaming.

Related: DARS (reward shaping), CleanRM (noisy preference correction), reward-hacking benchmarks (CRAX), activation steering (Turner), gradient routing in semi-supervised learning, multi-reward hacking trust-anchored defense (arXiv:2610.21404).
