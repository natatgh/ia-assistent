
# Assistente IA

Um assistente de IA básico que utiliza reconhecimento de fala, síntese de fala e processamento de linguagem natural para executar tarefas simples.

## Configuração

1. **Crie um ambiente virtual**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # ou venv\Scripts\activate no Windows
   ```

2. **Instale as dependências**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Execute o assistente**:
   ```bash
   python src/main.py
   ```

## Estrutura do Projeto

```plaintext
assistente_ia/
│
├── README.md
├── requirements.txt
├── .gitignore
│
├── config/
│   └── settings.py
│
├── data/
│   └── intents.json
│
├── src/
│   ├── main.py
│   ├── assistant/
│   │   ├── __init__.py
│   │   ├── voice/
│   │   │   ├── __init__.py
│   │   │   ├── recognizer.py
│   │   │   └── synthesizer.py
│   │   ├── nlp/
│   │   │   ├── __init__.py
│   │   │   └── processor.py
│   │   └── actions/
│   │       ├── __init__.py
│   │       └── task_manager.py
└── tests/
    ├── __init__.py
    ├── test_voice.py
    ├── test_nlp.py
```

## Como Contribuir

1. **Faça um fork do repositório**.
2. **Crie uma branch para a sua feature** (`git checkout -b minha-feature`).
3. **Faça commit das suas alterações** (`git commit -am 'Adiciona nova feature'`).
4. **Faça push para a branch** (`git push origin minha-feature`).
5. **Abra um Pull Request**.

## Licença

Este projeto está sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.
