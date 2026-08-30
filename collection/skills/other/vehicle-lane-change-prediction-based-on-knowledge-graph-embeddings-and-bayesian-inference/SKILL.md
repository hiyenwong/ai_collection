# Vehicle Lane Change Prediction based on Knowledge Graph Embeddings and Bayesian Inference

**arXiv ID:** 2312.06336
**Authors:** M. Manzour, A. Ballardini, R. Izquierdo, M. A. Sotelo
**Published:** 2023-12-11T12:33:44Z
**Abstract:**
Prediction of vehicle lane change maneuvers has gained a lot of momentum in the last few years. Some recent works focus on predicting a vehicle's intention by predicting its trajectory first. This is not enough, as it ignores the context of the scene and the state of the surrounding vehicles (as they might be risky to the target vehicle). Other works assessed the risk made by the surrounding vehicles only by considering their existence around the target vehicle, or by considering the distance and relative velocities between them and the target vehicle as two separate numerical features. In this work, we propose a solution that leverages Knowledge Graphs (KGs) to anticipate lane changes based on linguistic contextual information in a way that goes well beyond the capabilities of current perception systems. Our solution takes the Time To Collision (TTC) with surrounding vehicles as input to assess the risk on the target vehicle. Moreover, our KG is trained on the HighD dataset using the TransE model to obtain the Knowledge Graph Embeddings (KGE). Then, we apply Bayesian inference on top of the KG using the embeddings learned during training. Finally, the model can predict lane changes two seconds ahead with 97.95% f1-score, which surpassed the state of the art, and three seconds before changing lanes with 93.60% f1-score.

## Skill Description

This skill is generated from the arXiv paper: Vehicle Lane Change Prediction based on Knowledge Graph Embeddings and Bayesian Inference (2312.06336).

## How to Use

[To be filled in by the user or by future automation]

## References

- [arXiv:2312.06336](http://arxiv.org/abs/2312.06336v1)
