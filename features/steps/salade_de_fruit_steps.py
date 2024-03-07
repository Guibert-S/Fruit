from behave import given, when, then
from Fruit import *  # Assurez-vous d'importer correctement vos classes

@given('une salade de fruits vide')
def step_impl(context):
    context.salade = SaladeDeFruit()

@when('j\'ajoute un fruit "{nom}" de couleur "{couleur}" pesant {poids} grammes')
def step_impl(context, nom, couleur, poids):
    fruit = Fruit(nom, couleur, int(poids))
    context.salade.add_fruit(fruit)

@then('la salade devrait contenir {nombre_fruits:d} fruits')
def step_impl(context, nombre_fruits):
    assert len(context.salade.fruits) == nombre_fruits

@then('le poids total devrait être {poids_total:d} grammes')
def step_impl(context, poids_total):
    assert context.salade.get_poids_total() == poids_total

@when('je retire le fruit "{nom}"')
def step_impl(context, nom):
    fruit_a_retirer = next((f for f in context.salade.fruits if f.name == nom), None)
    if fruit_a_retirer:
        context.salade.remove_fruit(fruit_a_retirer)

@then('la salade devrait contenir {nombre_fruits:d} fruit')  # Cette ligne est modifiée pour gérer "1 fruit" au singulier
def step_impl(context, nombre_fruits):
    assert len(context.salade.fruits) == nombre_fruits

@then('le poids total devrait être {poids_total:d} grammes')
def step_impl(context, poids_total):
    assert context.salade.get_poids_total() == poids_total


@then('le fruit "{nom}" devrait être considéré comme lourd')
def step_impl(context, nom):
    fruit = next((f for f in context.salade.fruits if f.name == nom), None)
    assert fruit is not None and fruit.is_heavy(), f"{nom} n'est pas considéré comme lourd"
