# 2026-05-29: Dynamic Entanglement Packet Scheduling

## Paper: arxiv:2605.28795 (IEEE QuNAP 2026 / INFOCOM 2026)

### Abstract
Sharing entanglement among multiple users remains a central challenge for scalable quantum networks. An on-demand entanglement packet architecture uses TDMA for periodic scheduling, but static schedules offer limited flexibility when outcomes are stochastic and arrivals are asynchronous. The proposed online scheduler dynamically schedules, defers, retries, or drops entanglement distribution reservations.

### Results
- Dynamic scheduler achieves lower completion time than static baseline
- Higher completion ratio and throughput
- Under overload: continues to construct deadline-feasible schedules and degrades gracefully
- Static baseline degrades catastrophically under overload

### Systems Engineering Connection
This paper applies classical real-time scheduling theory (EDF, online scheduling) to quantum network resource allocation — a prime example of systems engineering principles applied to quantum infrastructure.
