import zlib, base64
exec(zlib.decompress(base64.b64decode('eJzNWetv4kgS/85f0YcUYScOY2dmTys0vTrIzGTnsRfvJblclEOWAw0Y8GNsM+Qh/vfrtsFVZTfJzOhOug8g3FVdXfWrZ5t2u30ah8kqFxnLZ4KJ+0SMcjFm6yBiqZ8LFk9YHAmW5epp+sD8qR9EWc78KJYb0m673W79Y5klf//jX+9dn3/wl5mAhTN+ma7Q82eerUJ4XPMgU9L8aISYbrh/l8HjhOerZInoY56kQZTDwoqHQQSPl/z9/UgkeRDD4vyKp340BSlzl4f+PTz2+TLIQOZ8wPOHRLQmaRyyUbxcSlikvIwFYRKnOYv8UIxLvcZiwqqzL4xJZPZa1cKVy582LUZ4ZsZhRZ4rZhYA9WrOJLJMwg8iFAt6vAXeIZ9ERJrkTEW+SqM9/K062Z1RA343Ku5zpduW3TmG5dbfwFy6+Z9GYbw0J3p70mvq4vottuAnLbaeBUvBFoeLtzzaAhAdLDi3C1M1u9jiiDtN5c/263Je6hIV+8rzFLB1XbcMW8ERlfEBwOhb1c8BwgXovzkyJ8awMCgXkIQDoElLWZwiZqD1Jc2kanwEIdckuASHzDLAzdfw83E4wec8ksC6Hsp4eY6u8NFLfcVBCapsBMreWXGSyOoR5V42ilOBcHtTZdrVF44cXa1ecEgxo3Mmf1/ksgJ1rNtOISvrWJ1tUQqKh/Uslt9JKr555c88CEVHWliJnBGRl1KNSmTuL5cPcs/MzzypsPwVrUIvlXmfKRHEwBAMHCuL/CwTKQqsNaJD0MxMyCWS7+Pu9lAmZOnE64VSoP7vAPnMKGjctrZ7EYRWpXkjjj5pNRv9lBENXeqKH8EBDS2R0Tj6Rpw7SH3EXS0eOTWbAqyoYvHGwUh48SofxaEA1dffb+WFqeN8RraCRVsosAll1CLGc0yVIYtIHzBpF9KI/pGgLeMc0SKIhbCptNkiwbfelly8dr4rw0jkSeVN9wYwGxw4NvSFwatXjq0akIrj7xPQJwL6WwE6ZYDpCGyPWtVZoAWlB99XzV9y3wBW+1TBL3X4Ph78ymHjmjaFD38B0jnFKEQUpkUROGiXxup/4kD5KJPl4FcNRt8nCOQ0k/7CKMOZ74HUgtJMcqBatWRAAyW0dkGOQLBUYMPzp1rip7UyvCuuNmX7pmerFlPKHhtFtozlLIg7rWzBsN4cQyZA7Qa5CDPDRH0n5Uj8k9NzrBP5eS0/b+TnF/n5q/xs0I5vz+7AnLGG8/WW8zVm/PM5xq0SasPeeepPAHJtEZBqBeXYIUV9V2JKzJ6gnfWcDSpb0EDISceOhYGvCF+LsZrMLncQgO/IGPOw84lSg2wZwZap2lIdRRMvB90+GbrzRip1CA55Y4r/WshEzzBO5UNut/bSUEF7B6P+lAQn7NR06K/UkQ9GkYZ2maOONY39JXdsm8Q7MhmddHXK6WZ5Wp4+kOJyD+pClbAtW18TTotCYEP+S4cXeW+TarT4CaHOHqElPAaYCujdF2CYRzraoqSZr+T1RRT3S0DrVM4LjNbYcy5kuZOqla0dCH5FANXB3edDxOuODYFudE7XBv+fU6d+LaJ7ezkdS7G1qeCM7xa71Y8oXhsop1y4q7h3qoBhyp7d0LzPauX5Dis0i6fNovlgyOXuJIj8pbd7vVCllBvV5I1qdfyFhq2Ztz5DSJPeUYUwncpV3NQHoTWIWIGIzxY+FpxqD/d0R/2Q9GPCHSQcTydKeD08L6vwTP0A3THcBZ5/G7NhvYTNr2TKOY6pEXSvHaTXmmK0pm7N8UZdJXrRv3jCW+0B/DeuRPcY5JLd/UUNRtjefpPLqfMMNJJaWheOaIjVg/9d3W6C2t4m/E6L86p2zamebjjWbqJvsZBzZFaqvxrI4ZBL0tgmuL3C0dC2kJPpdU0ne20iu0yod5fNULqBV35XahwgSE31SJEmN0fxhJb7HOrxeLh7eQRkYucYzOzfHjvDeh2pJ5F7RbP+pfBmu+qkrxS1MGPPtKba7DMmWvVLDqQmxoCLglomvSD6/3BQoTMG/PbHIiMxayGZ6CNReYFY6wpi7YAC6qL3J0KW7YKI64poepHc6+Yu2CG2rjPfQtTVwe13/SQR6OWgKygyFH3QWzGN4igPopUomgjWEt5m0P0VhPO+SYLPfSznTooUBZWKqgViwBtmN7BDNTmQhXg/KI9HXFblw6RYpmU3kE55Yat+m6PblvhZtuXe9mAqSmO6K4alYi956LFF3JzEiUHbqt5L7hy85J7qOizhbfYTSh4tpYmoBsCRl0q2KpSeF0RB7nlAukaTBqnl7nU5sOJqWTsB+n+p/csn1FrWD7yae1YvQtW8SlzvdJOjFFHNRH9XtN9/85crX/3ho/7/cpf+g0jZk73pZOzJ2TydbLacYsyeXm8sWQtkysg9gSz3q/BOMsttxcntrkyu0Ecd8BquBVZjUXMlwBuGXc9T77A9T7O1SL/bXs84dszDQ+12SweOWXfm4ued6X75nzlTpGmM3qR8+W85UqXZuPjzcyLRiNdBNGXFWb1/R6oySAf32NObzf+pJ+cDow6SqZVdklqBwqykct72vNAPIs9r98htr3MTr1J1a2PF9az6N1gCsek0cFCXRbP1H4dA36s=')))
# Created by pyminifier (https://github.com/liftoff/pyminifier)

