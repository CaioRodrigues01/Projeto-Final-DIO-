"""
Testes unitários para os comandos /trilha, /desafio e /certificado.
Aluno de referência: Carlos Mendes | Tecnologia: Java
Cobertura alvo: >= 70%
"""

import os
import sys
import unittest
from datetime import date
from unittest.mock import patch

# Garante que o módulo seja importável sem instalação
sys.path.insert(0, os.path.dirname(__file__))

import dio_commands as cmd

# Caminho absoluto para o JSON real
DATA_PATH = os.path.join(os.path.dirname(__file__), "..", "data", "trilhas_dio.json")


# ---------------------------------------------------------------------------
# Helpers de fixture
# ---------------------------------------------------------------------------

def _trilha_java():
    """Retorna os dados esperados para a trilha Java."""
    return {
        "id": 2,
        "nome": "Formação Java Developer",
        "tecnologia": "Java",
        "nivel": "Intermediário",
        "numero_de_modulos": 12,
        "xp_total": 7200,
        "badges_disponiveis": [
            "Java Fundamentos",
            "POO com Java",
            "Spring Boot Expert",
            "Java Developer",
        ],
        "vitalicio": True,
        "lives_ao_vivo": [
            {"titulo": "Spring Boot na Prática", "data": "2025-08-20", "duracao_minutos": 120},
            {"titulo": "Microsserviços com Java e Docker", "data": "2025-09-18", "duracao_minutos": 90},
            {"titulo": "Java e AWS: Deploy na Nuvem", "data": "2025-10-02", "duracao_minutos": 60},
        ],
        "promocoes": {
            "desconto_percentual": 15,
            "cupom": "JAVA15",
            "validade": "2025-10-15",
        },
    }


# ===========================================================================
# Testes — _load_trilhas
# ===========================================================================

class TestLoadTrilhas(unittest.TestCase):
    """Verifica o carregamento do JSON."""

    def test_retorna_lista(self):
        trilhas = cmd._load_trilhas(DATA_PATH)
        self.assertIsInstance(trilhas, list)

    def test_lista_nao_vazia(self):
        trilhas = cmd._load_trilhas(DATA_PATH)
        self.assertGreater(len(trilhas), 0)

    def test_cada_item_tem_campos_obrigatorios(self):
        campos = {"id", "nome", "tecnologia", "nivel", "numero_de_modulos",
                  "xp_total", "badges_disponiveis", "promocoes", "vitalicio", "lives_ao_vivo"}
        for trilha in cmd._load_trilhas(DATA_PATH):
            with self.subTest(trilha=trilha["nome"]):
                self.assertTrue(campos.issubset(trilha.keys()))

    def test_arquivo_inexistente_lanca_erro(self):
        with self.assertRaises(FileNotFoundError):
            cmd._load_trilhas("/caminho/inexistente/trilhas.json")


# ===========================================================================
# Testes — _find_trilha
# ===========================================================================

class TestFindTrilha(unittest.TestCase):
    """Verifica a busca de trilha por tecnologia."""

    def test_encontra_java_case_insensitive_maiusculo(self):
        trilha = cmd._find_trilha("JAVA", DATA_PATH)
        self.assertIsNotNone(trilha)
        self.assertEqual(trilha["tecnologia"], "Java")

    def test_encontra_java_case_insensitive_minusculo(self):
        trilha = cmd._find_trilha("java", DATA_PATH)
        self.assertIsNotNone(trilha)
        self.assertEqual(trilha["tecnologia"], "Java")

    def test_encontra_java_exato(self):
        trilha = cmd._find_trilha("Java", DATA_PATH)
        self.assertIsNotNone(trilha)

    def test_retorna_none_para_tecnologia_inexistente(self):
        trilha = cmd._find_trilha("COBOL", DATA_PATH)
        self.assertIsNone(trilha)

    def test_campos_da_trilha_java(self):
        trilha = cmd._find_trilha("Java", DATA_PATH)
        esperado = _trilha_java()
        self.assertEqual(trilha["id"], esperado["id"])
        self.assertEqual(trilha["nome"], esperado["nome"])
        self.assertEqual(trilha["nivel"], esperado["nivel"])
        self.assertEqual(trilha["numero_de_modulos"], esperado["numero_de_modulos"])
        self.assertEqual(trilha["xp_total"], esperado["xp_total"])


# ===========================================================================
# Testes — _available_technologies
# ===========================================================================

class TestAvailableTechnologies(unittest.TestCase):

    def test_retorna_lista_de_strings(self):
        techs = cmd._available_technologies(DATA_PATH)
        self.assertIsInstance(techs, list)
        self.assertTrue(all(isinstance(t, str) for t in techs))

    def test_contem_java(self):
        techs = cmd._available_technologies(DATA_PATH)
        self.assertIn("Java", techs)

    def test_pelo_menos_dez_tecnologias(self):
        techs = cmd._available_technologies(DATA_PATH)
        self.assertGreaterEqual(len(techs), 10)


# ===========================================================================
# Testes — comando_trilha (/trilha)
# ===========================================================================

class TestComandoTrilha(unittest.TestCase):
    """Testa o comando /trilha com foco na trilha Java."""

    # --- Caminho feliz ---

    def test_status_ok_para_java(self):
        resultado = cmd.comando_trilha("Java", DATA_PATH)
        self.assertEqual(resultado["status"], "ok")

    def test_retorna_nome_correto(self):
        resultado = cmd.comando_trilha("Java", DATA_PATH)
        self.assertEqual(resultado["nome"], "Formação Java Developer")

    def test_retorna_tecnologia_java(self):
        resultado = cmd.comando_trilha("Java", DATA_PATH)
        self.assertEqual(resultado["tecnologia"], "Java")

    def test_nivel_intermediario(self):
        resultado = cmd.comando_trilha("Java", DATA_PATH)
        self.assertEqual(resultado["nivel"], "Intermediário")

    def test_numero_de_modulos(self):
        resultado = cmd.comando_trilha("Java", DATA_PATH)
        self.assertEqual(resultado["numero_de_modulos"], 12)

    def test_xp_total(self):
        resultado = cmd.comando_trilha("Java", DATA_PATH)
        self.assertEqual(resultado["xp_total"], 7200)

    def test_badges_disponiveis(self):
        resultado = cmd.comando_trilha("Java", DATA_PATH)
        self.assertIn("Java Developer", resultado["badges_disponiveis"])
        self.assertIn("Spring Boot Expert", resultado["badges_disponiveis"])

    def test_vitalicio_true(self):
        resultado = cmd.comando_trilha("Java", DATA_PATH)
        self.assertTrue(resultado["vitalicio"])

    def test_lives_ao_vivo_tres_lives(self):
        resultado = cmd.comando_trilha("Java", DATA_PATH)
        self.assertEqual(len(resultado["lives_ao_vivo"]), 3)

    def test_promocao_desconto(self):
        resultado = cmd.comando_trilha("Java", DATA_PATH)
        self.assertEqual(resultado["promocao"]["desconto_percentual"], 15)

    def test_promocao_cupom(self):
        resultado = cmd.comando_trilha("Java", DATA_PATH)
        self.assertEqual(resultado["promocao"]["cupom"], "JAVA15")

    def test_case_insensitive_java_minusculo(self):
        resultado = cmd.comando_trilha("java", DATA_PATH)
        self.assertEqual(resultado["status"], "ok")

    # --- Caminho triste ---

    def test_tecnologia_inexistente_status_not_found(self):
        resultado = cmd.comando_trilha("COBOL", DATA_PATH)
        self.assertEqual(resultado["status"], "not_found")

    def test_tecnologia_inexistente_lista_disponiveis(self):
        resultado = cmd.comando_trilha("COBOL", DATA_PATH)
        self.assertIn("tecnologias_disponiveis", resultado)
        self.assertIn("Java", resultado["tecnologias_disponiveis"])

    def test_tecnologia_inexistente_mensagem(self):
        resultado = cmd.comando_trilha("COBOL", DATA_PATH)
        self.assertIn("COBOL", resultado["mensagem"])


# ===========================================================================
# Testes — comando_desafio (/desafio)
# ===========================================================================

class TestComandoDesafio(unittest.TestCase):
    """Testa o comando /desafio com foco em Java Intermediário."""

    # --- Caminho feliz ---

    def test_status_ok_java_intermediario(self):
        resultado = cmd.comando_desafio("Java", "Intermediário", DATA_PATH)
        self.assertEqual(resultado["status"], "ok")

    def test_tecnologia_retornada_correta(self):
        resultado = cmd.comando_desafio("Java", "Intermediário", DATA_PATH)
        self.assertEqual(resultado["tecnologia"], "Java")

    def test_nivel_retornado_correto(self):
        resultado = cmd.comando_desafio("Java", "Intermediário", DATA_PATH)
        self.assertEqual(resultado["nivel"], "Intermediário")

    def test_enunciado_nao_vazio(self):
        resultado = cmd.comando_desafio("Java", "Intermediário", DATA_PATH)
        self.assertTrue(len(resultado["enunciado"]) > 0)

    def test_enunciado_pertence_ao_banco(self):
        resultado = cmd.comando_desafio("Java", "Intermediário", DATA_PATH)
        self.assertIn(resultado["enunciado"], cmd.DESAFIOS_POR_NIVEL["Intermediário"])

    def test_numero_desafio_dentro_do_range(self):
        resultado = cmd.comando_desafio("Java", "Intermediário", DATA_PATH)
        self.assertGreaterEqual(resultado["numero_desafio"], 1)
        self.assertLessEqual(resultado["numero_desafio"], 999)

    def test_xp_dentro_do_range_intermediario(self):
        resultado = cmd.comando_desafio("Java", "Intermediário", DATA_PATH)
        self.assertGreaterEqual(resultado["xp"], 300)
        self.assertLessEqual(resultado["xp"], 600)

    def test_tempo_dentro_do_range_intermediario(self):
        resultado = cmd.comando_desafio("Java", "Intermediário", DATA_PATH)
        self.assertGreaterEqual(resultado["tempo_sugerido_minutos"], 30)
        self.assertLessEqual(resultado["tempo_sugerido_minutos"], 60)

    def test_nivel_basico_xp_range(self):
        resultado = cmd.comando_desafio("Java", "Básico", DATA_PATH)
        self.assertEqual(resultado["status"], "ok")
        self.assertGreaterEqual(resultado["xp"], 100)
        self.assertLessEqual(resultado["xp"], 300)

    def test_nivel_avancado_xp_range(self):
        resultado = cmd.comando_desafio("Java", "Avançado", DATA_PATH)
        self.assertEqual(resultado["status"], "ok")
        self.assertGreaterEqual(resultado["xp"], 600)
        self.assertLessEqual(resultado["xp"], 1200)

    def test_case_insensitive_nivel(self):
        resultado = cmd.comando_desafio("Java", "intermediário", DATA_PATH)
        self.assertEqual(resultado["status"], "ok")
        self.assertEqual(resultado["nivel"], "Intermediário")

    # --- Caminhos tristes ---

    def test_tecnologia_inexistente(self):
        resultado = cmd.comando_desafio("COBOL", "Básico", DATA_PATH)
        self.assertEqual(resultado["status"], "not_found")

    def test_nivel_invalido(self):
        resultado = cmd.comando_desafio("Java", "Expert", DATA_PATH)
        self.assertEqual(resultado["status"], "nivel_invalido")

    def test_nivel_invalido_lista_validos(self):
        resultado = cmd.comando_desafio("Java", "Expert", DATA_PATH)
        self.assertIn("niveis_validos", resultado)
        self.assertIn("Intermediário", resultado["niveis_validos"])


# ===========================================================================
# Testes — _gerar_codigo_certificado
# ===========================================================================

class TestGerarCodigoCertificado(unittest.TestCase):

    def test_formato_correto(self):
        hoje = date(2025, 7, 15)
        codigo = cmd._gerar_codigo_certificado(hoje)
        self.assertTrue(codigo.startswith("DIO-20250715-"))

    def test_sufixo_quatro_digitos(self):
        hoje = date(2025, 7, 15)
        codigo = cmd._gerar_codigo_certificado(hoje)
        sufixo = codigo.split("-")[-1]
        self.assertEqual(len(sufixo), 4)
        self.assertTrue(sufixo.isdigit())

    def test_unicidade_provavel(self):
        hoje = date(2025, 7, 15)
        codigos = {cmd._gerar_codigo_certificado(hoje) for _ in range(50)}
        # Com 9000 possibilidades, é altamente provável obter pelo menos 2 únicos em 50 tentativas
        self.assertGreater(len(codigos), 1)

    def test_usa_data_atual_por_padrao(self):
        hoje = date.today()
        codigo = cmd._gerar_codigo_certificado()
        esperado_prefixo = f"DIO-{hoje.strftime('%Y%m%d')}-"
        self.assertTrue(codigo.startswith(esperado_prefixo))


# ===========================================================================
# Testes — comando_certificado (/certificado)
# ===========================================================================

class TestComandoCertificado(unittest.TestCase):
    """Testa o comando /certificado para Carlos Mendes / Java."""

    HOJE = date(2025, 7, 20)
    NOME = "Carlos Mendes"

    def _gerar(self, nome=None, tech="Java"):
        return cmd.comando_certificado(
            nome or self.NOME, tech, DATA_PATH, hoje=self.HOJE
        )

    # --- Caminho feliz ---

    def test_status_ok(self):
        self.assertEqual(self._gerar()["status"], "ok")

    def test_nome_usuario_preservado(self):
        resultado = self._gerar()
        self.assertEqual(resultado["nome_usuario"], "Carlos Mendes")

    def test_nome_trilha_correto(self):
        resultado = self._gerar()
        self.assertEqual(resultado["nome_trilha"], "Formação Java Developer")

    def test_tecnologia_correta(self):
        resultado = self._gerar()
        self.assertEqual(resultado["tecnologia"], "Java")

    def test_nivel_correto(self):
        resultado = self._gerar()
        self.assertEqual(resultado["nivel"], "Intermediário")

    def test_numero_de_modulos(self):
        resultado = self._gerar()
        self.assertEqual(resultado["numero_de_modulos"], 12)

    def test_xp_total(self):
        resultado = self._gerar()
        self.assertEqual(resultado["xp_total"], 7200)

    def test_badges_presentes(self):
        resultado = self._gerar()
        self.assertIn("Java Developer", resultado["badges"])

    def test_lives_participadas(self):
        resultado = self._gerar()
        self.assertEqual(resultado["lives_participadas"], 3)

    def test_vitalicio(self):
        resultado = self._gerar()
        self.assertTrue(resultado["vitalicio"])

    def test_data_emissao_formatada(self):
        resultado = self._gerar()
        self.assertEqual(resultado["data_emissao"], "20/07/2025")

    def test_codigo_certificado_formato(self):
        resultado = self._gerar()
        codigo = resultado["codigo_certificado"]
        self.assertTrue(codigo.startswith("DIO-20250720-"))

    def test_nome_case_sensitive_preservado(self):
        resultado = self._gerar(nome="CARLOS MENDES")
        self.assertEqual(resultado["nome_usuario"], "CARLOS MENDES")

    def test_case_insensitive_tecnologia(self):
        resultado = self._gerar(tech="java")
        self.assertEqual(resultado["status"], "ok")

    # --- Caminho triste ---

    def test_tecnologia_inexistente_not_found(self):
        resultado = self._gerar(tech="COBOL")
        self.assertEqual(resultado["status"], "not_found")

    def test_tecnologia_inexistente_lista_disponiveis(self):
        resultado = self._gerar(tech="COBOL")
        self.assertIn("Java", resultado["tecnologias_disponiveis"])


# ===========================================================================
# Ponto de entrada
# ===========================================================================

if __name__ == "__main__":
    unittest.main(verbosity=2)
