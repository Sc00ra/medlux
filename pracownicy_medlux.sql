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