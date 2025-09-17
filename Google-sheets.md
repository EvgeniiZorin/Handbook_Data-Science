
Split column by a character (e.g. newline) VERTICALLY:
```
=ArrayFormula( QUERY( UNIQUE( TRIM( FLATTEN( SPLIT($A$1:$A, char(10) )))), "where Col1 is not null order by Col1"))
```

or a semicolon:
```
=ArrayFormula( QUERY( UNIQUE( TRIM( FLATTEN( SPLIT($A$1:$A, ";")))), "where Col1 is not null order by Col1"))
```

