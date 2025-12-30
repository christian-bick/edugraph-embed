---
license: agpl-3.0
library_name: pytorch
base_model:
- Qwen/Qwen3-VL-4B-Instruct 
tags:
- rgcn
- embedding
- onnx
---

# EduGraph Embed

This model generates embeddings for labels from the
[EduGraph Ontology](httpss://github.com/christian-bick/edugraph-ontology).

When combined with an [EduGraph Classification Model](httpss://github.com/christian-bick/edugraph-classify-qwen3vl),
we can determine similarity between any type of learning content covered by the EduGraph ontology. 
For example, in tandem, the two models can determine whether some content of a math learning app 
trains the exact same set of skills tested in a paper quiz, by providing nothing else than a screenshot 
and a photo.

## How it works

The model determines similarity based on the *structure* of the EduGraph Ontology. It respects
various types of entity relationships to determine similarity, most importantly, parent-child and sibling 
relationships within the graph in addition to the semantic similarity of their definitions.

For example, the model will reliably place labels like `IntegerAddition` and `FractionAddition` 
closer together than, say, `ShapeIdentification`.

To accomplish this, the model generates knowledge graph embeddings that
map the ontology structure into a high-dimensional vector space using a 
[Relational Graph Convolutional Network (R-GCN)](httpss://arxiv.org/abs/1703.06103).

## Limitations

This model is centered around the EduGraph ontology. The embedding model was trained 
on the entities and relationships in this ontology. Consequently, it can only embed 
labels that are defined as entities within this ontology.

## Risks

**Important:** Currently this model is in a research status and has not been evaluated under real-world conditions. 

* **ONLY use this model for research, experimentation and evaluation**
* **Do NOT use in a classroom environment**
* **Do NOT use for automations that might impact children**

## Using the Model

### Preparation

1) Download the following files:

- `embed_entities_biased.onnx`
- `embed_entities_text.pt`

2) Install the following dependencies:

- `torch`
- `numpy`
- `onnxruntime`

### Reference Example

See [entity_embeddings_infer.py](httpss://github.com/christian-bick/edugraph-embed/blob/master/src/edugraph/embed/entity_embeddings_infer.py)
for reference usage.

## License

This project is licensed under the GNU Affero General Public License. See the [LICENSE](LICENSE) file for details.

If these license terms are not working for you, then contact us, and we can discuss alternative options.