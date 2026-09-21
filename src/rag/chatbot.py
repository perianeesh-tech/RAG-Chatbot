from llama_index.core import Settings, SimpleDirectoryReader, VectorStoreIndex
from llama_index.core.prompts import RichPromptTemplate
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.llms.ollama import Ollama


def load_data():
    while True:
        choice = input(
            "Do you want to load data from a directory or a file? (d/f): "
        )

        if choice == "d":
            while True:
                try:
                    directory = input("Enter the directory path: ").strip('"')
                    documents = SimpleDirectoryReader(
                        input_dir = directory
                    ).load_data()
                    return documents
                except ValueError:
                    print("Directory not found. Please try again.")

        elif choice == "f":
            while True:
                try:
                    file_path = input("Enter the file path: ").strip('"')
                    documents = SimpleDirectoryReader(
                        input_files = [file_path]
                    ).load_data()
                    return documents
                except ValueError:
                    print("File not found. Please try again.")

        else:
            print("Invalid input. Please enter 'd' or 'f'.")


def create_query_engine(documents):
    print("Creating index...")

    index = VectorStoreIndex.from_documents(documents)

    template = RichPromptTemplate(
        """
You are an intelligent chatbot who only uses the available context
and does not make up any new information to answer the question.

Do not give ambiguous answers. If you don't know the answer,
say "I don't know". But if the answer is in the context,
answer the question as accurately as possible. Do not answer questions that 
are not related to the context.

Context:
{{context_str}}

Question:
{{query_str}}

Answer:
"""
    )

    print("Creating query engine...")

    query_engine = index.as_query_engine()

    query_engine.update_prompts(
        {"response_synthesizer:text_qa_template": template}
    )

    return query_engine


def chat(query_engine):
    while True:
        choice = input("Do you want to ask a question? (y/n): ")

        if choice == "y":
            question = input(
                "Ask me anything about the loaded data: "
            )
            answer = query_engine.query(question)
            print(answer.response)

        elif choice == "n":
            print("Goodbye!")
            break

        else:
            print("Invalid input. Please enter 'y' or 'n'.")


def main():
    print("Loading modules...")

    embedding_model = HuggingFaceEmbedding(
        model_name="BAAI/bge-small-en-v1.5"
    )

    Settings.embed_model = embedding_model

    language_model = Ollama(
        model="qwen2.5:1.5b-instruct",
        request_timeout=300.0,
    )

    Settings.llm = language_model

    print("Loading data...")
    documents = load_data()

    query_engine = create_query_engine(documents)

    chat(query_engine)


if __name__ == "__main__":
    main()