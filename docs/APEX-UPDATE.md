# Kako objaviti update za korisnike Apex OS-a

Kad instaliraju Apex na disk, ažuriranje ide preko **Apex Update** (ne novog ISO-a svaki put).

## Za korisnike (na laptopu)

1. Spoji internet
2. Otvori **Apex Update** (ili Apex Postavke → Apex Update)
3. **Provjeri ažuriranja** → **Instaliraj ažuriranja**
4. Po potrebi restart

To ažurira programe i sustav (pacman).

## Za tebe (developer) — nova verzija Apex OS

1. Uredi `os/apex-version.json` na GitHubu:

```json
{
  "version": "1.1",
  "notes": "Nova trgovina, popravci zvuka.",
  "iso_url": "https://link-do-novog-iso.iso"
}
```

2. U `os/archiso/apexos/airootfs/etc/apex-release` stavi istu verziju i URL:

```
APEX_VERSION=1.1
APEX_UPDATE_URL=https://raw.githubusercontent.com/TVOJ_USER/TVOJ_REPO/main/os/apex-version.json
```

3. Push na GitHub — korisnici s Apex Update vide poruku da postoji 1.1.

4. Za velike promjene: izgradi novi ISO (GitHub Actions) i stavi `iso_url` u JSON.

## Samo paketi (bez nove verzije broja)

Korisnik samo pokrene Apex Update — `pacman -Syu` povuče najnovije pakete iz Arch repozitorija.
