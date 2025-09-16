

Combine different sheets called sheet1, sheet2, and sheet 3 into one
and then filter them all based on regexp condition - that they contain `pattern1*` or `pattern2*`

```txt
=filter(
    {sheet1!1:818; 'sheet/2'!1:818; 'sheet 3'!1:818}, 
    REGEXMATCH(
        {sheet1!H1:H818; 'sheet/2'!H1:H818; 'sheet 3'!H1:H818}, 
        "pattern1*|pattern2*") = true
)
```

