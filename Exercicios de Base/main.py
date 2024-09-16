import flask as Flask
from flask import request, jsonify
import oracledb
import sys
app =Flask(__name__)

def obter_conexao():
    connection = oracledb.connect(user='SYSTEM', password='pedro', dsn='<localhost/1521>')
    return connection

# Rota para classificação da qualidade do ar e efeitos à saúde
@app.route('/classificacao', methods=['GET'])
def classificar():
    connection=obter_conexao()
    cursor = connection.cursor()
    cursor.execute('SELECT AVG(MP10), AVG(MP25), AVG(O3), AVG(SO2), AVG(NO2), AVG(CO) FROM QUALIDADE_DO_AR')
    resultado = cursor.fetchone()

    if resultado is not None:
        MP10, MP25, O3, SO2, NO2, CO = resultado

        if (MP10 >= 0 and MP10 <= 50) and (MP25 >= 0 and MP25 <= 25) and (O3 >= 0 and O3 <= 100) and (SO2 >= 0 and SO2 <= 20) and (NO2 >= 0 and NO2 <= 200) and (CO >= 0 and CO <= 9):
            classificacao = {
                "qualidade_ar": "Boa"
            }
        elif (MP10 > 50 and MP10 <= 100) or (MP25 > 25 and MP25 <= 50) or (O3 > 100 and O3 <= 130) or (SO2 > 20 and SO2 <= 40) or (NO2 > 200 and NO2 <= 240) or (CO > 9 and CO <= 11):
            classificacao = {
                "qualidade_ar": "Moderada",
                "efeitos_saude": "Pessoas de grupos sensíveis (crianças, idosos e pessoas com doenças respiratórias e cardíacas) podem apresentar sintomas como tosse seca e cansaço. A população, em geral, não é afetada."
            }
        elif (MP10 > 100 and MP10 <= 150) or (MP25 > 50 and MP25 <= 75) or (O3 > 130 and O3 <= 160) or (SO2 > 40 and SO2 <= 365) or (NO2 > 240 and NO2 <= 320) or (CO > 11 and CO <= 13):
            classificacao = {
                "qualidade_ar": "Ruim",
                "efeitos_saude": "Toda a população pode apresentar sintomas como tosse seca, cansaço, ardor nos olhos, nariz e garganta. Pessoas de grupos sensíveis (crianças, idosos e pessoas com doenças respiratórias e cardíacas) podem apresentar efeitos mais sérios na saúde."
            }
            
        elif (MP10 > 150 and MP10 <= 250) or (MP25 > 75 and MP25 <= 125) or (O3 > 160 and O3 <= 200) or (SO2 > 365 and SO2 <= 800):    
             classificacao = {
                "qualidade_ar": "Muito Ruim",
                "efeitos_saude": "Toda a população pode apresentar agravamento dos sintomas como tosse seca, cansaço, ardor nos olhos, nariz e garganta, e ainda falta de ar e respiração ofegante. Efeitos ainda mais graves na saúde de grupos sensíveis (crianças, idosos e pessoas com doenças respiratórias)."
            }
        elif (MP10 > 250) or (MP25 > 125) or (O3 > 200) or (SO2 > 800) or (NO2 > 1130) or (CO > 15):
            classificacao = {
                "qualidade_ar": "Péssima",
                "efeitos_saude": "Toda a população pode apresentar sérios riscos de manifestações de doenças respiratórias e cardiovasculares. Aumento de mortes prematuras em pessoas de grupos sensíveis."
            }
        else:
            classificacao = {
            "qualidade_ar": "Insira os valores no Banco de dados"
            }
        return jsonify(classificacao) 
    else:
        return "Nenhum dado disponível" 
     
# Rota para inserção de dados de amostras
@app.route('/cadastro', methods=['POST'])
def cadastrar():
    try:
        connection = obter_conexao() 
        cursor = connection.cursor()
    
    
        MP10 = request.form['']
        MP25 = request.form['']
        O3 = request.form['']
        NO2 = request.form['']
        CO = request.form['']
    
        cursor.execute("INSERT INTO QUALIDADE_DO_AR (MP10, MP25, O3, NO2, CO) VALUES (:MP10, :MP25, :O3, :NO2, :CO)",
                   (MP10, MP25, O3, NO2, CO))
        connection.commit()
        cursor.close()
    
        return f"MP10: {MP10}<br>MP25: {MP25}<br>O3: {O3}<br>NO2: {NO2}<br>CO: {CO}"

    except oracledb.Error as error:
        return "Erro ao cadastrar"
    
    
    
# Rota para atualização de dados de amostras
@app.route('/alteracao/<id>', methods=['PUT'])
def alterar(id):
    try:
        connection = obter_conexao()
        cursor = connection.cursor()
    # Implemente a lógica para atualizar os dados de amostra no banco de dados
    # Utilize a request.get_json() para obter os dados enviados pelo cliente
    # Retorne uma resposta adequada para indicar o sucesso ou falha da atualização
    
    except oracledb.Error as error:
        return"erro"


    
# Rota para exclusão de dados de amostras
@app.route('/exclusao/<id>', methods=['DELETE'])
def excluir(id):
    # Implemente a lógica para excluir os dados de amostra do banco de dados
    # Retorne uma resposta adequada para indicar o sucesso ou falha da exclusão
    try:
        connection = obter_conexao()
        cursor = connection.cursor()
        colunas_selecionadas = request.form.getlist('')
        
        
        for coluna_id in colunas_selecionadas:
            cursor.execute("DELETE FROM tabela WHERE coluna = :id", {"id": coluna_id})
            connection.commit()
            cursor.close()
            return "Registros excluídos com sucesso"
        
    except oracledb.Error as error:
        return "Erro ao excluir registros: " + str(error)
        
# Rota para sair do sistema
@app.route('/sair', methods=['GET'])
def sair():
    shutdown_server()
    return 'Saindo do sistema'

def shutdown_server():
    func = request.environ.get('werkzeug.server.shutdown')
    if func is None:
        raise RuntimeError('Não é possível encerrar o servidor Flask!')
    func()
    
if __name__ == '__main__':
    app.run(debug=True)

