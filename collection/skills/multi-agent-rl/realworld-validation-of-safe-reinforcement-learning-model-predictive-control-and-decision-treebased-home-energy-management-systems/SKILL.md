# Real-world validation of safe reinforcement learning, model predictive control and decision tree-based home energy management systems

**arXiv ID:** 2408.07435
**Authors:** Julian Ruddick, Glenn Ceusters, Gilles Van Kriekinge, Evgenii Genov, Cedric De Cauwer, Thierry Coosemans, Maarten Messagie
**Published:** 2024-08-14T10:12:15Z
**Abstract:**
Recent advancements in machine learning based energy management approaches, specifically reinforcement learning with a safety layer (OptLayerPolicy) and a metaheuristic algorithm generating a decision tree control policy (TreeC), have shown promise. However, their effectiveness has only been demonstrated in computer simulations. This paper presents the real-world validation of these methods, comparing against model predictive control and simple rule-based control benchmark. The experiments were conducted on the electrical installation of 4 reproductions of residential houses, which all have their own battery, photovoltaic and dynamic load system emulating a non-controllable electrical load and a controllable electric vehicle charger. The results show that the simple rules, TreeC, and model predictive control-based methods achieved similar costs, with a difference of only 0.6%. The reinforcement learning based method, still in its training phase, obtained a cost 25.5\% higher to the other methods. Additional simulations show that the costs can be further reduced by using a more representative training dataset for TreeC and addressing errors in the model predictive control implementation caused by its reliance on accurate data from various sources. The OptLayerPolicy safety layer allows safe online training of a reinforcement learning agent in the real-world, given an accurate constraint function formulation. The proposed safety layer method remains error-prone, nonetheless, it is found beneficial for all investigated methods. The TreeC method, which does require building a realistic simulation for training, exhibits the safest operational performance, exceeding the grid limit by only 27.1 Wh compared to 593.9 Wh for reinforcement learning.

## Skill Description

This skill is generated from the arXiv paper: Real-world validation of safe reinforcement learning, model predictive control and decision tree-based home energy management systems (2408.07435).

## How to Use

[To be filled in by the user or by future automation]

## References

- [arXiv:2408.07435](http://arxiv.org/abs/2408.07435v2)
