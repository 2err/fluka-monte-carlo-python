# FLUKA i Monte Carlo w Pythonie

Repozytorium dokumentuje moją naukę metod Monte Carlo w Pythonie oraz przygotowanie do pracy z tematami związanymi z FLUKA, transportem cząstek, absorpcją, transmisją i prostymi modelami fizycznymi.

## Co znajdziesz w repo
- skrypty Python z kolejnych etapów nauki
- proste modele Monte Carlo
- wykresy i mini-projekty
- dziennik postępów

## Jak uruchomić projekt
```bash
uv sync
# albo
pip install -r requirements.txt
```

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

## Autorstwo i sposób przygotowania materiałów

W repozytorium znajdują się zarówno przykłady tworzone wspólnie w ramach procesu nauki, jak i zadania wykonywane samodzielnie.

- Skrypty bez dopisku `homework` zostały przygotowane z wykorzystaniem wsparcia ChatGPT podczas wspólnej nauki, omawiania teorii i budowania przykładów.
- Skrypty z dopiskiem `homework` stanowią moją indywidualną pracę i samodzielne rozwiązania zadań.

### Dzień 1 23.03
- skonfigurowałam środowisko w PyCharm
- podpięłam lokalne `.venv`
- uruchomiłam pierwszy skrypt z `numpy`, `pandas`, `matplotlib`
- przećwiczyłam losowanie z rozkładu jednostajnego
- zaobserwowałam, że wraz ze wzrostem liczby prób średnia zbliża się do wartości teoretycznej 0.5

#### Projekty: 
01_start

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

#### Projekty: 
02_uniform_sampling
03_monte_carlo_pi
04_hist_uniform

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

#### Projekty: 
05_seed_test
06_seed_histogram.
07_compare_sample_sizes
07_homework_compare_seeds

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

#### Projekty: 
08_basic_statistics.py
09_compare_statistics.py
09_homework_compare stat.py


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

#### Projekty:
10_monte_carlo_pi.py
11_pi_stability.py]
12_pi_convergence_plot.py
12_pi_homework.py
13_pi_uncer_homework.py
13_pi_uncertainty.py

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

#### Projekty:

14_mc_integration_x2.py
15_mc_integration_stability.py
16_mc_integration_x.py

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

#### Projekty:
17_importance_sampling_intro.py
18_importance_sampling_compare.py
18_importance_sampling_homework.py


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

#### Projekty:
19_area_under_curve_mc.py
19_area_under_homework.py


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

#### Projekty:
20_mc_2d_integration_xy.py
21_mc_2d_integration_stability.py
21_mc_integration_2d_homework.py

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

#### Projekty:
22_random_walk_1d.py
23_homework_randomwalk_different steps.py
23_random_walk_many_particles.py

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

#### Projekty:
24_random_walk_2d_single.py
25_random_2d_homework.py
25_random_walk_2d_many.py


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

#### Projekty:
26_random_walk_absorbing_1d_single.py
27_random_walk_absorbing_1d_many.py
27_random_walk_absorbing_homework.py

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

#### Projekty:
28_absorption_model_basic.py
29_absorption_compare.py
29_absorption_homework.py

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

#### Projekty:
30_abs_vs_thick_homework.py
30_absorption_vs_thickness.py

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

#### Projekty:
31_portfolio_plot_transmission.py
32_homework_integral_beautiful_graph.py
32_portfolio_histogram_absorption_time.py

### Dzień 16: Projekt podsumowujący – transmisja przez materiał warstwowy

W projekcie zasymulowano przejście wiązki cząstek przez materiał o różnej grubości metodą Monte Carlo. Każda warstwa dawała cząstce określone prawdopodobieństwo absorpcji. Dla każdej grubości wykonano 20 niezależnych uruchomień, aby policzyć średnią transmisję oraz odchylenie standardowe.

#### Co zaobserwowałam
- transmisja malała wraz ze wzrostem liczby warstw,
- grubszy materiał przepuszczał coraz mniejszą część wiązki,
- odchylenie standardowe między uruchomieniami było niewielkie względem głównego trendu.

#### Wniosek
Projekt pokazał, że prosty model warstwowy pozwala połączyć losowość, absorpcję, transmisję, analizę niepewności i prezentację wyników na wykresie. Jest to uproszczona, ale sensowna intuicja osłabiania wiązki w materiale.

#### Projekty: 
33_mc_transport_summary_project.py
33_particle in layerd material.py

### Dzień 17 – porównanie dwóch materiałów i interpretacja niepewności

Dzisiaj porównywałam dwa materiały o różnych prawdopodobieństwach absorpcji w modelu warstwowym Monte Carlo.

#### Co zrobiłam
- porównałam materiał `M.1` (`p_absorption = 0.15`) i materiał `M.2` (`p_absorption = 0.30`),
- dla każdej grubości wykonałam wiele niezależnych uruchomień,
- policzyłam średnią transmisję i odchylenie standardowe,
- narysowałam wykres z error barami.

#### Co zaobserwowałam
- materiał `M.2` dawał niższą transmisję dla wszystkich analizowanych grubości,
- w obu materiałach transmisja malała wraz ze wzrostem liczby warstw,
- odchylenie standardowe było niewielkie w porównaniu do różnicy między materiałami.

#### Wniosek
Porównywanie modeli Monte Carlo wymaga patrzenia nie tylko na średni wynik, ale też na rozrzut między uruchomieniami. W tym projekcie różnica między materiałami była wyraźna i wyglądała na sensowną fizycznie, a nie tylko losową.

#### Projekty:
34_compare_materials_homework.py
34_compare_two_materials_uncertainty.py