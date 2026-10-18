from colorama import Fore, Style, init

# Inicializa o colorama para garantir compatibilidade em diferentes terminais (Windows, Linux, macOS)
init()

# 1. Utilizando uma lista para armazenar os níveis e descrições do reservatório
niveis_reservatorio = [
    {"nivel": 1, "situacao": "Muito baixo (crítico)"},
    {"nivel": 2, "situacao": "Baixo"},
    {"nivel": 3, "situacao": "Médio"},
    {"nivel": 4, "situacao": "Alto"},
    {"nivel": 5, "situacao": "Muito alto (alerta)"},
]


def definir_cor_mensagem(nivel):
  """3. Função responsável por definir e retornar a cor da mensagem

  conforme o nível informado.
  """
  if nivel == 1:
    return Fore.RED  # Vermelho para crítico
  elif nivel == 2:
    return Fore.YELLOW  # Amarelo para baixo
  elif nivel == 3:
    return Fore.GREEN  # Verde para médio
  elif nivel == 4:
    return Fore.CYAN  # Ciano para alto
  elif nivel == 5:
    return Fore.BLUE  # Azul para alerta/muito alto
  else:
    return Style.RESET_ALL


def monitorar_reservatorio():
  print("=" * 45)
  print("   SISTEMA DE MONITORAMENTO - RESERVATÓRIO DE ÁGUA")
  print("=" * 45 + "\n")

  # Percorre a lista para exibir a situação atual
  for item in niveis_reservatorio:
    nivel_atual = item["nivel"]
    situacao_atual = item["situacao"]

    # Chama a função para obter a cor correspondente
    cor = definir_cor_mensagem(nivel_atual)

    # 4 e 5. Exibe no terminal a situação com a cor e restaura o estilo padrão ao final
    print(
        f"{cor}Nível {nivel_atual} - Situação: {situacao_atual}{Style.RESET_ALL}"
    )

  print("\n" + "=" * 45)


if __name__ == "__main__":
  monitorar_reservatorio()