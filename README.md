# RAG-Chatbot

A RAG (Retrieval-Augmented Generation) based chatbot system using Neo4j, FastAPI, and Streamlit.

## Prerequisites

- Python 3.8+
- Docker Desktop
- OpenAI API Key
- Git

## Installation and Setup

1. Clone the repository
```bash
git clone https://github.com/TahirRida/RAG-Chatbot
cd RAG-Chatbot
```

2. Create and activate a virtual environment
```bash
python -m venv venv
./venv/Scripts/activate  # On Windows
source venv/bin/activate  # On Unix or MacOS
```

3. Install required packages
```bash
pip install -r requirements.txt
```

4. Create a `.env` file in the root directory with the following content:
```env
OPENAI_API_KEY="Enter your OpenAI API Key"

# Neo4j Configuration
NEO4J_URI=bolt://localhost:7687
NEO4J_USERNAME=neo4j
NEO4J_PASSWORD=password

# Data Source Paths
HOSPITALS_CSV_PATH=https://raw.githubusercontent.com/hfhoffman1144/langchain_neo4j_rag_app/main/data/hospitals.csv
PAYERS_CSV_PATH=https://raw.githubusercontent.com/hfhoffman1144/langchain_neo4j_rag_app/main/data/payers.csv
PHYSICIANS_CSV_PATH=https://raw.githubusercontent.com/hfhoffman1144/langchain_neo4j_rag_app/main/data/physicians.csv
PATIENTS_CSV_PATH=https://raw.githubusercontent.com/hfhoffman1144/langchain_neo4j_rag_app/main/data/patients.csv
VISITS_CSV_PATH=https://raw.githubusercontent.com/hfhoffman1144/langchain_neo4j_rag_app/main/data/visits.csv
REVIEWS_CSV_PATH=https://raw.githubusercontent.com/hfhoffman1144/langchain_neo4j_rag_app/main/data/reviews.csv

# Model Configuration
HOSPITAL_AGENT_MODEL=gpt-3.5-turbo-1106
HOSPITAL_CYPHER_MODEL=gpt-3.5-turbo-1106
HOSPITAL_QA_MODEL=gpt-3.5-turbo-0125

# Service URLs
CHATBOT_URL=http://host.docker.internal:8000/hospital-rag-agent
```

> **Note**: Make sure to update the `OPENAI_API_KEY` with your actual API key.

## Setting up Neo4j

1. Start the Neo4j container with APOC plugin:
```bash
docker run --name neo4j-apoc \
  -e NEO4J_AUTH=neo4j/password \
  -p 7474:7474 -p 7687:7687 \
  -e NEO4J_apoc_export_file_enabled=true \
  -e NEO4J_apoc_import_file_enabled=true \
  -e NEO4J_apoc_import_file_use_neo4j_config=true \
  -e NEO4J_PLUGINS='["apoc"]' \
  -e NEO4J_dbms_security_procedures_unrestricted=apoc.* \
  -e NEO4J_dbms_security_procedures_allowlist=apoc.* \
  neo4j:latest
```

2. Install APOC Core in the Neo4j container:
   - Open Docker Desktop
   - Find the neo4j-apoc container
   - Open the container's terminal (Exec)
   - Run the following command:
```bash
cp /var/lib/neo4j/labs/apoc-5.26.0-core.jar /var/lib/neo4j/plugins/
```

## Loading Data

Navigate to the ETL directory and run the data loading script:
```bash
cd hospital_neo4j_etl/src
python hospital_bulk_csv_write.py
```

## Starting the Application

1. Start the FastAPI backend:
```bash
cd chatbot_api/src
uvicorn main:app --host 0.0.0.0 --port 8000
```

2. In a new terminal, start the Streamlit frontend:
```bash
cd chatbot_frontend/src
streamlit run main.py
```

## Accessing the Application

- Neo4j Browser: http://localhost:7474
- FastAPI Backend: http://localhost:8000
- Streamlit Frontend: http://localhost:8501

## Project Structure

```
RAG-Chatbot/
├── chatbot_api/          # FastAPI backend
├── chatbot_frontend/     # Streamlit frontend
├── chroma_data/         # Vector store data
├── data/                # Raw data files
├── hospital_neo4j_etl/  # ETL scripts
├── langchain_intro/     # LangChain setup
├── tests/              # Test files
└── requirements.txt    # Project dependencies
```
