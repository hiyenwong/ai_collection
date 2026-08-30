# Internet Explorer: Targeted Representation Learning on the Open Web

**arXiv ID:** 2302.14051
**Authors:** Alexander C. Li, Ellis Brown, Alexei A. Efros, Deepak Pathak
**Published:** 2023-02-27T18:59:55Z
**Abstract:**
Modern vision models typically rely on fine-tuning general-purpose models pre-trained on large, static datasets. These general-purpose models only capture the knowledge within their pre-training datasets, which are tiny, out-of-date snapshots of the Internet -- where billions of images are uploaded each day. We suggest an alternate approach: rather than hoping our static datasets transfer to our desired tasks after large-scale pre-training, we propose dynamically utilizing the Internet to quickly train a small-scale model that does extremely well on the task at hand. Our approach, called Internet Explorer, explores the web in a self-supervised manner to progressively find relevant examples that improve performance on a desired target dataset. It cycles between searching for images on the Internet with text queries, self-supervised training on downloaded images, determining which images were useful, and prioritizing what to search for next. We evaluate Internet Explorer across several datasets and show that it outperforms or matches CLIP oracle performance by using just a single GPU desktop to actively query the Internet for 30--40 hours. Results, visualizations, and videos at https://internet-explorer-ssl.github.io/

## Skill Description

This skill is generated from the arXiv paper: Internet Explorer: Targeted Representation Learning on the Open Web (2302.14051).

## How to Use

[To be filled in by the user or by future automation]

## References

- [arXiv:2302.14051](http://arxiv.org/abs/2302.14051v2)
