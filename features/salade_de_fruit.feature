Feature: Gestion de salade de fruits
  Scenario: Ajouter et retirer des fruits dans une salade
    Given une salade de fruits vide
    When j'ajoute un fruit "Pomme" de couleur "Rouge" pesant 150 grammes
    And j'ajoute un fruit "Banane" de couleur "Jaune" pesant 120 grammes
    Then la salade devrait contenir 2 fruits
    And le poids total devrait être 270 grammes
    When je retire le fruit "Pomme"
    Then la salade devrait contenir 1 fruit
    And le poids total devrait être 120 grammes


    Scenario: Vérifier si un fruit est considéré comme lourd
    Given une salade de fruits vide
    When j'ajoute un fruit "Melon" de couleur "Vert" pesant 600 grammes
    Then le fruit "Melon" devrait être considéré comme lourd
