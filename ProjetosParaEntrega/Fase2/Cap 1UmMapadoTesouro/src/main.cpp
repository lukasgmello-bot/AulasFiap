#include <Arduino.h>
#include <DHT.h>

// ==========================
// PINOS
// ==========================
#define PINO_N    13
#define PINO_P    12
#define PINO_K    14
#define PINO_PH   36   // VP - conectado ao potenciômetro
#define PINO_DHT  23
#define PINO_RELE 27
#define PINO_LED  26

// ==========================
// DHT22
// ==========================
#define TIPO_DHT DHT22
DHT dht(PINO_DHT, TIPO_DHT);

// ==========================
// PARÂMETROS - ALFACE
// ==========================
const float PH_MINIMO          = 6.0;
const float PH_MAXIMO          = 7.0;
const float UMIDADE_LIMITE     = 70.0;
const float TEMPERATURA_MINIMA = 15.0;
const int   NUTRIENTES_MINIMOS = 0;

// ==========================
// VARIÁVEIS
// ==========================
bool bombaLigada = false;

void setup() {
  Serial.begin(115200);
  delay(1000);

  pinMode(PINO_N,    INPUT_PULLUP);
  pinMode(PINO_P,    INPUT_PULLUP);
  pinMode(PINO_K,    INPUT_PULLUP);
  pinMode(PINO_RELE, OUTPUT);
  pinMode(PINO_LED,  OUTPUT);

  digitalWrite(PINO_RELE, LOW);
  digitalWrite(PINO_LED,  LOW);

  dht.begin();

  Serial.println("======================================");
  Serial.println("  FarmTech Solutions - Irrigacao      ");
  Serial.println("  Cultura: Alface                     ");
  Serial.println("  pH ideal: 6.0 a 7.0                 ");
  Serial.println("======================================");
}

void loop() {

  Serial.println(">>> LOOP EXECUTANDO <<<");

  // --- Leitura dos nutrientes ---
  bool nitrogenio = (digitalRead(PINO_N) == LOW);
  bool fosforo    = (digitalRead(PINO_P) == LOW);
  bool potassio   = (digitalRead(PINO_K) == LOW);

  int nutrientes = 0;
  if (nitrogenio) nutrientes++;
  if (fosforo)    nutrientes++;
  if (potassio)   nutrientes++;

  // --- Leitura do pH ---
  int   leituraPH  = analogRead(PINO_PH);
  float phSimulado = 5.0 + (leituraPH / 4095.0) * 3.0;

  // --- Leitura do DHT22 ---
  float umidade     = dht.readHumidity();
  float temperatura = dht.readTemperature();
  bool  erroDHT     = isnan(umidade) || isnan(temperatura);

  // --- Condições ---
  bool phOk          = (phSimulado >= PH_MINIMO && phSimulado <= PH_MAXIMO);
  bool umidadeOk     = (!erroDHT && umidade < UMIDADE_LIMITE);
  bool nutrientesOk  = (nutrientes >= NUTRIENTES_MINIMOS);
  bool temperaturaOk = (!erroDHT && temperatura >= TEMPERATURA_MINIMA);

  bool ligarBomba = phOk && umidadeOk && nutrientesOk && temperaturaOk;

  // --- Acionamento ---
  if (ligarBomba) {
    digitalWrite(PINO_RELE, HIGH);
    digitalWrite(PINO_LED,  HIGH);
    bombaLigada = true;
  } else {
    digitalWrite(PINO_RELE, LOW);
    digitalWrite(PINO_LED,  LOW);
    bombaLigada = false;
  }

  // --- SERIAL (DENTRO DO LOOP) ---
  Serial.println("----------- LEITURA -----------");

  Serial.print("N (Nitrogenio): ");
  Serial.println(nitrogenio ? "PRESENTE" : "AUSENTE");

  Serial.print("P (Fosforo): ");
  Serial.println(fosforo ? "PRESENTE" : "AUSENTE");

  Serial.print("K (Potassio): ");
  Serial.println(potassio ? "PRESENTE" : "AUSENTE");

  Serial.print("Total nutrientes: ");
  Serial.println(nutrientes);

  Serial.print("Potenciometro pH (raw): ");
  Serial.println(leituraPH);

  Serial.print("pH simulado: ");
  Serial.println(phSimulado, 2);

  if (erroDHT) {
    Serial.println("ERRO: DHT22 nao respondeu!");
  } else {
    Serial.print("Umidade: ");
    Serial.print(umidade, 1);
    Serial.println(" %");

    Serial.print("Temperatura: ");
    Serial.print(temperatura, 1);
    Serial.println(" C");
  }

  Serial.println("--------- DIAGNOSTICO ---------");

  Serial.print("pH adequado: ");
  Serial.println(phOk ? "SIM" : "NAO");

  Serial.print("Solo seco: ");
  Serial.println(umidadeOk ? "SIM" : "NAO");

  Serial.print("Nutrientes suficientes: ");
  Serial.println(nutrientesOk ? "SIM" : "NAO");

  Serial.print("Temperatura adequada: ");
  Serial.println(temperaturaOk ? "SIM" : "NAO");

  Serial.print(">>> BOMBA: ");
  Serial.println(bombaLigada ? "LIGADA <<<" : "DESLIGADA <<<");

  Serial.println("--------------------------------\n");

  delay(2000);
}