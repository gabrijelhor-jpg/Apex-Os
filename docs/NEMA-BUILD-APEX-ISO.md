# Na GitHubu nema "Build Apex ISO" — rješenja

## Zašto ga ne vidiš?

Workflow **Build Apex ISO** živi u **skrivenoj** mapi:

```
Apex/.github/workflows/build-iso.yml
```

Na Windowsu mape koje počinju s točkom **često se ne uploadaju** ako ne paziš. Bez te mape GitHub **nema** što pokrenuti — zato u Actions nema ničega.

---

## Rješenje 1 — GitHub Desktop (preporuka)

1. Instaliraj [GitHub Desktop](https://desktop.github.com)
2. **File → Add local repository**
3. Odaberi: `C:\Users\TVOJE_IME\Desktop\Apex`
4. Ako pita „create repository” — potvrdi
5. **Repository → Repository settings** — provjeri da postoji mapa `.github` u listi datoteka
6. **Publish repository** (ili **Push origin**)
7. Na github.com otvori repo → tab **Actions**
8. Ako piše *"Workflows aren't being run"* → klikni **I understand my repositories, enable Actions**
9. Lijevo moraš vidjeti: **Build Apex ISO**

### Ručno pokretanje

1. **Actions** → **Build Apex ISO** (lijevo)
2. Desno **Run workflow** → **Run workflow**

---

## Rješenje 2 — ZIP s .github mapom

1. U Exploreru: **View → Show → Hidden items** (Prikaži skrivene datoteke)
2. Provjeri da u `Desktop\Apex` postoji mapa **`.github`**
3. Pokreni (dvostruki klik na **`napravi-zip-za-github.bat`**)  
   ili u PowerShellu:

```powershell
cd $env:USERPROFILE\Desktop\Apex
.\napravi-zip-za-github.bat
```

Ako piše da su skripte blokirane, koristi **.bat** datoteku — ona zaobilazi tu blokadu.

4. Na GitHubu: **Add file → Upload files** → povuci **`Apex-za-GitHub.zip`**
5. Osvježi **Actions**

---

## Rješenje 3 — Ručno dodaj workflow na GitHubu

Ako uploadaš bez `.github`:

1. Na GitHubu repo → **Add file** → **Create new file**
2. U ime datoteke upiši točno:

```
.github/workflows/build-iso.yml
```

(GitHub sam napravi mape `.github` i `workflows`)

3. Kopiraj cijeli sadržaj iz svog PC-a:  
   `Apex\.github\workflows\build-iso.yml`
4. **Commit changes**
5. Otvori **Actions** — trebao bi se pojaviti **Build Apex ISO**

---

## Još uvijek prazno?

| Provjeri | Gdje |
|----------|------|
| Actions uključen | Repo → **Settings** → **Actions** → **General** → Allow all actions |
| Gledaš pravi repo | Ime repozitorija koji si uploadao |
| Default branch | **main** ili **master** (workflow mora biti na toj grani) |
| Osvježi stranicu | Actions tab, F5 |

---

## Nakon što vidiš Build Apex ISO

1. Klikni **Run workflow** (ili pričekaj automatski run nakon pusha)
2. Žuto = radi, zeleno = gotovo, crveno = greška (otvori log)
3. Na dnu uspješnog runa: **Artifacts** → **apexos-iso** → preuzmi ZIP → unutra je `.iso`

---

## Ne želiš GitHub?

Tada ISO mora izgraditi netko s Arch Linuxom ili ti treba pomoć developera — bez ISO-a nema instalacije na laptop. Vidi [ISO-ZA-POCETNIKE.md](ISO-ZA-POCETNIKE.md).
