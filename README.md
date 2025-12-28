# EduGraph Embed

This project provides a model for embedding labels from the
[EduGraph ontology](https://github.com/christian-bick/edugraph-ontology). 

When combined, with an [Edugraph classification model](https://github.com/christian-bick/edugraph-classify-qwen3vl) 
we can determine skill similarity with high accuaracy between any type of learning content that is
covered by the EduGraph ontology. For example, we can determine that on a screenshot from a math
learning app the exact same set of skills that is being trained as what is being tested by a quiz
that we provide as a PDF of photo.

The embedding model determines similarity based on the structure of the ontology itself and respects 
various types of entity relationships to determine similarity in addition to semantic relations, most
importantly parent-child as well as sibling relationships.

For example, it will place related labels like IntegerAddition and FractionAddition closer together 
than let's say ShapeIdentification based on their distance within the hierarchy of math areas.

To accomplish this we are using state-of-the-art knowledge graph embedding strategies that 
map the knowledge graph structures into high dimensional vector spaces using an RGCN.

## Ontology

This project is centered around the EduGraph ontolog which is automatically retrieved from the 
[ontology repository](https://github.com/christian-bick/edugraph-ontology) during model generation.

The emedding model is trained on the entities and relationships in this model. It can only embed
labels that are defined a entities within this ontology.

## Getting Started

### Prerequisites

*   Python >= 3.13
*   [UV](https://astral.sh/blog/uv) for build & dependency management
*   Updated CUDA drivers

### Installation

1. Install the dependencies using uv:
    ```bash
    uv sync
    ```

3.  Set up the environment variables by copying the `.env.example` file to `.env` and filling in the required values:
    ```bash
    cp .env.example .env
    ```

## Usage

To train the embeddings model, run the following command:

```bash
uv run src.edugraph.models.embeddings.entity_embeddings_train
```

This script will:
1.  Download the ontology from the specified URL.
2.  Build a PyTorch Geometric graph from the ontology.
3.  Train an RGCN model.
4.  Export the trained model to ONNX format (`out/embed_entities_biased.onnx` and `out/embed_entities_neutral.onnx`) and save the inference data (`out/embed_entities_text.pt`).

## Contributing

Contributions are welcome!

Ideally always open an issue first to make sure your contribution aligns with the project's scope.

Also please make sure to add tests with your contribution and to only submit PRs with green tests.

Please be aware that you need to sign a contributor agreement that allows us to relicense
your contribution under other terms _in addition_ to the AGPL license. We aim for a balanced 
approach between open source availability and project viability. Being able to redistribute 
your contributions under other licenses as well is what helps us accomplish that goal.

## License

This project is licensed under the GNU AFFERO GENERAL PUBLIC LICENSE. See the [LICENSE](LICENSE) file for details.

If these license terms are not working for you then contact us and we can discuss alternative options.
