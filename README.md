# FLUKA i Monte Carlo w Pythonie

## Cel nauki
Uczę się metod Monte Carlo w Pythonie oraz przygotowuję się do pracy z tematami związanymi z analizą danych, symulacjami i środowiskiem FLUKA.

## Narzędzia
- Python
- PyCharm
- numpy
- matplotlib
- pandas

## Plan pracy
- codzienna nauka 30–60 minut,
- tworzenie skryptów w Pythonie,
- wizualizacja wyników,
- budowanie mini-projektów do portfolio i CV.

### Dzień 1 23.03
- skonfigurowałam środowisko w PyCharm
- podpięłam lokalne `.venv`
- uruchomiłam pierwszy skrypt z `numpy`, `pandas`, `matplotlib`
- przećwiczyłam losowanie z rozkładu jednostajnego
- zaobserwowałam, że wraz ze wzrostem liczby prób średnia zbliża się do wartości teoretycznej 0.5

### Dzień 2 – losowość, histogram i seed

Dzisiaj ćwiczyłam podstawy losowości w Pythonie z użyciem biblioteki NumPy.

#### Czego się nauczyłam
- generator liczb losowych w Pythonie tworzy liczby pseudolosowe,
- histogram pokazuje, jak często wartości wpadają do określonych przedziałów,
- średnia opisuje przeciętną wartość całego zbioru danych,
- ziarno losowości (seed) to wartość startowa generatora pseudolosowego,
- ustawienie seeda pozwala uzyskać powtarzalne wyniki przy każdym uruchomieniu programu.

#### Co zrobiłam
- porównałam histogramy dla różnych seedów,
- sprawdziłam, jak zmieniają się średnie dla różnych losowań,
- porównałam wyniki z ustawionym seedem i bez ustawionego seeda,
- utrwaliłam różnicę między histogramem a średnią.

#### Wniosek
Seed nie sprawia, że liczby są bardziej losowe, ale pozwala odtworzyć dokładnie tę samą sekwencję wyników. Histogram pomaga wizualnie ocenić rozkład danych, a średnia daje ich pojedyncze podsumowanie liczbowe.


### Dzień 3 – podstawy statystyki do Monte Carlo

Dzisiaj ćwiczyłam podstawowe pojęcia statystyczne potrzebne do metod Monte Carlo.

#### Czego się nauczyłam
- próbka to zestaw danych, na którym wykonuje się analizę,
- średnia opisuje przeciętną wartość danych,
- minimum i maksimum pokazują zakres danych,
- wariancja i odchylenie standardowe opisują rozrzut wyników,
- histogram pokazuje, jak często wartości wpadają do określonych przedziałów,
- wartość oczekiwana to teoretyczna wartość, do której dąży średnia przy dużej liczbie prób,
- błąd przybliżenia pokazuje, jak daleko wynik eksperymentu jest od wartości oczekiwanej.

#### Co zrobiłam
- liczyłam podstawowe statystyki dla losowych próbek,
- porównywałam próbki o różnych rozmiarach,
- analizowałam histogramy i błędy względem wartości oczekiwanej 0.5.

#### Wniosek
Monte Carlo opiera się nie tylko na losowaniu, ale też na analizie statystycznej wyników. Im większa liczba prób, tym zwykle bardziej stabilne są wyniki i lepsze przybliżenie wartości oczekiwanej.


### Dzień 4 – estymacja liczby pi metodą Monte Carlo

Dzisiaj uczyłam się estymacji liczby pi metodą Monte Carlo.

#### Czego się nauczyłam
- losując punkty w kwadracie jednostkowym można oszacować pole ćwiartki koła,
- punkt należy do ćwiartki koła, jeśli spełnia warunek `x² + y² <= 1`,
- stosunek liczby punktów w kole do liczby wszystkich punktów przybliża `pi / 4`,
- dzięki temu można obliczyć estymację `pi ≈ 4 * points_inside / n`,
- jakość wyniku poprawia się wraz ze wzrostem liczby prób.

#### Jak oceniam stabilizację
- porównuję estymację pi dla różnych wartości `n`,
- obserwuję, czy błąd względem `np.pi` maleje,
- sprawdzam, czy kolejne wyniki zbliżają się do prawdziwej wartości pi,
- pamiętam, że stabilizacja oznacza ogólny trend poprawy, a nie idealnie równy spadek błędu w każdej próbie.


### Dzień 5 – rozrzut wyników i niepewność w Monte Carlo

Dzisiaj uczyłam się interpretować rozrzut wyników Monte Carlo i opisywać niepewność estymacji.

#### Czego się nauczyłam
- pojedynczy wynik Monte Carlo nie opisuje w pełni jakości metody,
- ten sam eksperyment uruchomiony wiele razy daje różne wyniki z powodu losowości,
- rozrzut wyników można ocenić, wykonując wiele powtórzeń tego samego eksperymentu,
- średnia z wielu uruchomień daje bardziej stabilny obraz wyniku,
- odchylenie standardowe opisuje skalę rozrzutu i prostą formę niepewności,
- mniejszy rozrzut oznacza mniejszą niepewność estymacji.

#### Wniosek
Metoda Monte Carlo daje wynik przybliżony, który naturalnie waha się między kolejnymi uruchomieniami. Aby sensownie ocenić jakość wyniku, trzeba patrzeć nie tylko na pojedynczą estymację, ale też na rozrzut i niepewność.


#### Dzień 5 - notatka M-C

## Metoda Monte Carlo – notatka

Metoda Monte Carlo to metoda obliczeniowa i statystyczna, w której wykorzystuje się losowanie wielu scenariuszy oraz analizę wyników, aby oszacować wartość, prawdopodobieństwo lub zakres możliwych rezultatów.

### Jak działa
Zamiast liczyć wynik jednym wzorem, wykonuje się bardzo wiele losowych prób, a następnie analizuje się:
- średni wynik,
- rozrzut wyników,
- niepewność,
- błąd względem wartości oczekiwanej lub rzeczywistej.

### Gdzie jest używana
- transport cząstek,
- fizyka,
- finanse,
- analiza ryzyka,
- inżynieria,
- modelowanie procesów losowych.

### Zalety
- dobrze działa dla złożonych problemów,
- pozwala analizować niepewność,
- pokazuje nie tylko jeden wynik, ale też zakres możliwych wyników.

### Wady
- daje wynik przybliżony, a nie dokładny,
- wymaga dużej liczby prób,
- przy małej liczbie prób wyniki mogą być niestabilne.

### Rozrzut i niepewność
Rozrzut oznacza, że kolejne uruchomienia tej samej symulacji mogą dawać trochę różne wyniki.
Niepewność mówi, o ile wynik może się jeszcze wahać z powodu losowości metody.
Mniejsze odchylenie standardowe oznacza mniejszy rozrzut i większą stabilność estymacji.

### Pytania kontrolne – metoda Monte Carlo

**Dlaczego metoda Monte Carlo jest nazywana metodą statystyczną?**  
Ponieważ opiera się na wielu losowych próbach i analizie statystycznej wyników, takich jak średnia, rozrzut i niepewność.

**Co daje wykonanie wielu losowych prób zamiast jednej?**  
Pozwala lepiej oszacować wynik, ocenić jego stabilność oraz opisać rozrzut i niepewność estymacji.

**Jaka jest różnica między błędem a niepewnością?**  
Błąd to różnica między wynikiem estymacji a wartością rzeczywistą lub oczekiwaną. Niepewność opisuje, jak bardzo wynik może się wahać z powodu losowości metody.

**Dlaczego Monte Carlo bywa przydatna tam, gdzie trudno policzyć coś dokładnie wzorem?**  
Ponieważ pozwala oszacować wynik przez wiele losowych prób i analizę otrzymanych rezultatów, nawet dla bardzo złożonych problemów.

**Co oznacza, że wynik Monte Carlo jest przybliżeniem, a nie dokładną odpowiedzią?**  
Oznacza to, że wynik nie jest idealnie dokładny, tylko stanowi oszacowanie, które może różnić się od wartości rzeczywistej i jest obarczone niepewnością.

### Podsumowanie tygodnia 1

Po pierwszym tygodniu nauki rozumiem podstawy metody Monte Carlo:
- rolę losowości i seeda,
- znaczenie histogramu, średniej i odchylenia standardowego,
- sens wykonywania wielu prób,
- estymację liczby pi metodą Monte Carlo,
- pojęcia rozrzutu, błędu i niepewności.

Najlepiej rozumiem ogólną ideę metody, podstawy statystyki i wpływ liczby prób na stabilność wyniku.

Do dalszej pracy pozostaje:
- bardziej precyzyjne i techniczne formułowanie odpowiedzi,
- lepsze rozróżnianie błędu i niepewności,
- utrwalenie, że większa próbka nie zmienia rozkładu, tylko lepiej go odwzorowuje,
- dokładniejsze wyjaśnianie geometrycznej logiki estymacji liczby pi.

### Dzień 6 – całkowanie Monte Carlo dla f(x)=x^3

Dzisiaj samodzielnie wykonałam całkowanie Monte Carlo dla funkcji `f(x)=x^3` na przedziale `[0,1]`.

#### Co zrobiłam
- ustawiłam `seed = 42`,
- przetestowałam liczby punktów: 100, 1000, 10000 i 100000,
- losowałam punkty z przedziału `[0,1]`,
- obliczałam wartości funkcji `x^3`,
- estymowałam całkę jako średnią wartość funkcji pomnożoną przez długość przedziału,
- porównywałam wynik z wartością dokładną `1/4`,
- liczyłam błąd estymacji,
- narysowałam wykres stabilizacji wyniku.

#### Co zaobserwowałam
- mała liczba punktów dawała większy błąd,
- większa liczba punktów zwykle poprawiała dokładność wyniku,
- wynik nie musi poprawiać się idealnie przy każdym kolejnym zwiększeniu liczby prób,
- najlepsza estymacja została uzyskana dla 100000 punktów.

#### Wniosek
Całkowanie Monte Carlo pozwala oszacować wartość całki na podstawie losowania punktów i średniej wartości funkcji. Większa liczba prób zwykle prowadzi do lepszej i bardziej stabilnej estymacji.

### Dzień 7 – porównanie zwykłego Monte Carlo i importance sampling

Dzisiaj porównywałam zwykłe Monte Carlo oraz importance sampling dla całki funkcji `f(x)=x^3` na przedziale `[0,1]`.

#### Co zrobiłam
- wykonałam 20 eksperymentów dla zwykłego Monte Carlo,
- wykonałam 20 eksperymentów dla importance sampling,
- w obu przypadkach użyłam `n = 5000`,
- obliczyłam średnią estymację całki,
- policzyłam błąd względem wartości dokładnej `1/4`,
- obliczyłam odchylenie standardowe jako prostą miarę niepewności,
- porównałam dokładność i stabilność obu metod.

#### Co zaobserwowałam
- zwykłe Monte Carlo dało poprawny wynik przybliżony,
- importance sampling dał mniejszy błąd estymacji,
- importance sampling dał także mniejsze odchylenie standardowe,
- oznacza to, że importance sampling był w tym przykładzie bardziej stabilny.

#### Wniosek
Importance sampling może poprawić jakość estymacji, jeśli częściej losuje punkty w obszarach, które mają większy wpływ na wartość całki. Dzięki temu przy tej samej liczbie prób można uzyskać dokładniejszy i mniej rozrzutny wynik.

### Dzień 8 – matematyka importance sampling i Monte Carlo w 2D

Dzisiaj uczyłam się matematycznego sensu importance sampling oraz estymacji pola obszaru w 2D metodą Monte Carlo.

#### Czego się nauczyłam o importance sampling
- w zwykłym Monte Carlo punkty są losowane równomiernie,
- w importance sampling losuje się z innego rozkładu `p(x)`,
- po zmianie rozkładu trzeba skorygować estymację przez dzielenie przez `p(x)`,
- jeśli `u ~ U(0,1)` i `x = sqrt(u)`, to nowy rozkład ma gęstość `p(x)=2x`,
- taki wybór pozwala częściej losować punkty blisko `1`, co pomaga dla funkcji rosnących jak `x^3`.

#### Czego się nauczyłam o Monte Carlo w 2D
- pole obszaru można estymować jako udział punktów, które wpadają do tego obszaru,
- jeśli losuję punkty w prostokącie, to:
  `pole obszaru ≈ pole prostokąta * liczba punktów w obszarze / liczba wszystkich punktów`,
- pole pod wykresem funkcji w 2D można połączyć z wcześniej poznanym pojęciem całki.

#### Wniosek
Monte Carlo w 2D jest naturalnym rozwinięciem wcześniejszych metod: zamiast średniej wysokości funkcji można estymować pole obszaru przez zliczanie punktów spełniających odpowiedni warunek geometryczny.

### Dzień 9 – samodzielne całkowanie Monte Carlo 2D

Dzisiaj samodzielnie wykonałam całkowanie Monte Carlo w 2D dla funkcji `f(x,y)=x*y` na kwadracie `[0,1] x [0,1]`.

#### Co zrobiłam
- losowałam punkty `(x,y)` w kwadracie jednostkowym,
- obliczałam wartości funkcji `x*y`,
- estymowałam całkę jako średnią wartość funkcji pomnożoną przez pole obszaru,
- porównywałam wynik z wartością dokładną `1/4`,
- analizowałam błąd estymacji dla różnych liczb prób.

#### Co zaobserwowałam
- wszystkie wyniki były bliskie wartości dokładnej,
- najlepszy wynik w tym pojedynczym przebiegu uzyskałam dla 1000 prób,
- większa liczba prób nie musi dawać najlepszego wyniku w każdym pojedynczym eksperymencie,
- Monte Carlo należy interpretować statystycznie, a nie tylko przez jeden przebieg.

#### Wniosek
Całkowanie Monte Carlo w 2D jest naturalnym rozszerzeniem wersji 1D i pozwala estymować objętość pod powierzchnią funkcji dwóch zmiennych. Wyniki potwierdziły poprawność metody i pokazały losowy charakter estymacji.

### Dzień 10 – random walk dla różnych liczb kroków

Dzisiaj porównywałam random walk 1D dla różnych liczb kroków: 10, 100 i 1000.

#### Co zrobiłam
- zasymulowałam 1000 cząstek,
- dla każdej liczby kroków wykonałam losowy ruch w lewo lub w prawo,
- zebrałam końcowe pozycje cząstek,
- narysowałam histogramy końcowych pozycji,
- obliczyłam średnią końcową pozycję i odchylenie standardowe.

#### Co zaobserwowałam
- średnia końcowa pozycja pozostawała bliska 0,
- rozrzut końcowych pozycji rósł wraz ze wzrostem liczby kroków,
- histogramy stawały się coraz szersze dla większej liczby kroków.

#### Wniosek
W random walk większa liczba kroków nie powoduje przesunięcia układu w jedną stronę, ale zwiększa rozproszenie końcowych pozycji. To daje intuicję, jak może zachowywać się układ wielu cząstek poruszających się losowo.


### Dzień 11 – random walk 2D dla różnych liczb kroków

Dzisiaj porównywałam random walk 2D dla 10, 100 i 1000 kroków.

#### Co zrobiłam
- zasymulowałam 1000 cząstek,
- dla każdej liczby kroków wykonywałam losowe ruchy w lewo, prawo, górę i dół,
- zapisałam końcowe położenia cząstek,
- obliczyłam średnie końcowe wartości `x` i `y`,
- policzyłam rozrzut położeń w obu osiach,
- narysowałam chmury końcowych położeń.

#### Co zaobserwowałam
- średnie końcowe wartości `x` i `y` pozostawały bliskie zeru,
- wraz ze wzrostem liczby kroków rosło rozproszenie końcowych położeń,
- największy rozrzut pojawił się dla 1000 kroków.

#### Wniosek
Random walk 2D pokazuje, że ruch losowy nie przesuwa układu w jedną stronę, ale powoduje coraz większe rozproszenie położeń cząstek. To daje intuicję związaną z dyfuzją i transportem cząstek w dwóch wymiarach.

### Dzień 12 – random walk z zatrzymaniem dla różnych granic

Dzisiaj porównywałam random walk 1D z granicami absorbującymi `-5, 5` oraz `-10, 10`.

#### Co zrobiłam
- zasymulowałam 1000 cząstek dla każdego przypadku,
- każda cząstka poruszała się losowo w lewo lub w prawo,
- ruch kończył się po osiągnięciu granicy absorbującej,
- zapisywałam liczbę kroków do zatrzymania,
- sprawdzałam, po której stronie cząstka została zatrzymana,
- porównywałam histogramy czasu do zatrzymania.

#### Co zaobserwowałam
- dla granic `-5, 5` cząstki zatrzymywały się średnio szybciej,
- dla granic `-10, 10` średni czas do zatrzymania był znacznie większy,
- liczba zatrzymań po lewej i prawej stronie była bardzo podobna,
- układ zachowywał się symetrycznie względem zera.

#### Wniosek
Warunki brzegowe silnie wpływają na czas ruchu cząstki w random walk. Bliższe granice oznaczają szybsze zatrzymanie, a szerszy obszar pozwala cząstce poruszać się dłużej. Przy symetrycznych granicach i symetrycznych krokach liczba zatrzymań po obu stronach pozostaje podobna.

### Dzień 13 – porównanie transmisji dla różnych poziomów absorpcji

Dzisiaj porównywałam transmisję i absorpcję dla różnych prawdopodobieństw pochłonięcia cząstek.

#### Co zrobiłam
- przyjęłam 1000 cząstek dla każdego przypadku,
- porównałam prawdopodobieństwa absorpcji: 0.2, 0.4, 0.6 i 0.8,
- dla każdej wartości obliczyłam:
  - liczbę cząstek pochłoniętych,
  - liczbę cząstek, które przeszły,
  - transmisję,
  - udział absorpcji,
- narysowałam wykres transmisji.

#### Co zaobserwowałam
- transmisja malała wraz ze wzrostem prawdopodobieństwa absorpcji,
- udział absorpcji rósł wraz ze wzrostem prawdopodobieństwa absorpcji,
- wyniki były bliskie wartościom oczekiwanym, ale nie idealnie równe z powodu losowości symulacji.

#### Wniosek
Materiał o większym prawdopodobieństwie absorpcji przepuszcza mniej cząstek i daje mniejszą transmisję. Model pokazuje, jak interpretować liczbę zdarzeń oraz udział cząstek pochłoniętych i transmitowanych w symulacji Monte Carlo.

### Dzień 14 – wpływ grubości materiału na absorpcję

Dzisiaj analizowałam prosty model absorpcji zależnej od grubości materiału.

#### Co zrobiłam
- przyjęłam 1000 cząstek,
- ustawiłam prawdopodobieństwo absorpcji w jednej warstwie na `0.3`,
- porównałam grubości materiału: `1`, `3`, `5`, `8`, `12`,
- dla każdej grubości liczyłam:
  - liczbę cząstek pochłoniętych,
  - liczbę cząstek transmitowanych,
  - transmisję,
  - udział absorpcji.

#### Co zaobserwowałam
- wraz ze wzrostem grubości materiału rosła liczba zdarzeń absorpcji,
- transmisja malała bardzo wyraźnie,
- najlepszą osłoną w tym modelu okazała się grubość `12`,
- dla największej grubości przechodziła już tylko niewielka liczba cząstek.

#### Wniosek
Grubszy materiał daje cząstce więcej okazji do pochłonięcia, dlatego działa jako skuteczniejsza osłona. Prosty model warstwowy dobrze pokazuje intuicję osłabiania wiązki i spadku transmisji wraz ze wzrostem grubości materiału.

### Dzień 15 – czytelne wykresy do portfolio

Dzisiaj uczyłam się, jak tworzyć czytelne wykresy dla wyników Monte Carlo, tak aby nadawały się do portfolio lub raportu.

#### Czego się nauczyłam
- dobry wykres powinien mieć jasny tytuł i podpisane osie,
- typ wykresu powinien pasować do rodzaju danych,
- legenda jest potrzebna wtedy, gdy porównuję kilka serii danych,
- warto dodać linię odniesienia, jeśli znam wartość dokładną,
- delikatna siatka i odpowiedni rozmiar wykresu poprawiają czytelność,
- `tight_layout()` pomaga uporządkować wygląd wykresu,
- wykres można zapisać do pliku PNG i wykorzystać później w README lub portfolio.

#### Wniosek
Czytelny wykres nie tylko pokazuje wynik, ale też pomaga zrozumieć jego sens. W projektach Monte Carlo wykres powinien wspierać interpretację danych, a nie być tylko ozdobą.

### Projekt podsumowujący – transmisja przez materiał warstwowy

W projekcie zasymulowano przejście wiązki cząstek przez materiał o różnej grubości metodą Monte Carlo. Każda warstwa dawała cząstce określone prawdopodobieństwo absorpcji. Dla każdej grubości wykonano 20 niezależnych uruchomień, aby policzyć średnią transmisję oraz odchylenie standardowe.

#### Co zaobserwowałam
- transmisja malała wraz ze wzrostem liczby warstw,
- grubszy materiał przepuszczał coraz mniejszą część wiązki,
- odchylenie standardowe między uruchomieniami było niewielkie względem głównego trendu.

#### Wniosek
Projekt pokazał, że prosty model warstwowy pozwala połączyć losowość, absorpcję, transmisję, analizę niepewności i prezentację wyników na wykresie. Jest to uproszczona, ale sensowna intuicja osłabiania wiązki w materiale.