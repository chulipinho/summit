# Summit: Resumo Automático de Reuniões do Google Meet

O Summit é uma ferramenta que utiliza a API do Google e a inteligência artificial para gerar resumos automáticos das suas reuniões do Google Meet.

### Funcionalidades:

- **Acesse suas gravações**: O Summit conecta-se ao seu Google Drive para buscar automaticamente as gravações das suas reuniões da última semana.

- **Resumos inteligentes**: A inteligência artificial do Google resume cada reunião, capturando os pontos chave e as decisões tomadas.

- **Emails personalizados**: Os resumos são enviados por email para os participantes da reunião e outros destinatários que você especificar.

### Benefícios:

- **Economize tempo**: Obtenha rapidamente os pontos principais de suas reuniões sem precisar assistir a tudo novamente.

- **Melhore a comunicação**: Garanta que todos os participantes estejam na mesma página e acompanhem as decisões tomadas.

- **Aumente a produtividade**: Tome decisões mais rapidamente e mantenha seus projetos em andamento.

## Índice

1. [Instalação](#instalacao)

2. [Utilização](#utilizacao)

3. [Como funciona](#como-funciona)

4. [Observações](#observacoes)

5. [Contato](#contato)

## Instalação

**Pré-requisitos**:

- Python 3.6 ou superior

- Pip

- Conta no Google Cloud Platform

- Conta no Google Workspace

**Passos**:

1. **Clone o repositório**:

```bash
git clone https://github.com/chulipinho/summit
```

2. **Instale as dependências:**

```bash
cd summit
python -m pip install -r requirements.txt
```

3. **Crie o arquivo** `.env`:

Crie um arquivo chamado `.env` na pasta raiz do projeto e adicione as seguintes informações:

```
API_KEY=sua_chave_de_api_do_ai_studio  # Sua chave de API do Ai Studio
VIDEO_PATH=reunioes                   # O nome da pasta onde estão as gravações no Google Drive


# Outras configurações opcionais
# CLEAR_TMP: Booleano - Define se o conteúdo da pasta tmp será apagado após a execução
# LOG_PATH: String - Caminho da pasta onde será armazenado o Log
# PORT_NUMBER: String - Porta para redirecionamento da sua URL de autenticação do OAuth2, valor padrão é 3031
# LANGUAGE: String - Idioma da resposta do Ai Studio, valor padrão é PT-BR (suporta apenas português e inglês atualmente)
```

4. **Crie os arquivos JSON de credenciais**:

Siga as instruções em [este tutorial](https://developers.google.com/workspace/guides/create-credentials?hl=pt-br) do Google para criar os arquivos JSON de credenciais. Remova o "_example" dos nomes dos seus arquivos.

**Observações**:

- A chave de API do Ai Studio pode ser obtida na sua conta do Google Cloud Platform.

- O caminho da pasta de vídeos no Google Drive deve ser ajustado de acordo com a sua organização.

- As configurações opcionais no arquivo `.env` podem ser personalizadas de acordo com suas necessidades.

## Utilização

1. **Execute o script**:

```bash
python main.py
```

2. **Siga as instruções na tela**:
- Informe os emails dos destinatários que receberão os resumos.

- Autentique-se com sua conta do Google.

**O Summit processará suas gravações de reuniões e enviará os resumos por email para os destinatários especificados.**

## Como funciona

1. **O Summit acessa o Google Drive**: Busca automaticamente por arquivos de vídeo na pasta configurada no arquivo `.env`.

2. **Processamento de cada vídeo**:
- **Armazenamento local**: O vídeo é armazenado localmente no computador.

- **Extração de áudio**: Somente o áudio é extraído do vídeo para reduzir o uso de tokens da API do Ai Studio.

- **Análise do Ai Studio**: O arquivo de áudio é enviado para o Ai Studio, que gera um resumo da reunião.

- **Armazenamento do resumo**: O resumo é armazenado em uma lista.
3. **Envio de emails**:
- **Criação de emails**: Para cada resumo, um email é criado com o conteúdo do resumo e os destinatários informados.

- **Envio via API do Gmail**: Os emails são enviados para os destinatários usando a API do Gmail.

## Observações

- O Summit está em desenvolvimento e novas funcionalidades serão adicionadas em breve.

- Se você encontrar algum problema, por favor, envie um relatório de bug no repositório do GitHub.

## Contato

Para obter mais informações sobre o Summit ou para relatar problemas, você pode entrar em contato conosco através dos seguintes canais:

- **LinkedIn:** [Fellipe Machado](https://www.linkedin.com/in/fellipe-luz/)
- **Email:** fellipe.luz.machado@gmail.com

Agradecemos seu interesse no Summit!

