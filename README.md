1. Skapa ett publikt repository på GitHub.
2. Lägg till en enkel applikation. Det kan vara ett enkelt pythonskript, en HTML-sida eller ett
bashskript som gör något meningsfullt (till exempel miniräknaren från testningskursen, en
enkel API-klient eller liknande).
3. Arbeta med minst två branches, en main-branch och en feature-branch.
4. Gör minst fem commits med beskrivande commit-meddelanden.
5. Skapa en pull request från din feature-branch till main och merga den.
6. Konfigurera en CI-pipeline med hjälp av GitHub Actions.
7. Pipelinen ska innehålla minst följande steg:
1. Checkout av koden
2. Installation av eventuella beroenden
3. Körning av minst ett automatiserat test (till exempel pytest, unittest eller liknande)
8. Pipeline ska triggas automatiskt vid push till main.
9. Inkludera en README.md i ditt repository som förklarar:
1. Vad applikationen gör
2. Hur man kör applikationen lokalt
3. Hur CI-pipeline fungerar
