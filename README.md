# Apex OS

**Apex** je besplatan, offline operativni sustav za laptope — poznat izgled radne površine, bez pretplate i bez stalne internetske veze nakon instalacije.

> Apex **nije** Microsoft Windows. Temelji se na **Linuxu** (Arch) s desktop okruženjem koje podsjeća na Windows (KDE Plasma). To je legalan, otvoren i održiv put za vlastiti „OS“ brend.

## Za koga

- Pojedinci, škole, male firme — svi koji žele jednostavan laptop bez cloud ovisnosti
- Besplatno, bez licence

## Platforme

| Što | Podrška |
|-----|---------|
| **Laptopi (PC)** x86_64 | ✅ Glavna meta — boot s USB ili instalacija na disk |
| **Apple Mac** | ⚠️ Ne kao zamjena macOS-a; moguće dual-boot / VM (ograničenja Apple hardvera) |
| **Stari PC** | ✅ Uglavnom x86_64; provjeri RAM (preporuka 4 GB+) |

„Svi“ u praksi znači: **jedan ISO za većinu laptopa** + web stranica dostupna s bilo kojeg preglednika za preuzimanje.

## Što dobiješ nakon preuzimanja

1. Preuzmeš `apex-os-*.iso` s weba
2. Zapišeš na USB (Rufus, balenaEtcher, Ventoy…)
3. Boot s USB → live radna površina ili instalacija na disk
4. Radi **offline**: ugrađeni preglednik, ured, multimedija, upravitelj datoteka

## Struktura repozitorija

```
Apex/
├── website/          # Stranica za preuzimanje
├── os/archiso/       # Profil za izgradnju ISO-a
├── os/scripts/       # Build skripte (Linux / WSL)
└── .github/workflows # Automatska gradnja ISO-a (opcionalno)
```

## Kako izgraditi ISO (razvoj)

Potreban je **Linux** ili **WSL2** na Windowsu:

```bash
# WSL2 (Ubuntu) — jednokratno
sudo pacman -Syu   # ako koristiš Arch WSL; inače vidi docs/BUILD.md

cd os/scripts
./build.sh
```

Detalji: [docs/BUILD.md](docs/BUILD.md)

## Roadmap

- [x] Projektna struktura + web landing
- [x] Archiso profil (live ISO, Plasma, offline paketi)
- [x] Calamares installer (instalacija na disk)
- [x] Apex Store + Google (Chromium)
- [ ] Apex branding u bootu i loginu
- [ ] Automatski release na GitHub Releases / CDN

## Licenca

Kod ovog repozitorija: MIT. Komponente u ISO-u (kernel, Plasma, LibreOffice…) imaju svoje open-source licence.
