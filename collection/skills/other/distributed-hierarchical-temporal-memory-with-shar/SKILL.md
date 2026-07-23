---
name: distributed-hierarchical-temporal-memory-with-shar
description: Skill derived from arXiv paper 2606.31789: Distributed Hierarchical Temporal Memory with Shared Associative Memory for Cross-Entity Preemptive Warning
category: other
created: 2026-07-23
arxiv_id: 2606.31789
utility: 1.0
---
# distributed-hierarchical-temporal-memory-with-shar

Derived from arXiv paper [2606.31789]: Distributed Hierarchical Temporal Memory with Shared Associative Memory for Cross-Entity Preemptive Warning

## Abstract
Anomaly detection in multivariate time series remains a critical challenge in large-scale distributed systems, where related entities may exhibit transferable precursor behavior prior to anomaly onset. Existing methods typically operate independently on each data stream and therefore remain fundamentally reactive. To address this limitation, we introduce Distributed Hierarchical Temporal Memory (D-HTM), a neuromorphic framework that enables cross-entity preemptive warning through a Shared Associative Memory (SAM).   D-HTM combines a Spatial Pooler (SP) that projects observations into a common Sparse Distributed Representation (SDR) space, Temporal Memory (TM) modules that learn entity-specific dynamics online, and a Shared Associative Memory that stores recurring pre-anomaly signatures. By reusing precursor knowledge across related entities, D-HTM can issue warnings prior to local anomaly onset while preserving HTM's online learning capabilities.   We evaluate D-HTM on the Server Machine Dataset (SMD), the Soil Moisture Active Passive (SMAP) dataset, the Mars Science Laboratory (MSL) dataset, and a synthetic cascade benchmark designed to isolate precursor transfer. Experimental results demonstrate effective cross-entity warning propagation while maintaining competitive reactive anomaly detection performance. Across the real-world datasets, D-HTM provides an average warning lead time of 8.1 samples prior to anomaly onset.   These findings demonstrate that transferable precursor structure can emerge within a shared SDR space and be reused for preemptive warning generation, extending HTM beyond isolated reactive detection toward distributed predictive reasoning.

## Authors
Pavia Bera, Jennifer Adorno, Sanjukta Bhanja

## Published
2026-06-30

## Categories
cs.NE

## Utility
1.0

## Note
This skill was automatically generated from the arXiv paper as part of the daily cron job.
