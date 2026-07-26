---
name: palmclaw-a-native-on-device-agent-framework-for-mo
description: "PalmClaw: A Native On-Device Agent Framework for Mobile Phones - Large Language Model (LLM) agents have moved beyond generating responses to executing multi-step tasks by calling tools, observing the results, and it..."
version: 1.0.0
author: Hongru Cai, Yongqi Li, Ran Wei et al.
arxiv_id: 2607.13027
created: 2026-07-14
category: other
tags: [cs.CL, cs.AI]
activation_keywords: [palmclaw, native, device, agent, framework, mobile, phones, large, language, model]
---

# PalmClaw: A Native On-Device Agent Framework for Mobile Phones

## Overview

Large Language Model (LLM) agents have moved beyond generating responses to executing multi-step tasks by calling tools, observing the results, and iteratively deciding the next action. Most agent systems run on desktops or servers, which support tool use and task automation. Mobile devices are also important agent environments because they are widely accessible and contain users' data, sensors, and daily-use applications. Existing mobile agents mainly operate smartphones through graphical user interface (GUI) actions such as tapping, swiping, and typing, which often form long, interface-dependent sequences, cannot directly access device capabilities, and make execution boundaries difficult to define. We present \textbf{PalmClaw}, an open-source agent framework that runs natively on mobile phones and manages the sessions, memory, skills, tools, and agent loop directly on the device. PalmClaw exposes device capabilities as device tools with explicit arguments, structured results, and clearly defined execution boundaries. This design enables agents to use mobile capabilities directly while keeping each action explicit and controlled. Experiments show an 11.5\% relative improvement in task success and a 94.9\% reduction in completion time over the strongest baseline, with lower setup burden and traces illustrating how execution boundaries are applied. Code is available at https://github.com/ModalityDance/PalmClaw.

## Key Insights

- TODO: Extract key insights from the paper

## Implementation Approach

- TODO: Describe how to implement the techniques from this paper

## Applications

- TODO: List potential applications

## Activation Keywords

palmclaw, native, device, agent, framework, mobile, phones, large, language, model

---
