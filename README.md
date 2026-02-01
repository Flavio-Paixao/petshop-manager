🐾 PetShop Manager
O PetShop Manager é uma aplicação web desenvolvida com Django para facilitar a gestão de atendimentos e cadastros em estabelecimentos veterinários. O projeto foi construído focando na praticidade do administrador e na segurança da aplicação.

🚀 Funcionalidades
Gestão de Pets: Cadastro completo de animais.

Controle de Clientes: Vinculação de pets aos seus respectivos donos.

Painel Administrativo: Interface customizada para gerenciamento rápido de dados.

Busca Inteligente: Filtro de animais diretamente na página inicial.

🛠️ Tecnologias Utilizadas
Python 3.x

Django Framework

SQLite (Banco de dados)

Gunicorn (Servidor HTTP para produção)

Render (Plataforma de Deploy)

🌐 Deploy e Acesso
O projeto está disponível online através do Render:
🔗 https://petshop-manager-b4is.onrender.com/

🧠 Desafios Superados
Durante o desenvolvimento, um dos maiores aprendizados foi a configuração de segurança para o ambiente de produção. Enfrentei erros de DisallowedHost que foram resolvidos através do ajuste preciso da variável ALLOWED_HOSTS no settings.py e a correta sincronização entre o Git e o servidor de deploy.

📥 Como rodar o projeto localmente
Clone o repositório:

Bash
git clone https://github.com/Flavio-Paixao/petshop-manager.git
Crie um ambiente virtual:

Bash
python -m venv venv
source venv/Scripts/activate  # No Windows: venv\Scripts\activate
Instale as dependências:

Bash
pip install -r requirements.txt
Execute as migrações e inicie o servidor:

Bash
python manage.py migrate
python manage.py runserver

Feito com ☕ por Flávio Paixão

🚀 Próximos Passos & Melhorias Futuras
Calendário Interativo: Implementação de uma interface de calendário (FullCalendar) para visualização e gestão de horários de consultas e banho/tosa.

Sistema de Disparo de Lembretes: Integração com APIs (como Twilio ou SendGrid) para envio automático de confirmações de consulta via WhatsApp ou E-mail.

Confirmação de Presença: Funcionalidade onde o cliente pode confirmar ou desmarcar o horário através de um link único, atualizando o status no dashboard em tempo real.

Gestão de Horários: Lógica de bloqueio de horários conflitantes e definição de janelas de atendimento por profissional.
