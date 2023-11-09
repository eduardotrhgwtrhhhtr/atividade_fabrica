import mysql.connector

con = mysql.connector.connect(host='10.28.1.207', database='', user='suporte', password='suporte')

if con.is_connected():
    db_info = con.get_server_info()
    print("Conectado ao banco de dados=",db_info)
    
    
consulta_sql = "select * from usuario"
cursor = con.cursor()
cursor.execute(consulta_sql)
linhas = cursor.fetchall()
print("Número total de registros retornados: ", cursor.rowcount)   

#comando = "insert into usuario (cpf, nome, email, telefone, nascimento, genero, palestra) values ('1231212312', 'Hentony', 'silvahentony38@gmail.com', '67992363684', '24/07/2005', 'masculino', '306');"
#comando = ("update usuario set nome = 'Antonio' where cpf= 12345678901;") #para adcionar um novo usuario
#comando = ("delete from usuario where cpf = 89202214196;") #para deletar um usuario

#cursor.execute(comando)
#con.commit()

print("\nMostrando os Registros\n")
for linha in linhas:
    print("Nome = ", linha[0])
    print("CPF = ", linha[1])
    print("Telefone = ", linha[2])
    print("Email = ", linha[3])
    print("Senha = ", linha[4])
    print("=-"*20)

    
if con.is_connected():
    cursor.close()
    con.close()
    print("Conexão encerrada")

