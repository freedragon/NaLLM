import openai
from embedding.base_embedding import BaseEmbedding


class AzureOpenAIEmbedding(BaseEmbedding):
    """Wrapper around OpenAI embedding models."""

    def __init__(
        self,
        azure_openai_api_key: str,
        azure_openai_api_endpoint: str,
        model_name: str = "text-embedding-ada-002"
    ) -> None:
        # openai.api_key = openai_api_key
        self.client = AzureOpenAI(
            api_key=azure_openai_api_key,  
            azure_endpoint=azure_openai_api_endpoint,
            api_version=azure_openai_api_version)
        self.model = model_name

    def generate(
        self,
        input: str,
    ) -> str:
        # embedding = openai.Embedding.create(input=input, model=self.model)
        embedding = client.embeddings.create(input=input, model=selfmodel)
        return embedding["data"][0]["embedding"]
