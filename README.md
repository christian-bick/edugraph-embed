# EduGraph Embed

This project provides a model for embedding labels from the
[EduGraph ontology](https://github.com/christian-bick/edugraph-ontology).

When combined with an [EduGraph classification model](https://github.com/christian-bick/edugraph-classify-qwen3vl),
we can determine skill similarity with high accuracy between any type of learning content
covered by the EduGraph ontology. For example, we can determine that a screenshot from a math
learning app trains the exact same set of skills tested in a quiz provided as a PDF or photo.

The embedding model determines similarity based on the structure of the ontology itself. It respects
various types of entity relationships to determine similarity, including semantic relations, and most
importantly, parent-child and sibling relationships.

For example, it will place related labels like `IntegerAddition` and `FractionAddition` closer together
than, say, `ShapeIdentification`, based on their distance within the hierarchy of math areas.

To accomplish this, we are using state-of-the-art knowledge graph embedding strategies that
map the knowledge graph structures into high-dimensional vector spaces using an RGCN.

## Ontology

This project is centered around the EduGraph ontology, which is automatically retrieved from the
[ontology repository](https://github.com/christian-bick/edugraph-ontology) during model generation.

The embedding model is trained on the entities and relationships in this ontology. It can only embed
labels that are defined as entities within this ontology.

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

2.  Set up the environment variables by copying the `.env.example` file to `.env` and filling in the required values:
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

Ideally, always open an issue first to make sure your contribution aligns with the project's scope.

Please also make sure to add tests with your contribution and to only submit PRs with green tests.

Please be aware that you need to sign a contributor agreement that allows us to relicense
your contribution under other terms _in addition_ to the AGPL license. We aim for a balanced
approach between open source availability and project viability. Being able to redistribute
contributions under other licenses helps us accomplish that goal.

## License

This project is licensed under the GNU Affero General Public License. See the [LICENSE](LICENSE) file for details.

If these license terms are not working for you, then contact us, and we can discuss alternative options.

