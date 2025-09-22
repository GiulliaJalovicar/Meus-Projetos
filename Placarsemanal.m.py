<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <!-- META TAGS - Configurações básicas da página -->
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>🏆 Placar RPG - Ranking Semanal</title>
  
  <!-- CSS - Estilos da página -->
  <style>
    /* ESTILOS GLOBAIS - Configurações gerais do corpo da página */
    body {
      font-family: "Segoe UI", Arial, sans-serif;
      background: linear-gradient(135deg, #1e1e2f, #2c2c54);
      color: white;
      margin: 0;
      padding: 20px;
      text-align: center;
      min-height: 100vh;
    }

    /* TÍTULO PRINCIPAL - Estilo do cabeçalho principal */
    h1 {
      font-size: 2.5em;
      margin-bottom: 20px;
      text-shadow: 2px 2px 8px rgba(0,0,0,0.6);
      background: linear-gradient(45deg, #ffd700, #ffed4e);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
      background-clip: text;
      font-weight: bold;
    }

    /* TABELA PRINCIPAL - Container da tabela de ranking */
    table {
      margin: auto;
      border-collapse: collapse;
      width: 80%;
      max-width: 900px;
      background: rgba(255,255,255,0.05);
      border-radius: 12px;
      overflow: hidden;
      box-shadow: 0 4px 20px rgba(0,0,0,0.5);
      border: 2px solid rgba(255,215,0,0.3);
    }

    /* CÉLULAS DA TABELA - Estilo geral para th e td */
    th, td {
      padding: 15px 12px;
      border-bottom: 1px solid rgba(255,255,255,0.1);
      text-align: center;
      transition: all 0.3s ease;
    }

    /* CABEÇALHO DA TABELA - Estilo das colunas de título */
    th {
      background: rgba(255,255,255,0.1);
      font-size: 1.1em;
      font-weight: bold;
      color: #ffd700;
      text-transform: uppercase;
      letter-spacing: 1px;
    }

    /* LINHAS PARES - Efeito zebra na tabela */
    tr:nth-child(even) {
      background: rgba(255,255,255,0.03);
    }

    /* EFEITO HOVER - Animação ao passar o mouse nas linhas */
    tr:hover {
      background: rgba(255,255,255,0.15);
      transform: scale(1.01);
      transition: all 0.3s ease;
    }

    /* PODIO - Estilos especiais para as 3 primeiras posições */
    .primeiro {
      background: linear-gradient(135deg, #ffd700, #ffed4e);
      color: #1e1e2f;
      font-weight: bold;
      box-shadow: 0 0 20px rgba(255,215,0,0.6);
    }

    .segundo {
      background: linear-gradient(135deg, #c0c0c0, #e5e5e5);
      color: #1e1e2f;
      font-weight: bold;
      box-shadow: 0 0 15px rgba(192,192,192,0.5);
    }

    .terceiro {
      background: linear-gradient(135deg, #cd7f32, #d4a574);
      color: #1e1e2f;
      font-weight: bold;
      box-shadow: 0 0 15px rgba(205,127,50,0.5);
    }

    /* POSIÇÃO ESPECIAL - Destaca posições de 4º a 10º */
    .top10 {
      background: rgba(255,215,0,0.1);
      border-left: 4px solid #ffd700;
    }

    /* MENSAGEM DE CARREGAMENTO - Estilo para loading */
    .loading {
      text-align: center;
      padding: 40px;
      font-size: 1.2em;
      color: #ffd700;
    }

    /* MENSAGEM DE ERRO - Estilo para erros de conexão */
    .error {
      text-align: center;
      padding: 40px;
      color: #ff6b6b;
      background: rgba(255,107,107,0.1);
      border-radius: 8px;
      margin: 20px auto;
      max-width: 600px;
    }

    /* RESPONSIVIDADE - Ajustes para telas menores */
    @media (max-width: 768px) {
      table {
        width: 95%;
        font-size: 0.9em;
      }
      
      th, td {
        padding: 10px 8px;
      }
      
      h1 {
        font-size: 2em;
      }
    }
  </style>
</head>

<body>
  <!-- CABEÇALHO PRINCIPAL - Título da página -->
  <h1>🏆 Ranking Semanal - RPG</h1>
  
  <!-- MENSAGEM DE CARREGAMENTO - Mostrada enquanto carrega os dados -->
  <div id="loading" class="loading">
    🔄 Carregando ranking em tempo real...
  </div>
  
  <!-- TABELA DE RANKING - Container principal dos dados -->
  <table id="placar">
    <!-- CABEÇALHO DA TABELA - Colunas fixas -->
    <thead>
      <tr>
        <th>🏅 Posição</th>
        <th>👤 Nome</th>
        <th>👥 Grupo</th>
        <th>⭐ Pontos</th>
      </tr>
    </thead>
    <tbody>
      <!-- LINHAS SERÃO POPULADAS VIA JAVASCRIPT -->
    </tbody>
  </table>

  <!-- Firebase SDK - Integração com banco de dados em tempo real -->
  <script type="module">
    // IMPORTAÇÕES DO FIREBASE - Carrega as bibliotecas necessárias
    import { 
      initializeApp 
    } from "https://www.gstatic.com/firebasejs/10.12.2/firebase-app.js";
    
    import { 
      getFirestore, 
      collection, 
      query, 
      orderBy, 
      onSnapshot,
      getDocs
    } from "https://www.gstatic.com/firebasejs/10.12.2/firebase-firestore.js";

    // CONFIGURAÇÃO DO FIREBASE - Credenciais do projeto
    const firebaseConfig = {
      apiKey: "AIzaSyDYetEdyCkoyHDn4YLZ7diPuuAuNlU-hik",
      authDomain: "placar-ad517.firebaseapp.com",
      projectId: "placar-ad517",
      storageBucket: "placar-ad517.appspot.com", // CORREÇÃO: .appspot.com em vez de .firebasestorage.app
      messagingSenderId: "661469222559",
      appId: "1:661469222559:web:b657cf46df0537130334aa",
      measurementId: "G-2EMK83SN4E"
    };

    // INICIALIZAÇÃO DO FIREBASE - Cria a instância do app
    const app = initializeApp(firebaseConfig);
    const db = getFirestore(app);

    // ELEMENTOS DO DOM - Referências aos elementos HTML
    const tabela = document.getElementById("placar");
    const loadingElement = document.getElementById("loading");
    const tbody = tabela.querySelector("tbody");

    // FUNÇÃO PARA APLICAR CLASSES DE PODIO - Define estilos para top 3
    function aplicarClassePosicao(posicao) {
      if (posicao === 1) return "primeiro";
      if (posicao === 2) return "segundo";
      if (posicao === 3) return "terceiro";
      if (posicao <= 10) return "top10";
      return "";
    }

    // FUNÇÃO PARA FORMATAR NÚMERO - Adiciona separadores de milhares
    function formatarNumero(numero) {
      return numero.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ".");
    }

    // FUNÇÃO PARA CRIAR LINHA DA TABELA - Gera HTML para cada jogador
    function criarLinhaTabela(doc, posicao) {
      const dados = doc.data();
      const nome = dados.nome || "Jogador Sem Nome";
      const grupo = dados.grupo || dados.membros || "-";
      const pontos = dados.pontos || 0;
      
      const classe = aplicarClassePosicao(posicao);
      
      return `
        <tr class="${classe}">
          <td>
            <span style="font-size: 1.2em; font-weight: bold;">
              ${posicao}º
            </span>
          </td>
          <td>
            <strong>${nome}</strong>
          </td>
          <td>${grupo}</td>
          <td>
            <span style="color: #ffd700; font-weight: bold; font-size: 1.1em;">
              ${formatarNumero(pontos)} pts
            </span>
          </td>
        </tr>
      `;
    }

    // FUNÇÃO PARA ATUALIZAR TABELA - Renderiza todos os dados
    function atualizarTabela(snapshot) {
      // OCULTA LOADING - Remove mensagem de carregamento
      loadingElement.style.display = "none";
      
      // LIMPA CORPO DA TABELA - Remove linhas anteriores
      tbody.innerHTML = "";
      
      let posicao = 1;
      
      // ITERA SOBRE DOCUMENTOS - Para cada jogador no ranking
      snapshot.forEach((doc) => {
        // CRIA E ADICIONA LINHA - Gera HTML e insere na tabela
        const linhaHTML = criarLinhaTabela(doc, posicao);
        tbody.innerHTML += linhaHTML;
        posicao++;
      });
      
      // LOG DE DEBUG - Informações no console
      console.log(`📊 Ranking atualizado - ${snapshot.size} jogadores carregados`);
      
      // VERIFICAÇÃO DE DADOS VAZIOS - Mensagem se não há dados
      if (snapshot.empty) {
        tbody.innerHTML = `
          <tr>
            <td colspan="4" style="padding: 40px; color: #888;">
              🏆 Ainda não há participantes no ranking desta semana!
            </td>
          </tr>
        `;
      }
    }

    // CONFIGURAÇÃO DA QUERY - Ordena por pontos (maior para menor)
    const q = query(
      collection(db, "placar"), 
      orderBy("pontos", "desc")
    );

    // OBSERVADOR EM TEMPO REAL - Escuta mudanças na coleção
    onSnapshot(q, 
      // CALLBACK DE SUCESSO - Quando dados são recebidos
      (snapshot) => {
        atualizarTabela(snapshot);
      },
      
      // CALLBACK DE ERRO - Em caso de falha na conexão
      (error) => {
        console.error("❌ Erro ao carregar ranking:", error);
        
        // MOSTRA MENSAGEM DE ERRO - Interface para o usuário
        loadingElement.style.display = "none";
        tabela.style.display = "none";
        
        const erroDiv = document.createElement("div");
        erroDiv.className = "error";
        erroDiv.innerHTML = `
          <h3>⚠️ Erro de Conexão</h3>
          <p>Não foi possível carregar o ranking. Verifique sua conexão.</p>
          <p><strong>Código do erro:</strong> ${error.code}</p>
          <button onclick="window.location.reload()" 
                  style="background: #ffd700; color: #1e1e2f; padding: 10px 20px; border: none; border-radius: 5px; cursor: pointer; margin-top: 10px;">
            🔄 Tentar Novamente
          </button>
        `;
        document.body.insertBefore(erroDiv, tabela);
      }
    );

    // FUNÇÃO DE TESTE - Para verificar conexão (opcional)
    window.testarConexao = async () => {
      try {
        console.log("🧪 Testando conexão com Firestore...");
        const testSnapshot = await getDocs(collection(db, "placar"));
        console.log(`✅ Conexão OK - ${testSnapshot.size} documentos encontrados`);
        alert("Conexão funcionando perfeitamente! 🎉");
      } catch (error) {
        console.error("❌ Falha na conexão:", error);
        alert("Erro na conexão: " + error.message);
      }
    };

    // EVENTO DE CARREGAMENTO - Inicialização da página
    window.addEventListener('load', () => {
      console.log("🚀 Placar RPG inicializado - Monitorando ranking em tempo real");
      
      // MOSTRA LOADING INICIAL - Feedback visual
      loadingElement.style.display = "block";
    });

    // INTERVALO DE ATUALIZAÇÃO VISUAL - Pisca o título a cada minuto
    setInterval(() => {
      const h1 = document.querySelector('h1');
      h1.style.transform = 'scale(1.02)';
      setTimeout(() => {
        h1.style.transform = 'scale(1)';
      }, 200);
    }, 60000);
  </script>
</body>
</html>
