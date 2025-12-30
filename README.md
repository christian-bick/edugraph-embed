# EduGraph Embed

This project trains a model for embedding labels from the
[EduGraph ontology](https://github.com/christian-bick/edugraph-ontology).

The trained model is made available on [Huggingface](https://huggingface.co/christian-bick/edugraph-embedding).

## About

When combined with an [EduGraph Classification Model](https://github.com/christian-bick/edugraph-classify-qwen3vl),
we can determine similarity between any type of learning content covered by the EduGraph ontology. 
For example, in tandem, the two models can determine whether some content of a math learning app 
trains the exact same set of skills tested in a paper quiz, by providing nothing else than a screenshot 
and a photo.

The embedding model we train here determines similarity based on the *structure* of the EduGraph Ontology. It respects
various types of entity relationships to determine similarity, most importantly, parent-child and sibling 
relationships within the graph in addition to the semantic similarity of their definitions.

For example, the trained model will reliably place labels like `IntegerAddition` and `FractionAddition` 
closer together than, say, `ShapeIdentification`.

To accomplish this, the model is trained to generate knowledge graph embeddings that
map the ontology structure into a high-dimensional vector space using a 
[Relational Graph Convolutional Network (R-GCN)](https://arxiv.org/abs/1703.06103).

## Ontology

This model is centered around the EduGraph ontology, which is automatically retrieved from the
[ontology repository](https://github.com/christian-bick/edugraph-ontology) during model generation.

The embedding model is trained on the entities and relationships in this ontology. Consequently, 
it can only embed labels that are defined as entities within this ontology.

## Getting Started

### Prerequisites

*   Python >= 3.13
*   [UV](https://astral.sh/blog/uv) for build & dependency management
*   Updated CUDA drivers

### Installation

Install the dependencies using uv:
```bash
uv sync
```

## Usage

### Train

To train the embedding model, run the following command:

```bash
uv run src/edugraph/embed/entity_embeddings_train.py
```

This script will:
1.  Download the ontology from the repository.
2.  Build a PyTorch Geometric graph from the ontology.
3.  Train an RGCN model.
4.  Export the trained model to ONNX format (`out/embed_entities_biased.onnx` and `out/embed_entities_neutral.onnx`) and save the inference data (`out/embed_entities_text.pt`).

### Publish

To publish the model on huggingface:

1.  **Log in to Hugging Face Hub:**
    You need to authenticate with your Hugging Face account. You can do this by running the following command and entering your Hugging Face token:
    ```bash
    huggingface-cli login
    ```

2.  **Run the publishing script:**
    The `publish_model.py` script will upload the trained model in the `out` directory to a Hugging Face model repository.
    
    To publish to the repository, run:
    ```bash
    uv run src/edugraph/publish_model.py your-username/your-repo-name
    ```

## Contributing

Contributions are welcome!

Ideally, **always open a Github issue** first to make sure your contribution aligns with the project's scope.

Please also make sure to add tests with your contribution and to only submit PRs with green tests.

Please be aware that you need to sign a contributor agreement that allows us to relicense
your contribution under other terms _in addition_ to the AGPL license. We aim for a balanced
approach between open source availability and project viability. Being able to redistribute
contributions under other licenses helps us accomplish that goal.

## License

This project is licensed under the GNU Affero General Public License. See the [LICENSE](LICENSE) file for details.

If these license terms are not working for you, then contact us, and we can discuss alternative options.
