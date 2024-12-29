# EmergencyFlow: Sistema de Otimização de Rotas para Auxílio Humanitário

## Descrição do Projeto
EmergencyFlow é um sistema de otimização de rotas desenvolvido para auxiliar na logística de distribuição de suprimentos durante desastres naturais. Utilizando conceitos de teoria dos grafos e fluxo em redes, o sistema calcula rotas otimizadas para garantir a entrega eficiente de recursos às áreas afetadas.

## Modelagem do Problema

### Estrutura de Dados
O projeto utiliza uma combinação de Lista de Arestas e Dicionário de Vértices para representar o grafo. Esta escolha foi baseada nas seguintes considerações:

1. **Flexibilidade na Representação**
   - Facilita a adição de atributos extras em vértices e arestas
   - Permite representação natural de informações como estado da rota e tipos de suprimentos
   - Suporta atualizações dinâmicas do estado da rede

2. **Eficiência Computacional**
   - Acesso O(1) aos vértices através do dicionário
   - Iteração eficiente sobre arestas para encontrar caminhos aumentantes
   - Boa performance para grafos esparsos

3. **Manutenibilidade**
   - Estrutura orientada a objetos clara e modular
   - Facilidade de debug e visualização
   - Código mais legível e organizado

### Algoritmo de Ford-Fulkerson
O algoritmo de Ford-Fulkerson foi escolhido para resolver o problema de fluxo máximo pelos seguintes motivos:

1. **Adequação ao Problema**
   - Garante a otimalidade do fluxo máximo
   - Permite adaptações para múltiplas restrições
   - Funciona bem com a estrutura de dados escolhida

2. **Características**
   - Complexidade O(|E|·f), onde |E| é o número de arestas e f é o fluxo máximo
   - Facilita a incorporação de restrições adicionais



## Funcionalidades

1. **Gestão de Rotas**
   - Adição/remoção de rotas
   - Atualização de status de disponibilidade
   - Monitoramento de capacidade

2. **Otimização de Fluxo**
   - Cálculo de rotas otimizadas
   - Consideração de múltiplas restrições
   - Adaptação a mudanças em tempo real

3. **Análise de Rede**
   - Identificação de gargalos
   - Sugestão de rotas alternativas
   - Relatórios de utilização

## Requisitos
- Python 3.8+
- Bibliotecas: (listar dependências)

## Instalação e Uso
```bash
# Clone o repositório
git clone https://github.com/seu-usuario/reliefroute.git

# Instale as dependências
pip install -r requirements.txt

# Execute o programa
python main.py
```

## Exemplo de Uso
```python
# Criar uma instância do grafo
grafo = Grafo()

# Adicionar vértices
grafo.adicionar_vertice("A", "origem")
grafo.adicionar_vertice("B", "intermediario")
grafo.adicionar_vertice("C", "destino")

# Adicionar arestas
grafo.adicionar_aresta("A", "B", 100, 10)
grafo.adicionar_aresta("B", "C", 50, 5)

# Calcular fluxo máximo
fluxo = grafo.calcular_fluxo_maximo("A", "C")
```

## Decisões de Projeto

### Por que Lista de Arestas + Dicionário de Vértices?
1. **Flexibilidade**: Facilita a adição de novos atributos e funcionalidades
2. **Performance**: Boa eficiência para as operações mais comuns
3. **Clareza**: Estrutura intuitiva e fácil de manter

### Por que Ford-Fulkerson?
1. **Simplicidade**: Algoritmo bem estabelecido e de fácil implementação
2. **Adaptabilidade**: Pode ser modificado para incluir restrições adicionais
3. **Garantia**: Encontra sempre o fluxo máximo ótimo

## Limitações e Trabalhos Futuros

### Limitações Atuais
- Não considera múltiplos tipos de suprimentos simultaneamente
- Assume capacidades constantes nas arestas
- Não implementa priorização dinâmica

### Melhorias Planejadas
1. Suporte a múltiplos tipos de recursos
2. Implementação de priorização dinâmica
3. Interface gráfica para visualização
4. Sistema de log e monitoramento em tempo real

## Licença
MIT License - veja o arquivo LICENSE.md para detalhes

## Contato
[Seu Nome] - [seu.email@dominio.com]

## Agradecimentos
- Professor [Nome] pela orientação
- [Outros agradecimentos relevantes]