# Teste_Software_Mutantes_2024_Silva_Bruno

Projeto desenvolvido para a atividade 2 da Disciplina de Teste de Software.

A atividade planeja cobrir assunto relacionados a mutações e cobertura de testes.

## Projeto Base

 - minimal-pytest-project - https://github.com/maet3608/minimal-pytest-project.git

## Vídeo de demonstração

 - https://drive.google.com/file/d/1Skw_jFWckp0Rrb6mhgd5DV6OkGp-c838/view?usp=sharing

## Requisitos

- Python 3.7 ou superior
- python3-venv
- pytest
- pytest-cov
- mutmut

## Instalação

1. Clonando repositório:

```bash
git clone https://github.com/macedobruno/Teste_Software_Mutantes_2024_Silva_Bruno.git
```

2. Preparando ambiente virtual

```bash
pip install python3-venv
python -m venv Teste_Software_Mutantes_2024_Silva_Bruno/
cd Teste_Software_Mutantes_2024_Silva_Bruno
source bin/activate
```

3. Instalando dependências

```bash
pip install -r requirements.txt
python minimal-pytest-project-master/setup.py install
```

## Execução

1. Testes iniciais

```bash
cd minimal-pytest-project-master/
pytest -v tests/test_calculator.py
```

2. Verificar cobertura de testes

```bash
pytest -vv tests/test_calculator.py --cov
```

3. Gerar relatório de cobertura de testes

```bash
pytest -vv tests/test_calculator.py --cov --cov-report html
```

4. Executar testes usando mutmut

```bash
mutmut run --paths-to-mutate=mymath/calculator.py
```

5. Verificar resultado de mutantes sobreviventes

```bash
mutmut results
```

6. Verificar mutação sobrevivente por id

```bash
mutmut show <id>
```

7. Gerar relatório de mutações sobreviventes

```bash
mutmut html
```