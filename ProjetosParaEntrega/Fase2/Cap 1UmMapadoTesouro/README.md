# FarmTech Solutions - Sistema de Irrigação Inteligente (Alface)

## Integrante

Lucas Henrique Aparecido Gomes de Mello

## Descrição do Projeto

Este projeto foi desenvolvido para a Fase 2 da FarmTech Solutions, com o objetivo de simular um sistema de irrigação inteligente utilizando ESP32 no ambiente virtual Wokwi.

A proposta consiste em monitorar condições do solo e do ambiente para decidir automaticamente quando irrigar uma plantação de alface.

## Cultura Escolhida

Alface

## Componentes Utilizados

* ESP32
* 3 botões para simulação dos nutrientes Nitrogênio (N), Fósforo (P) e Potássio (K)
* Sensor DHT22 para simulação da umidade do solo
* Potenciômetro para simulação do pH do solo
* Relé para representar a bomba d’água
* LED para indicação visual do acionamento da irrigação

## Lógica do Sistema

A irrigação é acionada apenas quando todas as condições abaixo são atendidas:

* pH entre 6.0 e 7.0
* Umidade abaixo de 70%
* Temperatura acima de 15°C
* Nutrientes mínimos configurados no sistema

O sistema foi configurado em modo demonstrativo (NUTRIENTES_MINIMOS = 0), permitindo validar a lógica sem a necessidade de acionamento obrigatório dos botões.

## Mapeamento de Pinos

* Nitrogênio (N): GPIO 13
* Fósforo (P): GPIO 12
* Potássio (K): GPIO 14
* pH (Potenciômetro): GPIO 36
* DHT22: GPIO 23
* Relé: GPIO 27
* LED: GPIO 26

## Funcionamento

O sistema realiza leituras contínuas dos sensores simulados.

O potenciômetro representa o pH do solo, convertendo o valor analógico em uma escala aproximada. O sensor DHT22 fornece dados de umidade e temperatura.

Com base nesses dados, o sistema avalia se as condições são adequadas para a cultura da alface. Quando todas as condições são atendidas, o relé é acionado e o LED acende, indicando o início da irrigação.

Caso contrário, o sistema mantém a bomba desligada.

## Circuito no Wokwi

![Circuito](imagens/circuito.png)

## Vídeo Demonstrativo

https://youtu.be/qXe5QHBt5KI

## Conclusão

O projeto demonstra a aplicação de conceitos de Internet das Coisas (IoT) e automação na agricultura, permitindo a simulação de um sistema inteligente de irrigação baseado em dados de sensores.

A abordagem adotada contribui para o uso eficiente de recursos hídricos e para a melhoria da produtividade agrícola.
