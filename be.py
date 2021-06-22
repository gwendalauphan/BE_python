from math import gamma, sin
import matplotlib.pyplot as plt

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


#entrées
print("Dans l'équation θ\"+ Γθ'+ ω0²sinθ : ")
print("exemple d'entrée: Γ=0.5, ω=1, θ'(0)=0")

gamma=float(input("Entrez la valeur du coefficient de frottement Γ : "))
omega=float(input("Entrez la valeur de la vitesse angulaire ω : "))
thetapoint=float(input("Entrez la valeur de θ'(0) : "))
methode = input("quelle méthode vouslez vous utiliser ? (entrer r pour rk4 et e pour euler) :")

#légende du graphique suivant la méthode choisie
if methode == "r":
	tmp = "RK4"
else : tmp = "Euler"

#création et paramètrage de la figure
plt.figure()
plt.grid(True)
plt.xlim(-1,4)
plt.ylim(-2,2)
plt.title(f"Pendule sous amorti - {tmp}")
plt.xlabel('angle')
plt.ylabel('dangle')

#calcul de différentes courbes suivant les valeurs de theta
for theta in [0, 0.5, 1, 1.6, 2, 2.5, 3, 3.141592654]:
	tableau_t = [0]
	tableau_theta=[theta]
	tableau_theta_point=[thetapoint]

	if methode == "r":
		tableau_theta, tableau_theta_point = rk4(gamma, omega, theta, thetapoint, h, n, tableau_t, tableau_theta, tableau_theta_point)
	else:
		tableau_theta, tableau_theta_point = euler(gamma, omega, theta, thetapoint, h, n, tableau_t, tableau_theta, tableau_theta_point)

	plt.plot(tableau_theta, tableau_theta_point)

#affichage des courbes
plt.show()
