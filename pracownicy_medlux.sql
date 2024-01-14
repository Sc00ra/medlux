CREATE DATABASE medlux;
CREATE SCHEMA medlux;

\dt --update tabelek

INSERT INTO pracownicy_pracownik (imie, nazwisko, pesel, stanowisko)
VALUES
('Jan', 'Kowalski', '98765432101', 'Dyrektor'),
('Anna', 'Nowak', '98765432102', 'Lekarz'),
('Paweł', 'Wiśniewski', '98765432103', 'Pielęgniarz'),
('Krzysztof', 'Piotrowski', '98765432104', 'Recepcjonista'),
('Magdalena', 'Zielonka', '98765432105', 'Księgowa'),
('Marek', 'Czarnecki', '98765432106', 'Kierowca'),
('Agnieszka', 'Adamska', '98765432107', 'Sprzątaczka'),
('Jakub', 'Nowakowski', '98765432108', 'Ochroniarz'),
('Marta', 'Kwiatkowska', '98765432109', 'Księgowy');
DELETE FROM pracownicy_pracownik;
INSERT INTO zaopatrzenie_zaopatrzenie (nazwa, ilosc, data_ostatniej_kontroli, miejsce_skladowania, wartosc_netto, wartosc_brutto, cena_za_szt, opis_slowny)
VALUES
  ('strzykawka', 100, '2023-01-01', 'Magazyn A', 5.99, 7.99, 0.50, 'Przydatna w medycynie.'),
  ('maseczka', 500, '2023-02-15', 'Magazyn B', 1.50, 2.00, 0.20, 'Ochrona przed wirusami.'),
  ('długopis', 200, '2023-03-10', 'Magazyn C', 2.99, 3.99, 0.80, 'Pisze na czarno.'),
  ('płyn antybakteryjny', 50, '2023-01-05', 'Magazyn A', 8.99, 11.99, 0.30, 'Skuteczny przeciwko bakteriom.'),
  ('mydło', 300, '2023-04-20', 'Magazyn B', 4.49, 5.99, 0.15, 'O zapachu kwiatowym.'),
  ('pisak', 150, '2023-02-28', 'Magazyn C', 1.99, 2.49, 0.60, 'Do pisania na białej tablicy.'),
  ('ołówek', 100, '2023-03-15', 'Magazyn A', 0.99, 1.29, 0.30, 'Z gumką do mazania.'),
  ('pieczątka', 30, '2023-01-10', 'Magazyn B', 15.99, 19.99, 0.50, 'Drobna pieczątka firmowa.'),
  ('zszywacz', 80, '2023-02-05', 'Magazyn C', 6.49, 8.49, 1.00, 'Do zszywania dokumentów.'),
  ('segregator', 40, '2023-03-01', 'Magazyn A', 12.99, 16.99, 2.50, 'Na dokumenty firmowe.');