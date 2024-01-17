# Projekts

## Projekta mērķis

Projekta mērķis bija izstrādāt Python skriptu, kas izmanto Selenium bibliotēku, lai veiktu "login" noteiktā Instagram kontā un atzīmētu "patīk" jaunākajai bildei noteiktam Instagram kontam. Šajā gadījumā, kā piemērs tika izmantots "daily_otis" konts, jo tajā katru dienu tiek publicēta viena jauna bilde, jau vairākus gadus pēc kārtas (šobrīd ir publicētas vairāk nekā 2000 bildes), visticamāk, arī ar kādu automatizēšanas veidu.

### Izmantotās bibliotēkas

Selenium: Tika izmantota tīmekļa pārlūka automatizācijai. Ar tās palīdzību Python skripts varēja izmantot, jeb kontrolēt pārlūkprogrammu.

webdriver.manager: Palīgbibliotēka, kas nodrošināja nepieciešamo "driver" (šajā gadījumā, ChromeDriver) Selenium darbībai ar pārlūkprogrammu.

### Programmatūras izmantošanas metodes

Inicializācija un pārlūka kontrole: Skripts sākas ar pārlūka atvēršanu izmantojot Selenium WebDriver. Pēc tam tiek atvērta un ielādēta Instagram pieteikšanās, jeb "login" lapa.
Pieteikšanās Instagram: Skripts aizpilda lietotājvārda un paroles laukus, un pēc tam nospiež ienākšanas pogu.
Navigācija uz konkrēto kontu: Pēc pieteikšanās, skripts atver noteiktā Intagram konta saiti.
Interakcija ar lapu: Skripts meklē jaunāko bildi un izmanto Selenium ActionChains funkciju, lai veiktu dubultklišķi un bildes, tādējādi atzīmējot to ar "patīk" funkciju.
Automātiska pārlūka aizvēršana: Beigās skripts automātiski aizver pārlūkprogrammu.
