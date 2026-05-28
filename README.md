Miniräknare med CI-pipeline

Denna miniräknar-applikationskriven i Python testar enkla uträkningar som användaren ger via terminalen. 

Hur du som användare kör applikationen:
1. Klona repot från GitHub
2. Kör testerna med 'pytest'

Hur CI-pipeline fungerar:
När kod pushas till `main`-branchen triggas en GitHub Action. Den startar upp en Ubuntu-server, checkar ut koden, installerar Python och `pytest`, och kör sedan testerna automatiskt för att säkerställa att koden fungerar.
