# AURORA - Modelagem Matematica da Autonomia Energetica

Este repositorio apresenta a modelagem matematica e a implementacao em Python do sistema de autonomia energetica da base lunar AURORA. O projeto analisa a descarga de uma bateria durante a noite lunar e estima em quanto tempo a reserva de energia atinge um limite operacional seguro.

O trabalho foi desenvolvido como um relatorio tecnico de matematica aplicada, conectando funcoes exponenciais, simulacao computacional, geracao de graficos e reflexao critica sobre energia, infraestrutura e sustentabilidade.

## Objetivo

Modelar a perda de energia armazenada pela base AURORA usando a funcao exponencial:

```text
E(t) = E0 * e^(-k*t)
```

A partir desse modelo, o projeto calcula a autonomia da base ate o limite seguro de energia, gera graficos de analise e discute a importancia de decisoes automaticas para economia de energia em ambientes extremos.

## Contexto do Problema

Durante a noite lunar, a base pode passar aproximadamente 336 horas sem geracao solar suficiente. Nesse periodo, ela depende da energia acumulada em baterias para manter sistemas essenciais, como comunicacao, sensores, controle termico, suporte operacional e processamento local.

A funcao exponencial foi escolhida porque representa uma descarga proporcional ao estoque restante de energia. Assim, a queda e maior quando a bateria esta cheia e diminui gradualmente conforme a energia armazenada se aproxima de zero.

## Modelo Matematico

| Variavel | Simbolo | Unidade | Valor usado | Significado |
|---|---:|---:|---:|---|
| Energia restante | E(t) | kWh | Variavel | Energia disponivel no instante t |
| Energia inicial | E0 | kWh | 120 | Reserva inicial da bateria |
| Taxa de descarga | k | h^-1 | 0,067 | Velocidade proporcional de perda energetica |
| Tempo | t | horas | t >= 0 | Tempo decorrido desde o inicio da descarga |
| Limite seguro | E_seg | kWh | 48 | 40% da energia inicial |
| Potencia solar maxima | P_max | kW | 15 | Pico de potencia dos paineis solares |
| Ciclo lunar | T | horas | 708 | Duracao aproximada de um ciclo lunar completo |

Para encontrar a autonomia, o modelo resolve o instante `t*` em que a energia restante atinge o limite seguro:

```text
E(t*) = E_seg
E0 * e^(-k*t*) = E_seg
t* = (1/k) * ln(E0/E_seg)
```

Com os parametros da AURORA:

```text
t* = (1/0,067) * ln(120/48)
t* = 13,68 horas
```

## Resultado Principal

A base AURORA atinge o limite seguro de 48 kWh em aproximadamente:

```text
13,7 horas
```

Esse valor cobre apenas cerca de:

```text
4,1% da noite lunar de 336 horas
```

Portanto, a autonomia calculada nao e suficiente para atravessar a noite lunar mantendo consumo normal. O resultado justifica a necessidade de estrategias como corte automatico de cargas, priorizacao de sistemas vitais, armazenamento ampliado e previsao inteligente de geracao solar.

## Modelo Avancado de Geracao Solar

O projeto tambem inclui um modelo trigonometrico para estimar a geracao solar durante o ciclo lunar:

```text
P(t) = P_max * sen(2*pi*t/T)
```

Como a geracao so ocorre durante a fase iluminada, o codigo considera apenas os valores positivos da funcao. Esse segundo modelo ajuda a comparar geracao e consumo, aproximando a simulacao de uma situacao mais realista de operacao energetica.

## Arquivos do Projeto

| Arquivo | Descricao |
|---|---|
| `autonomia.py` | Codigo Python com o calculo da autonomia, simulacao da descarga e geracao dos graficos |
| `relatorio_aurora.pdf` | Relatorio tecnico final com desenvolvimento matematico, graficos, interpretacao e reflexao critica |
| `README.md` | Apresentacao geral do projeto, resultados e instrucoes de execucao |

Ao executar o codigo, tambem podem ser geradas as imagens:

| Arquivo gerado | Descricao |
|---|---|
| `aurora_autonomia.png` | Grafico da descarga exponencial com curva E(t), limite seguro, t* e zona segura |
| `aurora_modelo_solar.png` | Grafico do modelo trigonometrico de geracao solar no ciclo lunar |

## Como Executar

1. Abra o terminal dentro da pasta do projeto.
2. Instale as dependencias, se necessario:

```powershell
pip install numpy matplotlib
```

3. Execute o arquivo principal:

```powershell
python autonomia.py
```

4. Confira a saida no terminal e os graficos gerados na pasta do projeto.

## Saida Esperada

O programa apresenta os principais parametros da simulacao e calcula:

```text
Autonomia estimada: 13.7 horas
Cobertura da noite lunar: 4.1%
Energia no instante t*: 48.0 kWh
Energia solar gerada no dia lunar: aproximadamente 3380 kWh
```

## Analise Critica

O modelo mostra que a AURORA precisa tomar decisoes energeticas antes que a bateria entre em uma faixa insegura. Em uma base lunar, esse tipo de controle deve ser rapido e local, pois depender de comandos externos pode ser arriscado em situacoes criticas.

Ao mesmo tempo, a funcao exponencial e uma simplificacao. Ela nao considera fatores como variacao de temperatura, envelhecimento das baterias, poeira lunar, perdas nos conversores, falhas nos paineis solares, picos de demanda ou diferencas entre cargas essenciais e nao essenciais.

Por isso, o modelo trigonometrico de geracao solar complementa a analise. Ele permite observar quando existe geracao, quando a base depende apenas das baterias e como a energia poderia ser melhor distribuida ao longo do ciclo lunar.

## Relacao com os ODS

O projeto se conecta principalmente a tres Objetivos de Desenvolvimento Sustentavel:

| ODS | Relacao com o projeto |
|---|---|
| ODS 7 - Energia limpa e acessivel | Discute o uso eficiente, seguro e inteligente de energia renovavel |
| ODS 9 - Industria, inovacao e infraestrutura | Aplica modelagem e automacao a uma infraestrutura energetica resiliente |
| ODS 10 - Reducao das desigualdades | Mostra como tecnologias de autonomia energetica podem inspirar solucoes para regioes isoladas na Terra |

## Conclusao

A modelagem demonstra que a base AURORA, com 120 kWh de energia inicial e taxa de descarga de 0,067 h^-1, atinge o limite seguro em cerca de 13,7 horas. Como esse tempo e muito menor que a duracao da noite lunar, o projeto evidencia a importancia de armazenamento eficiente, controle automatico de consumo e planejamento da geracao solar.

O codigo Python e o relatorio tecnico tornam a analise reprodutivel, visual e conectada a uma aplicacao real de engenharia em ambiente extremo.
