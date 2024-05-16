import flet as ft
from database import create_connection
import datetime




def main(page: ft.Page):
    
    def cadastro_pedido(e):
        
        
        
        produto_table = produto.value
        fornecedor_table = fornecedor.value
        frequencia_table=frequencia.value
        quantidade_table = quantidade.value
        preco_table = preco.value
        data_inicio_table = date_picker.value
        data_fim_table = date_picker2.value
        


        conn = create_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO produtos (produto,fornecedor,frequencia,quantidade,preco,data_inicio,data_fim,usuario_id) VALUES (?,?,?,?,?,?,?,?)", (produto_table,fornecedor_table,frequencia_table,quantidade_table,preco_table,data_inicio_table,data_fim_table,valor_legal))
        conn.commit()
        conn.close()

        produto.value = ""
        fornecedor.value = ""
        frequencia.value =""
        quantidade.value = ""
        preco.value = ""
        date_picker.value = ""
        date_picker2.value = ""

    
    
    logo = ft.Image(src="logo.jpg" , width=100 , height=100)
    container = ft.Container(bgcolor='blue',content= logo,
                             shape=ft.BoxShape.CIRCLE,clip_behavior=ft.ClipBehavior.ANTI_ALIAS, )
    produto = ft.TextField(bgcolor="blue",border_radius=50,width=120)
    fornecedor = ft.TextField(bgcolor="blue",border_radius=50,width=120)
    frequencia = ft.TextField(bgcolor="blue",border_radius=50,width=120)
    quantidade = ft.TextField(bgcolor="blue",border_radius=50,width=120)
    preco = ft.TextField(bgcolor="blue",border_radius=50,width=120)
    

    def change_date(e):
        print(f"Date picker changed, value is {date_picker.value}")

    def date_picker_dismissed(e):
        print(f"Date picker dismissed, value is {date_picker.value}")

    date_picker = ft.DatePicker(
        on_change=change_date,
        on_dismiss=date_picker_dismissed,
        first_date=datetime.datetime(2023, 10, 1),
        last_date=datetime.datetime(2024, 10, 1),
    )
    date_picker2 = ft.DatePicker(
        on_change=change_date,
        on_dismiss=date_picker_dismissed,
        first_date=datetime.datetime(2023, 10, 1),
        last_date=datetime.datetime(2024, 10, 1),
    )

    page.overlay.append(date_picker)
    page.overlay.append(date_picker2)

    date_inicio = ft.ElevatedButton(
        "Data Inicio",
        icon=ft.icons.CALENDAR_MONTH,
        width=120,
        on_click=lambda _: date_picker.pick_date(),
    )
    date_fim = ft.ElevatedButton(
        "Data Fim",
        icon=ft.icons.CALENDAR_MONTH,
        width=120,
        on_click=lambda _: date_picker2.pick_date(),
    )
    cadastrar_pedido = ft.ElevatedButton("Cadastrar Pedido",bgcolor="blue",color="white",on_click=cadastro_pedido)

       
    # novo pedido fim
    

    logo_1 = ft.Image(src="logo.jpg" , width=100 , height=100)
    container_2 = ft.Container(bgcolor='blue',content= logo,
                             shape=ft.BoxShape.CIRCLE,clip_behavior=ft.ClipBehavior.ANTI_ALIAS, )
    meus_pedidos = ft.Container(
        content=ft.Text("MEUS PEDIDOS", color="white"),
        bgcolor="blue",
        border_radius=100,
        width=150,
        height=35,
        alignment=ft.alignment.center,
    )

    quadrado = ft.Container(bgcolor='blue', width=50, height=50,content=ft.Icon(name=ft.icons.STAR_BORDER, color=ft.colors.WHITE, size=50))

    


    
    def novo_pedido(e):
        page.clean()
        page.add(
          container_2,
          ft.Column([
              ft.Row([ft.Text("PRODUTO",width=120,bgcolor="blue"),produto]),
              ft.Row([ft.Text("FORNECEDOR",width=120,bgcolor="blue"),fornecedor]),
              ft.Row([ft.Text("FREQUÊNCIA",width=120,bgcolor="blue"),frequencia]),
              ft.Row([ft.Text("QUANTIDADE",width=120,bgcolor="blue"),quantidade]),
              ft.Row([ft.Text("PREÇO",width=120,bgcolor="blue"),preco]),
              ft.Row([date_inicio,date_fim]),cadastrar_pedido])
            


           )
    def cadastro(e):
        nome = entrada_nome.value
        senha = entrada_senha.value

    # Conectando ao banco de dados
        conn = create_connection()
        cursor = conn.cursor()

    # Inserindo dados na tabela
        cursor.execute("INSERT INTO usuarios (nome, senha) VALUES (?, ?)", (nome, senha))
        conn.commit()
        conn.close()

    # Limpando os campos de texto
        entrada_nome.value = ""
        entrada_senha.value = ""

        ft.SnackBar(page, "Usuário cadastrado com sucesso!")


    def login(e):
        nome = entrada_nome.value
        senha = entrada_senha.value
        conn = create_connection()
        cursor = conn.cursor()
        

    # Inserindo dados na tabela
        
        try:
            cursor.execute("SELECT id,nome, senha FROM usuarios WHERE nome = ?", (nome,))
            linha_filtrada = cursor.fetchone()
            item = list(linha_filtrada)
            global valor_legal
            valor_legal = item[0]
            
            
                
            
            if item[2] == senha:
                print("usuario logado com sucesso")
                conn = create_connection()
                cursor = conn.cursor()
                cursor.execute("SELECT * FROM produtos WHERE usuario_id = ?", (valor_legal,))
                linha_filtrada = cursor.fetchall()
                item_2 = list(linha_filtrada)
                
                print(item_2)
                lista = ft.ListView(data=item_2)
                for i in item_2:
                    ll = ft.Row([ft.Text(i[1],color="blue",bgcolor="white"),ft.Text(i[2],color="blue",bgcolor="white"),ft.Text(i[3],color="blue",bgcolor="white"),ft.Text(i[6][0:10],color="blue",bgcolor="white"),ft.Text(i[7][0:10],color="blue",bgcolor="white")])
                    lista.controls.append(ll)
                    
                
                page.clean()
                page.add(ft.Column(
            [
                ft.Row(
                    [
                        meus_pedidos,
                        ft.ElevatedButton("Adicionar Pedido",on_click=novo_pedido)
                    ]
                ),ft.Row([ft.Text("PRODUTO"),ft.Text("FORNECEDOR"),ft.Text("QUANTIDADE"),ft.Text("DATA INICIO"),ft.Text("DATA FIM")]),lista
                
                
            ]
        ))
            
            else:
                page.clean()
                page.add(ft.Text("Não existe esse usuário"))
        except TypeError:
            print("usuario não encontrado")
        return item[0]

    
        
        
        

        
   
    entrada_nome = ft.TextField(prefix_icon=ft.icons.PEOPLE,border_radius=100,bgcolor='blue',color='white',width=300)
    entrada_senha = ft.TextField(prefix_icon=ft.icons.LOCK,border_radius=100,bgcolor='blue', width=300,)
    
    logo = ft.Image(src="logo.jpg" , width=300 , height=300)
    container = ft.Container(bgcolor='blue',content= logo,
                             shape=ft.BoxShape.CIRCLE,clip_behavior=ft.ClipBehavior.ANTI_ALIAS, )
   
    page.add(
        container,
        entrada_nome,
        entrada_senha,
        
           ft.ElevatedButton("Entrar",width=300,on_click=login ),
           ft.ElevatedButton("Cadastre - se",width=300 ,on_click=cadastro)
        )


ft.app(main)