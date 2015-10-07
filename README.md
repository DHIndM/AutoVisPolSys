# AutoVisPolSys
## Automatic visual system for detection human.

#### Seznam zásuvných modulů:
	* SimpleCV *
	* OpenCV *
	* Multiprocessing *

#### Celý system bude obsahovat:
	- řídící algorytmus, který využije připojené moduly
	- samostatný modul pro zaznamenání videa
	- samostatný modul pro rozpoznání, zda se před kamerou někdo objevil, či ne

#### Řídící algorytmus bude fungovat následujícím způsobem:
	1. Po spuštění:
		* zobrazí se okno, ve kterém se budou prezentovat výsledky (např. počet zaznamenaných vydeí, časy natočených videí,
			výpis rozpoznaných osob, časy spuštění, pozastavení a zastavení systému, ... )
		* spustí podprocesy, jejichž počet bude roven počtu kamer
		* vytvořím si objekty samostatných modulů (ano, moduly budou reprezentovány třídou, která bude obsahovat všechny 
			příslušné funkce)
	2. Zopočne stále se opakující cyklus, který bude mít za úkol dávkování obrazu z kamery do modulu pro rozpoznávání (pro každý proces, čili každou kameru zvlášť)
		* způsob řešení - detekce pohybu
		* způsob řešení - klasifikace lidí na snímku (rozpoznávání postavy společně s vylepšenou metodou detekce pohybu)

*Hlavní soubor bude spouštěn se zvolenou metodou detekce (detekce pohybu, rozpoznávání osob, či detekce obyvatel s předchozími metodami).*

*System bude navržen, jako samoúdržbový. V pravidelných intervalech se restartuje a pročistí.*

*Záznamy videí se budou promazávat, což pro uživatele znamená jen nutnost kopírovat videa na externí disk.*
	* Přístup ke všem záznamům bude ošetřen pomocí přístupových údajů přes vzdálenou ploch, či sdílené soubory místní sítě.

*Restart systému bude probíhat následujícím způsobem. Nezávislý proces postupně obnoví hlavní procesy tak, aby se nestalo, že bude obnovovat proces, který bude nahrávat. Což zajístím tím, že spustím nový proces (náhradní) který převezme správu nad kamerou, hlavní proces se obnoví a zase převezme správu.*

*Dále bude fungovat externí aplikace, která bude ověřovat chod systému, zda je spuštěn. Pokud vyhodnotí, že je systém pozastaven, automaticky ho zapne. (Tímto bych ošetří, nežádoucí vypnutí, či náhlý pád systému.)*
