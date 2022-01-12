# Exercise 8: Widgets and Gizmos
# Takes number of widgets and gizmos purchased and outputs their total weight
# Widget = 75 grams
# Gizmo = 112 grams

widgets = input("Please enter the number of widgets purchased: ")
gizmos = input("Please enter the number of gizmos purchased: ")
widgets = int(widgets)
gizmos = int(gizmos)
widgetGrams = widgets * 75
gizmoGrams = gizmos * 112
totalGrams = widgetGrams + gizmoGrams
print("The total weight of the order is",totalGrams,"grams.")