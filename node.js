// Script Node.js ultra simple

// Fonction pour afficher un message
function afficherMessage() {
	const maintenant = new Date();
	console.log(`Bonjour ! Il est ${maintenant.toLocaleTimeString()}`);
}

// Exécute la fonction toutes les secondes
setInterval(afficherMessage, 1000);
