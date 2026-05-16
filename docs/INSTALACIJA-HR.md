# Kako instalirati Apex OS na svoj laptop

Ovaj vodič pretpostavlja da imaš **Windows laptop** i želiš Apex OS na disku (ili dual-boot).

## Što ti treba

- Laptop s **64-bit** procesorom (Intel ili AMD)
- **USB stick 8 GB** ili veći (sve će biti obrisano s USB-a)
- ISO datoteka Apex OS-a
- Alat za pisanje ISO-a na USB: [Rufus](https://rufus.ie) ili [balenaEtcher](https://etcher.balena.io)

## Korak 1: Nabavi ISO

1. Ako je ISO objavljen na webu — preuzmi s gumba **Preuzmi ISO** (kad je URL postavljen u `website/download.json`).
2. Ako još nema linka — moraš **izgraditi ISO** na Arch Linuxu / WSL-u (vidi [BUILD.md](BUILD.md)).

## Korak 2: Zapiši ISO na USB

### Rufus (Windows)

1. Umetni USB.
2. Otvori Rufus → **Select** → odaberi `apexos-....iso`.
3. **Partition scheme:** GPT (za novije laptope) ili MBR (stariji).
4. **Start** → pričekaj da završi.

### balenaEtcher

1. Flash from file → odaberi ISO.
2. Odaberi USB → **Flash**.

## Korak 3: Boot s USB-a

1. Umetni USB u laptop.
2. Restartaj računalo.
3. Odmah pritisni tipku za boot menu (često **F12**, **F2**, **Esc**, **Del** — ovisi o proizvođaču).
4. Odaberi **USB** / **UEFI: ime tvog USB-a**.
5. Ako ne vidiš USB: u BIOS/UEFI isključi **Fast Boot** i po potrebi **Secure Boot**.

## Korak 4: Isprobaj live (opcionalno)

Nakon boota vidiš Apex radnu površinu **bez instalacije** na disk.

- Korisnik: `liveuser`
- Lozinka: `apex`
- Na radnoj površini: **Google**, **Apex Store**, **Instaliraj Apex OS**

## Korak 5: Instalacija na disk

1. Spoji **Wi‑Fi** (instalacija i Apex Store za nove aplikacije trebaju internet).
2. Klikni **Instaliraj Apex OS** (Calamares).
3. Slijedi čarobnjak:
   - jezik / dobrodošlica
   - **particije** — pazi:
     - **Erase disk** briše cijeli disk (Windows nestaje).
     - **Alongside** / ručno particioniranje = dual-boot s Windowsom (naprednije).
   - kreiraj **korisničko ime i lozinku**
   - instalacija traje 10–30 minuta
4. Kad završi → **Restart** → izvadi USB.

## Korak 6: Prvi boot s diska

Nakon restarta laptop bi trebao pokrenuti Apex OS s tvrdog diska.

- Otvori **Apex Store** za dodatne aplikacije (Discord, Steam…).
- **Google** ikona otvara Google u Chromium pregledniku.

## Dual-boot s Windowsom (kratko)

- Napravi **backup** važnih datoteka.
- U Windowsu: **Disk Management** → smanji C: particiju za slobodan prostor (npr. 50 GB+).
- U Calamaresu odaberi slobodan prostor za Apex.
- Nakon instalacije pri bootu biraš Windows ili Apex (GRUB izbornik).

## Problemi?

| Problem | Rješenje |
|--------|----------|
| Ne boota USB | Isključi Secure Boot; probaj drugi USB port; GPT vs MBR u Rufusu |
| Crn ekran | Na bootu odaberi safe graphics / probaj `nomodeset` u GRUB |
| Nema Wi‑Fi | Kabel Ethernet ili drugi Wi‑Fi čip (možda treba firmware) |
| Calamares ne radi | U terminalu: `sudo archinstall` |

## Web stranica lokalno

Ako download gumb ne radi kad otvoriš `index.html` dvostrukim klikom:

```powershell
cd website
python -m http.server 8080
```

Otvori: http://localhost:8080
