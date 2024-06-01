from math import sin
import matplotlib.pyplot as plt
import numpy as np

def f (gamma, omega, theta, thetapoint) :
	"""
	Fonction correpsondant à l'equation du pendule
	"""
	return -gamma*thetapoint-omega*sin(theta)


def rk4(gamma, omega, theta, thetapoint, h, n, tableau_t, tableau_theta, tableau_theta_point):
	"""
	Fonction de l'algorithme RK4
	"""
	for _ in range(n) :
		a1 = h*thetapoint
		a2 = h*f(gamma, omega, theta, thetapoint)
		b1 = h*(thetapoint+a1/2)
		b2 = h*f(gamma, omega, theta + a1/2, thetapoint + a2/2)
		c1 = h*(thetapoint + b2/2)
		c2 = h*f(gamma, omega, theta + b1/2, thetapoint + b2/2)
		d1 = h*(thetapoint + c2)
		d2 = h*f(gamma, omega, theta + c1, thetapoint + c2)
		theta = theta + (a1+ 2*b1+ 2*c1+ d1)/6
		thetapoint += (a2+ 2*b2+ 2*c2+ d2)/6
		tableau_t += [h]
		tableau_theta += [theta]
		tableau_theta_point += [thetapoint]

	return (tableau_theta, tableau_theta_point)

def euler(gamma, omega, theta, thetapoint, h, n, tableau_t, tableau_theta, tableau_theta_point) :
	"""
	Fonction de l'algorithme d'Euler
	"""
	for _ in range(n) :
		theta1 = theta+h*thetapoint
		thetapoint1 = thetapoint+h*f(gamma, omega, theta, thetapoint)
		theta = theta1
		thetapoint = thetapoint1
		tableau_t += [h]
		tableau_theta += [theta]
		tableau_theta_point += [thetapoint]
	return (tableau_theta, tableau_theta_point)

#pas et nombre de points
h=0.1
n=200

# Explication du modèle
print("Equation: θ\"+ Γθ'+ ω0²sinθ : ")
print("Simulation du pendule de Foucault avec frottement et oscillation harmonique.")
print("Exemple d'entrée: Γ=0.5, ω=1, θ'(0)=0 pour une faible friction et oscillation standard.")

# Entrée des paramètres
gamma = float(input("Entrez le coefficient de frottement Γ (ex. 0.5) : "))
omega = float(input("Entrez la vitesse angulaire ω (ex. 1) : "))
thetapoint = float(input("Entrez la vitesse angulaire initiale θ'(0) (ex. 0) : "))


# Choix de la méthode de résolution numérique
print("\nEntrez 'r' pour la méthode de Runge-Kutta d'ordre 4 (rk4) ou 'e' pour la méthode d'Euler (euler).")
methode = input("Quelle méthode souhaitez-vous utiliser ? (r/e) : ")

# Assurer une validation simple de l'entrée
while methode not in ['r', 'e']:
    print("Erreur : Vous devez entrer 'r' pour rk4 ou 'e' pour euler.")
    methode = input("Veuillez réessayer : ")

#légende du graphique suivant la méthode choisie
if methode == "r":
	algo = "RK4"
else : algo = "Euler"

# Création et paramétrage de la figure
plt.figure()
plt.grid(True)
plt.title(f"Pendule sous amorti - {algo}, Γ={gamma}, ω={omega}, θ'(0)={thetapoint}")
plt.xlabel('angle')
plt.ylabel('dangle')

# Valeurs de theta pour lesquelles calculer les courbes
thetas = [0, 0.5, 1, 1.6, 2, 2.5, 3, 3.141592654]
colors = plt.cm.viridis(np.linspace(0, 1, len(thetas)))  # Génération de couleurs

max_theta = float('-inf')
min_theta = float('inf')
max_theta_point = float('-inf')
min_theta_point = float('inf')

# Calcul de différentes courbes suivant les valeurs de theta
for idx, theta in enumerate(thetas):
    tableau_t = [0]
    tableau_theta = [theta]
    tableau_theta_point = [thetapoint]

    if methode == "r":
        tableau_theta, tableau_theta_point = rk4(gamma, omega, theta, thetapoint, h, n, tableau_t, tableau_theta, tableau_theta_point)
    else:
        tableau_theta, tableau_theta_point = euler(gamma, omega, theta, thetapoint, h, n, tableau_t, tableau_theta, tableau_theta_point)

    plt.plot(tableau_theta, tableau_theta_point, label=f'$\\theta$={theta:.1f}', color=colors[idx])

    # Mise à jour des limites pour les axes
    max_theta = max(max_theta, max(tableau_theta))
    min_theta = min(min_theta, min(tableau_theta))
    max_theta_point = max(max_theta_point, max(tableau_theta_point))
    min_theta_point = min(min_theta_point, min(tableau_theta_point))

# Réglage des limites des axes
plt.xlim(min_theta - 1, max_theta + 1)
plt.ylim(min_theta_point - 1, max_theta_point + 1)

# Ajout d'une légende
plt.legend()

# Affichage des courbes
plt.show()

# Affichage des valeurs de gamma, omega, et thetapoint
print(f"gamma: {gamma}")
print(f"omega: {omega}")
print(f"thetapoint: {thetapoint}")