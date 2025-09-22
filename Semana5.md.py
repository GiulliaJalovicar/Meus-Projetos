<!DOCTYPE html>
<html lang="pt-br">
<head>
  <!-- META TAGS - Configurações básicas da página -->
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Casa da Moeda - Vale do Espantalho</title>
  
  <!-- CSS - Estilos da página -->
  <style>
    /* IMPORTAÇÃO DE FONTES - Carrega fontes do Google Fonts */
    @import url('https://fonts.googleapis.com/css2?family=Cinzel+Decorative:wght@700&family=Cardo&display=swap');

    /* ESTILOS GLOBAIS - Configurações gerais do corpo da página */
    body {
      font-family: 'Cardo', serif;
      background: url('https://www.transparenttextures.com/patterns/aged-paper.png');
      margin: 0;
      padding: 0;
      color: #2c1c18;
      font-size: 18px;
      line-height: 1.6;
    }

    /* HEADER - Estilo do cabeçalho principal */
    header {
      background: linear-gradient(135deg, #6a3b2e, #3b1f1a);
      color: #f4d58d;
      padding: 20px 10px;
      text-align: center;
      font-family: 'Cinzel Decorative', cursive;
      letter-spacing: 2px;
      box-shadow: 0 4px 15px rgba(0,0,0,0.5);
      border-bottom: 4px solid #d4af37;
    }

    header h1 {
      font-size: 1.8em;
      margin: 0;
      text-shadow: 2px 2px 6px rgba(0,0,0,0.7);
    }

    /* EXIBIÇÃO DA MOEDA - Seção que mostra a imagem da moeda */
    .coin-display {
      text-align: center;
      margin: 20px;
    }

    .coin-display img {
      width: 160px;
      height: 160px;
      object-fit: cover;
      border-radius: 50%;
      border: 5px solid #d4af37;
      box-shadow: 0 0 25px rgba(0,0,0,0.5), inset 0 0 15px rgba(255,215,0,0.7);
    }

    .coin-display p {
      margin-top: 12px;
      font-style: italic;
      color: #5a322e;
      font-size: 1.1em;
    }

    /* SEÇÕES - Estilo geral para as seções de conteúdo */
    section {
      padding: 20px;
      margin: 20px;
      background: #fdf6e3;
      border-radius: 15px;
      box-shadow: 0 3px 12px rgba(0,0,0,0.3);
      border: 3px solid #d4af37;
    }

    /* TÍTULOS H2 - Estilo dos títulos das seções */
    h2 {
      color: #6a3b2e;
      font-family: 'Cinzel Decorative', cursive;
      font-size: 1.5em;
      margin-bottom: 15px;
      text-align: center;
    }

    /* DIVISORES - Separadores decorativos entre seções */
    .divider {
      text-align: center;
      font-size: 22px;
      color: #d4af37;
      margin: 10px 0 20px 0;
    }

    /* LISTAS - Estilo das listas sem marcadores */
    ul {
      list-style: none;
      padding-left: 0;
    }

    ul li {
      margin: 12px 0;
      padding-left: 35px;
      position: relative;
    }

    /* ÍCONE PERSONALIZADO - Cria moedas como marcadores de lista */
    ul li::before {
      content: "";
      position: absolute;
      left: 0;
      top: 4px;
      width: 20px;
      height: 20px;
      border-radius: 50%;
      background: radial-gradient(circle at 30% 30%, #ffd700, #b8860b);
      border: 2px solid #8b7500;
      box-shadow: inset 0 0 4px rgba(255,255,255,0.6), 0 0 6px rgba(0,0,0,0.4);
    }

    /* CONTAINER DO PLACAR - Layout em grid para os cards */
    .placar-container {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(180px, 1fr));
      gap: 20px;
    }

    /* CARDS DO PLACAR - Estilo individual dos cards de jogadores */
    .card {
      background: #fff8dc;
      border: 2px solid #d4af37;
      border-radius: 15px;
      box-shadow: 0 4px 10px rgba(0,0,0,0.3);
      text-align: center;
      padding: 15px;
      transition: transform 0.2s;
    }

    .card:hover {
      transform: scale(1.05);
    }

    .card h3 {
      font-family: 'Cinzel Decorative', cursive;
      color: #3b1f1a;
      margin-bottom: 10px;
    }

    /* VALOR DAS MOEDAS - Destaque para o número de moedas */
    .moedas {
      font-size: 1.5em;
      font-weight: bold;
      color: #b8860b;
      margin-bottom: 10px;
    }

    /* BOTÕES - Container para os botões de incremento/decremento */
    .buttons {
      display: flex;
      justify-content: center;
      gap: 10px;
    }

    .buttons button {
      background: #d4af37;
      border: none;
      padding: 6px 12px;
      border-radius: 8px;
      cursor: pointer;
      font-weight: bold;
      color: #3b1f1a;
      transition: background 0.3s;
    }

    .buttons button:hover {
      background: #b8860b;
    }

    /* FOOTER - Estilo do rodapé */
    footer {
      background: #3b1f1a;
      color: #f4d58d;
      text-align: center;
      padding: 15px;
      font-size: 15px;
      border-top: 4px solid #d4af37;
      box-shadow: 0 -4px 12px rgba(0,0,0,0.6);
      font-family: 'Cinzel Decorative', cursive;
    }
  </style>
</head>

<body>
  <!-- HEADER - Cabeçalho principal da página -->
  <header>
    <h1>🏛 Casa da Moeda de Vale do Espantalho 🏛</h1>
  </header>

  <!-- EXIBIÇÃO DA MOEDA - Seção que mostra a imagem oficial da moeda -->
  <div class="coin-display">
    <img src="https://via.placeholder.com/160x160/6a3b2e/d4af37?text=Moeda" alt="Moeda Oficial">
    <!-- CORREÇÃO: Removido caminho local, usando placeholder -->
    <p>Espiga Coin – Símbolo da prosperidade e sobrevivência do vale</p>
  </div>

  <!-- SEÇÃO INFORMAÇÕES DA MOEDA - Detalhes sobre a moeda oficial -->
  <section>
    <h2>Moeda da Cidade</h2>
    <div class="divider">✦</div>
    <p><strong>Nome:</strong> Espiga Coins</p>
    <p><strong>Valor:</strong> 1 Espiga Coin = 1 unidade de valor local</p>
    <p><strong>Controle:</strong> Casa da Moeda sob proteção real</p>
  </section>

  <!-- SEÇÃO PROCESSO DE PRODUÇÃO - Informações sobre fabricação -->
  <section>
    <h2>Produção</h2>
    <div class="divider">⚒️</div>
    <ul>
      <li>1 ferro consegue fazer 15 unidades de moeda.</li>
      <li>Multas: trocas irregulares da moeda entre jogadores (sem autorização da casa da moeda).</li>
      <li>Averiguação feita pelos mestres da Casa da Moeda.</li>
    </ul>
  </section>

  <!-- SEÇÃO CURIOSIDADES - Fatos interessantes sobre o sistema monetário -->
  <section>
    <h2>Curiosidades</h2>
    <div class="divider">⚔️</div>
    <ul>
      <li><strong>Tributo Real:</strong> Mercadão pagam uma taxa à cidade em suas trocas.</li>
      <li><strong>Ter a Espiga Coin:</strong> Apenas fazendo as missões semanais e o salário do distrito.</li>
      <li><strong>Segurança:</strong> O Quartel é o único que impede falsificações.</li>
    </ul>
  </section>

  <!-- SEÇÃO PLACAR DE MOEDAS - Exibição em tempo real das moedas dos jogadores -->
  <section>
    <h2>Placar de Moedas</h2>
    <div class="divider">💰</div>
    <div class="placar-container" id="placar">
      <!-- Cards dos jogadores serão carregados dinamicamente via JavaScript -->
    </div>
  </section>

  <!-- FOOTER - Rodapé com informações de copyright -->
  <footer>
    <p>© 2025 Casa da Moeda de Vale do Espantalho – Todos os direitos reservados</p>
  </footer>

  <!-- JAVASCRIPT - Lógica de integração com Firebase -->
  <script type="module">
    // IMPORTAÇÕES DO FIREBASE - Carrega as bibliotecas necessárias
    import { initializeApp } from "https://www.gstatic.com/firebasejs/10.12.0/firebase-app.js";
    import { 
      getFirestore, 
      collection, 
      onSnapshot, 
      doc, 
      updateDoc,
      query,
      orderBy 
    } from "https://www.gstatic.com/firebasejs/10.12.0/firebase-firestore.js";
    // CORREÇÃO: Import correto do Firestore (não database)

    // CONFIGURAÇÃO DO FIREBASE - Credenciais do projeto
    const firebaseConfig = {
      apiKey: "AIzaSyBmR7MTbn5IAeMZFYrccZ-gRrWwfst0yqY",
      authDomain: "cidade-do-espantalho.firebaseapp.com",
      projectId: "cidade-do-espantalho",
      storageBucket: "cidade-do-espantalho.appspot.com",
      messagingSenderId: "716072345880",
      appId: "1:716072345880:web:549f953a1068aa5885be6d"
    };

    // INICIALIZAÇÃO DO FIREBASE - Cria a instância do app
    const app = initializeApp(firebaseConfig);
    const db = getFirestore(app); // CORREÇÃO: Firestore em vez de Realtime Database

    // ELEMENTO DO DOM - Referência ao container do placar
    const placarContainer = document.getElementById("placar");

    // FUNÇÃO DE CARREGAMENTO INICIAL - Executa quando a página carrega
    window.onload = function() {
      console.log("Página carregada - Sistema de moedas inicializado");
    };

    // OBSERVADOR EM TEMPO REAL - Escuta mudanças na coleção "participantes"
    const q = query(collection(db, "participantes"), orderBy("moedas", "desc"));
    onSnapshot(q, (snapshot) => {
      // LIMPA O CONTAINER - Remove cards anteriores antes de recarregar
      placarContainer.innerHTML = "";
      
      // ITERA SOBRE OS DOCUMENTOS - Para cada jogador no Firestore
      snapshot.forEach((docSnap) => {
        const data = docSnap.data();
        const id = docSnap.id;
        const nome = data.nome || "Jogador Sem Nome";
        const moedas = data.moedas || 0;

        // CRIA O CARD - Elemento HTML para cada jogador
        const card = document.createElement("div");
        card.className = "card";
        card.innerHTML = `
          <h3>${nome}</h3>
          <div class="moedas" id="moedas-${id}">${moedas} 💰</div>
          <div class="buttons">
            <button onclick="alterarMoedas('${id}', ${moedas - 1})" ${moedas <= 0 ? 'disabled' : ''}>-</button>
            <button onclick="alterarMoedas('${id}', ${moedas + 1})">+</button>
          </div>
        `;
        
        // ADICIONA O CARD - Ao container do placar
        placarContainer.appendChild(card);
      });
      
      console.log(`Placar atualizado - ${snapshot.size} jogadores carregados`);
    }, (error) => {
      // TRATAMENTO DE ERRO - Em caso de falha na conexão
      console.error("Erro ao carregar placar:", error);
      placarContainer.innerHTML = '<p style="color: red; text-align: center;">Erro ao carregar dados</p>';
    });

    // FUNÇÃO DE ALTERAÇÃO DE MOEDAS - Atualiza o valor no Firestore
    window.alterarMoedas = async (id, novoValor) => {
      // VALIDAÇÃO - Não permite valores negativos
      if (novoValor < 0) {
        alert("Não é possível ter moedas negativas!");
        return;
      }

      try {
        // REFERÊNCIA DO DOCUMENTO - Localiza o jogador no Firestore
        const jogadorRef = doc(db, "participantes", id);
        
        // ATUALIZA O DOCUMENTO - Salva o novo valor
        await updateDoc(jogadorRef, { 
          moedas: novoValor,
          ultimaAtualizacao: new Date()
        });
        
        console.log(`Moedas atualizadas para ${id}: ${novoValor}`);
      } catch (error) {
        // TRATAMENTO DE ERRO - Em caso de falha na atualização
        console.error("Erro ao atualizar moedas:", error);
        alert("Erro ao atualizar moedas. Tente novamente.");
      }
    };

    // FUNÇÃO DE DEBUG - Para testar a conexão (opcional)
    window.testarConexao = async () => {
      try {
        const testDoc = await getDoc(doc(db, "test", "connection"));
        console.log("Conexão com Firestore OK:", testDoc.data());
      } catch (error) {
        console.error("Erro na conexão:", error);
      }
    };
  </script>
</body>
</html>
