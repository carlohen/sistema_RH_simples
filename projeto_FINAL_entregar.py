def exibir_separador():
    print("-" * 80)

def exibir_titulo(titulo):
    exibir_separador()
    print(titulo.center(80).upper())
    exibir_separador()

def cadastrar_cargo():
    nome_cargo = input("Digite o nome do cargo: ")
    try:
        salario_cargo = float(input("Digite o salário do cargo: "))
    except ValueError:
        print("Salário inválido. Digite um número válido.")
        return
    
    cargos.append({"nome": nome_cargo, "salário": salario_cargo})
    print("Cargo cadastrado com sucesso!")
    
    exibir_separador()

def verifica_funcionario_repetido(codigo_fun):
    if any(func['codigo'] == codigo_fun for func in funcionarios):
        print("Código de funcionário já em uso.")
        return True  # Retorna True se o funcionário já existe
    return False

def cadastrar_funcionario():
    nome_fun = input("Digite o nome do funcionário: ")
    codigo_fun = input("Digite o código do funcionário: ")
    
    if verifica_funcionario_repetido(codigo_fun):
        return  # Retorna se o funcionário já existe
    
    exibir_separador()
    
    print("Cargos disponíveis:")
    for idx, cargo in enumerate(cargos):
        print(f"{idx} - Cargo: {cargo['nome']}, Salário: {cargo['salário']:.2f}")
    try:
        codigo_cargo = int(input("Digite o código do cargo: "))
    except ValueErro:
        print("Código de cargo inválido. Digite um número válido.")
        return
    
    if 0 <= codigo_cargo < len(cargos):
        funcionarios.append({'codigo': codigo_fun, 'nome': nome_fun, 'cargo': codigo_cargo})
        print("Funcionário cadastrado com sucesso!")
    else:
        print("Código de cargo inválido.")
    
    exibir_separador()

def relatorio():
    exibir_titulo("Relatório de Funcionários")
    
    if not funcionarios:
        print("Nenhum funcionário cadastrado!")
    else:
        for func in funcionarios:
            cargo = cargos[func['cargo']]
            print(f"Código: {func['codigo']}, Nome: {func['nome']}, Cargo: {cargo['nome']}, Salário: {cargo['salário']:.2f}")
    
    exibir_separador()

def salario_cargo():
    try:
        codigo_cargo = int(input("Digite o código do cargo para calcular o valor total dos salários: "))
    except ValueError:
        print("Código de cargo inválido. Digite um número válido.")
        return
        
    if 0 <= codigo_cargo < len(cargos):
        total_salario = sum(cargos[func['cargo']]['salário'] for func in funcionarios if func['cargo'] == codigo_cargo)
        print(f"Total de salário para o cargo {cargos[codigo_cargo]['nome']}: {total_salario:.2f}")
    else:
        print("Código de cargo inválido.")
    
    exibir_separador()

def menu():
    while True:
        print("1 - Cadastrar cargo.")
        print("2 - Cadastrar funcionário.")
        print("3 - Mostrar relatório de funcionários.")
        print("4 - Mostrar o total de salário por cargo.")
        print("9 - Sair.")
        
        try:
            opcao = int(input("Digite o número da opção desejada: "))
        
            if opcao == 1:
                cadastrar_cargo()
            elif opcao == 2:
                cadastrar_funcionario()
            elif opcao == 3:
                relatorio()
            elif opcao == 4:
                salario_cargo()
            elif opcao == 9:
                print("Programa encerrado!")
                break
            else:
                print("Opção não existe.")
            
        except ValueError:
            print("Entrada inválida. Digite um número válido.")
        
        exibir_separador()

exibir_titulo("Bem-vindo ao Sistema Robson Construções!")
cargos = [
    {"nome": " 0 ", "salário": 2500.0},
    {"nome": " 1 ", "salário": 1500.0},
    {"nome": " 2 ", "salário": 10000.0},
    {"nome": " 3 ", "salário": 1200.0},
    {"nome": " 4 ", "salário": 800.0}
]
funcionarios = []
menu()
