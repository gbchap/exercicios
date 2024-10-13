
#chat
#Toda função deve ser definida antes de ser mencionada. O resto não tem muita ordem.
#depois de 'on_click' sempre deve existir um 'evento'
#file.picker pra mandar anexos

import flet as ft

def main(pagina):
    titulo = ft.Text('Zapzap')
    pagina.add(titulo)
    
    def enviar_msg_tunel(mensagem_todos):
        mensagem = ft.Texto(mensagem_todos)
        chat.controls.append(mensagem)
        pagina.update()

    pagina.pubsub.subscribe(enviar_msg_tunel) 
        
    def enviar_msg(evento):
        nome_user = caixa_nome.value
        mensagem_todos = (f'{nome_user}: {caixa_msg.value}')
        pagina.pubsub.sendall(mensagem_todos)
        caixa_msg.value = '' #limpa caixa de enviar msg
        pagina.update()
        print('Botão de enviar mensagem clicado.')
    
    chat = ft.Column()
    caixa_msg = ft.TextField(label='Digite aqui a sua fofoca', on_submit=enviar_msg) #enviar c enter
    botao_enviar = ft.ElevatedButton('Enviar', on_click=enviar_msg)
    
    def entrar_chat(evento):
        popup.open = False
        pagina.remove(titulo)
        pagina.remove(botao)
        pagina.add(chat)
        pagina.add(linha_enviar)
        nome_user = caixa_nome.value
        mensagem_todos = (f'{nome_user} entrou no chat.')
        pagina.pubsub.sendall(mensagem_todos)
        pagina.update()
        print('Botão de entrar no chat clicado.')
        
    linha_enviar = ft.Row([caixa_msg, botao_enviar])
    titulo_popup = ft.Text('Bem-vindah ao Zapzap diva!')
    caixa_nome = ft.TextField(label='Digite seu nick :v')
    botao_popup = ft.ElevatedButton('Entrar no Zapzap', on_click=entrar_chat)
    popup = ft.AlertDialog(title=titulo_popup, content=caixa_nome, actions=[botao_popup])

    def abrir_popup(evento):
        pagina.dialog = popup
        popup.open = True
        pagina.update()
        print('Botão de entrar no zapzap clicado.')
        
    botao = ft.ElevatedButton('Iniciar Chat', on_click=abrir_popup)
    pagina.add(botao)


ft.app(main, view=ft.AppView.WEB_BROWSER, port=8000)