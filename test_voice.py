import unittest
from unittest.mock import patch, MagicMock
from src.assistant.voice.recognizer import recognize_speech

class TestVoice(unittest.TestCase):

    @patch('src.assistant.voice.recognizer.sr.Recognizer.listen')
    @patch('src.assistant.voice.recognizer.sr.Recognizer.recognize_google')
    def test_recognize_speech(self, mock_recognize_google, mock_listen):
        # Simula o resultado da função recognize_google
        mock_recognize_google.return_value = "Teste de reconhecimento de fala"
        
        # Chama a função recognize_speech e verifica o resultado
        result = recognize_speech()
        self.assertEqual(result, "Teste de reconhecimento de fala")

        # Verifica se as funções mockadas foram chamadas
        mock_listen.assert_called_once()
        mock_recognize_google.assert_called_once()

if __name__ == "__main__":
    unittest.main()
