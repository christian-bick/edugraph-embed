import argparse
import os
import shutil

from huggingface_hub import HfApi, HfFolder


def publish_model(repo_id: str, model_dir: str = "out"):
    """
    Publishes the generated model to a Hugging Face repository.

    Args:
        repo_id (str): The ID of the repository on Hugging Face Hub (e.g., "username/repo-name").
        model_dir (str): The directory containing the model files. Defaults to "out".
    """
    if not os.path.exists(model_dir):
        print(f"Error: Model directory '{model_dir}' not found.")
        print("Please run the training script to generate the model files.")
        return

    # Copy MODEL.md to README.md in the model directory
    model_readme_path = os.path.join(model_dir, "README.md")
    shutil.copy("MODEL.md", model_readme_path)
    print(f"Copied MODEL.md to {model_readme_path}")

    # Copy LICENSE to the model directory
    shutil.copy("LICENSE", os.path.join(model_dir, "LICENSE"))
    print(f"Copied LICENSE to {model_dir}/LICENSE")

    # Authenticate with Hugging Face Hub
    # Assumes the user has already logged in via `huggingface-cli login` or has set HF_TOKEN
    token = HfFolder.get_token()
    if token is None:
        print("Error: Hugging Face token not found.")
        print("Please log in using 'huggingface-cli login' or set the HF_TOKEN environment variable.")
        return

    api = HfApi()

    # Create the repository if it doesn't exist
    api.create_repo(
        repo_id=repo_id,
        repo_type="model",
        exist_ok=True,
    )
    print(f"Repository '{repo_id}' created or already exists.")

    # Upload the contents of the model directory
    print(f"Uploading contents of '{model_dir}' to '{repo_id}'...")
    api.upload_folder(
        folder_path=model_dir,
        repo_id=repo_id,
        repo_type="model",
    )
    print("Model published successfully!")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Publish a model to Hugging Face Hub.")
    parser.add_argument("repo_id", type=str, nargs='?', default="christian-bick/edugraph-embedding", help="The ID of the repository on Hugging Face Hub (e.g., 'username/repo-name').")
    args = parser.parse_args()

    publish_model(args.repo_id)
