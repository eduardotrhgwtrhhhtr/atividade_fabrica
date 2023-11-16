from os import system as ss 
import mysql.connector

con = mysql.connector.connect(
    host = '10.28.1.207',
    database = 'usuario',
    user = 'suporte',
    password = 'suporte'
)
print("conectado ao banco de dados.")

while True:
    try:
        options = int(input("escolha uma das opções\n1- cadastrar\n2- sair\n escolha: "))
    except:
        ss('cls')
        ss('inexiste')
        ss('pause')
        ss('cls')
        
    else:
        ss('cls')
        if options == 1:
            try:
                nome = input("nome: ")
                idade = input("idade: ")             
                estadocivil = input("estado civil: ")
                cpf = input("cpf: ")
                sexo = input("sexo: ")
                email = input("email: ")
                pais = input("país: ")
                estado = input("estado: ")
                cidade = input("cidade: ")
            except: 
                ss('cls')
                ss("erro")
                ss('cls')
            else: 
                ss('cls')
                print("cadastrado.")
                #                insertsql =f"insert info usuario(nome,idade,estado civil, cpf, sexo, email, pais, estado, cidade) values ('{nome}','({idade})','({estadocivil})','({cpf})','({sexo})','({email})','({pais})','({estado})','({cidade})')"
                insertsql ="insert into cliente (nome, idade, estadocivil, cpf, sexo, email, pais, estado, cidade) values ('"+nome+"',"+idade+",'"+estadocivil+"','"+cpf+"','"+sexo+"','"+email+"','"+pais+"','"+estado+"','"+cidade+"');"
                #insert into cliente (nome, idade, estadocivil, cpf, sexo, email, pais, estado, cidade) values ('ederson',39,'casado','95787878','m','dasdas@','br','ms','cg')
                print(insertsql)
                cursor = con.cursor()
                cursor.execute(insertsql)
                con.commit()
                
                
                
                
                select = 'select * from cliente'
                #cursor = con.cursor()
                cursor.execute(select)
                linhas = cursor.fetchall()
                con.commit()
                
                
                
        elif options == 2:
            print("saiu")
            break         
                