
# Assistente IA

Um assistente de IA básico que utiliza reconhecimento de fala, síntese de fala e processamento de linguagem natural para executar tarefas simples.

## Configuração

1. Crie um ambiente virtual:
   ```bash
   python -m venv venv
   source venv/bin/activate  # ou venv\Scripts\activate no Windows
   ```

2. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

3. Execute o assistente:
   ```bash
   python src/main.py
   ```

## Estrutura de Pastas

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

## Funcionalidades

- **Reconhecimento de Fala**: Utiliza a biblioteca `SpeechRecognition` para ouvir comandos de voz.
- **Síntese de Fala**: Utiliza `pyttsx3` para converter texto em fala.
- **Processamento de Linguagem Natural**: Utiliza intents definidas em um arquivo JSON para entender e responder a comandos.

## Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues e pull requests.

## Licença

Este projeto está sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.
