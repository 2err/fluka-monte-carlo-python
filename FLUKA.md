## Pierwszy kontakt z Flair

Dzisiaj uruchomiłam Flair i zapoznałam się z podstawową strukturą projektu FLUKA.

### Co zobaczyłam
- główne zakładki: Input, Geometry, Run, Plot
- szkielet inputu zawierający m.in. `GEOBEGIN`, `GEOEND` i `STOP`
- w geometrii dostępne są różne typy body, np. `RPP`, `SPH`, `RCC`
- `RPP` jest opisywany przez granice `Xmin/Xmax`, `Ymin/Ymax`, `Zmin/Zmax`

### Co zrozumiałam
- `Body` opisuje kształty geometryczne
- `Region` opisuje właściwe obszary symulacji
- region jest definiowany logicznie, m.in. przez pole `expr`
- geometria FLUKA jest budowana tekstowo i logicznie, a nie tylko przez rysowanie obiektów

## Kolejna sesja z Flair – pierwszy model z beamem

Dzisiaj kontynuowałam budowanie pierwszego modelu FLUKA w Flair.

### Co zrobiłam
- utworzyłam dwa body typu `RPP`:
  - `rpp1` jako mały blok
  - `world` jako większy obszar świata
- zdefiniowałam dwa regiony:
  - `reg1 = rpp1`
  - `reg_w = world-rpp1`
- przypisałam materiały przez `ASSIGNMAT`:
  - `LEAD` do `reg1`
  - `AIR` do `reg_w`
- dodałam kartę `BEAM`
- ustawiłam typ cząstki jako `PROTON`
- zaczęłam pracę z kartą `BEAMPOS`, która definiuje pozycję startową i kierunek wiązki

### Co zrozumiałam
- `BEAM` mówi, jaka cząstka wpada do modelu
- `BEAMPOS` mówi, skąd i w jakim kierunku ta wiązka startuje
- pełny model FLUKA zaczyna składać się z geometrii, materiałów i źródła cząstek

### Wniosek
Mój model ma już podstawową strukturę fizyczną: blok ołowiu w powietrzu oraz wiązkę protonów, która może zostać skierowana na obiekt. Kolejnym krokiem będzie dokończenie ustawień wiązki i dodanie pierwszego scoringu.