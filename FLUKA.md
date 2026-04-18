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