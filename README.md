# AutoVisPolSys
Automatic visual system for detection human.

- seznam zásuvných modulů:
	a) SimpleCV
	a) OpenCV
	c) Multiprocessing

Celý system bude obsahovat:
	- řídící algorytmus, který využije připojené moduly
	- samostatný modul pro zaznamenání videa
	- samostatný modul pro rozpoznání, zda se před kamerou někdo objevil, či ne

Řídící algorytmus bude fungovat následujícím způsobem:
	1) Po spuštění:
		a) zobrazí se okno, ve kterém se budou prezentovat výsledky (např. počet zaznamenaných vydeí, časy natočených videí,
			výpis rozpoznaných osob, časy spuštění, pozastavení a zastavení systému, ... )
		b) spustí podprocesy, jejichž počet bude roven počtu kamer
		c) vytvořím si objekty samostatných modulů (ano, moduly budou reprezentovány třídou, která bude obsahovat všechny 
			příslušné funkce)
 -> 2) Zopočne stále se opakující cyklus, který bude mít za úkol dávkování obrazu z kamery do modulu pro rozpoznávání (pro každý
|		proces, čili každou kameru zvlášť)
|			1. způsob řešení - detekce pohybu
 ---------	2. způsob řešení - klasifikace lidí na snímku (rozpoznávání postavy společně s vylepšenou metodou detekce pohybu)

 System bude navržen, jako samoúdržbový. Což znamená, že se v pravidelných intervalech restartuje a pročistí (záznamy videí se budou v pravidelných intervalech promazávat, což pro uživatele znamená to, že si je bude muset kopírovat na externí disk). Samozřejmě bude mít přístup ke všem záznamům (po správném zadání přístupového hesla) buď přes vzdálenou správu, či přes sdílené soubory v místní sítí.
 
 Restart systému bude probíhat následujícím způsobem. Nezávislý proces postupně obnoví hlavní procesy tak, aby se nestalo, že bude obnovovat proces, který bude nahrávat. Což zajístím tím, že spustím nový proces (náhradní) který převezme správu nad kamerou, hlavní proces se obnoví a zase převezme správu.

 Dále bude fungovat externí aplikace, která bude ověřovat chod systému, zda je spuštěn. Pokud vyhodnotí, že je systém pozastaven, automaticky ho zapne. 
 (Tímto se ošetří, nežádoucí vypnutí, či náhlý pád systému.)