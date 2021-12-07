![Logo Semáforo Inteligente](https://github.com/Delmith/TCC_SemaforoInteligente/blob/main/Misc/Logo.png)

# Semaforo Inteligente

## Descrição

O transporte rodoviário é o modal mais utilizado nas grandes metrópoles e cada vez mais temos veículos transitando nas vias públicas. Há uma maior necessidade de controle de tráfego, evitando acidentes e controlando o fluxo das estradas, portanto, o semáforo torna-se um dos itens mais indispensável e necessário que possa se adaptar a um ambiente volátil como o trânsito. Neste trabalho buscamos propor uma solução viável que atenda a melhora no índice chave de fluidez e consequente redução no congestionamento e tempo de espera no semáforo, além disto, inicialmente, com um custo mais baixo em comparação a outras formas de mitigação deste problema. Este projeto se baseia num modelo virtual de via com volumetria de trafego variável para determinada hora e utilizando-se de duas categorias de alternância dos estados do semáforo sendo uma forma tradicional, temporizada, e a outra, a proposta apresentada neste trabalho. Verificou-se grande diferença entre os métodos utilizados no controle do tráfego com reduções de até cinquenta por cento nos valores analisados para algumas amostragens. A partir destes resultados, pudemos concluir que ao utilizarmos semáforos inteligentes, que utilizam dados baseados na volumetria e horário, somos capazes de reduzir o tempo total de espera nos semáforos, consequentemente, o tempo total das viagens nas rodovias urbanas das grandes metrópoles sem despender, primeiramente, de grande valor monetário e tempo para adequação.

## Objeto de Estudo do Projeto

Foram encontradas interseções problemáticas em certos horários do dia, principalmente nos horários de ida e volta do trabalho. Como critério para eliminação de outros possíveis cruzamentos, foram considerados apenas cruzamentos semaforizados com distância para outro semáforo qualquer de no mínimo 300 metros e que houvesse ao menos 3 travessias conflitantes.

### Cruzamento Utilizado

O local selecionado foi o cruzamento das Ruas Cândido Benício com a Capitão Menezes, próximo ao mercado mundial e a estação do BRT Capitão Menezes:

![Semáforo Rua Cândido Benício pista direção norte.](https://github.com/Delmith/TCC_SemaforoInteligente/blob/main/Misc/SemaforoCandidoBen%C3%ADcio.png)
Rua Cândido Benício no sentido Cascadura. Via principal com maior fluxo de veículos e maior prioridade. Atribuído o ID 'gneE2' no modelo virtual utilizado.

![Semáforo Rua Cândido Benício pista direção sul.](https://github.com/Delmith/TCC_SemaforoInteligente/blob/main/Misc/SemaforoCandidoBenicioSul.png)
Rua Cândido Benício em direção a Praça Seca, via principal com maior fluxo de veículos. Para esta via foi atribuído o ID 'gneE0' no modelo virtual.

![Rua Capitão Menezes mão única.](https://github.com/Delmith/TCC_SemaforoInteligente/blob/main/Misc/SemaforoCapitaoMenezesOeste.png)
Rua Capitão Menezes entre os números 643 e 803. Via concorrente da principal de menor densidade de veículos. Utilizado o ID 'gneE9' para identificação desta aresta na simulação.

![Rua Capitão Menezes mão dupla.](https://github.com/Delmith/TCC_SemaforoInteligente/blob/main/Misc/SemaforoCapitaoMenezesLeste.png)
Via de mão única na Rua Capitão Menezes próximo ao número 1051, via com o menor fluxo de veículos observado. Dado o ID 'gneE11' para identificação da rua no modelo virtual.

Vista aérea do cruzamento com o gráfico de trafego na região para dado horário.

![Vista aérea](https://github.com/Delmith/TCC_SemaforoInteligente/blob/main/Misc/Vista%20a%C3%A9rea%20.png)

### Dados de volumetria do tráfego

Para encontrarmos os horários de pico testados neste trabalho utilizamos dados quantitativos disponíveis no sítio web: https://www.tomtom.com/en_gb/traffic-index/rio-de-janeiro-traffic/ referentes ao ano de 2020 para o Rio de Janeiro. Segundo o sítio teve, no período do ano passado, a seguinte taxa de congestionamento no estado:

![Congestionamento Semanal por horário - 2020 Rio de janeiro.](https://github.com/Delmith/TCC_SemaforoInteligente/blob/main/Misc/TabelaTransitoRiodeJaneiro.png)

Foi escolhido, desta forma, o pior dia da semana e três horários distintos neste dia um com pouco tráfego outro com uma boa média de congestionamento e o pico registrado:
Horas, dia e volumes selecionados para teste.

| Horários | Sexta-feira |
|:--------:|:-----------:|
| 04:00    | 0%          |
| 09:00    | 38%         |
| 18:00    | 69%         |

Como não foi possível encontrar um valor Real para a volumetria diária e os únicos dados disponíveis eram o percentil deste valor. Fizemos testes no simulador estressando a via com o máximo possível de carros e reduzindo as quantidades de automóveis para adequação no percentual encontrado para o horário. A faixa de 100% das vias ficou entre 1304 a 1468 carros por hora na via sem considerar outros tipos de automóveis.

## SUMO

[SUMO](https://www.eclipse.org/sumo/) consiste em vários programas separados para diferentes tarefas relacionadas a simulação. Apenas o sumo-gui (sumo-gui.exe) e o netedit (netedit.exe) tem uma interface gráfica (GUI). Todos os outros programas devem ser utilizados pelo prompt de comando. Para este estudo utilizamos as aplicações com interface gráfica para visualização da simulação, porém os testes ocorreram através do uso da aplicação sumo (sumo.exe), que não contem interface gráfica.

O comando que foi utilizado no sumo que foi replicado, salvo alteração dos arquivos ",sumocfg" para adequação da densidade do tráfego baseado em horários específicos do dia, foi:

`sumo -c map_0.sumocfg --duration-log.statistics`

E utilizamos o seguinte comando para visualizarmos a simulação com interface gráfica:

`sumo-gui -c map_69.sumocfg --duration-log.statistics`


## Arquivos Básicos

### Arquivo gerador da malha viária

O arquivo com as ruas, vias, estradas, interseções, etc. Chamado neste estudo, e que será comum a todas as simulações, de "CruzamentoBRT.net.xml" foi criado utilizando-se a aplicação netedit 

### Arquivo gerador da demanda de tráfego

O arquivo de demanda do tráfego também precisa ser especificado. Este arquivo descreve as categorias de veículos e suas rotas. Para este trabalho construiu-se um arquivo para cada horário com cargas de veículos diferentes chamados de "cruzamentoBRT_0.rou.xml", "cruzamentoBRT_38.rou.xml" e "cruzamentoBRT_69.rou.xml".

###  Arquivo de configuração do simulador

Os arquivos descritos acima são utilizados como base para a simulação e carregados no arquivo ".sumocfg". Para os testes deste trabalho, respeitando a alteração da volumetria do tráfego para horários diferentes, foram criados três arquivos distintos de configuração, foram eles:

| Arquivo        | Horário | Volume |
|----------------|---------|--------|
| map_0.sumocfg  | 04:00   | 0%     |
| map_38.sumocfg | 09:00   | 38%    |
| map_69.sumocfg | 18:00   | 69%    |

## Semáforo Inteligente

### Bibliotecas utilizadas

Foram utilizadas as seguintes bibliotecas no código:

```
import os
import traci
```

| Módulo       | Descrição                                                                                                                          |
|--------------|------------------------------------------------------------------------------------------------------------------------------------|
| import os    | Este módulo fornece meios de utilizar as funcionalidades dependentes do sistema operacional.                                       |
| import traci | Dá acesso a uma simulação de tráfego viário em execução, permitindo recuperar valores de objetos na simulação e a sua manipulação. |

### Carregamento dos dados

Carregamos as variáveis com as informações necessárias para os parâmetros da linha de comando que inicia a simulação, questionando se irá rodar apenas o "sumo" ou o "sumo-gui", com interface gráfica. Além de solicitar a escolha do arquivo de configuração referente a volumetria a rodar.

```
escolha = int(input("Com \"-gui\"? (1)Sim (0)Não"))
gui = "sumo-gui" if escolha == 1 else "sumo"

escolha = int(input("Qual simulação? (1) map_0.sumocfg (2) map_38.sumocfg (3) map_69.sumocfg"))
sumocfg = "map_0.sumocfg" if escolha == 1 else "map_38.sumocfg" if escolha == 2 else "map_69.sumocfg"
```
###  Iniciação do TraCI

Uma vez carregadas as variáveis podemos repassa-las como parâmetro para a linha de comando que inicia o processo de simulação.

```
sumoCmd = [gui, "-c", sumocfg, '--duration-log.statistics']
traci.start(sumoCmd)
```

### Carregamento das Variáveis

Agora são iniciadas e carregadas variáveis e listas utilizadas na lógica para alteração dos estágios do semáforo.

```
pistas = ["gneE0_0", "gneE0_1", "gneE2_0", "gneE2_1", "gneE9_0", "gneE9_1", "gneE11_0"]
numeroVeiculos = []

congest = -10
pistaConAntiga = ""
balanco = 0

os.system("cls")
traci.trafficlight.setProgram("gneJ1", "1")
```
os.system("cls") para limpar no prompt de comando qualquer outra informação irrelevante a simulação que será iniciada. A linha 10 traci.trafficlight.setProgram("gneJ1", "1") está setando o semáforo da junção "gneJ1" para a segunda (index "1") lógica semafórica presente no arquivo "CruzamentoBRT.net.xml".

### Execução da Simulação

Iniciamos a aplicação com um loop que segue até o fim dos passos explicitados no arquivo "CruzamentoBRT.net.xml". A linha 2 traci.simulationStep() avança os passos da simulação.

```
while traci.simulation.getMinExpectedNumber() > 0:
    traci.simulationStep()
```

Carregamos a lista numeroVeículos com as quantidades de cada carro parado no semáforo neste passo. Utilizando o comanto traci.lane.getLastStepHaltingNumber(id), onde o id é o id das arestas.

A variável pistaConNova recebe o ID da pista onde está a maior quantidade de carros parados.

```
 for index, id in enumerate(pistas):
        numeroVeiculos.append(traci.lane.getLastStepHaltingNumber(id))

    pistaConNova = pistas[numeroVeiculos.index(max(numeroVeiculos))]
```
Na primeira linha abaixo se o número de veículos esperando no semáforo for maior que a quantidade antiga aguardando no semáforo ele fará a troca dos estágios do semáforo. congest é iniciado com -10 portanto na primeira rodada qualquer semáforo com carros parados irá para a fase verde. O valor de 0,5 adicionado ao if é valor de ajuste, evitando que troquem indiscriminadamente os semáforos com prioridade.

A variável balanco é utilizada para equilibrar as quantidades necessárias de carros em cada aresta para alterar o semáforo em verde. Ela sempre será zerada ao entrar no if.

```
    if congest + 0.5 < (max(numeroVeiculos) + balanco) or congest == 0:
        balanco = 0
```
Ao entrar no if anterior, teremos outra validação para sabermos se tratar da mesma aresta. Caso não seja verdadeiro seguiremos sem alterar o estágio do semáforo, permitindo que mais carros passem pelo sinal. Uma vez, verdadeiro entraremos em outra sequencia de ifs para avaliação de qual aresta terá o foco verde.

```    
if pistaConNova != pistaConAntiga :
```

Trocamos as fases do semáforo utilizando o traci.trafficlight.setPhase("gneJ1", <índice da lógica semafórica utilizada>). Seguindo a lógica utilizada os índices que correspondem ao verde para um semáforo sempre são seguidos pelas fases amarelas destes semáforos. Então utilizamos a lógica para trocar para a fase verde quando encontramos uma nova aresta com maior trânsito e simplesmente andamos para a próxima fase do semáforo, que será sua fase amarela.

O array das fases da Lógica Semafórica tem apenas 6 índices e caso já estejamos no último índice, isto é, 5 não podemos trocar a fase utilizando a fase atual +1 (traci.trafficlight.setPhase("gneJ1", traci.trafficlight.getPhase("gneJ1") + 1).

```
           if traci.trafficlight.getPhase("gneJ1") < 5 :
                traci.trafficlight.setPhase("gneJ1", traci.trafficlight.getPhase("gneJ1") + 1)
```

Caso esteja no tempo de amarelo dos semáforos (não atuado por segurança) não fazemos nenhum tipo de alteração nas fases dos focos, pois não podemos mudar abruptamente para o verde, podendo causar acidentes e freadas muito bruscas.

```
while traci.trafficlight.getPhase("gneJ1") == 1 or traci.trafficlight.getPhase("gneJ1") == 3 or traci.trafficlight.getPhase("gneJ1") == 5:
    traci.simulationStep()
```

Nestas linhas alteramos as fases dos semáforos. Pelo Id da via, sabemos em qual fase devemos setar a simulação para utilizar, realizando assim a troca para o verde do semáforo com maior congestionamento no sinal.

```
if pistaConNova == "gneE0_0" or pistaConNova == "gneE0_1" or pistaConNova == "gneE2_0" or pistaConNova == "gneE2_1":
    traci.trafficlight.setPhase("gneJ1", 0)
else:
    if pistaConNova == "gneE9_0" or pistaConNova == "gneE9_1" :
         traci.trafficlight.setPhase("gneJ1", 2)
    else:
        if pistaConNova == "gneE11_0" :
            traci.trafficlight.setPhase("gneJ1", 4)
```

Finalizando o script atribuímos a nova aresta a pistaConAntiga e repassamos o novo valor de congestionamento encontrado (congest = max(numeroVeiculos)).

Seguindo a identação, fora do primeiro if, adicionamos valores à variavel balanco para igualarmos os valores da variavel congest e não ficarmos presos no verde de apenas um semáforo. 

Apagamos a lista com a quantidade de veículos em cada semáforo neste passo para poder carrega-la no próximo (numeroVeiculos.clear()).

Encerramos a simulação com a linha traci.close().

```
        pistaConAntiga = pistaConNova
        congest = max(numeroVeiculos)

    balanco += 0.01
    numeroVeiculos.clear()


print("Arquivo testado: ", sumocfg, "\n")

traci.close()
```
## Resultados

### Resultados Semáforos tempo-fixo.

No primeiro teste a simulação gerou a seguinte estatística para a volumetria de 0%

| Valores estatísticos  | Valor médio |
|-----------------------|-------------|
| RouteLength           | 629.56      |
| Speed                 | 11.07 m/s   |
| Duration              | 59 s        |
| WaitingTime           | 9.26 s      |
| TimeLoss              | 13.48 s     |
| DepartDelay:          | 0.2 s       |

# gif

Os valores para a densidade seguinte, como era esperado, teve um aumento considerável. Os números para o caso das 09:00hr foi:

| Valores estatísticos  | Valor médio |
|-----------------------|-------------|
| RouteLength           | 619.88      |
| Speed                 | 9.43 m/s    |
| Duration              | 68.38 s     |
| WaitingTime           | 12.03 s     |
| TimeLoss              | 23.32 s     |
| DepartDelay:          | 0.5 s       |

# gif

Já para os valores com o pico do tráfego, baseado nos dados obtidos, tiveram um salto e demonstram através dos números a dificuldade com o congestionamento:

| Valores estatísticos  | Valor médio |
|-----------------------|-------------|
| RouteLength           | 611,42      |
| Speed                 | 4,20 m/s    |
| Duration              | 196,85 s    |
| WaitingTime           | 53,81 s     |
| TimeLoss              | 152,35 s    |
| DepartDelay:          | 174,78 s    |

# gif

### Resultados Semáforo Inteligente.

Para a volumetria de 0% do semáforo Inteligente temos:

| Valores estatísticos  | Valor médio |
|-----------------------|-------------|
| RouteLength           | 630.01      |
| Speed                 | 12,43 m/s   |
| Duration              | 52,16 s     |
| WaitingTime           | 3,62 s      |
| TimeLoss              | 6,64 s      |
| DepartDelay:          | 0,19 s      |

# gif

Para a densidade de 38% no semáforo inteligente tivemos as seguintes importâncias:

| Valores estatísticos  | Valor médio |
|-----------------------|-------------|
| RouteLength           | 619,48      |
| Speed                 | 9,92 m/s    |
| Duration              | 67,35 s     |
| WaitingTime           | 12,60 s     |
| TimeLoss              | 22,32 s     |
| DepartDelay:          | 0,54 s      |

# gif

As quantidades averiguadas ao utilizarmos os semáforos por densidade do tráfego no horário de pico foram as seguintes:

| Valores estatísticos  | Valor médio |
|-----------------------|-------------|
| RouteLength           | 620,29      |
| Speed                 | 7,23 m/s    |
| Duration              | 92,64 s     |
| WaitingTime           | 28,04 s     |
| TimeLoss              | 47,52 s     |
| DepartDelay:          | 0,39 s      |

# gif

## Cruzamento dos dados obtidos.

Com todos os valores de ambos os tipos de semáforos foi realizado o cruzamento dos dados. Nosso objetivo central do trabalho é a diminuição do tempo de viagem (TimeLoss) e o tempo total aguardando no semáforo (WaitingTime). Foi realizado o cruzamento respeitando a ordem de sequência dos testes. Desta forma, foi cruzado os dados para volumetria de 0%, primeiramente, seguido dos dados para 38% e finalizando com os dados cruzados para a densidade de 69%.

### Comparação dos dado da volumetria 0%

Realizado a comparação entre os dados obtidos dos semáforos temporizados e os semáforos inteligentes foram encontrados as seguintes informações:

| 0%          | Semáforo Temporizado | Semáforo Inteligente |
|-------------|----------------------|----------------------|
| Route       | 629,56               | 630,01               |
| Speed       | 11,07                | 12,43                |
| Duration    | 59                   | 52,16                |
| WaitingTime | 9,26                 | 3,62                 |
| Timeloss    | 13,48                | 6,64                 |
| DepartDelay | 0,2                  | 0,19                 |

Houve ganho nos critérios chaves com diminuição nos valores de WaitingTime e Timeloss de 61% e 51% respectivamente. Além disto observou-se também uma melhora no fluxo pela velocidade máxima média subir 12% ficando, no Semáforo Inteligente, na média de 12,43 m/s.

<img width="365" alt="Semaforo0" src="https://user-images.githubusercontent.com/41927965/145091327-3a7bc723-ba6a-414d-bce2-795cd4b99093.png">

### Comparação dos dados da volumetria 38%

Não houve ganho com a utilização do semáforo inteligente para essa volumetria. Para o critério de WaitingTime foi obtido um aumento de 5% com a utilização destes semáforos. Já o TimeLoss obteve uma redução de 4%, muito pouco para se justificar seu uso.

| 38%         | Semáforo Temporizado | Semáforo Inteligente |
|-------------|----------------------|----------------------|
| Route       | 619,88               | 619,48               |
| Speed       | 9,43                 | 9,92                 |
| Duration    | 68,38                | 67,35                |
| WaitingTime | 12,03                | 12,6                 |
| Timeloss    | 23,32                | 22,32                |
| DepartDelay | 0,5                  | 0,54                 |

<img width="368" alt="Semaforo38(2)" src="https://user-images.githubusercontent.com/41927965/145091565-01ef0ca4-a646-4ec4-b141-bfeedee8a756.png">


### Comparação dos dados da volumetria 69%

| 69%         | Semáforo Temporizado | Semáforo Inteligente |
|-------------|----------------------|----------------------|
| Route       | 611,42               | 620,29               |
| Speed       | 4,20                 | 7,23                 |
| Duration    | 196,85               | 92,64                |
| WaitingTime | 53,81                | 28,04                |
| Timeloss    | 152,35               | 47,52                |
| DepartDelay | 174,78               | 0,39                 |

Utilizando o semáforo inteligente para controle de tráfegos em horário de pico retornou com os melhores resultados possíveis. Há melhora em todos os indicadores e as reduções nos critérios chaves foram bruscas ficando o WaitingTime, que apresentava o valor de 53,81s no semáforo temporizado, com o valor atual de 28,04. Isto representa uma queda de 48% no tempo parado ao semáforo. E o tempo perdido total também foi reduzido drasticamente passando de 152,35s na primeira avaliação para 47,52s. Queda de 69%.

<img width="365" alt="Semaforo69" src="https://user-images.githubusercontent.com/41927965/145091717-7ceda188-77d7-48cb-99b8-5e485a084735.png">

## Conclusão

Em baixa volumetria e em grandes volumetrias, como no horário de pico, este modelo se provou muito eficiente. Já para os casos de volumetria média, sugerimos a utilização hibrida do aqui proposto. Utilizando o reconhecimento das vias com maior tráfego, porém, mantendo um temporizador para a troca da fase verde, aumentando assim o fluxo de saturação dos semáforos para o horário. Importante frisar que não há nenhuma perda em manter a utilização dos Semáforos Inteligentes para volumes médios de tráfego, uma vez que não houve aumento significativo nos valores averiguados e mesmo tais valores já se mantinham dentro do aceitável (em comparação com grandes densidades). Sendo necessário ao usuário aguardar apenas um ciclo do Semáforo para realizar sua travessia.

Após análise dos resultados obtidos é consenso que há ganho em qualidade de vida, saúde e melhoria no trânsito a utilização do proposto neste trabalho. Bem como se provou plausível os objetivos buscados de redução do tempo de viagem e tempo de espera no semáforo.

Com isto, afirmo que para Controladores atuados pelo tráfego, com estratégia de controle isolado em interseções independentes das outras e em cruzamentos distantes, esta programação dinâmica das fases do semáforo é adequada para diminuir os transtornos do congestionamento urbano nos horários de pico e nos momentos de menor volume de tráfego.

Também é previsto quesitos mínimos a serem cumpridos para completude do controlador atuado pelo tráfego no que incide à lógica utilizada para as condições de Segurança e Manutenibilidade.

Para Segurança espera-se que os acessos aos recursos do controlador sejam por usuários autorizados (Confidencialidade), e apenas estes poderão modificar o controlador (Integridade). Ainda em Segurança, é necessário a disponibilidade em qualquer momento para os usuários autorizados (Disponibilidade) além do não-repúdio.

Enquanto para a Manutenibilidade é previsto o versionamento do código para atendimento, por exemplo, de Bugs descobertos (corretiva), inclusão de novas funcionalidades como um controlador atuado por pedestres (melhoria), ao identificar-se melhorias para qualidade ou prevenção de bugs (preventiva) e principalmente para adaptação às mudanças dos cruzamentos que irão atuar (adaptativa), podendo ser feito pelo ajuste das variáveis de controle, por exemplo.
