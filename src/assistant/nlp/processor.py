import json
import random
from pathlib import Path
from difflib import SequenceMatcher

# Carrega intents do arquivo JSON
with open(Path(__file__).parent.parent.parent / 'data/intents.json', 'r', encoding='utf-8') as file:
    intents = json.load(file)["intents"]

def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()

def process_command(command):
    command = command.lower().strip()  # Normaliza o comando para minúsculas e remove espaços desnecessários
    print(f"Processando comando: {command}")  # Debug: Verificar o comando que está sendo processado

    highest_similarity = 0.0
    best_response = None
    best_intent_tag = None

    for intent in intents:
        for pattern in intent["patterns"]:
            pattern = pattern.lower()
            similarity = similar(command, pattern)
            print(f"Comparando '{command}' com padrão '{pattern}': Similaridade = {similarity}")  # Debug

            if similarity > highest_similarity and similarity > 0.7:  # Limite de similaridade ajustado
                highest_similarity = similarity
                best_intent_tag = intent["tag"]
                # Verifica se há uma resposta específica para o padrão mais próximo
                if pattern == command:
                    best_response = random.choice(intent["responses"])
                else:
                    best_response = random.choice(intent["responses"])

    # Caso a similaridade não seja suficiente, usar uma resposta padrão
    if best_response is None:
        best_response = "Desculpe, não entendi o que você quis dizer."

    print(f"Intenção encontrada: {best_intent_tag} com similaridade {highest_similarity}")  # Debug
    print(f"Resposta escolhida: {best_response}")  # Debug: Verificar resposta escolhida
    return best_response
