# Izgradi Apex ISO preko GitHuba (Windows, bez Linuxa)

Ovaj vodič je za ljude koji **ne znaju što je Linux** i ne žele ručno graditi sustav — GitHub to napravi u oblaku.

## Što trebaš

- Račun na [github.com](https://github.com) (besplatno)
- Mapa `Apex` s Desktopa
- Internet
- Strpljenje ~1 sat za prvi build

---

## Korak 1: GitHub račun

1. Otvori [github.com/signup](https://github.com/signup)
2. Registriraj se (email + lozinka)

---

## Korak 2: Novi repozitorij

1. Prijavi se → gumb **+** (gore desno) → **New repository**
2. Ime npr. **`apex-os`**
3. **Public** ili Private (oba rade)
4. **Create repository** (ne označavaj README ako uploadaš cijelu mapu)

---

## Korak 3: Upload Apex projekta

### Opcija A — GitHub Desktop (lakše)

1. Preuzmi [GitHub Desktop](https://desktop.github.com)
2. **File → Add local repository** → odaberi `C:\Users\TVojeIme\Desktop\Apex`
3. **Publish repository** → odaberi ime `apex-os`
4. **Push origin** (pošalji datoteke na GitHub)

### Opcija B — Web upload

1. Na stranici repozitorija: **Add file → Upload files**
2. Povuci cijelu mapu Apex (ili zip pa raspakiraj na GitHubu — sporije za velike projekte)

---

## Korak 4: Pokreni gradnju ISO-a

1. Na GitHubu otvori svoj repo **`apex-os`**
2. Tab **Actions**
3. Ako piše da Actions nisu uključeni → **Enable Actions** / **I understand…**
4. Lijevo: **Build Apex ISO**

   **Ne vidiš "Build Apex ISO"?** → vidi [NEMA-BUILD-APEX-ISO.md](NEMA-BUILD-APEX-ISO.md)  
   (najčešće nisi uploadao skrivenu mapu `.github`)

5. Desno: **Run workflow** → **Run workflow** (potvrdi)
6. Osvježi stranicu — vidi se žuti krug (u tijeku)

Pričekaj dok ne postane **zelena kvačica** (✓). Ako je crveno (✗), otvori run i pogledaj grešku (često nedostaje `prepare-profile` ili mreža).

---

## Korak 5: Preuzmi gotov ISO

1. Klikni na završeni **workflow run**
2. Dolje: sekcija **Artifacts**
3. Preuzmi **`apexos-iso`** (ZIP datoteka)
4. Raspakiraj ZIP — unutra je **`apexos-....iso`**

To je tvoja instalacijska datoteka.

---

## Korak 6: Stavi link na web (opcionalno)

U projektu na računalu otvori `website/download.json`:

```json
{
  "version": "1.0",
  "url": "https://github.com/TVOJ_USER/apex-os/releases/download/v1.0/apexos.iso",
  "filename": "apexos-1.0-x86_64.iso"
}
```

Ili za test samo drži ISO lokalno i koristi Rufus — web link nije obavezan za tebe osobno.

Za javno preuzimanje: **Releases** → **Create new release** → priloži ISO → kopiraj link u `download.json`.

---

## Korak 7: Instalacija na laptop

Slijedi [INSTALACIJA-HR.md](INSTALACIJA-HR.md):

1. Rufus → ISO na USB  
2. Boot s USB  
3. **Instaliraj Apex OS**

---

## Problemi?

| Problem | Rješenje |
|--------|----------|
| Nema tab Actions | U repo Settings → Actions → Allow all |
| Build failed | Otvori log; često privremena greška — Run workflow ponovo |
| Artifact prazan | Pričekaj da build u potpunosti završi |
| Prevelik ISO za upload | GitHub Release dopušta velike datoteke (do limita); ili drži ISO samo lokalno |

---

## Sažetak jednom rečenicom

**ISO = jedna datoteka = cijeli Apex za USB** → najlakše je neka je **GitHub Actions** izgradi umjesto tebe.
