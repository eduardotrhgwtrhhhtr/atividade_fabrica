import mysql.connector
con=mysql.connector.connect(
host='10.28.1.207',
database='HubInnovation',
user='suporte',
password='suporte')

if con.is_connected():
    db_info = con.get_server_info()
    print("conectado ao banco de dados = ",db_info)
    
    
    
comando = "INSERT INTO usuario (nome,email,fone,cpf,data_nasc,sexo,id_palestra)VALUES ('gravena','@gmail','999','999','2000-11-01','feminino','1');"
cursor = con.cursor()
cursor.execute(comando)
con.commit()   



    
comando = ("UPDATE usuario set nome = 'Ederson' where cpf = 999;")
cursor.execute(comando)
con.commit()
    
'''comando = ("DELETE from usuario where cpf = 999;")
cursor.execute(comando)
con.commit()'''
    

consulta_sql = "select * from usuario"
cursor = con.cursor()
cursor.execute(consulta_sql)
linhas = cursor.fetchall()
print("numero total de registros retomados: ",cursor.rowcount)

print("Mostrando Registros")
for linha in linhas:
    print("id_palestra = ",linha[0])
    print("nome = ",linha[1])
    print("email = ",linha[2])
    print("fone = ",linha[3])
    print("data_nasc = ",linha[4])
    print("sexo = ",linha[5])
    print("id_palestra = ",linha[6])   

if con.is_connected():
    cursor.close()
    con.close()
    print("conexão encerrada. ")