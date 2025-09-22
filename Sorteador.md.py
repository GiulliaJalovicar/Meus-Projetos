<!doctype html>
<html lang="pt-BR">
<head>
  <!-- META TAGS - Configurações básicas da página -->
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <!-- TÍTULO DA PÁGINA - Nome exibido na aba do navegador -->
  <title>Sorteador Fofo</title>
  
  <!-- CSS - Estilos da página -->
  <style>
    /* VARIÁVEIS CSS - Paleta de cores com tema pastel fofa */
    :root {
      --bg: #f4f1f8; /* Fundo lavanda suave */
      --card: #ffffff; /* Cor de fundo dos cards */
      --accent: #f9a8d4; /* Rosa pastel - cor principal */
      --accent-hover: #ec4899; /* Rosa mais vibrante para hover */
      --muted: #4b3f72; /* Roxo suave para texto principal */
      --muted-2: #7c6d9e; /* Roxo claro para texto secundário */
      --border: #e2e8f0; /* Borda suave e neutra */
      --highlight: #fefce8; /* Amarelo clarinho para destaque */
      --shadow: rgba(0, 0, 0, 0.08); /* Sombra suave para profundidade */
    }

    /* RESET CSS - Configurações básicas para todos os elementos */
    * {
      box-sizing: border-box; /* Inclui padding e border no cálculo de largura */
    }

    /* ESTILOS GLOBAIS - Configurações do HTML e Body */
    html, body {
      height: 100%; /* Altura total da viewport */
      margin: 0; /* Remove margens padrão */
    }

    /* CORPO DA PÁGINA - Layout principal e fundo */
    body {
      /* FONTE - Tipografia fofa e moderna */
      font-family: 'Comic Neue', 'Inter', system-ui, sans-serif;
      /* GRADIENTE - Fundo com transição suave de lavanda para roxo */
      background: linear-gradient(180deg, var(--bg) 0%, #f3e8ff 100%);
      color: var(--muted); /* Cor do texto principal */
      /* LAYOUT CENTRALIZADO - Centraliza todo o conteúdo na tela */
      display: flex;
      align-items: center;
      justify-content: center;
      padding: 24px; /* Espaçamento nas bordas */
    }

    /* CONTAINER PRINCIPAL - Estrutura geral da página */
    .container {
      width: 720px; /* Largura padrão */
      max-width: 95%; /* Máximo 95% da tela em dispositivos pequenos */
      display: flex;
      flex-direction: column; /* Elementos empilhados verticalmente */
      gap: 24px; /* Espaçamento entre as seções */
    }

    /* CARDS - Componentes visuais principais da interface */
    .card {
      /* BACKGROUND - Fundo branco com bordas arredondadas */
      background: var(--card);
      border-radius: 24px; /* Bordas bem arredondadas */
      padding: 28px; /* Espaçamento interno */
      border: 1px solid var(--border); /* Borda sutil */
      /* SOMBRA - Efeito de elevação e profundidade */
      box-shadow: 0 10px 30px var(--shadow);
      /* ANIMAÇÃO - Transição suave para efeitos hover */
      transition: transform 0.3s ease, box-shadow 0.3s ease;
      position: relative; /* Para posicionamento de elementos filhos */
    }

    /* EFEITO HOVER DOS CARDS - Animação ao passar o mouse */
    .card:hover {
      transform: translateY(-6px); /* Levanta o card levemente */
      box-shadow: 0 14px 36px var(--shadow); /* Sombra mais intensa */
    }

    /* TÍTULO PRINCIPAL - Estilo do h1 */
    h1 {
      margin: 0; /* Remove margem padrão */
      font-size: 28px; /* Tamanho do texto */
      font-weight: 700; /* Peso da fonte */
      color: var(--muted); /* Cor do texto */
      text-align: center; /* Centraliza o texto */
      position: relative; /* Para posicionamento dos pseudo-elementos */
    }

    /* DECORAÇÃO ESQUERDA DO TÍTULO - Espaço reservado para ícone */
    h1::before {
      content: ' '; /* Conteúdo vazio para posicionamento */
      position: absolute;
      left: -30px; /* Posiciona à esquerda do título */
      top: 50%; /* Centraliza verticalmente */
      transform: translateY(-50%); /* Ajuste fino da centralização */
    }

    /* DECORAÇÃO DIREITA DO TÍTULO - Espaço reservado para ícone */
    h1::after {
      content: ' '; /* Conteúdo vazio para posicionamento */
      position: absolute;
      right: -30px; /* Posiciona à direita do título */
      top: 50%; /* Centraliza verticalmente */
      transform: translateY(-50%); /* Ajuste fino da centralização */
    }

    /* UTILITÁRIO - Classe para centralizar conteúdo */
    .center {
      text-align: center; /* Centraliza texto dentro do elemento */
    }

    /* ÁREA DE RESULTADO - Seção superior que exibe o ganhador */
    .result {
      height: 200px; /* Altura fixa da área */
      display: flex;
      flex-direction: column; /* Elementos empilhados verticalmente */
      align-items: center; /* Centraliza horizontalmente */
      justify-content: center; /* Centraliza verticalmente */
      border-radius: 20px; /* Bordas arredondadas */
      /* BACKGROUND ROSA TRANSPARENTE - Gradiente sutil */
      background: linear-gradient(180deg, rgba(249, 168, 212, 0.1), rgba(249, 168, 212, 0.05));
      border: 1px solid var(--border); /* Borda sutil */
      /* ANIMAÇÃO - Transição para mudança de cor */
      transition: background 0.3s ease;
      position: relative; /* Para pseudo-elementos */
      overflow: hidden; /* Esconde conteúdo que extrapola */
    }

    /* DECORAÇÃO SUPERIOR ESQUERDA - Espaço para ícone futuro */
    .result::before {
      content: ' '; /* Conteúdo vazio */
      position: absolute;
      top: 10px; /* Posição superior */
      left: 10px; /* Posição esquerda */
      font-size: 24px; /* Tamanho do ícone futuro */
    }

    /* DECORAÇÃO INFERIOR DIREITA - Espaço para ícone futuro */
    .result::after {
      content: ' '; /* Conteúdo vazio */
      position: absolute;
      bottom: 10px; /* Posição inferior */
      right: 10px; /* Posição direita */
      font-size: 24px; /* Tamanho do ícone futuro */
    }

    /* TEXTO DO ITEM SORTEADO - Nome do prêmio */
    #resultItem {
      font-size: 30px; /* Tamanho grande para destaque */
      font-weight: 700; /* Peso da fonte */
      margin: 0; /* Remove margem */
      color: var(--muted); /* Cor do texto */
    }

    /* NOME DO GANHADOR - Resultado principal em destaque */
    #resultWinner {
      font-size: 38px; /* Muito grande para destaque máximo */
      font-weight: 800; /* Peso extra pesado */
      color: var(--accent); /* Cor rosa para destaque */
      margin-top: 10px; /* Espaçamento superior */
      /* SOMBRA - Efeito de relevo no texto */
      text-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    }

    /* FORMULÁRIO - Container dos campos de entrada */
    .field {
      margin-top: 18px; /* Espaçamento entre campos */
    }

    /* LABELS - Textos descritivos dos campos de formulário */
    label {
      display: block; /* Ocupa largura total */
      font-size: 15px; /* Tamanho pequeno */
      font-weight: 500; /* Peso médio */
      margin-bottom: 8px; /* Espaçamento inferior */
      color: var(--muted-2); /* Cor secundária */
    }

    /* INPUTS E TEXTAREA - Estilo dos campos de entrada */
    input[type="text"], 
    input[type="number"], 
    textarea {
      width: 100%; /* Largura total do container */
      padding: 14px 18px; /* Espaçamento interno */
      border-radius: 14px; /* Bordas arredondadas */
      border: 1px solid var(--border); /* Borda sutil */
      /* BACKGROUND - Fundo alaranjado suave */
      background: #fff7ed;
      color: var(--muted); /* Cor do texto */
      font-size: 16px; /* Tamanho padrão */
      outline: none; /* Remove outline padrão do navegador */
      /* ANIMAÇÕES - Transições suaves */
      transition: border-color 0.2s ease, box-shadow 0.2s ease;
    }

    /* EFEITO DE FOCO - Animação quando o campo é selecionado */
    input:focus, textarea:focus {
      border-color: var(--accent); /* Borda rosa no foco */
      /* SOMBRA - Halo colorido ao redor do campo */
      box-shadow: 0 0 0 4px rgba(249, 168, 212, 0.2);
    }

    /* LAYOUT EM LINHA - Para campos dispostos lado a lado */
    .row {
      display: flex; /* Layout flexível */
      gap: 18px; /* Espaçamento entre colunas */
    }

    /* COLUNA - Cada campo ocupa metade do espaço */
    .col {
      flex: 1; /* Divide o espaço igualmente */
    }

    /* CONTROLES - Container dos botões principais */
    .controls {
      display: flex; /* Layout horizontal */
      gap: 14px; /* Espaçamento entre botões */
      margin-top: 24px; /* Espaçamento superior */
      justify-content: center; /* Centraliza os botões */
    }

    /* BOTÕES BASE - Estilo comum para todos os botões */
    button.btn {
      padding: 14px 24px; /* Espaçamento interno */
      border-radius: 16px; /* Bordas bem arredondadas */
      border: none; /* Remove borda padrão */
      cursor: pointer; /* Cursor de mão */
      font-weight: 600; /* Peso da fonte */
      font-size: 16px; /* Tamanho do texto */
      /* ANIMAÇÕES - Transições para todos os efeitos */
      transition: background 0.2s ease, transform 0.1s ease, box-shadow 0.2s ease;
      display: flex; /* Para alinhar ícone e texto */
      align-items: center; /* Centraliza verticalmente */
      gap: 8px; /* Espaço entre ícone e texto */
    }

    /* EFEITO HOVER DOS BOTÕES - Animação ao passar o mouse */
    button.btn:hover {
      transform: translateY(-3px); /* Levanta o botão */
    }

    /* EFEITO CLICK DOS BOTÕES - Animação ao clicar */
    button.btn:active {
      transform: scale(0.96); /* Reduz levemente o tamanho */
    }

    /* BOTÃO DE AÇÃO PRINCIPAL - Botão "Sortear" */
    .btn-action {
      /* BACKGROUND - Cor rosa principal */
      background: var(--accent);
      color: white; /* Texto branco */
      /* SOMBRA - Efeito de profundidade rosa */
      box-shadow: 0 4px 14px rgba(249, 168, 212, 0.3);
    }

    /* ÍCONE DO BOTÃO DE AÇÃO - Adiciona ícone antes do texto */
    .btn-action::before {
      content: ' '; /* Espaço para ícone (futuro uso) */
    }

    /* HOVER DO BOTÃO DE AÇÃO - Cor mais escura */
    .btn-action:hover {
      background: var(--accent-hover); /* Rosa mais vibrante */
    }

    /* BOTÃO SECUNDÁRIO - Botão "Limpar" com estilo fantasma */
    .btn-ghost {
      background: transparent; /* Fundo transparente */
      color: var(--muted); /* Cor do texto */
      border: 2px solid var(--border); /* Borda visível */
    }

    /* ÍCONE DO BOTÃO GHOST - Adiciona ícone antes do texto */
    .btn-ghost::before {
      content: ' '; /* Espaço para ícone (futuro uso) */
    }

    /* HOVER DO BOTÃO GHOST - Efeito sutil */
    .btn-ghost:hover {
      /* BACKGROUND - Rosa muito transparente */
      background: rgba(249, 168, 212, 0.1);
      border-color: var(--accent); /* Borda rosa */
    }

    /* LISTA DE PARTICIPANTES - Container da lista rolável */
    .list {
      max-height: 220px; /* Altura máxima antes do scroll */
      overflow: auto; /* Adiciona scrollbar quando necessário */
      padding: 14px; /* Espaçamento interno */
      border-radius: 14px; /* Bordas arredondadas */
      /* BACKGROUND - Fundo alaranjado suave */
      background: #fff7ed;
      border: 1px solid var(--border); /* Borda sutil */
      margin-top: 14px; /* Espaçamento superior */
    }

    /* ITEM DA LISTA - Cada pessoa ou número individual */
    .person {
      padding: 12px 14px; /* Espaçamento interno */
      border-radius: 10px; /* Bordas arredondadas */
      margin-bottom: 10px; /* Espaçamento entre itens */
      display: flex; /* Layout flexível */
      justify-content: space-between; /* Espaça conteúdo nas extremidades */
      align-items: center; /* Centraliza verticalmente */
      color: var(--muted); /* Cor do texto */
      /* ANIMAÇÃO - Transição suave para highlight */
      transition: background 0.2s ease;
    }

    /* ITEM SELECIONADO - Participante que ganhou o sorteio */
    .person.highlight {
      /* BACKGROUND - Fundo amarelo para destaque */
      background: var(--highlight);
      /* BARRA LATERAL - Linha rosa à esquerda */
      border-left: 5px solid var(--accent);
      padding-left: 12px; /* Ajusta padding para compensar a barra */
      font-weight: 600; /* Texto mais pesado */
      position: relative; /* Para posicionamento do ícone */
    }

    /* ÍCONE DE TROFÉU - Adicionado ao item vencedor */
    .person.highlight::after {
      content: ' '; /* Ícone de troféu (futuro uso) */
      position: absolute;
      right: 12px; /* Posiciona à direita */
    }

    /* RODAPÉ - Texto explicativo na parte inferior */
    footer {
      text-align: center; /* Centraliza o texto */
      font-size: 14px; /* Tamanho pequeno */
      color: var(--muted-2); /* Cor secundária */
      margin-top: 16px; /* Espaçamento superior */
      font-style: italic; /* Estilo itálico */
      opacity: 0.7; /* Transparência sutil */
    }

    /* RESPONSIVIDADE - Ajustes para telas menores que 640px */
    @media (max-width: 640px) {
      /* CONTAINER - Usa quase toda a largura disponível */
      .container {
        width: 95%;
      }
      
      /* RESULTADO - Reduz altura em dispositivos móveis */
      .result {
        height: 180px;
      }
      
      /* TEXTO DO ITEM - Reduz tamanho em mobile */
      #resultItem {
        font-size: 26px;
      }
      
      /* NOME DO GANHADOR - Reduz tamanho em mobile */
      #resultWinner {
        font-size: 32px;
      }
      
      /* TÍTULO PRINCIPAL - Reduz tamanho em mobile */
      h1 {
        font-size: 24px;
      }
      
      /* DECORAÇÕES DO TÍTULO - Reduz tamanho dos ícones */
      h1::before, h1::after {
        font-size: 20px;
      }
    }
  </style>
</head>

<body>
  <!-- CONTAINER PRINCIPAL - Envolve toda a estrutura da página -->
  <div class="container">
    
    <!-- ÁREA DE RESULTADO - Seção superior que mostra o ganhador -->
    <div class="card result center">
      <div id="resultItem">—</div> <!-- Nome do item sorteado -->
      <div id="resultWinner">Sorteio</div> <!-- Nome do ganhador -->
    </div>

    <!-- FORMULÁRIO PRINCIPAL - Configurações do sorteio -->
    <div class="card">
      <!-- TÍTULO DO FORMULÁRIO - Cabeçalho da seção -->
      <h1>Sorteador de Itens</h1>
      
      <!-- CAMPO DO ITEM - Nome do prêmio sendo sorteado -->
      <div class="field">
        <label for="item">Nome do item</label>
        <input id="item" type="text" placeholder="Ex.: Espada, Brinde..." />
      </div>
      
      <!-- CAMPOS DE INTERVALO - Números mínimo e máximo -->
      <div class="row field">
        <div class="col">
          <!-- CAMPO MÍNIMO - Limite inferior dos números -->
          <label for="min">Número mínimo</label>
          <input id="min" type="number" min="1" value="1" />
        </div>
        <div class="col">
          <!-- CAMPO MÁXIMO - Limite superior dos números -->
          <label for="max">Número máximo</label>
          <input id="max" type="number" min="1" value="10" />
        </div>
      </div>
      
      <!-- CAMPO DE NOMES - Lista personalizada de participantes -->
      <div class="field">
        <label for="names">(Opcional) Cole nomes — um por linha</label>
        <textarea id="names" placeholder="Malu\Giullia\Queirós"></textarea>
      </div>
      
      <!-- BOTÕES DE AÇÃO - Controles principais do formulário -->
      <div class="controls">
        <!-- BOTÃO SORTEAR - Executa o sorteio -->
        <button type="button" class="btn btn-action" id="drawBtn">Sortear</button>
        <!-- BOTÃO LIMPAR - Reseta todos os campos -->
        <button type="button" class="btn btn-ghost" id="clearBtn">Limpar</button>
      </div>
    </div>

    <!-- LISTA DE PARTICIPANTES - Visualização dos participantes -->
    <div class="card">
      <!-- TÍTULO DA LISTA - Cabeçalho da seção -->
      <div class="center" style="margin-bottom:14px"><strong>Lista de participantes</strong></div>
      <!-- CONTAINER DA LISTA - Área rolável dos itens -->
      <div class="list" id="peopleList"></div>
      
      <!-- BOTÕES RÁPIDOS - Atalhos para configurações comuns -->
      <div style="text-align:center; margin-top:18px">
        <!-- BOTÃO 1-5 - Configuração rápida para 5 participantes -->
        <button type="button" class="btn btn-ghost" id="quick5">1-5</button>
        <!-- BOTÃO 1-10 - Configuração rápida para 10 participantes -->
        <button type="button" class="btn btn-ghost" id="quick10" style="margin-left:12px">1-10</button>
      </div>
    </div>
    
    <!-- RODAPÉ - Instruções de uso do sorteador -->
    <footer>
      Se colar nomes, o sorteio usará apenas eles. Caso contrário, será sorteado um número entre mínimo e máximo.
    </footer>
  </div>

  <!-- JAVASCRIPT - Lógica interativa da aplicação -->
  <script>
    // INICIALIZAÇÃO - Executa quando o DOM está completamente carregado
    document.addEventListener('DOMContentLoaded', () => {
      // ELEMENTOS DO DOM - Referências aos componentes HTML
      const itemInput = document.getElementById('item'); // Campo do nome do item
      const minInput = document.getElementById('min'); // Campo número mínimo
      const maxInput = document.getElementById('max'); // Campo número máximo
      const namesTextarea = document.getElementById('names'); // Área de texto dos nomes
      const drawBtn = document.getElementById('drawBtn'); // Botão principal de sortear
      const clearBtn = document.getElementById('clearBtn'); // Botão de limpar
      const quick5 = document.getElementById('quick5'); // Botão rápido 1-5
      const quick10 = document.getElementById('quick10'); // Botão rápido 1-10
      const resultItem = document.getElementById('resultItem'); // Texto do item no resultado
      const resultWinner = document.getElementById('resultWinner'); // Nome do ganhador
      const peopleList = document.getElementById('peopleList'); // Container da lista de participantes

      // FUNÇÃO PARA PROCESSAR NOMES - Converte texto em array de nomes
      function parseNames() {
        const raw = namesTextarea.value.trim(); // Remove espaços em branco
        if (!raw) return []; // Retorna array vazio se não há texto
        
        // Divide por linha, remove espaços extras e filtra linhas vazias
        return raw.split('\n').map(s => s.trim()).filter(Boolean);
      }

      // FUNÇÃO DE ALEATÓRIO - Gera número inteiro aleatório entre min e max
      function randomInt(min, max) {
        // Fórmula padrão para números inteiros aleatórios inclusivos
        return Math.floor(Math.random() * (max - min + 1)) + min;
      }

      // FUNÇÃO PARA CONSTRUIR LISTA - Cria elementos visuais da lista
      function buildPeopleList(namesArr, min, max) {
        peopleList.innerHTML = ''; // Limpa lista anterior
        
        // MODO COM NOMES - Se há nomes na textarea
        if (namesArr && namesArr.length) {
          namesArr.forEach(name => {
            const d = document.createElement('div'); // Cria elemento div
            d.className = 'person'; // Aplica classe CSS
            d.textContent = name; // Define o texto
            peopleList.appendChild(d); // Adiciona à lista
          });
          return; // Sai da função
        }
        
        // LIMITE DE EXIBIÇÃO - Evita listas muito grandes
        const cap = 1000;
        if (max - min > cap) {
          const note = document.createElement('div');
          note.className = 'person';
          // Mensagem de aviso para intervalos muito grandes
          note.textContent = 'Intervalo muito grande para listar. Use um intervalo menor ou cole nomes.';
          peopleList.appendChild(note);
          return;
        }
        
        // MODO NUMÉRICO - Gera lista de números sequenciais
        for (let i = min; i <= max; i++) {
          const d = document.createElement('div');
          d.className = 'person';
          d.textContent = String(i); // Converte número para string
          peopleList.appendChild(d);
        }
      }

      // FUNÇÃO PRINCIPAL DO SORTEIO - Lógica central da aplicação
      function doDraw() {
        // Captura valores dos campos de entrada
        let item = itemInput.value.trim() || 'Item'; // Nome do item ou padrão
        const names = parseNames(); // Processa lista de nomes
        let min = parseInt(minInput.value, 10); // Converte para inteiro
        let max = parseInt(maxInput.value, 10); // Converte para inteiro
        
        // VALIDAÇÃO - Garante valores mínimos válidos
        if (isNaN(min) || min < 1) min = 1;
        if (isNaN(max) || max < min) max = min;
        
        // RECONSTRÓI LISTA - Atualiza visual dos participantes
        buildPeopleList(names, min, max);
        
        let winnerText = ''; // Texto do resultado
        let winnerIndex = -1; // Índice do vencedor na lista
        
        // SORTEIO POR NOMES - Se há nomes na lista
        if (names.length) {
          const idx = randomInt(0, names.length - 1); // Índice aleatório
          winnerText = names[idx]; // Seleciona o nome
          winnerIndex = idx; // Define índice para highlight
        } else {
          // SORTEIO POR NÚMEROS - Se não há nomes
          const chosen = randomInt(min, max); // Número aleatório
          winnerText = String(chosen); // Converte para string
          winnerIndex = chosen - min; // Calcula índice na lista
        }
        
        // ATUALIZA RESULTADO - Mostra o ganhador
        resultItem.textContent = item; // Nome do item
        resultWinner.textContent = winnerText; // Nome do ganhador
        
        // DESTACA VENCEDOR - Aplica classe highlight
        const personDivs = Array.from(peopleList.querySelectorAll('.person'));
        personDivs.forEach((d, i) => {
          // Toggle da classe highlight baseado no índice
          d.classList.toggle('highlight', i === winnerIndex);
        });
        
        // SCROLL AUTOMÁTICO - Centraliza o vencedor na lista
        const highlighted = peopleList.querySelector('.person.highlight');
        if (highlighted) {
          highlighted.scrollIntoView({ 
            behavior: 'smooth', // Scroll suave
            block: 'center' // Centraliza na viewport
          });
        }
      }

      // EVENT LISTENER - Botão principal de sortear
      drawBtn.addEventListener('click', doDraw);

      // EVENT LISTENER - Botão de limpar formulário
      clearBtn.addEventListener('click', () => {
        // Limpa todos os campos de entrada
        itemInput.value = '';
        minInput.value = '1';
        maxInput.value = '10';
        namesTextarea.value = '';
        
        // Reseta área de resultado
        resultItem.textContent = '—';
        resultWinner.textContent = 'Pronto para sortear';
        
        // Limpa lista de participantes
        peopleList.innerHTML = '';
      });

      // EVENT LISTENER - Botão rápido 1-5
      quick5.addEventListener('click', () => {
        minInput.value = '1';
        maxInput.value = '5';
        doDraw(); // Executa sorteio imediatamente
      });

      // EVENT LISTENER - Botão rápido 1-10
      quick10.addEventListener('click', () => {
        minInput.value = '1';
        maxInput.value = '10';
        doDraw(); // Executa sorteio imediatamente
      });

      // INICIALIZAÇÃO - Carrega lista padrão ao abrir a página
      buildPeopleList([], parseInt(minInput.value, 10) || 1, parseInt(maxInput.value, 10) || 10);
    });
  </script>
</body>
</html>
