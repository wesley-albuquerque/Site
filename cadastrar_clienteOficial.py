from flask import Flask, request, jsonify
from flask_cors import CORS
import mysql.connector

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*", "headers":"*"}}, supports_credentials=True)
@app.route("/inserir-dados", methods=["POST"])
def inserir_dados():
    data = request.get_json(force=True)
    cpf_cnpj = data["cpf_cnpj"]
    nome_razao_social = data["nome"]
    nome_fantasia = data.get("fantasia", "")
    email = data.get("email", "")
    telefone = data.get("telefone", "")
    celular = data.get("celular", "")
    cep = data["CEP"]
    logradouro = data["logradouro"]
    complemento = data.get("complemento", "")
    numero = data["numero"]
    bairro = data["bairro"]
    cidade = data["cidade"]
    estado = data["estado"]
    pais = data["pais"]

    # Conecta ao banco de dados
    conexao = mysql.connector.connect(
        host="localhost",
        user="wesley",
        password="waa123",
        database="banco_smart_monkey"
    )

    # Cria um cursor para executar comandos SQL
    cursor = conexao.cursor()

    # Define a consulta SQL para inserir dados na tabela "clientes"
    sql = "INSERT INTO clientes (cpf_cnpj, nome_razao_social, nome_fantasia, email, telefone, celular, cep, logradouro, complemento, numero, bairro, cidade, estado, pais) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"

    # Define os valores para os campos da tabela
    valores = (cpf_cnpj, nome_razao_social, nome_fantasia, email, telefone, celular, cep, logradouro, complemento, numero, bairro, cidade, estado, pais)

    try:
        # Executa a consulta SQL
        cursor.execute(sql, valores)

        # Salva as alterações no banco de dados
        conexao.commit()

        return "Cliente cadastrado com sucesso"

    except Exception as e:
        return "CPF já cadastrado"
        #return f"Erro ao inserir dados: {str(e)}"

    finally:
        # Fecha a conexão com o banco de dados
        conexao.close()

@app.route("/delete-dados", methods=["DELETE"])
def delete_dados():
    data = request.get_json(force=True)
    cpf_cnpj = data["cpf_cnpj"]
    
    # Conecta ao banco de dados
    conexao = mysql.connector.connect(
        host="localhost",
        user="wesley",
        password="waa123",
        database="banco_smart_monkey"
    )

    # Cria um cursor para executar comandos SQL
    cursor = conexao.cursor()

    # Define a consulta SQL para inserir dados na tabela "clientes"
    sql = "DELETE FROM clientes WHERE cpf_cnpj = %s"

    # Define os valores para os campos da tabela
    valores = (cpf_cnpj,)

    try:
        # Executa a consulta SQL
        cursor.execute(sql, valores)

        if cursor.rowcount == 0:
            return "CPF não encontrado"
        
        else:
        # Salva as alterações no banco de dados
            conexao.commit()
            return "Cliente excluído com sucesso"

    except Exception as e:
        return f"Erro ao deletar dados: {str(e)}"

    finally:
        # Fecha a conexão com o banco de dados
        conexao.close()

@app.route("/consulta-dados", methods=["POST"])
def consulta_dados():
    data = request.get_json(force=True)
    cpf_cnpj = data["cpf_cnpj"]
    
    # Conecta ao banco de dados
    conexao = mysql.connector.connect(
        host="localhost",
        user="wesley",
        password="waa123",
        database="banco_smart_monkey"
    )

    # Cria um cursor para executar comandos SQL
    cursor = conexao.cursor()

    # Define a consulta SQL para inserir dados na tabela "clientes"
    sql = "SELECT * FROM clientes WHERE cpf_cnpj = %s"

    # Define os valores para os campos da tabela
    valores = (cpf_cnpj,)

    try:
        # Executa a consulta SQL
        cursor.execute(sql, valores)
        
        # Obtém todas as linhas da consulta
        resultados = cursor.fetchall()

        if resultados:
            # Obtém as informações das colunas selecionadas na consulta
            colunas = [col[0] for col in cursor.description]

            # Cria uma lista de dicionários com os resultados da consulta
            dados = [dict(zip(colunas, linha)) for linha in resultados]

            # Retorna os resultados da consulta em formato JSON
            return jsonify(dados)
        else:
            return "CPF não encontrado"

    except Exception as e:
        return "CPF não encontrado"
        #return f"Erro ao inserir dados: {str(e)}"

    finally:
        # Fecha a conexão com o banco de dados
        conexao.close()
@app.route("/atualiza-dados", methods=["POST"])
def atualiza_dados():
    data = request.get_json(force=True)
    cpf_cnpj = data["cpf_cnpj"]
    nome_razao_social = data["nome"]
    nome_fantasia = data.get("fantasia", "")
    email = data.get("email", "")
    telefone = data.get("telefone", "")
    celular = data.get("celular", "")
    cep = data["CEP"]
    logradouro = data["logradouro"]
    complemento = data.get("complemento", "")
    numero = data["numero"]
    bairro = data["bairro"]
    cidade = data["cidade"]
    estado = data["estado"]
    pais = data["pais"]

    # Conecta ao banco de dados
    conexao = mysql.connector.connect(
        host="localhost",
        user="wesley",
        password="waa123",
        database="banco_smart_monkey"
    )

    # Cria um cursor para executar comandos SQL
    cursor = conexao.cursor()

    # Define a consulta SQL para inserir dados na tabela "clientes"
    sql = "UPDATE clientes SET nome_razao_social=%s, nome_fantasia=%s, email=%s, telefone=%s, celular=%s, cep=%s, logradouro=%s, complemento=%s, numero=%s, bairro=%s, cidade=%s, estado=%s, pais=%s WHERE cpf_cnpj=%s"

    # Define os valores para os campos da tabela
    valores = (nome_razao_social, nome_fantasia, email, telefone, celular, cep, logradouro, complemento, numero, bairro, cidade, estado, pais, cpf_cnpj)

    try:
        # Executa a consulta SQL
        cursor.execute(sql, valores)

        # Salva as alterações no banco de dados
        conexao.commit()

        return "Cliente atualizado com sucesso"

    except Exception as e:
        return f"Erro ao atualizar dados: {str(e)}"

    finally:
        # Fecha a conexão com o banco de dados
        conexao.close()

if __name__ == "__main__":
    app.run(debug=True)


