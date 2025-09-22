<!DOCTYPE html>
<html lang="pt-br">
<head>
  <!-- Meta tags essenciais para a codificação e responsividade -->
  <meta charset="UTF-8"> <!-- Define o conjunto de caracteres para UTF-8, suportando acentuação e caracteres especiais -->
  <meta name="viewport" content="width=device-width, initial-scale=1.0"> <!-- Torna a página responsiva em dispositivos móveis -->
  <title>Casa da Moeda - Vale do Espantalho</title> <!-- O título da página, que aparece na aba do navegador -->
  
  <style>
    /* Importação de fontes externas para o estilo da página */
    @import url('https://fonts.googleapis.com/css2?family=Cinzel+Decorative:wght@700&family=Cardo&display=swap');

    /* Estilos do corpo da página */
    body {
      font-family: 'Cardo', serif; /* Define a fonte do corpo do texto */
      background: url('https://www.transparenttextures.com/patterns/aged-paper.png'); /* Imagem de fundo com textura de papel envelhecido */
      margin: 0; /* Remove as margens padrão */
      padding: 0; /* Remove o padding padrão */
      color: #2c1c18; /* Cor do texto */
      font-size: 18px; /* Tamanho da fonte */
      line-height: 1.6; /* Distância entre linhas do texto */
    }

    /* Estilos do cabeçalho da página */
    header {
      background: linear-gradient(135deg, #6a3b2e, #3b1f1a); /* Cor de fundo com gradiente */
      color: #f4d58d; /* Cor do texto do cabeçalho */
      padding: 20px 10px; /* Espaçamento interno */
      text-align: center; /* Alinha o conteúdo ao centro */
      font-family: 'Cinzel Decorative', cursive; /* Fonte decorativa */
      letter-spacing: 2px; /* Espaçamento entre as letras */
      box-shadow: 0 4px 15px rgba(0,0,0,0.5); /* Sombra ao redor do cabeçalho */
      border-bottom: 4px solid #d4af37; /* Borda inferior */
    }

    /* Estilos do título dentro do cabeçalho */
    header h1 {
      font-size: 1.8em; /* Define o tamanho do título */
      margin: 0; /* Remove margens ao redor do título */
      text-shadow: 2px 2px 6px rgba(0,0,0,0.7); /* Sombra no texto */
    }

    /* Exibição da moeda */
    .coin-display {
      text-align: center; /* Alinha o conteúdo ao centro */
      margin: 20px; /* Adiciona uma margem ao redor */
    }

    .coin-display img {
      width: 160px; /* Define a largura da imagem */
      height: 160px; /* Define a altura da imagem */
      object-fit: cover; /* Faz a imagem cobrir toda a área sem distorcer */
      border-radius: 50%; /* Torna a imagem circular */
      border: 5px solid #d4af37; /* Borda dourada ao redor da imagem */
      box-shadow: 0 0 25px rgba(0,0,0,0.5), inset 0 0 15px rgba(255,215,0,0.7); /* Sombra na imagem */
    }

    .coin-display p {
      margin-top: 12px; /* Adiciona espaço entre a imagem e o texto */
      font-style: italic; /* Torna o texto em itálico */
      color: #5a322e; /* Cor do texto */
      font-size: 1.1em; /* Tamanho da fonte do texto */
    }

    /* Estilos das seções */
    section {
      padding: 20px; /* Define o padding interno */
      margin: 20px; /* Define o espaço externo */
      background: #fdf6e3; /* Cor de fundo das seções */
      border-radius: 15px; /* Borda arredondada */
      box-shadow: 0 3px 12px rgba(0,0,0,0.3); /* Sombra na seção */
      border: 3px solid #d4af37; /* Borda dourada ao redor da seção */
    }

    /* Títulos das seções */
    h2 {
      color: #6a3b2e; /* Cor do título */
      font-family: 'Cinzel Decorative', cursive; /* Fonte do título */
      font-size: 1.5em; /* Tamanho do título */
      margin-bottom: 15px; /* Margem abaixo do título */
      text-align: center; /* Alinha o título ao centro */
    }

    /* Separadores de seções (decorativos) */
    .divider {
      text-align: center; /* Alinha ao centro */
      font-size: 22px; /* Tamanho da fonte */
      color: #d4af37; /* Cor dourada */
      margin: 10px 0 20px 0; /* Margens */
    }

    /* Estilos da lista */
    ul {
      list-style: none; /* Remove os pontos padrão da lista */
      padding-left: 0; /* Remove o padding à esquerda */
    }

    ul li {
      margin: 12px 0; /* Define a margem ao redor de cada item */
      padding-left: 35px; /* Adiciona padding à esquerda */
      position: relative; /* Necessário para a posição absoluta do ícone */
    }

    /* Ícone de lista personalizado (moeda) */
    ul li::before {
      content: ""; /* Necessário para exibir o ícone */
      position: absolute; /* Posiciona o ícone de forma absoluta */
      left: 0; /* Alinha à esquerda */
      top: 4px; /* Alinha um pouco abaixo do topo */
      width: 20px; /* Define o tamanho do ícone */
      height: 20px; /* Define o tamanho do ícone */
      border-radius: 50%; /* Torna o ícone redondo */
      background: radial-gradient(circle at 30% 30%, #ffd700, #b8860b); /* Gradiente radial para o ícone */
      border: 2px solid #8b7500; /* Borda dourada ao redor do ícone */
      box-shadow: inset 0 0 4px rgba(255,255,255,0.6), 0 0 6px rgba(0,0,0,0.4); /* Sombra no ícone */
    }

    /* Estilos do rodapé */
    footer {
      background: #3b1f1a; /* Cor de fundo do rodapé */
      color: #f4d58d; /* Cor do texto */
      text-align: center; /* Alinha o texto ao centro */
      padding: 15px; /* Padding interno */
      font-size: 15px; /* Tamanho da fonte */
      border-top: 4px solid #d4af37; /* Borda superior dourada */
      box-shadow: 0 -4px 12px rgba(0,0,0,0.6); /* Sombra no rodapé */
      font-family: 'Cinzel Decorative', cursive; /* Fonte decorativa */
    }
  </style>
</head>
<body>
  <!-- Cabeçalho da página -->
  <header>
    <h1>🏛 Casa da Moeda de Vale do Espantalho 🏛</h1> <!-- Título principal da página -->
  </header>

  <!-- Exibição da moeda -->
  <div class="coin-display">
    <img src="https://static.wixstatic.com/media/371a13_074e9c94648e476a984ca8bcf4ee60e4~mv2.jpg/v1/fill/w_480,h_480,al_c,q_80,usm_0.66_1.00_0.01,enc_avif,quality_auto/371a13_074e9c94648e476a984ca8bcf4ee60e4~mv2.jpg" alt="Moeda Oficial"> <!-- Imagem da moeda -->
    <p>Espiga Coin – Símbolo da prosperidade e sobrevivência do vale</p> <!-- Descrição da moeda -->
  </div>

  <!-- Seção sobre a moeda -->
  <section>
    <h2>Moeda da Cidade</h2> <!-- Título da seção -->
    <div class="divider">✦</div> <!-- Separador decorativo -->
    <p><strong>Nome:</strong> Espiga Coins</p> <!-- Nome da moeda -->
    <p><strong>Valor:</strong> 1 Espiga Coin = 1 unidade de valor local</p> <!-- Valor da moeda -->
    <p><strong>Controle:</strong> Casa da Moeda sob proteção real</p> <!-- Informação sobre o controle da moeda -->
  </section>

  <!-- Seção sobre a Produção das Moedas -->
  <section>
    <h2>Produção</h2> <!-- Título da seção -->
    <div class="divider">⚒️</div> <!-- Separador decorativo -->
    <ul>
      <li>1 ferro consegue fazer 15 unidades de moeda.</li> <!-- Informação sobre a produção -->
      <li>Multas: troca irregular da moeda entre jogadores (sem autorização da casa da moeda).</li> <!-- Informação sobre trocas irregulares -->
      <li>Averiguação feita pelos mestres da Casa da Moeda.</li> <!-- Informação sobre fiscalização -->
    </ul>
  </section>

  <!-- Seção sobre Curiosidades da Moeda -->
  <section>
    <h2>Curiosidades</h2> <!-- Título da seção -->
    <div class="divider">⚔️</div> <!-- Separador decorativo -->
    <ul>
      <li><strong>Tributo Real:</strong> Mercadões pagam uma taxa à cidade em suas trocas.</li> <!-- Curiosidade sobre tributo -->
      <li><strong>Ter a Espiga Coin:</strong> Apenas fazendo as missões semanais e o salário do distrito.</li> <!-- Como obter a moeda -->
      <li><strong>Segurança:</strong> O Quartel é o único que impede falsificações.</li> <!-- Informações sobre a segurança da moeda -->
    </ul>
  </section>

  <!-- Rodapé da página -->
  <footer>
    <p>© 2025 Casa da Moeda de Vale do Espantalho – Todos os direitos reservados</p> <!-- Direitos autorais -->
  </footer>
</body>
</html>
