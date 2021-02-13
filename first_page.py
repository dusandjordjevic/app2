class Osoba():
    def __init__(self,ime, prezime, jmbg, adresa, pol):
        self.ime = ime
        self.prezime = prezime
        self.jmbg = jmbg
        self.adresa = adresa
        self.pol = pol
class Zaposleni(Osoba):
    def __init__(self, ime, prezime, jmbg, adresa, pol, plata, korisnicko_ime, sifra):
        super().__init__(ime, prezime, jmbg, adresa, pol)
        self.plata = plata
        self.korisnicko_ime = korisnicko_ime
        self.sifra = sifra

class Clanovi_videoteke(Osoba):
    def __init__(self, ime, prezime, jmbg, adresa, pol, broj_clanske_karte, aktivnost_clana):
        super().__init__(ime, prezime, jmbg, adresa, pol)
        self.broj_clanske_karte = broj_clanske_karte
        self.aktivnost_clana = aktivnost_clana

clan1 = Clanovi_videoteke("Marko","Djordjevic","4234634","Blagoje Parovica 40", "Muski", "4", "Aktivan" )

print(clan1.aktivnost_clana)
    