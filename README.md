# Pbtt

Repository of *"Pbtt"* (Post Body Translator Tool). Give a HTTP body param as input and it will output the XML + Json versions of it.

Enjoy !

# Install

```bash
chmod +x scripts/install.sh
sudo scripts/install.sh
```

# Uninstall

```bash
chmod +x scripts/uninstall.sh
sudo scripts/uninstall.sh
```

# Use

## Basic usage

```bash
pbtt '?blabla=truc&machin=test'
> application/json :
>         {"blabla": "truc", "machin": "test"}
> text/xml :
>         <?xml version="1.0" encoding="UTF-8"?><blabla>truc</blabla><machin>test</machin>
```

## XML as input

```bash
pbtt '<?xml version="1.0" encoding="UTF-8"?><blabla>truc</blabla><machin>test</machin>' -x
> application/x-www-form-urlencoded :
>         ?blabla=truc&machin=test
> application/json :
>         {"blabla": "truc", "machin": "test"}
```

## Json as input

```bash
pbtt '{"blabla": "truc", "machin": "test"}' -j
> application/x-www-form-urlencoded :
>         ?blabla=truc&machin=test
> text/xml :
>         <?xml version="1.0" encoding="UTF-8"?><application/x-www-form-urlencoded :?blabla>truc</application/x-www-form-urlencoded :?blabla><machin>test</machin>
```

# Contact

You shall not contact
