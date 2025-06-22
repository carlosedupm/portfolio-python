# AI Development Assistant Rules

## 🎯 Objetivo
Este documento define as diretrizes que devem ser seguidas por qualquer agente de IA que me auxilie no desenvolvimento deste projeto. O foco é melhorar minha produtividade sem comprometer qualidade, clareza ou boas práticas.

---

## ⚙️ Perfil do Desenvolvedor
- Desenvolvedor experiente em Java e Next.js
- Aprendendo Python com foco em:
  - Automação/Scripting
  - Backend com FastAPI

---

## 🧠 Como você (IA) deve me ajudar

1. **Explique como e por que**, não só o "o quê".
2. Evite sugestões automáticas sem contexto: **confirme antes se for ambíguo.**
3. Quando sugerir código:
   - Explique cada trecho em até 3 linhas abaixo do bloco.
   - Siga os padrões definidos abaixo.
4. Proponha melhorias ou refatorações se o código estiver repetitivo ou complexo.
5. Sugira testes automatizados com `pytest` sempre que possível.
6. Sempre prefira soluções claras a "clever hacks".

---

## 🧩 Linguagens e Ferramentas Usadas
- Python 3.12+
- FastAPI para APIs
- `schedule`, `os`, `pathlib`, `requests` para automações
- Docker Dev Containers
- GitHub para versionamento
- VS Code com `.devcontainer`

---

## 📦 Organização dos projetos
Cada projeto deve conter:
- `.devcontainer/`
- `README.md`
- `requirements.txt`
- `src/` com os arquivos Python
- Scripts com `argparse` para execução CLI

---

## 📐 Padrões de código
- Seguir a [PEP8](https://peps.python.org/pep-0008/) com black + isort
- Tipagem com `typing`
- Testes com `pytest`
- Nomes de variáveis devem ser descritivos e em snake_case
- Documentação de funções usando docstrings padrão Google

Exemplo:
```python
def process_data(file_path: str) -> List[str]:
    """Processa os dados de um arquivo e retorna uma lista de strings."""
    ...
