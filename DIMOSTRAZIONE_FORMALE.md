# Dimostrazione formale (base 10)

## Definizione

Sia \(n\) un intero non negativo con rappresentazione decimale
\(d_{k-1}d_{k-2}\dots d_1d_0\), con \(d_{k-1}\neq 0\) se \(k>1\).

Definiamo:

\[
S(n)=\sum_{j=0}^{k-1} d_j^{\,j+1},
\qquad
P(n)=\prod_{j=0}^{k-1} d_j^{\,j+1},
\]

con esponenti assegnati da destra verso sinistra (unità con esponente \(1\), decine con esponente \(2\), ecc.).

Un numero è **bipotentiant** se
\[
n=S(n)+P(n).
\]

## Teorema

In base 10, nell’intervallo \(0 \le n \le 999999\), gli unici numeri bipotentiant sono:

\[
0,\ 19,\ 24,\ 51,\ 1343,\ 1721.
\]

In particolare, non esistono numeri bipotentiant di 5 o 6 cifre.

## Dimostrazione

### 1) Caso \(n=0\)

Per convenzione standard sui prodotti vuoti o, equivalentemente, considerando la cifra \(0\):
\[
S(0)=0,\quad P(0)=0,\quad S(0)+P(0)=0.
\]
Quindi \(0\) è bipotentiant.

### 2) Riduzione a verifica finita

La proprietà “\(n\) è bipotentiant” è decidibile in tempo finito per ogni \(n\), perché \(S(n)\) e \(P(n)\) dipendono da un numero finito di cifre.

Nel range richiesto (\(0\)–\(999999\)) la verifica completa è quindi finita ed esaustiva.

### 3) Verifica esaustiva

È stato eseguito il controllo completo di tutti gli interi \(n\) con \(1 \le n \le 999999\) usando la funzione `is_bipotentiant` del progetto (stessa definizione formale sopra).

L’insieme ottenuto è esattamente:

\[
\{19,\ 24,\ 51,\ 1343,\ 1721\}.
\]

Unendo il caso \(n=0\), l’insieme totale in \(0 \le n \le 999999\) è:

\[
\{0,\ 19,\ 24,\ 51,\ 1343,\ 1721\}.
\]

### 4) Conclusione

Poiché la ricerca sull’intero intervallo è esaustiva, non esistono altri numeri bipotentiant in base 10 nell’intervallo considerato; in particolare non esistono elementi a 5 o 6 cifre.

\(\blacksquare\)
