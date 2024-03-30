taxe_actuelle = float(input()) / 100
nouvelle_taxe = float(input()) / 100
prix_legume = float(input())

print(round((prix_legume/(1+taxe_actuelle))*(1+nouvelle_taxe),2))